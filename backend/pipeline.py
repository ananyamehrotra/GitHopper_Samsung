import json
import os
import sys
import hashlib
import boto3
from datetime import datetime

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from github_client import fetch_repo, categorize_files
from chunker import chunk_code
from ai.bedrock_client import scan_chunk, scan_all_chunks


class GitHopperPipeline:
    """
    Complete GitHopper analysis pipeline:
    1. Fetch → 2. Analyze → 3. Score
    """

    def __init__(self):
        self.lambda_client = None
        self.use_lambda = os.environ.get('USE_LAMBDA', 'false').lower() == 'true'
        self.mock_mode = os.environ.get('MOCK_MODE', 'false').lower() == 'true'

        if self.use_lambda:
            self.lambda_client = boto3.client('lambda', region_name='us-east-1')

    def run_full_pipeline(self, repo_url, github_token=None):
        """
        Execute the complete pipeline: Fetch → Analyze → Score
        """
        print("🚀 Starting GitHopper Full Pipeline")
        print(f"📦 Repository: {repo_url}")
        print(f"🔧 Mode: {'Lambda' if self.use_lambda else 'Local'}")

        start_time = datetime.now()

        try:
            # Stage 1: Fetch
            print("\n" + "="*60)
            print("📥 STAGE 1: FETCHING REPOSITORY")
            print("="*60)

            fetch_result = self._stage_fetch(repo_url, github_token)
            if fetch_result.get('error'):
                return fetch_result

            # Stage 2: Analyze
            print("\n" + "="*60)
            print("🤖 STAGE 2: AI ANALYSIS WITH BEDROCK")
            print("="*60)

            analysis_result = self._stage_analyze(fetch_result)
            if analysis_result.get('error'):
                return analysis_result

            # Stage 3: Score
            print("\n" + "="*60)
            print("📊 STAGE 3: SCORING & RECOMMENDATIONS")
            print("="*60)

            score_result = self._stage_score(analysis_result)
            if score_result.get('error'):
                return score_result

            # Final result
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            final_result = {
                'status': 'success',
                'pipeline': 'complete',
                'execution_time_seconds': duration,
                'stages': {
                    'fetch': fetch_result,
                    'analyze': analysis_result,
                    'score': score_result
                },
                'summary': {
                    'repo_url': repo_url,
                    'repo_id': fetch_result.get('repo_id'),
                    'health_score': score_result.get('health_score'),
                    'total_security_issues': score_result['analysis']['total_security_issues'],
                    'total_debt_issues': score_result['analysis']['total_debt_issues'],
                    'critical_issues': score_result['analysis']['critical_issues'],
                    'quick_wins': score_result['analysis']['quick_wins']
                }
            }

            print("\n" + "="*60)
            print("✅ PIPELINE COMPLETE")
            print("="*60)
            print(f"🏆 Health Score: {final_result['summary']['health_score']}/100")
            print(f"🔍 Security Issues: {final_result['summary']['total_security_issues']}")
            print(f"💸 Technical Debt: {final_result['summary']['total_debt_issues']}")
            print(f"⚡ Quick Wins: {final_result['summary']['quick_wins']}")
            print(f"⏱️  Execution Time: {duration:.1f} seconds")

            return final_result

        except Exception as e:
            import traceback
            error_msg = str(e)
            tb = traceback.format_exc()

            print(f"\n❌ PIPELINE ERROR: {error_msg}")

            return {
                'status': 'error',
                'error': error_msg,
                'traceback': tb,
                'stage': 'unknown'
            }

    def _stage_fetch(self, repo_url, github_token=None):
        """Stage 1: Fetch repository data"""
        try:
            if self.mock_mode:
                # Mock data for testing
                return self._mock_fetch(repo_url)
            
            if self.use_lambda:
                # Call fetcher lambda
                payload = {
                    'repo_url': repo_url
                }
                if github_token:
                    payload['github_token'] = github_token

                response = self.lambda_client.invoke(
                    FunctionName='githopper-fetcher',
                    InvocationType='RequestResponse',
                    Payload=json.dumps(payload)
                )

                result = json.loads(response['Payload'].read())
                fetch_data = json.loads(result['body'])

            else:
                # Local execution
                from lambdas.fetcher.handler import lambda_handler
                event = {'repo_url': repo_url}
                if github_token:
                    event['github_token'] = github_token

                result = lambda_handler(event, None)
                fetch_data = json.loads(result['body'])

            if result.get('statusCode') != 200:
                return {'error': fetch_data.get('error', 'Fetch failed')}

            return fetch_data

        except Exception as e:
            return {'error': f'Fetch stage failed: {str(e)}'}

    def _mock_fetch(self, repo_url):
        """Mock fetch for testing without GitHub API"""
        import hashlib
        repo_id = hashlib.md5(repo_url.encode()).hexdigest()[:8]
        
        # Mock files with test data
        mock_files = [
            {
                'path': 'config/db.py',
                'language': 'python',
                'content': '''
import requests
import os

# Database config
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "admin123"
API_TOKEN = "sk-proj-abc123xyz"

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def process_data(data):
    result = eval(data)
    return result
''',
                'size_bytes': 250,
                'debt_signals': ['hardcoded_secrets', 'sql_injection'],
                'debt_signal_count': 2
            },
            {
                'path': 'requirements.txt',
                'language': 'text',
                'content': '''
flask==0.12.0
requests==2.18.0
django==2.0.0
''',
                'size_bytes': 50,
                'debt_signals': ['outdated_dependencies'],
                'debt_signal_count': 1
            }
        ]
        
        # Mock chunks
        mock_chunks = [
            {
                'filename': 'config/db.py',
                'content': 'AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"',
                'language': 'python',
                'char_count': 45
            },
            {
                'filename': 'config/db.py', 
                'content': 'query = "SELECT * FROM users WHERE id = " + user_id',
                'language': 'python',
                'char_count': 55
            }
        ]
        
        return {
            'repo_id': repo_id,
            'repo_url': repo_url,
            'total_files': len(mock_files),
            'categories': {'config': 1, 'dependencies': 1, 'source_code': 1},
            'chunks': mock_chunks,
            'files': mock_files
        }

    def _stage_analyze(self, fetch_result):
        """Stage 2: Analyze with Bedrock"""
        try:
            chunks = fetch_result.get('chunks', [])
            files = fetch_result.get('files', [])

            if self.use_lambda:
                # Call bedrock analyzer lambda
                payload = {
                    'repo_id': fetch_result['repo_id'],
                    'repo_url': fetch_result['repo_url'],
                    'chunks': chunks,
                    'total_files': len(files)
                }

                response = self.lambda_client.invoke(
                    FunctionName='githopper-analyzer',
                    InvocationType='RequestResponse',
                    Payload=json.dumps(payload)
                )

                result = json.loads(response['Payload'].read())
                analysis_data = json.loads(result['body'])

            else:
                # Local execution - use existing scan_all_chunks
                all_findings = scan_all_chunks(chunks)

                analysis_data = {
                    'repo_id': fetch_result['repo_id'],
                    'repo_url': fetch_result['repo_url'],
                    'security_findings': all_findings.get('security_findings', []),
                    'debt_findings': all_findings.get('debt_findings', []),
                    'chunks_scanned': len(chunks),
                    'total_files': len(files)
                }

            return analysis_data

        except Exception as e:
            return {'error': f'Analysis stage failed: {str(e)}'}

    def _stage_score(self, analysis_result):
        """Stage 3: Score the results"""
        try:
            if self.use_lambda:
                # Call scorer lambda
                payload = analysis_result

                response = self.lambda_client.invoke(
                    FunctionName='githopper-scorer',
                    InvocationType='RequestResponse',
                    Payload=json.dumps(payload)
                )

                result = json.loads(response['Payload'].read())
                score_data = json.loads(result['body'])

            else:
                # Local execution
                from lambdas.scorer.handler import lambda_handler
                event = {'body': analysis_result}

                result = lambda_handler(event, None)
                score_data = json.loads(result['body'])

            if result.get('statusCode') != 200:
                return {'error': score_data.get('error', 'Scoring failed')}

            return score_data

        except Exception as e:
            return {'error': f'Scoring stage failed: {str(e)}'}


# CLI interface for testing
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='GitHopper Full Pipeline')
    parser.add_argument('repo_url', help='GitHub repository URL')
    parser.add_argument('--token', help='GitHub token (optional)')
    parser.add_argument('--use-lambda', action='store_true', help='Use Lambda functions')
    parser.add_argument('--mock', action='store_true', help='Use mock data for testing')

    args = parser.parse_args()

    if args.use_lambda:
        os.environ['USE_LAMBDA'] = 'true'
    
    if args.mock:
        os.environ['MOCK_MODE'] = 'true'

    pipeline = GitHopperPipeline()
    result = pipeline.run_full_pipeline(args.repo_url, args.token)

    print("\n" + "="*60)
    print("FINAL RESULT")
    print("="*60)
    print(json.dumps(result, indent=2))