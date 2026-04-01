from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
from pathlib import Path
import json
import hashlib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from pipeline import GitHopperPipeline

# Initialize Flask app
app = Flask(__name__, 
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist'),
            static_url_path='/',
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend'))

# Enable CORS for frontend communication
CORS(app)

# ==================== API ROUTES ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'GitHopper backend is running',
        'version': '1.0.0'
    }), 200


@app.route('/api/scan', methods=['POST'])
def scan_repo():
    """
    Receive GitHub repository URL for scanning
    Fetches the repo, categorizes, and chunks the code.
    Falls back to mock data if GitHub API rate limit is hit.
    """
    try:
        print("[SCAN] Starting scan request...")
        data = request.get_json()
        repo_url = data.get('repo_url')
        
        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400
        
        # Normalize URL - add https://github.com/ if missing
        if not repo_url.startswith('http'):
            repo_url = f"https://github.com/{repo_url}"
        
        print(f"[SCAN] Repository: {repo_url}")
        
        # Optional: Auth token to bypass rate limits
        github_token = os.environ.get('GITHUB_TOKEN')
        
        # 1. Fetch
        print(f"[SCAN] Step 1: Fetching repo...")
        try:
            files = fetch_repo(repo_url, github_token=github_token)
            print(f"[SCAN] Step 1 DONE: Fetched {len(files)} files")
        except Exception as fetch_error:
            print(f"[SCAN] GitHub API Error: {str(fetch_error)}")
            # Fallback: Return simple mock response with chunking info
            print(f"[SCAN] Using mock chunking (rate limit fallback)...")
            response_data = {
                'status': 'success',
                'repo_url': repo_url,
                'message': 'Scan initiated (mock mode - GitHub rate limited)',
                'data': {
                    'total_files_fetched': 5,
                    'config_files': 1,
                    'dependency_files': 1,
                    'source_files': 3,
                    'total_chunks': 8,
                    'files_by_category': {
                        'config': [{'path': 'config/database.py', 'language': 'python'}],
                        'dependencies': [{'path': 'requirements.txt', 'language': 'text'}],
                        'source_code': [
                            {'path': 'main.py', 'language': 'python'},
                            {'path': 'app.js', 'language': 'javascript'},
                            {'path': 'utils.py', 'language': 'python'}
                        ]
                    },
                    'analysis_summary': {
                        'total_debt_signals': 5,
                        'files_with_debt_signals': 2,
                        'cost_estimate': {
                            'notes': 'Mock data - GitHub API rate limited',
                            'chunks_to_analyze': 8,
                            'total_code_chars': 2400,
                            'approx_tokens': 600
                        }
                    }
                }
            }
            return jsonify(response_data), 200
        
        # 2. Categorize
        print(f"[SCAN] Step 2: Categorizing files...")
        config_files, dep_files, source_code = categorize_files(files)
        print(f"[SCAN] Step 2 DONE: {len(config_files)} config, {len(dep_files)} deps, {len(source_code)} source")
        
        # 3. Chunk
        print(f"[SCAN] Step 3: Chunking code...")
        all_chunks = chunk_code(files)
        print(f"[SCAN] Step 3 DONE: Created {len(all_chunks)} chunks")
        
        # Extract just paths and language for frontend display
        print(f"[SCAN] Step 4: Building response...")
        def extract_file_info(file_list):
            return [{'path': f['path'], 'language': f.get('language', 'text')} for f in file_list]
        
        # Calculate overall debt statistics
        total_debt_signals = sum(f.get('debt_signal_count', 0) for f in files)
        files_with_signals = sum(1 for f in files if f.get('debt_signal_count', 0) > 0)
        
        response_data = {
            'status': 'success',
            'repo_url': repo_url,
            'message': 'Scan initiated for repository',
            'data': {
                'total_files_fetched': len(files),
                'config_files': len(config_files),
                'dependency_files': len(dep_files),
                'source_files': len(source_code),
                'total_chunks': len(all_chunks),
                'files_by_category': {
                    'config': extract_file_info(config_files),
                    'dependencies': extract_file_info(dep_files),
                    'source_code': extract_file_info(source_code)
                },
                'analysis_summary': {
                    'total_debt_signals': total_debt_signals,
                    'files_with_debt_signals': files_with_signals,
                    'cost_estimate': {
                        'notes': 'Total tokens estimated for Bedrock analysis',
                        'chunks_to_analyze': len(all_chunks),
                        'total_code_chars': sum(c.get('char_count', 0) for c in all_chunks),
                        'approx_tokens': int(sum(c.get('char_count', 0) for c in all_chunks) / 4)
                    }
                },
                'detailed_files': [
                    {
                        'path': f['path'],
                        'language': f['language'],
                        'size_bytes': f.get('size_bytes', 0),
                        'debt_signals': f.get('debt_signals', []),
                        'debt_signal_count': f.get('debt_signal_count', 0),
                        'debt_category_hint': f.get('debt_category_hint', 'code_quality'),
                        'metrics': f.get('metrics', {})
                    }
                    for f in files
                ]
            }
        }
        print(f"[SCAN] Step 4 DONE: Response built")
        
        # Print data structure to terminal for analysis
        print("\n" + "="*80)
        print("SCAN ANALYSIS - DATA STRUCTURE")
        print("="*80)
        print(f"Repository: {repo_url}")
        print(f"Status: {response_data['status']}")
        print(f"\nSUMMARY:")
        print(f"  Total Files: {response_data['data']['total_files_fetched']}")
        print(f"  Config Files: {response_data['data']['config_files']}")
        print(f"  Dependency Files: {response_data['data']['dependency_files']}")
        print(f"  Source Code Files: {response_data['data']['source_files']}")
        print(f"  Code Chunks: {response_data['data']['total_chunks']}")
        print(f"\nFILE STRUCTURE BY CATEGORY:")
        
        # Print config files
        if response_data['data']['files_by_category']['config']:
            print(f"\nConfiguration Files ({len(response_data['data']['files_by_category']['config'])}):")
            for file in response_data['data']['files_by_category']['config']:
                print(f"   - {file['path']} ({file['language']})")
        else:
            print(f"\nConfiguration Files (0): None")
        
        # Print dependency files
        if response_data['data']['files_by_category']['dependencies']:
            print(f"\nDependency Files ({len(response_data['data']['files_by_category']['dependencies'])}):")
            for file in response_data['data']['files_by_category']['dependencies'][:10]:  # Show first 10
                print(f"   - {file['path']} ({file['language']})")
            if len(response_data['data']['files_by_category']['dependencies']) > 10:
                print(f"   ... and {len(response_data['data']['files_by_category']['dependencies']) - 10} more")
        else:
            print(f"\nDependency Files (0): None")
        
        # Print source code files
        if response_data['data']['files_by_category']['source_code']:
            print(f"\nSource Code Files ({len(response_data['data']['files_by_category']['source_code'])}):")
            for file in response_data['data']['files_by_category']['source_code'][:10]:  # Show first 10
                print(f"   - {file['path']} ({file['language']})")
            if len(response_data['data']['files_by_category']['source_code']) > 10:
                print(f"   ... and {len(response_data['data']['files_by_category']['source_code']) - 10} more")
        else:
            print(f"\nSource Code Files (0): None")
        
        print("\n" + "="*80)
        print("RAW JSON RESPONSE:")
        print("="*80)
        print(json.dumps(response_data, indent=2))
        print("="*80 + "\n")
        print(f"[SCAN] COMPLETE: Returning response")
        
        return jsonify(response_data), 200
    
    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in scan_repo: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/scan/flagged-content', methods=['POST'])
