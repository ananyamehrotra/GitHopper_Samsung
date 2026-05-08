#!/usr/bin/env python
"""
Mock debt findings generator for testing when OpenClaw is unavailable.
Used to populate debt_report and other aggregated data without OpenClaw.
"""
import json

MOCK_DEBT_FINDINGS = [
    {
        "type": "HIGH_CYCLOMATIC_COMPLEXITY",
        "severity": "HIGH",
        "file": "src/components/AppLayout.jsx",
        "file_type": "app",
        "line_range": "45-120",
        "explanation": "Function has cyclomatic complexity of 18, exceeds recommended max of 10. Multiple nested conditions and branches make code hard to test and maintain.",
        "business_impact": "Increased bug risk, harder to maintain and test. Reduces team velocity on related features.",
        "estimated_minutes_to_fix": 45,
        "remediation": "Break into smaller functions, extract conditionals into helper functions, use strategy pattern for different code paths."
    },
    {
        "type": "CODE_DUPLICATION",
        "severity": "MEDIUM",
        "file": "frontend/src/services/apiClient.js",
        "file_type": "app",
        "line_range": "12-25, 45-58, 120-133",
        "explanation": "Same fetch-with-retry logic is duplicated 3 times across the file. Should be extracted to reusable utility.",
        "business_impact": "Bug fixes need to be applied in multiple places. Increases maintenance burden.",
        "estimated_minutes_to_fix": 20,
        "remediation": "Extract retry logic into a utility function: createRetryableFetch(). Use throughout codebase."
    },
    {
        "type": "LONG_FUNCTION",
        "severity": "MEDIUM",
        "file": "backend/ai/aggregator.py",
        "file_type": "app",
        "line_range": "240-350",
        "explanation": "Function 'aggregate_all' is 110 lines long. Exceeds recommended max of 50 lines. Does too many things.",
        "business_impact": "Hard to understand, test, and modify. Violates single responsibility principle.",
        "estimated_minutes_to_fix": 60,
        "remediation": "Split into: aggregate_by_severity(), aggregate_by_category(), aggregate_by_file(). Use composition to combine."
    },
    {
        "type": "MISSING_ERROR_HANDLING",
        "severity": "HIGH",
        "file": "frontend/src/pages/DashboardPage.jsx",
        "file_type": "app",
        "line_range": "77-92",
        "explanation": "fetch() call has no catch block for network errors. Page will crash silently on failed API calls.",
        "business_impact": "Poor user experience. Users won't know if scan failed. Hard to debug production issues.",
        "estimated_minutes_to_fix": 15,
        "remediation": "Add try-catch. Show error toast to user. Log to Sentry. Implement retry logic."
    },
    {
        "type": "UNUSED_IMPORT",
        "severity": "LOW",
        "file": "backend/utils/file_classifier.py",
        "file_type": "app",
        "line_range": "3",
        "explanation": "Module 'os' is imported but never used in this file.",
        "business_impact": "Adds to code bloat. Makes linting fail in strict mode.",
        "estimated_minutes_to_fix": 2,
        "remediation": "Remove: `import os`"
    },
    {
        "type": "COMPLEX_CONDITIONAL",
        "severity": "MEDIUM",
        "file": "backend/mcp_server/analyzer.py",
        "file_type": "app",
        "line_range": "156-162",
        "explanation": "Nested if statement is hard to read: if a and (b or c) and not (d and e). Multiple boolean checks in single line.",
        "business_impact": "Bug risk. Hard to understand intent. Difficult to unit test individual conditions.",
        "estimated_minutes_to_fix": 10,
        "remediation": "Extract to named boolean: is_valid_analysis = check_all_conditions(a,b,c,d,e). Use guard clauses."
    },
    {
        "type": "LARGE_PARAMETER_LIST",
        "severity": "LOW",
        "file": "backend/ai/synthesizer.py",
        "file_type": "app",
        "line_range": "45",
        "explanation": "Function 'synthesize_report' takes 8 parameters. Exceeds recommended max of 3.",
        "business_impact": "Hard to call correctly. Easy to pass arguments in wrong order. Makes testing harder.",
        "estimated_minutes_to_fix": 30,
        "remediation": "Group parameters: create ReportConfig dataclass with fields: vulnerabilities, billing, branch_name, etc."
    },
    {
        "type": "OUTDATED_DEPENDENCY",
        "severity": "HIGH",
        "file": "package.json",
        "file_type": "deps",
        "line_range": "15",
        "explanation": "jsPDF v2.4.0 is 6 months old. Current stable is v2.5.1. Has bug fixes and performance improvements.",
        "business_impact": "Missing security patches. Performance issues. PDF generation may fail in some edge cases.",
        "estimated_minutes_to_fix": 10,
        "remediation": "Run: npm update jspdf@latest. Test PDF download. Verify no breaking changes."
    },
]

def get_mock_debt_report():
    """Return a mock debt report for testing."""
    all_findings = MOCK_DEBT_FINDINGS.copy()
    
    critical = sum(1 for f in all_findings if f.get("severity") == "CRITICAL")
    high = sum(1 for f in all_findings if f.get("severity") == "HIGH")
    medium = sum(1 for f in all_findings if f.get("severity") == "MEDIUM")
    low = sum(1 for f in all_findings if f.get("severity") == "LOW")
    
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
                "code_complexity": 3,  # HIGH_CYCLOMATIC_COMPLEXITY, LONG_FUNCTION, COMPLEX_CONDITIONAL
                "dependency_issues": 1  # OUTDATED_DEPENDENCY
            }
        },
        "effort_estimate": {
            "total_minutes": total_estimated_minutes,
            "total_hours": round(total_estimated_hours, 1),
            "sprints_needed": max(1, round(total_estimated_hours / 40, 1))
        }
    }

if __name__ == "__main__":
    import json
    report = get_mock_debt_report()
    print(json.dumps(report, indent=2))
