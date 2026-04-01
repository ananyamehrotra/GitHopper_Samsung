from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
from pathlib import Path

# Fix path to import sibling modules easily
import sys
sys.path.append(os.path.dirname(__file__))

from github_client import fetch_repo, categorize_files
from chunker import chunk_code

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
    """
    try:
        data = request.get_json()
        repo_url = data.get('repo_url')
        
        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400
            
        # Optional: Auth token to bypass rate limits
        github_token = os.environ.get('GITHUB_TOKEN')
        
        # 1. Fetch
        print(f"Fetching repo: {repo_url}")
        files = fetch_repo(repo_url, github_token=github_token)
        
        # 2. Categorize
        config_files, dep_files, source_code = categorize_files(files)
        
        # 3. Chunk
        all_chunks = chunk_code(files)
        
        return jsonify({
            'status': 'success',
            'repo_url': repo_url,
            'message': 'Scan initiated for repository',
            'data': {
                'total_files_fetched': len(files),
                'config_files': len(config_files),
                'dependency_files': len(dep_files),
                'source_files': len(source_code),
                'total_chunks': len(all_chunks)
            }
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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
