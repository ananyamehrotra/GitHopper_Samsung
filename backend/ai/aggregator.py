# =============================================================================
# aggregator.py — Organize Bedrock findings by category for specialized scorers
# Owner: Ananya (Scoring & Reporting)
# 
# Purpose: 
#   Takes raw vulnerabilities from bedrock_client and groups them by type
#   Each scorer (SecurityAudit, DebtReport, BranchAnalysis, HealthScore) 
#   gets its specialized data
# =============================================================================

import json
import logging
import sys
import os

# Add parent directory to path to import billing module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    import billing
except ImportError:
    billing = None

logger = logging.getLogger(__name__)

# Category mapping: file_type -> score category
CATEGORY_MAP = {
    "app": "security",      # APP_SECURITY_PROMPT
    "iac": "infrastructure", # IAC_SECURITY_PROMPT
    "iam": "iam_security",  # IAM_PROMPT
    "deps": "dependencies",  # DEPENDENCY_PROMPT
    "debt": "code_quality"   # DEBT_PROMPT (assigned after analysis)
}

def categorize_vulnerabilities(vulnerabilities: list) -> dict:
    """
    Organize vulnerabilities by security category.
    
    Input: Raw vulnerabilities from bedrock_client.scan_all_chunks()
    Output: {
        "security": {...},           # App code + auth vulnerabilities
        "infrastructure": {...},      # S3, security groups, unencrypted storage
        "iam_security": {...},        # Wildcard permissions, policy issues
        "dependencies": {...},        # Outdated/vulnerable packages
        "code_quality": {...},        # Complexity, duplication, debt
        "summary": {...}
    }
    """
    
    categorized = {
        "security": {"critical": 0, "high": 0, "medium": 0, "low": 0, "findings": []},
        "infrastructure": {"critical": 0, "high": 0, "medium": 0, "low": 0, "findings": []},
        "iam_security": {"critical": 0, "high": 0, "medium": 0, "low": 0, "findings": []},
        "dependencies": {"critical": 0, "high": 0, "medium": 0, "low": 0, "findings": []},
        "code_quality": {"critical": 0, "high": 0, "medium": 0, "low": 0, "findings": []}
    }
    
    # Keywords that indicate code quality/debt issues
    code_quality_keywords = [
        "complexity", "debt", "duplication", "long_function", "function", "conditional",
        "parameter", "import", "unused", "dead_code", "refactor", "maintainability",
        "naming", "comment", "documentation", "smell", "code_smell"
    ]
    
    for vuln in vulnerabilities:
        file_type = vuln.get("file_type", "app")
        severity = vuln.get("severity", "MEDIUM").lower()
        vuln_type_lower = vuln.get("type", "").lower()
        
        # Map file type to category
        if file_type == "iam":
            category = "iam_security"
        elif file_type == "iac":
            category = "infrastructure"
        elif file_type == "deps":
            category = "dependencies"
        elif any(keyword in vuln_type_lower for keyword in code_quality_keywords):
            category = "code_quality"
        else:
            category = "security"
        
        # Add to category
        categorized[category]["findings"].append(vuln)
        categorized[category][severity] = categorized[category].get(severity, 0) + 1
    
    return categorized


def aggregate_for_security_audit(categorized: dict) -> dict:
    """
    Scorer input for SECURITY AUDIT page.
    Focuses on: security + infrastructure + iam_security vulnerabilities
    """
    security_findings = categorized.get("security", {}).get("findings", [])
    infra_findings = categorized.get("infrastructure", {}).get("findings", [])
    iam_findings = categorized.get("iam_security", {}).get("findings", [])
    
    all_findings = security_findings + infra_findings + iam_findings
    
    # Count by severity
    critical = sum(1 for f in all_findings if f.get("severity", "").upper() == "CRITICAL")
    high = sum(1 for f in all_findings if f.get("severity", "").upper() == "HIGH")
    medium = sum(1 for f in all_findings if f.get("severity", "").upper() == "MEDIUM")
    low = sum(1 for f in all_findings if f.get("severity", "").upper() == "LOW")
    
    return {
        "audit_type": "SECURITY_AUDIT",
        "findings": all_findings,
        "summary": {
            "total_issues": len(all_findings),
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "categories": {
                "app_security": len(security_findings),
                "infrastructure": len(infra_findings),
                "iam_risks": len(iam_findings)
            }
        },
        "risk_indicators": {
            "has_critical": critical > 0,
            "has_high": high > 0,
            "critical_percentage": (critical / len(all_findings) * 100) if all_findings else 0
        }
    }


