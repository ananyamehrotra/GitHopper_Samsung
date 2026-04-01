import hashlib
import json
from typing import Any, Dict, List

from chunker import chunk_code
from github_client import fetch_repo
from lambdas.scorer.handler import lambda_handler as scorer_lambda_handler

from .analyzer import build_debt_findings_from_files, scan_all_chunks_with_context
from .autofix import generate_and_validate_fixes
from .diffing import build_file_metadata, compute_incremental_changes
from .storage import MCPMemoryStore


def repo_id_from_url(repo_url: str) -> str:
    return hashlib.md5(repo_url.encode()).hexdigest()[:8]


def _severity_rank(severity: str) -> int:
    order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
    return order.get((severity or "LOW").upper(), 1)


def _issue_fingerprint(issue: Dict[str, Any]) -> str:
    raw = "|".join(
        [
            issue.get("file", issue.get("file_path", "unknown")),
            issue.get("type", "UNKNOWN"),
            str(issue.get("line_range", "?")),
            issue.get("explanation", issue.get("summary", ""))[:120],
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]


def _normalize_security_findings(vulnerabilities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    findings = []
    for vulnerability in vulnerabilities:
        findings.append(
            {
                **vulnerability,
                "file": vulnerability.get("file", "unknown"),
                "severity": vulnerability.get("severity", "LOW"),
                "estimated_minutes": vulnerability.get("estimated_minutes_to_fix", 15),
            }
        )
    return findings


def _issues_from_findings(security_findings: List[Dict[str, Any]], debt_findings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    issues: List[Dict[str, Any]] = []
    for finding in security_findings:
        issues.append(
            {
                "fingerprint": _issue_fingerprint(finding),
                "file_path": finding.get("file", "unknown"),
                "category": "security",
                "issue_type": finding.get("type", "UNKNOWN"),
                "severity": finding.get("severity", "LOW"),
                "status": "OPEN",
                "summary": finding.get("explanation", finding.get("type", "Security issue")),
                "metadata": {
                    "line_range": finding.get("line_range"),
                    "business_impact": finding.get("business_impact"),
                    "remediation": finding.get("remediation"),
                },
            }
        )
    for finding in debt_findings:
        issues.append(
            {
                "fingerprint": _issue_fingerprint(finding),
                "file_path": finding.get("file", "unknown"),
                "category": "debt",
                "issue_type": finding.get("type", "DEBT_SIGNAL"),
                "severity": finding.get("severity", "LOW"),
                "status": "OPEN",
                "summary": finding.get("summary", "Technical debt finding"),
                "metadata": finding.get("metadata", {}),
            }
        )
    issues.sort(key=lambda item: _severity_rank(item["severity"]), reverse=True)
    return issues


class ContinuousIntelligencePipeline:
    """
    Extension pipeline that wraps the existing fetch/chunk/score flow with:
    - memory
    - incremental scanning
    - context-aware analysis
    - auto-fix generation
    """

    def __init__(self, store: MCPMemoryStore = None):
        self.store = store or MCPMemoryStore()

    def run(
        self,
        repo_url: str,
        github_token: str = None,
        branch_name: str = "main",
        generate_fixes: bool = True,
    ) -> Dict[str, Any]:
        repo_id = repo_id_from_url(repo_url)
        files = fetch_repo(repo_url, github_token=github_token)
        file_map = {file["path"]: file for file in files}
        current_metadata = build_file_metadata(files)
        previous_snapshot = self.store.get_latest_snapshot(repo_id)
        previous_metadata = previous_snapshot["files"] if previous_snapshot else []
        changes = compute_incremental_changes(current_metadata, previous_metadata)
        unresolved = self.store.get_unresolved_issues(repo_id)
        unresolved_paths = {issue["file_path"] for issue in unresolved}

        if previous_snapshot is None:
            scan_mode = "full"
            selected_paths = [file["path"] for file in files]
        else:
            scan_mode = "incremental"
            selected_paths = sorted(
                set(changes["new_files"] + changes["modified_files"]) | unresolved_paths
            )

        selected_files = [file_map[path] for path in selected_paths if path in file_map]
        chunks = chunk_code(selected_files) if selected_files else []
        repo_context = self.store.get_context(repo_id)
        analysis = scan_all_chunks_with_context(chunks, repo_context, branch_name) if chunks else {
            "vulnerabilities": [],
            "vulnerable_files": [],
            "total_files_analyzed": 0,
            "files_with_issues": 0,
            "total_vulnerabilities": 0,
            "context_applied": True,
        }

        security_findings = _normalize_security_findings(analysis.get("vulnerabilities", []))
        debt_findings = build_debt_findings_from_files(selected_files)

        scorer_event = {
            "body": {
                "repo_id": repo_id,
                "repo_url": repo_url,
                "security_findings": security_findings,
                "debt_findings": debt_findings,
                "chunks_scanned": len(chunks),
                "total_files": len(files),
            }
        }
        score_response = scorer_lambda_handler(scorer_event, None)
        score_body = json.loads(score_response["body"])

        issues = _issues_from_findings(security_findings, debt_findings)
        stored = self.store.store_scan_results(
            repo_id=repo_id,
            repo_url=repo_url,
            branch_name=branch_name,
            scan_mode=scan_mode,
            issues=issues,
            summary={
                "total_files": len(files),
                "files_scanned": len(selected_files),
                "total_chunks": len(chunks),
                "analysis_summary": {
                    "security_findings": len(security_findings),
                    "debt_findings": len(debt_findings),
                },
            },
            scoring=score_body,
            change_summary=changes,
        )
        snapshot_info = self.store.store_snapshot(repo_id, branch_name, current_metadata)

        latest_context = self.store.get_context(repo_id)
        fixes = generate_and_validate_fixes(issues[:10], file_map, latest_context) if generate_fixes else []
        for fix in fixes:
            self.store.update_fix_status(
                repo_id=repo_id,
                issue_fingerprint=fix["fingerprint"],
                status="GENERATED",
                validation_status=fix["validation_status"],
                explanation=fix["explanation"],
                diff_patch=fix["diff"],
                remediated_code=fix["remediated_code"],
            )

        previous_scan = latest_context.get("history", [None, None])
        previous_score = None
        if len(previous_scan) > 1 and previous_scan[1]:
            previous_score = previous_scan[1].get("scoring", {}).get("health_score")
        current_score = score_body.get("health_score")

        return {
            "status": "success",
            "pipeline": "continuous_intelligence_extension",
            "repo_id": repo_id,
            "repo_url": repo_url,
            "branch_name": branch_name,
            "scan_mode": scan_mode,
            "data": {
                "total_files_fetched": len(files),
                "files_scanned": len(selected_files),
                "total_chunks": len(chunks),
                "changed_files": {
                    "new_files": changes["new_files"],
                    "modified_files": changes["modified_files"],
                    "deleted_files": changes["deleted_files"],
                    "unchanged_files_count": len(changes["unchanged_files"]),
                },
                "vulnerable_files": analysis.get("vulnerable_files", []),
                "security_findings": security_findings,
                "debt_findings": debt_findings,
                "autofix_suggestions": fixes,
            },
            "summary": {
                "repo_id": repo_id,
                "health_score": score_body.get("health_score"),
                "total_security_issues": score_body.get("analysis", {}).get("total_security_issues", 0),
                "total_debt_issues": score_body.get("analysis", {}).get("total_debt_issues", 0),
                "critical_issues": score_body.get("analysis", {}).get("critical_issues", 0),
                "quick_wins": score_body.get("analysis", {}).get("quick_wins", 0),
            },
            "continuous_intelligence": {
                "scan_id": stored["scan_id"],
                "snapshot_id": snapshot_info["snapshot_id"],
                "scan_mode": scan_mode,
                "history_depth": len(latest_context.get("history", [])),
                "files_considered": len(files),
                "files_scanned": len(selected_files),
                "new_issues": stored["new_issues"],
                "resolved_issues": stored["resolved_issues"],
                "persisting_issues": stored["persisting_issues"],
                "estimated_fix_minutes": sum(
                    item.get("estimated_minutes_to_fix", item.get("estimated_minutes", 0))
                    for item in security_findings + debt_findings
                ),
                "trend": {
                    "previous_health_score": previous_score,
                    "current_health_score": current_score,
                    "delta": (current_score - previous_score) if previous_score is not None and current_score is not None else None,
                },
            },
        }

