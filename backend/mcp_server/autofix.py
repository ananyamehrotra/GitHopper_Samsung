import difflib
import re
from typing import Any, Dict, List

from .analyzer import scan_chunk_with_context


def _make_patch(file_path: str, original: str, updated: str) -> str:
    return "".join(
        difflib.unified_diff(
            original.splitlines(keepends=True),
            updated.splitlines(keepends=True),
            fromfile=file_path,
            tofile=f"{file_path}.fixed",
        )
    )


def _fix_hardcoded_secret(content: str) -> Dict[str, Any]:
    updated = re.sub(r'(["\'])([^"\']{4,})(["\'])', '"REDACTED_FROM_ENV"', content, count=1)
    return {
        "updated": updated,
        "explanation": "Replaced a likely hardcoded secret with an environment-managed placeholder.",
    }


def _fix_unsafe_eval(content: str) -> Dict[str, Any]:
    updated = content.replace("eval(", "ast.literal_eval(")
    if updated != content and "import ast" not in updated:
        updated = "import ast\n" + updated
    return {
        "updated": updated,
        "explanation": "Replaced eval() with ast.literal_eval() for safer parsing.",
    }


def _fix_dependency_line(content: str, issue: Dict[str, Any]) -> Dict[str, Any]:
    recommended = issue.get("recommended_version") or issue.get("metadata", {}).get("recommended_version")
    package = issue.get("package") or issue.get("metadata", {}).get("package")
    if not package or not recommended:
        return {"updated": content, "explanation": "No concrete package/version data available for auto-upgrade."}
    updated = re.sub(
        rf"^{re.escape(package)}.*$",
        f"{package}=={recommended}",
        content,
        flags=re.MULTILINE,
    )
    return {
        "updated": updated,
        "explanation": f"Updated dependency suggestion for {package} to {recommended}.",
    }


def generate_fix(issue: Dict[str, Any], file_content: str) -> Dict[str, Any]:
    issue_type = (issue.get("issue_type") or issue.get("type") or "").upper()

    fixer_result = {"updated": file_content, "explanation": "No safe deterministic fix available yet."}
    if "SECRET" in issue_type:
        fixer_result = _fix_hardcoded_secret(file_content)
    elif "EVAL" in issue_type:
        fixer_result = _fix_unsafe_eval(file_content)
    elif issue_type in {"OUTDATED", "VULNERABLE", "UNPINNED"}:
        fixer_result = _fix_dependency_line(file_content, issue)

    updated = fixer_result["updated"]
    patch = _make_patch(issue["file_path"], file_content, updated)

    return {
        "issue": issue["summary"],
        "remediated_code": updated,
        "diff": patch,
        "explanation": fixer_result["explanation"],
    }


def validate_fix(
    issue: Dict[str, Any],
    fixed_code: str,
    repo_context: Dict[str, Any],
    language: str = "text",
) -> Dict[str, Any]:
    validation_chunk = {
        "file": issue["file_path"],
        "language": language,
        "code": fixed_code,
        "debt_signals": [],
        "context_note": "Validation pass on remediated code.",
        "start_line": 1,
        "end_line": max(1, len(fixed_code.splitlines())),
    }
    result = scan_chunk_with_context(validation_chunk, repo_context)
    remaining = [
        vuln for vuln in result.get("vulnerabilities", [])
        if (vuln.get("type") or "").upper() == issue["issue_type"].upper()
    ]

    status = "FAILED" if remaining else "VALIDATED"
    return {
        "status": status,
        "remaining_issues": remaining,
    }


def generate_and_validate_fixes(
    issues: List[Dict[str, Any]],
    file_map: Dict[str, Dict[str, Any]],
    repo_context: Dict[str, Any],
) -> List[Dict[str, Any]]:
    fixes = []
    for issue in issues:
        file_info = file_map.get(issue["file_path"])
        if not file_info:
            continue
        proposal = generate_fix(issue, file_info.get("content", ""))
        validation = validate_fix(
            issue,
            proposal["remediated_code"],
            repo_context,
            language=file_info.get("language", "text"),
        )
        fixes.append(
            {
                **proposal,
                "file_path": issue["file_path"],
                "fingerprint": issue["fingerprint"],
                "validation_status": validation["status"],
                "remaining_issues": validation["remaining_issues"],
            }
        )
    return fixes

