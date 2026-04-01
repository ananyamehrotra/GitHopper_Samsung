import json
import os
import sys

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))


def calculate_health_score(security_findings, debt_findings):
    """
    Calculate overall health score based on findings
    """
    health_score = 100

    # Penalize for security issues
    for finding in security_findings:
        severity = finding.get('severity', 'LOW')
        if severity == 'CRITICAL':
            health_score -= 20
        elif severity == 'HIGH':
            health_score -= 10
        elif severity == 'MEDIUM':
            health_score -= 5
        elif severity == 'LOW':
            health_score -= 1

    # Penalize for debt issues (less severe)
    for finding in debt_findings:
        severity = finding.get('severity', 'LOW')
        if severity == 'CRITICAL':
            health_score -= 5
        elif severity == 'HIGH':
            health_score -= 3
        elif severity == 'MEDIUM':
            health_score -= 2
        elif severity == 'LOW':
            health_score -= 0.5

    return max(0, min(100, health_score))


def categorize_findings(findings):
    """
    Categorize findings by type and severity
    """
    categories = {
        'critical': [],
        'high': [],
        'medium': [],
        'low': []
    }

    for finding in findings:
        severity = finding.get('severity', 'LOW').lower()
        if severity in categories:
            categories[severity].append(finding)

    return categories


def lambda_handler(event, context):
    """
    AWS Lambda handler for scoring analysis results
    """
    try:
        print("[SCORER] Starting scoring operation...")

        # Extract analysis results from event
        body = event.get('body', '{}')
        if isinstance(body, str):
            data = json.loads(body)
        else:
            data = body

        repo_id = data.get('repo_id')
        repo_url = data.get('repo_url')
        security_findings = data.get('security_findings', [])
        debt_findings = data.get('debt_findings', [])
        chunks_scanned = data.get('chunks_scanned', 0)
        total_files = data.get('total_files', 0)

        if not repo_id or not repo_url:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'repo_id and repo_url are required'})
            }

        print(f"[SCORER] Scoring repo: {repo_url} ({repo_id})")

        # Calculate health score
        health_score = calculate_health_score(security_findings, debt_findings)

        # Categorize findings
        security_categories = categorize_findings(security_findings)
        debt_categories = categorize_findings(debt_findings)

        # Identify quick wins (estimated_minutes < 30)
        quick_wins = [
            f for f in security_findings
            if f.get('estimated_minutes', 60) < 30
        ]

        # Critical issues
        critical_issues = security_categories['critical']

        # Generate recommendations
        recommendations = []

        if len(critical_issues) > 0:
            recommendations.append({
                'priority': 'CRITICAL',
                'action': 'Address critical security issues immediately',
                'count': len(critical_issues)
            })

        if len(quick_wins) > 0:
            recommendations.append({
                'priority': 'HIGH',
                'action': 'Implement quick wins to improve score rapidly',
                'count': len(quick_wins)
            })

        if health_score < 70:
            recommendations.append({
                'priority': 'MEDIUM',
                'action': 'Comprehensive code review and refactoring needed',
                'score': health_score
            })

        # Prepare response
        result = {
            'repo_id': repo_id,
            'repo_url': repo_url,
            'health_score': health_score,
            'chunks_scanned': chunks_scanned,
            'total_files': total_files,
            'analysis': {
                'total_security_issues': len(security_findings),
                'total_debt_issues': len(debt_findings),
                'critical_issues': len(critical_issues),
                'quick_wins': len(quick_wins)
            },
            'findings': {
                'security_findings': security_findings,
                'debt_findings': debt_findings,
                'security_by_severity': {
                    'critical': len(security_categories['critical']),
                    'high': len(security_categories['high']),
                    'medium': len(security_categories['medium']),
                    'low': len(security_categories['low'])
                },
                'debt_by_severity': {
                    'critical': len(debt_categories['critical']),
                    'high': len(debt_categories['high']),
                    'medium': len(debt_categories['medium']),
                    'low': len(debt_categories['low'])
                },
                'quick_wins': quick_wins,
                'critical_issues': critical_issues
            },
            'recommendations': recommendations,
            'scoring_metadata': {
                'scoring_version': '1.0',
                'scoring_algorithm': 'weighted_penalty',
                'max_score': 100,
                'min_score': 0
            }
        }

        print(f"[SCORER] Complete: Health score {health_score}/100")

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"[SCORER] ERROR: {error_msg}")
        print(f"[SCORER] Traceback: {tb}")

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': error_msg,
                'type': type(e).__name__,
                'traceback': tb
            })
        }