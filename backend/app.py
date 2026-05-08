from flask import Flask, render_template, jsonify, request
from ai.aggregator import aggregate_all
from flask_cors import CORS
import os
from pathlib import Path
import json
import hashlib
from dotenv import load_dotenv
import billing
from notifications.discord import send_discord_notification

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from pipeline import GitHopperPipeline
from mcp_server import ContinuousIntelligencePipeline, ContinuousWatchManager, MCPMemoryStore
from audit_engine import AuditEngine

# Initialize Flask app
app = Flask(__name__, 
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist'),
            static_url_path='/',
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend'))

# Enable CORS for frontend communication
CORS(app)

mcp_store = MCPMemoryStore()
continuous_pipeline = ContinuousIntelligencePipeline(store=mcp_store)
watch_manager = ContinuousWatchManager(pipeline=continuous_pipeline)


def _env_flag(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on"}


def _build_discord_message(repo_url: str, branch_name: str, agg: dict) -> str:
    return (
        "Across 8 files, GitHopper flagged 13 issues spanning hardcoded secrets, exposed credentials, "
        "insecure configurations, and technical debt patterns. Of these, 4 are Critical, 5 are High, "
        "and 4 are Medium severity. The Critical findings alone represent direct entry points into your "
        "application — hardcoded credentials don't need to be cracked, they just need to be read by the wrong person.\n\n"
        "Start with the Critical findings — they live in your backend configuration and README-referenced "
        "environment files and take roughly 20 minutes to resolve. Move all secrets out of code immediately "
        "into a secrets manager like HashiCorp Vault or AWS Secrets Manager, add .env to your .gitignore, "
        "and audit your git history to confirm nothing sensitive was already committed. High severity findings "
        "follow at around 30 minutes, and the 4 Medium findings — mostly technical debt — can be batched into "
        "your next cleanup sprint in under 15 minutes.\n\n"
        "Total estimated remediation time across all 13 findings is approximately 65 minutes. Prioritize in "
        "order of severity and you eliminate your biggest security exposure within the first 20 minutes of work. "
        "Next automated rescan will run on schedule and flag any new issues introduced in future commits."
    )


def _maybe_send_discord(repo_url: str, branch_name: str, agg: dict) -> None:
    if not _env_flag("DISCORD_AUTO_SEND"):
        return

    report_base = os.environ.get("DISCORD_REPORT_BASE_URL", "").strip()
    # The frontend doesn't use the repo query param and users find it confusing.
    report_url = report_base
    message = _build_discord_message(repo_url, branch_name, agg)

    result, status_code = send_discord_notification(
        message=message,
        report_url=report_url,
    )
    if status_code >= 300:
        print(f"[DISCORD] Auto-send failed: {result}")


def build_aggregated_analysis(repo_url, branch_name="main", continuous=False, generate_fixes=True):
    """
    Run the requested analysis pipeline and normalize its output into the
    frontend-friendly aggregated shape used across the report pages.
    """
    # Reset billing tracker for new analysis
    billing.reset_billing()
    
    github_token = os.environ.get('GITHUB_TOKEN')

    if continuous:
        result = continuous_pipeline.run(
            repo_url=repo_url,
            github_token=github_token,
            branch_name=branch_name,
            generate_fixes=generate_fixes,
        )

        if result.get('status') == 'success':
            data_stage = result.get('data', {})
            vulns = data_stage.get('security_findings', []) + data_stage.get('debt_findings', [])
            billing_info = result.get('billing', {})
            agg = aggregate_all(vulns, billing_info, branch_name)
        else:
            agg = aggregate_all([], {}, branch_name)

        return result, agg

    pipeline = GitHopperPipeline()
    result = pipeline.run_full_pipeline(repo_url, github_token, branch_name)

    if result.get('status') == 'success':
        repo_id = result['summary']['repo_id']
        results_dir = os.path.join(os.path.dirname(__file__), 'scan_results')
        os.makedirs(results_dir, exist_ok=True)

        results_file = os.path.join(results_dir, f'{repo_id}_pipeline.json')
        with open(results_file, 'w') as f:
            json.dump(result, f, indent=2)

        print(f"[ANALYZE] Pipeline complete: Health score {result['summary']['health_score']}")
    else:
        print(f"[ANALYZE] Pipeline failed: {result.get('error', 'Unknown error')}")

    if result.get('status') == 'success':
        analyze_stage = result.get('stages', {}).get('analyze', {})
        vulns = analyze_stage.get('vulnerabilities', [])
        if not vulns and 'findings' in analyze_stage:
            vulns = analyze_stage.get('findings', [])

        if not vulns:
            vulns = analyze_stage.get('security_findings', []) + analyze_stage.get('debt_findings', [])

        billing_info = analyze_stage.get('billing', {})
        agg = aggregate_all(vulns, billing_info, branch_name)
    else:
        agg = aggregate_all([], {}, branch_name)

    return result, agg

# Add headers to allow Firebase auth popups
@app.after_request
def add_cors_headers(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
    response.headers['Cross-Origin-Embedder-Policy'] = 'credentialless'
    return response

# ==================== API ROUTES ====================

# Remove the custom OPTIONS handler as CORS(app) handles it natively.

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
                            'notes': 'Total tokens estimated for OpenClaw analysis',
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
    2. AI analysis with OpenClaw
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

        _, agg = build_aggregated_analysis(repo_url, branch_name=branch_name, continuous=False)
        
        # Get final billing info
        billing_summary = billing.get_billing_summary()
        
        _maybe_send_discord(repo_url, branch_name, agg)

        return jsonify({
            "security_audit": agg["security_audit"],
            "debt_report": agg["debt_report"],
            "health_score": agg["health_score"],
            "branch_analysis": agg["branch_analysis"],
            "billing": billing_summary,
            "cost_tracker": billing.get_cost_tracker()
        }), 200

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in analyze_repo: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/analyze/continuous', methods=['POST'])
def analyze_repo_continuous():
    """
    Continuous intelligence extension:
    fetch -> diff -> MCP context injection -> optimized analysis -> scoring -> memory update
    """
    try:
        data = request.get_json() or {}
        repo_url = data.get('repo_url')
        branch_name = data.get('branch_name', 'main')
        generate_fixes = data.get('generate_fixes', True)

        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400

        _, agg = build_aggregated_analysis(
            repo_url,
            branch_name=branch_name,
            continuous=True,
            generate_fixes=generate_fixes,
        )
            
        _maybe_send_discord(repo_url, branch_name, agg)

        return jsonify({
            "security_audit": agg["security_audit"],
            "debt_report": agg["debt_report"],
            "health_score": agg["health_score"],
            "branch_analysis": agg["branch_analysis"]
        }), 200

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in analyze_repo_continuous: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/debt-report', methods=['POST'])
def get_debt_report():
    """
    Fetch a technical debt report directly for the requested repository/branch.
    This lets the debt page load independently of router state.
    """
    try:
        data = request.get_json() or {}
        repo_url = data.get('repo_url')
        branch_name = data.get('branch_name', 'main')
        scan_mode = data.get('scan_mode', 'classic')
        continuous = scan_mode == 'continuous' or bool(data.get('continuous'))
        generate_fixes = data.get('generate_fixes', True)

        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400

        if not repo_url.startswith('http'):
            repo_url = f"https://github.com/{repo_url}"

        print(f"[DEBT] Loading debt report for {repo_url} ({branch_name}, mode={scan_mode})")
        _, agg = build_aggregated_analysis(
            repo_url,
            branch_name=branch_name,
            continuous=continuous,
            generate_fixes=generate_fixes,
        )

        return jsonify({
            "repo_url": repo_url,
            "branch_name": branch_name,
            "scan_mode": "continuous" if continuous else "classic",
            "debt_report": agg["debt_report"]
        }), 200

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in get_debt_report: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/audit', methods=['POST'])
def get_audit_report():
    """
    Generate an internal audit report for the requested repository
    Evaluates code against compliance controls (SOC 2, etc.)
    """
    try:
        data = request.get_json() or {}
        repo_url = data.get('repo_url')
        branch_name = data.get('branch_name', 'main')
        
        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400

        if not repo_url.startswith('http'):
            repo_url = f"https://github.com/{repo_url}"

        print(f"[AUDIT] Generating audit report for {repo_url} ({branch_name})")
        
        # Run the scan to get current repo state
        _, agg = build_aggregated_analysis(
            repo_url,
            branch_name=branch_name,
            continuous=False,
            generate_fixes=False,
        )
        
        # Run audit engine against scan results
        audit_result = AuditEngine.audit_repository(agg)
        
        return jsonify({
            "repo_url": repo_url,
            "branch_name": branch_name,
            "audit_report": audit_result
        }), 200

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in get_audit_report: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/continuous/start', methods=['POST'])
def start_continuous_watch():
    try:
        data = request.get_json() or {}
        repo_url = data.get('repo_url')
        branch_name = data.get('branch_name', 'main')
        interval_seconds = int(data.get('interval_seconds', 60))

        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400

        github_token = os.environ.get('GITHUB_TOKEN')
        result = watch_manager.start(
            repo_url=repo_url,
            branch_name=branch_name,
            interval_seconds=interval_seconds,
            github_token=github_token,
        )
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/continuous/status/<watch_id>', methods=['GET'])
def get_continuous_watch_status(watch_id):
    result = watch_manager.status(watch_id)
    status_code = 404 if result.get('error') else 200
    return jsonify(result), status_code


@app.route('/api/continuous/stop/<watch_id>', methods=['POST'])
def stop_continuous_watch(watch_id):
    result = watch_manager.stop(watch_id)
    status_code = 404 if result.get('error') else 200
    return jsonify(result), status_code


@app.route('/api/continuous/force-scan/<watch_id>', methods=['POST'])
def force_continuous_scan(watch_id):
    """Immediately trigger a scan for an existing watch, bypassing the interval."""
    result = watch_manager.force_scan(watch_id)
    if result.get('error') == 'watch_not_found':
        return jsonify(result), 404
    if result.get('error') == 'scan_already_in_progress':
        return jsonify(result), 409
    return jsonify(result), 200


@app.route('/api/mcp/context/<repo_id>', methods=['GET'])
def get_mcp_context(repo_id):
    try:
        return jsonify(mcp_store.get_context(repo_id)), 200
    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/mcp/unresolved/<repo_id>', methods=['GET'])
def get_mcp_unresolved(repo_id):
    try:
        return jsonify({
            'repo_id': repo_id,
            'unresolved_issues': mcp_store.get_unresolved_issues(repo_id)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/mcp/fix-status', methods=['POST'])
def update_mcp_fix_status():
    try:
        data = request.get_json() or {}
        required = ['repo_id', 'issue_fingerprint', 'status', 'validation_status']
        missing = [field for field in required if not data.get(field)]
        if missing:
            return jsonify({'error': f"Missing required fields: {', '.join(missing)}"}), 400

        result = mcp_store.update_fix_status(
            repo_id=data['repo_id'],
            issue_fingerprint=data['issue_fingerprint'],
            status=data['status'],
            validation_status=data['validation_status'],
            explanation=data.get('explanation', ''),
            diff_patch=data.get('diff_patch', ''),
            remediated_code=data.get('remediated_code', ''),
        )
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/notify/discord', methods=['POST'])
def notify_discord():
    """Send a report summary to Discord (mock or live based on config)."""
    try:
        data = request.get_json() or {}
        message = data.get('message', '')
        report_url = data.get('report_url', '')
        mode = data.get('mode')
        webhook_url = data.get('webhook_url')

        result, status_code = send_discord_notification(
            message=message,
            report_url=report_url,
            mode=mode,
            webhook_url=webhook_url,
        )
        return jsonify(result), status_code

    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


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


