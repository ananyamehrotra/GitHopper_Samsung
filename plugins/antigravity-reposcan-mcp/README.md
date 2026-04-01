# Antigravity RepoScan MCP Plugin

This plugin registers the RepoScan continuous intelligence MCP server for local Antigravity/Codex-style plugin loading.

## Local MCP server target

- Server entry: `reposcan-continuous-intelligence`
- Command target: `../../backend/mcp_runtime_server.py`

## Before use

1. Install MCP runtime dependency:

```powershell
cd backend
python -m pip install -r requirements-mcp.txt
```

2. Set `GITHUB_TOKEN`

3. Make sure Antigravity/plugin host launches the server from stdio mode

## Test paths

- Direct MCP test: `backend/mcp_runtime_server.py`
- UI test path: existing Flask app + `/api/analyze/continuous`

## Main exposed MCP tool

- `continuous_scan`
- `sync_agent_change`
- `get_issue_delta`

## Main MCP resources

- `repomemory://context/{repo_id}`
- `repomemory://unresolved/{repo_id}`
- `repomemory://delta/{repo_id}`
- `repomemory://commands/{repo_id}`

## Antigravity Sync Model

When the main Claude/Antigravity agent edits code, call:

- `sync_agent_change(repo_url, branch_name, command_name, notes)`

Recommended usage:

1. Claude makes a code change
2. Antigravity calls `sync_agent_change`
3. MCP re-runs incremental analysis
4. Antigravity reads:
   - `repomemory://context/{repo_id}`
   - `repomemory://delta/{repo_id}`
   - `repomemory://commands/{repo_id}`

This lets the MCP layer reflect:

- newly introduced issues
- resolved issues
- persisting issues
- latest agent commands that caused the sync