def aggregate_for_debt_report(categorized: dict) -> dict:
    """
    Scorer input for DEBT REPORT page.
    Focuses on: code_quality + dependencies technical debt
    """
    debt_findings = categorized.get("code_quality", {}).get("findings", [])
    dep_findings = categorized.get("dependencies", {}).get("findings", [])
    
    all_findings = debt_findings + dep_findings
    
    # Count by severity
    critical = sum(1 for f in all_findings if f.get("severity", "").upper() == "CRITICAL")
    high = sum(1 for f in all_findings if f.get("severity", "").upper() == "HIGH")
    medium = sum(1 for f in all_findings if f.get("severity", "").upper() == "MEDIUM")
    low = sum(1 for f in all_findings if f.get("severity", "").upper() == "LOW")
    
    # Estimate fix time
    total_estimated_minutes = sum(f.get("estimated_minutes_to_fix", 0) for f in all_findings)
    total_estimated_hours = total_estimated_minutes / 60
    
    return {
        "report_type": "DEBT_REPORT",
        "findings": all_findings,
        "summary": {
            "total_issues": len(all_findings),
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "categories": {
                "code_complexity": len(debt_findings),
                "dependency_issues": len(dep_findings)
            }
        },
        "effort_estimate": {
            "total_minutes": total_estimated_minutes,
            "total_hours": round(total_estimated_hours, 1),
            "sprints_needed": max(1, round(total_estimated_hours / 40, 1))  # 1 sprint = 40 hours
        }
    }


def aggregate_for_branch_analysis(categorized: dict, branch_name: str = "main") -> dict:
    """
    Scorer input for ANALYSE BRANCHES page.
    Shows vulnerability breakdown by branch/category
    """
    all_findings = []
    for category in categorized.values():
        if isinstance(category, dict) and "findings" in category:
            all_findings.extend(category["findings"])
    
    # Count by type
    security_count = sum(1 for f in all_findings if "security" in f.get("type", "").lower())
    infra_count = sum(1 for f in all_findings if f.get("file_type") == "iac")
    iam_count = sum(1 for f in all_findings if f.get("file_type") == "iam")
    dep_count = sum(1 for f in all_findings if f.get("file_type") == "deps")
    debt_count = sum(1 for f in all_findings if "complexity" in f.get("type", "").lower())
    
    # Get billing info
    billing_info = {}
    if billing:
        billing_info = billing.get_billing_summary()
    
    return {
        "analysis_type": "BRANCH_ANALYSIS",
        "branch": branch_name,
        "findings": all_findings,
        "summary": {
            "total_issues": len(all_findings),
            "breakdown": {
                "security_issues": security_count,
                "infrastructure_misconfigs": infra_count,
                "iam_policy_risks": iam_count,
                "dependency_problems": dep_count,
                "code_debt": debt_count
            }
        },
        "by_severity": {
            "critical": sum(1 for f in all_findings if f.get("severity", "").upper() == "CRITICAL"),
            "high": sum(1 for f in all_findings if f.get("severity", "").upper() == "HIGH"),
            "medium": sum(1 for f in all_findings if f.get("severity", "").upper() == "MEDIUM"),
            "low": sum(1 for f in all_findings if f.get("severity", "").upper() == "LOW")
        },
        "billing": billing_info,  # Add billing to branch_analysis
    }


