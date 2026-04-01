import json
import os
import sys
import hashlib

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from github_client import fetch_repo, categorize_files
from chunker import chunk_code


def lambda_handler(event, context):
    """
    AWS Lambda handler for fetching and chunking GitHub repositories
    """
    try:
        print("[FETCHER] Starting fetch operation...")

        # Extract repo URL from event
        repo_url = event.get('repo_url')
        if not repo_url:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'repo_url is required'})
            }

        # Normalize URL
        if not repo_url.startswith('http'):
            repo_url = f"https://github.com/{repo_url}"

        print(f"[FETCHER] Repository: {repo_url}")

        # Generate repo ID
        repo_id = hashlib.md5(repo_url.encode()).hexdigest()[:8]

        # 1. Fetch repository
        print("[FETCHER] Step 1: Fetching repository...")
        github_token = os.environ.get('GITHUB_TOKEN')
        files = fetch_repo(repo_url, github_token=github_token)
        print(f"[FETCHER] Fetched {len(files)} files")

        # 2. Categorize files
        print("[FETCHER] Step 2: Categorizing files...")
        config_files, dep_files, source_code = categorize_files(files)
        print(f"[FETCHER] Categorized: {len(config_files)} config, {len(dep_files)} deps, {len(source_code)} source")

        # 3. Chunk code
        print("[FETCHER] Step 3: Chunking code...")
        chunks = chunk_code(files)
        print(f"[FETCHER] Created {len(chunks)} chunks")

        # Prepare response
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'repo_id': repo_id,
                'repo_url': repo_url,
                'total_files': len(files),
                'categories': {
                    'config': len(config_files),
                    'dependencies': len(dep_files),
                    'source_code': len(source_code)
                },
                'chunks': chunks,
                'files': files
            })
        }

        print(f"[FETCHER] Complete: {len(chunks)} chunks ready for analysis")
        return response

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"[FETCHER] ERROR: {error_msg}")
        print(f"[FETCHER] Traceback: {tb}")

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': error_msg,
                'type': type(e).__name__,
                'traceback': tb
            })
        }