def get_flagged_content():
    """
    Extract flagged files (with debt signals) and dependency files
    Returns JSON with their full content for agent processing
    """
    try:
        print("[FLAGGED] Extracting flagged files content...")
        data = request.get_json()
        repo_url = data.get('repo_url')
        
        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400
        
        # Fetch repo
        github_token = os.environ.get('GITHUB_TOKEN')
        files = fetch_repo(repo_url, github_token=github_token)
        
        # Filter: files with debt signals OR dependency/testing category
        flagged_files = [
            {
                'path': f['path'],
                'language': f['language'],
                'content': f['content'],
                'size_bytes': f.get('size_bytes', 0),
                'debt_signals': f.get('debt_signals', []),
                'debt_signal_count': f.get('debt_signal_count', 0),
                'debt_category_hint': f.get('debt_category_hint', 'code_quality'),
                'metrics': f.get('metrics', {}),
                'reasons_flagged': [
                    'has_debt_signals' if f.get('debt_signal_count', 0) > 0 else None,
                    'dependency_file' if f.get('debt_category_hint', '') in ['dependencies', 'testing'] else None
                ]
            }
            for f in files
            if f.get('debt_signal_count', 0) > 0 or f.get('debt_category_hint', '') in ['dependencies', 'testing']
        ]
        
        # Clean up reasons list
        for file in flagged_files:
            file['reasons_flagged'] = [r for r in file['reasons_flagged'] if r is not None]
        
        response_data = {
            'status': 'success',
            'repo_url': repo_url,
            'message': f'Extracted {len(flagged_files)} flagged/dependency files',
            'total_files_scanned': len(files),
            'flagged_files_count': len(flagged_files),
            'flagged_files': flagged_files
        }
        
        print(f"[FLAGGED] DONE: {len(flagged_files)} files flagged out of {len(files)}")
        print(json.dumps({
            'status': response_data['status'],
            'repo_url': response_data['repo_url'],
            'message': response_data['message'],
            'total_files_scanned': response_data['total_files_scanned'],
            'flagged_files_count': response_data['flagged_files_count'],
            'files_summary': [
                {
                    'path': f['path'],
                    'debt_signals': f['debt_signal_count'],
                    'reasons': f['reasons_flagged']
                }
                for f in flagged_files
            ]
        }, indent=2))
        
        return jsonify(response_data), 200
    
    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in get_flagged_content: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/scan/status/<scan_id>', methods=['GET'])
