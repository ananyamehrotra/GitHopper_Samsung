import requests
from urllib.parse import urlparse
from chunker import scan_debt_signals, compute_file_metrics, get_debt_category_hint

# Setup filtering constants
ALLOWED_EXTENSIONS = {
    '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.rb', '.php', 
    '.c', '.cpp', '.h', '.cs', '.md', '.json', '.yml', '.yaml', '.html', '.css'
}

CRITICAL_FILES = {
    'package.json', 'requirements.txt', '.env.example', 'pom.xml', 
    'go.mod', 'dockerfile', 'docker-compose.yml'
}

EXCLUDED_DIRS = {
    'node_modules', 'venv', '.git', 'build', 'dist', 'out', 'bin', 
    'obj', 'images', 'assets', '.next', '__pycache__', 'coverage'
}

EXT_MAP = {
    "py": "python",
    "js": "javascript",
    "ts": "typescript",
    "java": "java",
    "go": "go",
    "rb": "ruby",
    "php": "php",
    "c": "c",
    "cpp": "cpp",
    "cs": "csharp",
    "md": "markdown",
    "json": "json",
    "yml": "yaml",
    "yaml": "yaml",
    "html": "html",
    "css": "css"
}

def parse_repo_url(url):
    """Extract owner and repo from https://github.com/user/repo"""
    url = url.strip()
    if url.endswith('/'):
        url = url[:-1]
    if url.endswith('.git'):
        url = url[:-4]
        
    if url.startswith('http'):
        path = urlparse(url).path.strip('/')
    else:
        path = url.strip('/')
    
    parts = path.split('/')
    if len(parts) >= 2:
        return parts[-2], parts[-1]
    raise ValueError(f"Invalid GitHub URL: {url}")

def should_keep_file(file_path):
    """Determine if a file should be included in the AI scan."""
    path_parts = file_path.split('/')
    
    # 1. Ignore excluded directories
    if any(excluded in path_parts for excluded in EXCLUDED_DIRS):
        return False
        
    filename = path_parts[-1].lower()
    
    # 2. Keep critical configuration and dependency files
    if filename in CRITICAL_FILES:
        return True
        
    # 3. Check allowed extensions
    ext = '.' + filename.split('.')[-1] if '.' in filename else ''
    if ext in ALLOWED_EXTENSIONS:
        return True
        
    return False

