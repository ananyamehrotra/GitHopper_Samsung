#!/usr/bin/env python3
"""
GitHopper Codebase Dumper
Consolidates entire codebase into a single file for easy reference
Run this script to update CODEBASE_DUMP.md with all current code
"""

import os
import json
from pathlib import Path
from datetime import datetime
import mimetypes

# Configuration
REPO_ROOT = Path(__file__).parent
OUTPUT_FILE = REPO_ROOT / "CODEBASE_DUMP.md"

# Directories to exclude
EXCLUDE_DIRS = {
    '.git',
    'node_modules',
    '__pycache__',
    '.pytest_cache',
    'venv',
    'env',
    '.env',
    'dist',
    'build',
    '.venv',
    '.next',
    '.cache',
    'mcp_data',  # Skip data files
    'scan_results',  # Skip result files
    'public',  # Skip static assets
}

# File extensions to include
INCLUDE_EXTENSIONS = {
    # Python
    '.py',
    # JavaScript/TypeScript
    '.js', '.jsx', '.ts', '.tsx', '.mjs',
    # Web
    '.html', '.css', '.scss', '.less',
    # Configuration
    '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf',
    # Documentation
    '.md', '.txt', '.rst',
    # Environment
    '.env', '.env.example',
    # Other
    '.dockerfile', '.sql', '.sh', '.bash',
}

# Files to explicitly exclude
EXCLUDE_FILES = {
    '.DS_Store',
    'Thumbs.db',
    '.gitignore',
    '.gitkeep',
}

def should_include_file(file_path, file_name):
    """Determine if a file should be included in the dump"""
    # Skip excluded files
    if file_name in EXCLUDE_FILES:
        return False
    
    # Check file extension
    ext = Path(file_name).suffix.lower()
    if ext not in INCLUDE_EXTENSIONS:
        return False
    
    # Skip certain patterns
    if '.min.' in file_name:  # minified files
        return False
    
    return True

def should_include_dir(dir_name):
    """Determine if a directory should be explored"""
    return dir_name not in EXCLUDE_DIRS

def get_file_size(file_path):
    """Get file size in readable format"""
    size = file_path.stat().st_size
    for unit in ['B', 'KB', 'MB']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}GB"

def collect_files():
    """Collect all files to include in the dump"""
    files = []
    
    for root, dirs, filenames in os.walk(REPO_ROOT):
        # Filter directories
        dirs[:] = [d for d in dirs if should_include_dir(d)]
        
        rel_root = Path(root).relative_to(REPO_ROOT)
        
        for filename in filenames:
            if should_include_file(root, filename):
                file_path = Path(root) / filename
                rel_path = file_path.relative_to(REPO_ROOT)
                
                files.append({
                    'path': rel_path,
                    'full_path': file_path,
                    'size': get_file_size(file_path),
                    'ext': Path(filename).suffix.lower(),
                })
    
    return sorted(files, key=lambda x: str(x['path']))

def get_language_from_ext(ext):
    """Get markdown language identifier from file extension"""
    language_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'jsx',
        '.ts': 'typescript',
        '.tsx': 'tsx',
        '.html': 'html',
        '.css': 'css',
        '.scss': 'scss',
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.toml': 'toml',
        '.sh': 'bash',
        '.dockerfile': 'dockerfile',
        '.md': 'markdown',
        '.sql': 'sql',
    }
    return language_map.get(ext, 'text')

def read_file_safe(file_path):
    """Safely read file content"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        return f"[Error reading file: {str(e)}]"

def generate_table_of_contents(files):
    """Generate a table of contents"""
    toc = "## 📑 Table of Contents\n\n"
    
    current_dir = None
    for file_info in files:
        dir_name = file_info['path'].parent
        if dir_name != current_dir:
            current_dir = dir_name
            toc += f"- **{dir_name}/**\n"
        
        file_name = file_info['path'].name
        toc += f"  - {file_name}\n"
    
    return toc

def generate_dump():
    """Generate the codebase dump file"""
    print(f"🔍 Scanning codebase at: {REPO_ROOT}")
    
    files = collect_files()
    print(f"📦 Found {len(files)} files to include")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Start building the dump
    dump_content = f"""# 📚 GitHopper Complete Codebase Dump

**Generated:** {timestamp}
**Repository:** {REPO_ROOT.name}
**Total Files:** {len(files)}

---

"""
    
    # Add table of contents
    dump_content += generate_table_of_contents(files)
    
    dump_content += """
---

# 📂 File Contents

"""
    
    # Add all files
    for i, file_info in enumerate(files, 1):
        path_str = str(file_info['path']).replace('\\', '/')
        language = get_language_from_ext(file_info['ext'])
        
        dump_content += f"""## [{i}] {path_str}
**Size:** {file_info['size']}

```{language}
"""
        
        content = read_file_safe(file_info['full_path'])
        dump_content += content
        
        dump_content += f"""
```

---

"""
    
    # Write output file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(dump_content)
    
    print(f"✅ Dump saved to: {OUTPUT_FILE}")
    print(f"📊 Total size: {get_file_size(OUTPUT_FILE)}")
    print(f"⏱️  Timestamp: {timestamp}")

if __name__ == '__main__':
    try:
        generate_dump()
        print("\n✨ Codebase dump completed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)