def get_scan_status(scan_id):
    """Get the status of a scan"""
    return jsonify({
        'scan_id': scan_id,
        'status': 'completed',
        'progress': 100,
        'result': {
            'security_issues': 5,
            'technical_debt': 3,
            'health_score': 78
        }
    }), 200


@app.route('/api/analyze', methods=['POST'])
def analyze_repo():
    """
    Analyze code using the complete GitHopper pipeline:
    1. Fetch repository
    2. AI analysis with Bedrock
    3. Scoring and recommendations
    """
    try:
        print("[ANALYZE] Starting complete pipeline...")
        data = request.get_json()
        repo_url = data.get('repo_url')
        branch_name = data.get('branch_name', 'main')

        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400

        print(f"[ANALYZE] Repository: {repo_url}")
        print(f"[ANALYZE] Branch: {branch_name}")

        # Use the full pipeline
        pipeline = GitHopperPipeline()
        github_token = os.environ.get('GITHUB_TOKEN')
        result = pipeline.run_full_pipeline(repo_url, github_token, branch_name)

        if result.get('status') == 'success':
            # Save results
            repo_id = result['summary']['repo_id']
            results_dir = os.path.join(os.path.dirname(__file__), 'scan_results')
            os.makedirs(results_dir, exist_ok=True)

            results_file = os.path.join(results_dir, f'{repo_id}_pipeline.json')
            with open(results_file, 'w') as f:
                json.dump(result, f, indent=2)

            print(f"[ANALYZE] Pipeline complete: Health score {result['summary']['health_score']}")
        else:
            print(f"[ANALYZE] Pipeline failed: {result.get('error', 'Unknown error')}")

        return jsonify(result), 200

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in analyze_repo: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/findings/<repo_id>', methods=['GET'])
def get_findings(repo_id):
    """
    Retrieve saved findings for a repo
    """
    try:
        results_file = os.path.join(os.path.dirname(__file__), 'scan_results', f'{repo_id}_findings.json')
        
        if not os.path.exists(results_file):
            return jsonify({'error': f'No findings for repo_id: {repo_id}'}), 404
        
        with open(results_file, 'r') as f:
            findings = json.load(f)
        
        return jsonify(findings), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/', methods=['GET'])
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    """Serve static files"""
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return app.send_static_file(path)
    return render_template('index.html')


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


# ==================== DEVELOPMENT SERVER ====================

if __name__ == '__main__':
    # Development configuration
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    
    # Run the Flask development server
    print("=" * 60)
    print("GitHopper Backend Server")
    print("=" * 60)
    print("Server running at: http://localhost:5000")
    print("API Documentation: http://localhost:5000/api/health")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
