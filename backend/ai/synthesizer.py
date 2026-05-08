# =============================================================================
# synthesizer.py — Post-scan synthesis engine for GitHopper
# Owner: Ananya (AI / OpenClaw Eng)
#
# What this does:
#   1. Deduplicates findings across chunks
#   2. Assigns confidence scores to each finding
#   3. Produces a prioritized Top 5 action list
#   4. Classifies the repo into an archetype
# =============================================================================

import json
import logging

logger = logging.getLogger(__name__)

try:
    from .openclaw_client import invoke_openclaw
except ImportError:
    from openclaw_client import invoke_openclaw

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

DEDUP_AND_PRIORITIZE_PROMPT = """
You are a senior security engineer reviewing a list of findings from an automated scan.

Your job:
1. Remove duplicate findings (same issue in same file reported multiple times)
2. Assign a confidence score to each finding (HIGH / MEDIUM / LOW) based on how certain you are it's a real issue
3. Flag likely false positives — e.g. a "secret" in a test file is probably intentional
4. Return the top 5 most important findings to fix first, ranked by: severity first, then confidence, then estimated fix time

Return ONLY valid JSON, no preamble:
{{
  "top_5_actions": [
    {{
      "rank": 1,
      "type": "HARDCODED_SECRET",
      "severity": "CRITICAL",
      "file": "config/db.py",
      "explanation": "plain English explanation",
      "fix": "exact fix instruction",
      "remediated_code": "fixed code",
      "estimated_minutes": 10,
      "confidence": "HIGH",
      "false_positive_risk": "LOW",
      "business_impact": "what happens if not fixed"
    }}
  ],
  "total_findings": 12,
  "deduplicated_from": 18,
  "false_positives_removed": 3
}}

Findings to analyze:
{all_findings}
"""

ARCHETYPE_PROMPT = """
You are a codebase health analyst. Based on the scan results below, classify this repository into exactly one archetype.

Archetypes:
- STARTUP_DEBT_BOMB: moves fast, ignores debt, security is okay but code quality is poor
- LEGACY_ROTTING: high debt, outdated deps, low test coverage, architectural issues
- MISCONFIGURED_CLOUD: code is clean but infra/IaC/IAM is the problem
- SECURITY_BLIND_SPOT: hardcoded secrets pattern, good code quality otherwise
- ACTUALLY_HEALTHY: minimal issues, good practices overall

Also produce a risk radar with scores 0-100 for 5 dimensions.

Return ONLY valid JSON, no preamble:
{{
  "archetype": "STARTUP_DEBT_BOMB",
  "archetype_description": "2-3 sentence plain English description of what this means for this specific repo",
  "risk_radar": {{
    "security": 80,
    "debt": 40,
    "dependencies": 60,
    "iac": 20,
    "iam": 50
  }},
  "health_score": 64,
  "one_liner": "This repo ships fast but is one leaked key away from a breach."
}}

Scan results:
Security findings: {security_count} issues
Debt findings: {debt_count} issues
Finding types: {finding_types}
Severity breakdown: {severity_breakdown}
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def invoke_openclaw_json(prompt: str) -> dict:
    try:
        return invoke_openclaw(prompt, "synthesizer")
    except Exception as e:
        logger.error(f"Synthesizer OpenClaw error: {e}")
        return {}


def get_severity_breakdown(findings: list) -> dict:
    breakdown = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in findings:
        sev = f.get("severity", "LOW")
        breakdown[sev] = breakdown.get(sev, 0) + 1
    return breakdown


def get_finding_types(findings: list) -> list:
    return list(set(f.get("type", "UNKNOWN") for f in findings))


# ---------------------------------------------------------------------------
# Main synthesis function — called after scan_all_chunks()
# ---------------------------------------------------------------------------

def synthesize(scan_results: dict) -> dict:
    """
    Takes raw scan output and produces enriched report.

    Input:
        {
            "security_findings": [...],
            "debt_findings": [...]
        }

    Output:
        {
            "top_5_actions": [...],
            "archetype": "STARTUP_DEBT_BOMB",
            "risk_radar": {...},
            "health_score": 64,
            "one_liner": "...",
            "total_security": 8,
            "total_debt": 4,
            "deduplicated_from": 18
        }
    """
    security = scan_results.get("security_findings", [])
    debt = scan_results.get("debt_findings", [])
    all_findings = security + debt

    if not all_findings:
        return {
            "top_5_actions": [],
            "archetype": "ACTUALLY_HEALTHY",
            "risk_radar": {
                "security": 10, "debt": 10,
                "dependencies": 10, "iac": 10, "iam": 10
            },
            "health_score": 95,
            "one_liner": "No significant issues found.",
            "total_security": 0,
            "total_debt": 0
        }

    # Step 1 — dedup + top 5
    dedup_result = invoke_openclaw_json(
        DEDUP_AND_PRIORITIZE_PROMPT.format(
            all_findings=json.dumps(all_findings, indent=2)
        )
    )

    # Step 2 — archetype + risk radar
    severity_breakdown = get_severity_breakdown(all_findings)
    finding_types = get_finding_types(all_findings)

    archetype_result = invoke_openclaw_json(
        ARCHETYPE_PROMPT.format(
            security_count=len(security),
            debt_count=len(debt),
            finding_types=", ".join(finding_types),
            severity_breakdown=json.dumps(severity_breakdown)
        )
    )

    return {
        "top_5_actions": dedup_result.get("top_5_actions", []),
        "total_findings": dedup_result.get("total_findings", len(all_findings)),
        "deduplicated_from": dedup_result.get("deduplicated_from", len(all_findings)),
        "false_positives_removed": dedup_result.get("false_positives_removed", 0),
        "archetype": archetype_result.get("archetype", "UNKNOWN"),
        "archetype_description": archetype_result.get("archetype_description", ""),
        "risk_radar": archetype_result.get("risk_radar", {}),
        "health_score": archetype_result.get("health_score", 50),
        "one_liner": archetype_result.get("one_liner", ""),
        "total_security": len(security),
        "total_debt": len(debt)
    }