def aggregate_for_health_score(categorized: dict, cost_tracker: dict = None) -> dict:
    """
    Scorer input for HEALTH SCORE page.
    Calculates overall repo health across all dimensions
    """
    all_findings = []
    for category in categorized.values():
        if isinstance(category, dict) and "findings" in category:
            all_findings.extend(category["findings"])
    
    # Count critical issues (major impact on health)
    critical_count = sum(1 for f in all_findings if f.get("severity", "").upper() == "CRITICAL")
    high_count = sum(1 for f in all_findings if f.get("severity", "").upper() == "HIGH")
    medium_count = sum(1 for f in all_findings if f.get("severity", "").upper() == "MEDIUM")
    low_count = sum(1 for f in all_findings if f.get("severity", "").upper() == "LOW")
    
    # Calculate scores for each dimension (0-100, higher is better)
    security_score = max(0, 100 - (critical_count * 30 + high_count * 15 + medium_count * 5))
    infra_score = max(0, 100 - (len(categorized.get("infrastructure", {}).get("findings", [])) * 20))
    iam_score = max(0, 100 - (len(categorized.get("iam_security", {}).get("findings", [])) * 25))
    debt_score = max(0, 100 - (len(categorized.get("code_quality", {}).get("findings", [])) * 10))
    dep_score = max(0, 100 - (len(categorized.get("dependencies", {}).get("findings", [])) * 15))
    
    # Overall health = weighted average
    overall_score = round((security_score * 0.3 + infra_score * 0.2 + iam_score * 0.15 + debt_score * 0.2 + dep_score * 0.15))
    
    return {
        "score_type": "HEALTH_SCORE",
        "overall_health": overall_score,
        "dimension_scores": {
            "security": security_score,
            "infrastructure": infra_score,
            "iam_security": iam_score,
            "code_quality": debt_score,
            "dependencies": dep_score
        },
        "issue_summary": {
            "total_issues": len(all_findings),
            "critical": critical_count,
            "high": high_count,
            "medium": medium_count,
            "low": low_count
        },
        "cost_info": cost_tracker or {},
        "recommendations": generate_health_recommendations(overall_score, critical_count)
    }


def generate_health_recommendations(health_score: int, critical_count: int) -> list:
    """Generate actionable recommendations based on health score"""
    recommendations = []
    
    if critical_count > 0:
        recommendations.append(f"🔴 URGENT: Fix {critical_count} critical vulnerabilities immediately")
    
    if health_score < 30:
        recommendations.append("⚠️ Repo is in critical state - do not deploy")
        recommendations.append("- Start with Critical issues in Security Audit")
        recommendations.append("- Then address High severity issues")
    elif health_score < 60:
        recommendations.append("⚠️ Repo has significant issues - plan fixes")
        recommendations.append("- Review Security Audit for exploitation risks")
        recommendations.append("- Address infrastructure misconfigurations")
    elif health_score < 80:
        recommendations.append("✓ Repo is generally healthy - plan improvements")
        recommendations.append("- Reduce technical debt gradually")
        recommendations.append("- Update outdated dependencies")
    else:
        recommendations.append("✓ Repo is in good health - maintain current practices")
    
    return recommendations


def aggregate_all(vulnerabilities: list, cost_tracker: dict = None, branch_name: str = "main") -> dict:
    """
    Master aggregation function.
    Takes raw bedrock output and produces data for all 4 scorers.
    """
    
    print(f"\n{'='*60}")
    print(f"📊 AGGREGATING FINDINGS BY CATEGORY")
    print(f"{'='*60}")
    
    # Step 1: Categorize
    categorized = categorize_vulnerabilities(vulnerabilities)
    
    print(f"Security findings: {len(categorized['security']['findings'])}")
    print(f"Infrastructure findings: {len(categorized['infrastructure']['findings'])}")
    print(f"IAM findings: {len(categorized['iam_security']['findings'])}")
    print(f"Dependency findings: {len(categorized['dependencies']['findings'])}")
    print(f"Code quality findings: {len(categorized['code_quality']['findings'])}")
    
    # Step 2: Create scorer-specific aggregations
    return {
        "security_audit": aggregate_for_security_audit(categorized),
        "debt_report": aggregate_for_debt_report(categorized),
        "branch_analysis": aggregate_for_branch_analysis(categorized, branch_name),
        "health_score": aggregate_for_health_score(categorized, cost_tracker),
        "categorized": categorized  # Raw categorized data
    }
