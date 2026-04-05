"""
Audit Engine for comprehensive security and code quality audits.
"""

class AuditEngine:
    """Performs comprehensive audits on repository scan results."""
    
    @staticmethod
    def audit_repository(aggregated_analysis):
        """
        Audit a repository's aggregated analysis results.
        
        Args:
            aggregated_analysis: The combined analysis from the pipeline
            
        Returns:
            dict: Audit report with findings and recommendations
        """
        if not aggregated_analysis:
            return {
                "status": "error",
                "message": "No analysis data provided",
                "findings": []
            }
        
        # Extract data from aggregated analysis
        health_score = aggregated_analysis.get("overall_health_score", 0)
        security_findings = aggregated_analysis.get("security_findings", [])
        debt_findings = aggregated_analysis.get("debt_findings", [])
        quick_wins = aggregated_analysis.get("quick_wins", [])
        
        # Count issues by severity
        critical = len([f for f in [*security_findings, *debt_findings] if f.get("severity") == "CRITICAL"])
        high = len([f for f in [*security_findings, *debt_findings] if f.get("severity") == "HIGH"])
        medium = len([f for f in [*security_findings, *debt_findings] if f.get("severity") == "MEDIUM"])
        low = len([f for f in [*security_findings, *debt_findings] if f.get("severity") == "LOW"])
        
        total_issues = critical + high + medium + low
        
        # Generate risk assessment
        if health_score >= 80:
            risk_level = "LOW"
            recommendation = "Codebase is healthy. Continue monitoring."
        elif health_score >= 60:
            risk_level = "MEDIUM"
            recommendation = "Address medium-severity issues to improve health score."
        elif health_score >= 40:
            risk_level = "HIGH"
            recommendation = "Urgent: Multiple critical issues require immediate attention."
        else:
            risk_level = "CRITICAL"
            recommendation = "CRITICAL: Extensive security and quality issues detected. Immediate remediation required."
        
        return {
            "status": "success",
            "health_score": health_score,
            "risk_level": risk_level,
            "total_issues": total_issues,
            "issues_by_severity": {
                "critical": critical,
                "high": high,
                "medium": medium,
                "low": low
            },
            "security_issues": len(security_findings),
            "debt_issues": len(debt_findings),
            "quick_wins_count": len(quick_wins),
            "recommendation": recommendation,
            "security_findings": security_findings[:10],  # Top 10
            "debt_findings": debt_findings[:10],  # Top 10
            "quick_wins": quick_wins[:5]  # Top 5
        }
