import logging
import os

from mcp.server.fastmcp import FastMCP

from mcp_server import ContinuousIntelligencePipeline, MCPMemoryStore
from mcp_server.continuous_pipeline import repo_id_from_url


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("reposcan-mcp")

mcp = FastMCP("RepoScan Continuous Intelligence", json_response=True)
store = MCPMemoryStore()
pipeline = ContinuousIntelligencePipeline(store=store)


def _normalize_repo_url(repo_url: str) -> str:
    repo_url = repo_url.strip()
    if not repo_url.startswith("http"):
        repo_url = f"https://github.com/{repo_url}"
    return repo_url


@mcp.tool()
def continuous_scan(repo_url: str, branch_name: str = "main", generate_fixes: bool = True):
    """
    Run RepoScan continuous intelligence analysis with MCP memory, incremental scanning,
    context injection, and optional auto-fix generation.
    """
    github_token = os.environ.get("GITHUB_TOKEN")
    return pipeline.run(
        repo_url=_normalize_repo_url(repo_url),
        github_token=github_token,
        branch_name=branch_name,
        generate_fixes=generate_fixes,
    )


@mcp.tool()
def get_unresolved_issues(repo_id: str):
    """Return unresolved issues for a previously scanned repository."""
    return {
        "repo_id": repo_id,
        "unresolved_issues": store.get_unresolved_issues(repo_id),
    }


@mcp.tool()
def get_issue_delta(repo_id: str):
    """
    Return the latest issue delta for a repo:
    new issues, resolved issues, and persisting issues from the most recent sync.
    """
    return store.get_latest_issue_delta(repo_id)


@mcp.tool()
def sync_agent_change(
    repo_url: str,
    branch_name: str = "main",
    command_name: str = "agent_change",
    notes: str = "",
    generate_fixes: bool = True,
):
    """
    Call this after Antigravity/Claude makes a code change.
    It records the command event, runs a fresh sync, and returns the updated issue delta.
    """
    normalized_repo_url = _normalize_repo_url(repo_url)
    repo_id = repo_id_from_url(normalized_repo_url)
    command_event = store.record_command_event(
        repo_id=repo_id,
        command_name=command_name,
        notes=notes,
        metadata={"branch_name": branch_name},
    )
    github_token = os.environ.get("GITHUB_TOKEN")
    result = pipeline.run(
        repo_url=normalized_repo_url,
        github_token=github_token,
        branch_name=branch_name,
        generate_fixes=generate_fixes,
    )
    return {
        "command_event": command_event,
        "scan_result": result,
        "issue_delta": store.get_latest_issue_delta(repo_id),
        "context": store.get_context(repo_id),
    }


@mcp.tool()
def update_fix_status(
    repo_id: str,
    issue_fingerprint: str,
    status: str,
    validation_status: str,
    explanation: str = "",
    diff_patch: str = "",
    remediated_code: str = "",
):
    """Update auto-fix status for a stored issue."""
    return store.update_fix_status(
        repo_id=repo_id,
        issue_fingerprint=issue_fingerprint,
        status=status,
        validation_status=validation_status,
        explanation=explanation,
        diff_patch=diff_patch,
        remediated_code=remediated_code,
    )


@mcp.resource("repomemory://context/{repo_id}")
def repo_context(repo_id: str):
    """Read stored MCP context for a repository."""
    return str(store.get_context(repo_id))


@mcp.resource("repomemory://unresolved/{repo_id}")
def unresolved_resource(repo_id: str):
    """Read unresolved issues for a repository."""
    return str(store.get_unresolved_issues(repo_id))


@mcp.resource("repomemory://delta/{repo_id}")
def delta_resource(repo_id: str):
    """Read latest issue delta for a repository."""
    return str(store.get_latest_issue_delta(repo_id))


@mcp.resource("repomemory://commands/{repo_id}")
def commands_resource(repo_id: str):
    """Read recent agent/command events for a repository."""
    return str(store.list_recent_commands(repo_id, limit=20))


if __name__ == "__main__":
    transport = os.environ.get("MCP_TRANSPORT", "stdio").strip().lower()
    logger.info("Starting RepoScan MCP server with transport=%s", transport)
    if transport == "http":
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")
