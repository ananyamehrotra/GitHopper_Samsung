from typing import Any, Dict, List


def build_repo_context(repo_context: Dict[str, Any], file_path: str) -> Dict[str, Any]:
    file_history = repo_context.get("file_history", {}).get(file_path, {})
    unresolved = file_history.get("unresolved", [])
    resolved = file_history.get("resolved", [])
    latest_scan = repo_context.get("latest_scan") or {}
    history = repo_context.get("history", [])

    trend = None
    if len(history) >= 2:
        current = history[0].get("scoring", {}).get("health_score")
        previous = history[1].get("scoring", {}).get("health_score")
        if current is not None and previous is not None:
            trend = {
                "current_health_score": current,
                "previous_health_score": previous,
                "delta": current - previous,
            }

    return {
        "latest_scan_id": latest_scan.get("scan_id"),
        "history_depth": len(history),
        "unresolved_for_file": unresolved,
        "resolved_for_file": resolved[:5],
        "trend": trend,
    }


def render_context_block(file_path: str, repo_context: Dict[str, Any]) -> str:
    file_ctx = build_repo_context(repo_context, file_path)
    unresolved = file_ctx["unresolved_for_file"]
    resolved = file_ctx["resolved_for_file"]
    trend = file_ctx["trend"]

    lines: List[str] = [
        "MCP CONTEXT",
        f"File under analysis: {file_path}",
        f"History depth: {file_ctx['history_depth']} prior scan(s)",
    ]

    if unresolved:
        lines.append("Previously unresolved issues for this file:")
        for issue in unresolved[:5]:
            lines.append(
                f"- {issue['issue_type']} ({issue['severity']}): {issue['summary']}"
            )
    else:
        lines.append("Previously unresolved issues for this file: none")

    if resolved:
        lines.append("Recently resolved issues for this file:")
        for issue in resolved[:3]:
            lines.append(
                f"- {issue['issue_type']} ({issue['severity']}): {issue['summary']}"
            )

    if trend:
        lines.append(
            "Repo score trend: "
            f"{trend['previous_health_score']} -> {trend['current_health_score']} "
            f"(delta {trend['delta']:+})"
        )

    lines.append("Use this history to avoid duplicate noise and focus on regressions, unresolved risks, and meaningful changes.")
    return "\n".join(lines)