def get_default_branch(owner, repo, headers):
    """Fetch the default branch of a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 403:
        raise Exception("GitHub rate limit exceeded")
    if response.status_code == 200:
        return response.json().get('default_branch', 'main')
    return 'main' # Fallback


def get_latest_commit_sha(url, github_token=None, branch_name=None):
    """
    Fetch the latest commit SHA for a repository branch.
    Used by watch mode so scans trigger on actual repo changes, not polling alone.
    """
    owner, repo = parse_repo_url(url)

    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
    }
    if github_token:
        headers['Authorization'] = f'token {github_token}'

    branch = branch_name or get_default_branch(owner, repo, headers)
    
    import time
    commit_url = f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}?_ts={int(time.time())}"

    try:
        response = requests.get(commit_url, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        raise Exception(f"GitHub commit request timed out for {owner}/{repo}@{branch}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"GitHub API error fetching commit SHA: {str(e)}")

    if response.status_code == 403:
        raise Exception("GitHub rate limit exceeded")
    if response.status_code == 404:
        fallback_branch = get_default_branch(owner, repo, headers)
        if fallback_branch != branch:
            fallback_url = f"https://api.github.com/repos/{owner}/{repo}/commits/{fallback_branch}?_ts={int(time.time())}"
            try:
                response = requests.get(fallback_url, headers=headers, timeout=10)
            except requests.exceptions.Timeout:
                raise Exception(f"GitHub commit request timed out for {owner}/{repo}@{fallback_branch}")
            except requests.exceptions.RequestException as e:
                raise Exception(f"GitHub API error fetching commit SHA: {str(e)}")

            if response.status_code == 403:
                raise Exception("GitHub rate limit exceeded")
            if response.status_code != 200:
                raise Exception(
                    f"Failed to fetch latest commit (Status {response.status_code}): {response.text[:200]}"
                )
            branch = fallback_branch
        else:
            raise Exception(f"Failed to fetch latest commit (Status 404): {response.text[:200]}")

    if response.status_code != 200:
        raise Exception(f"Failed to fetch latest commit (Status {response.status_code}): {response.text[:200]}")

    data = response.json()
    return {
        "branch_name": branch,
        "commit_sha": data.get("sha"),
        "commit_url": data.get("html_url"),
    }

def fetch_repo(url, github_token=None, max_files=30):
    """
    Fetch the useful files from a GitHub repository.
    Uses GitHub Tree API directly then fetches Raw content to save API limit.
    """
    owner, repo = parse_repo_url(url)
    
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if github_token:
        headers['Authorization'] = f'token {github_token}'
        
    branch = get_default_branch(owner, repo, headers)
    
    # Get the recursive tree
    print(f"[DEBUG] Fetching tree for {owner}/{repo} branch {branch}...")
    tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    try:
        response = requests.get(tree_url, headers=headers, timeout=20)
    except requests.exceptions.Timeout:
        raise Exception(f"GitHub API tree request timed out for {owner}/{repo}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"GitHub API error fetching tree: {str(e)}")
    
    print(f"[DEBUG] Tree response status: {response.status_code}")
    
    if response.status_code == 403:
        raise Exception("GitHub rate limit exceeded")
    if response.status_code != 200:
        raise Exception(f"Failed to fetch repo tree (Status {response.status_code}): {response.text[:200]}")
    
    print(f"[DEBUG] Processing tree response...")    
    tree = response.json().get('tree', [])
    
    # Check if response was truncated (large repos)
    tree_data = response.json()
    if tree_data.get('truncated'):
        print(f"[WARN] Tree response was truncated. GitHub limits recursive tree to 100,000 items.")
        print(f"[WARN] Will use available {len(tree)} items")
    
    print(f"[DEBUG] Found {len(tree)} items in tree")
    
    # Filter tree
    valid_files = [item for item in tree if item['type'] == 'blob' and should_keep_file(item['path'])]
    
    # Optional: Prioritize config files, then regular code. Cap at max_files to prevent massive payloads.
    valid_files.sort(key=lambda x: 0 if x['path'].split('/')[-1].lower() in CRITICAL_FILES else 1)
    valid_files = valid_files[:max_files]
    
    fetched_files = []
    
    print(f"[DEBUG] Starting to fetch {len(valid_files)} files...")
    for idx, item in enumerate(valid_files):
        path = item['path']
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
        
        # We download via Raw endpoint as it rarely ratelimits compared to the API
        try:
            print(f"[DEBUG] Fetching file {idx+1}/{len(valid_files)}: {path}")
            file_resp = requests.get(raw_url, timeout=10)
        except requests.exceptions.Timeout:
            print(f"[WARN] File fetch timeout: {path}")
            continue
        except requests.exceptions.RequestException as e:
            print(f"[WARN] Failed to fetch {path}: {e}")
            continue
            
        if file_resp.status_code == 403:
            raise Exception("GitHub rate limit exceeded")
            
        if file_resp.status_code == 200:
            content = file_resp.text
            
            if not content.strip():
                print(f"[SKIP] Empty file: {path}")
                continue
                
            if len(content) > 10000:
                print(f"[SKIP] File too large ({len(content)} bytes): {path}")
                continue
            
            # Simple language detection based on extension
            raw_ext = path.split('.')[-1] if '.' in path else 'text'
            language = EXT_MAP.get(raw_ext.lower(), raw_ext)
            
            print(f"[OK] Fetched: {path} ({len(content)} bytes)")
            
            # Compute analysis metadata
            debt_signals = scan_debt_signals(content)
            metrics = compute_file_metrics(content, language)
            debt_hint = get_debt_category_hint(path)
            
            fetched_files.append({
                "path": path,
                "language": language,
                "content": content,
                "size_bytes": len(content.encode('utf-8')),
                "debt_category_hint": debt_hint,
                "debt_signals": debt_signals,
                "debt_signal_count": len(debt_signals),
                "metrics": metrics,
            })
            
    return fetched_files

def categorize_files(files):
    """
    Groups fetched files into config, dependencies, and code
    to allow for optimized, domain-specific AI processing.
    """
    config, deps, code = [], [], []

    for f in files:
        name = f["path"].lower()
        basename = name.split('/')[-1]
        
        if basename in ["package.json", "requirements.txt", "dockerfile", "pom.xml", "go.mod"]:
            deps.append(f)
        elif basename.endswith((".yml", ".yaml", ".json", ".env", ".env.example")):
            config.append(f)
        else:
            code.append(f)

    return config, deps, code
