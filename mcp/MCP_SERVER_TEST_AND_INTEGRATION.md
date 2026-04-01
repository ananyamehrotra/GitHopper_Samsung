# RepoScan MCP Server: Test First, Then Integrate into Antigravity

## Important Clarification

There are now two layers in this repo:

1. The internal continuous intelligence backend extension under `backend/mcp_server/`
2. A formal MCP protocol wrapper at `backend/mcp_runtime_server.py`

The wrapper exposes the extension through real MCP tools and resources so you can load it in an MCP host.

## Files You Need

- `backend/mcp_runtime_server.py`
- `backend/requirements-mcp.txt`

## What This MCP Server Exposes

### Tools

- `continuous_scan(repo_url, branch_name="main", generate_fixes=True)`
- `sync_agent_change(repo_url, branch_name="main", command_name="agent_change", notes="", generate_fixes=True)`
- `get_unresolved_issues(repo_id)`
- `get_issue_delta(repo_id)`
- `update_fix_status(...)`

### Resources

- `repomemory://context/{repo_id}`
- `repomemory://unresolved/{repo_id}`
- `repomemory://delta/{repo_id}`
- `repomemory://commands/{repo_id}`

## Step 1. Install MCP SDK

From the repo root:

```powershell
cd backend
python -m pip install -r requirements-mcp.txt
```

Official references:

- MCP Python SDK quick example: https://py.sdk.modelcontextprotocol.io/
- MCP server quickstart: https://modelcontextprotocol.io/quickstart/server
- MCP transports: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports

## Step 2. Test It Locally in STDIO Mode

STDIO is the most common way hosts launch an MCP server.

Run:

```powershell
cd backend
$env:GITHUB_TOKEN="your_token_here"
python mcp_runtime_server.py
```

Important:

- Do not add `print()` statements to stdout in a stdio MCP server.
- This server uses logging instead.

## Step 3. Test It with MCP Inspector

The official docs show using the Inspector to connect to MCP servers.

One common approach is:

```powershell
npx -y @modelcontextprotocol/inspector
```

Then configure the server command roughly as:

- Command: `python`
- Args: `mcp_runtime_server.py`
- Working directory: your `backend` folder

After connecting, call:

- `continuous_scan`
- `get_unresolved_issues`

## Step 4. Optional HTTP Test Mode

If you want browser-style inspection instead of stdio:

```powershell
cd backend
$env:MCP_TRANSPORT="http"
$env:GITHUB_TOKEN="your_token_here"
python mcp_runtime_server.py
```

Per the Python SDK quick example, `streamable-http` typically serves on `http://localhost:8000/mcp`.

If your SDK version behaves differently, check the latest Python SDK docs above.

## Step 5. What a Successful Test Looks Like

You should be able to:

1. Load the MCP server
2. See the tools and resources
3. Run `continuous_scan` on a GitHub repo
4. Get a response containing:
   - scan summary
   - continuous intelligence fields
   - incremental scan info
   - autofix suggestions

## Step 6. Integrate into Antigravity After Testing

There are two good integration patterns.

### Option A. Antigravity loads this as an external MCP server

Use this if Antigravity already supports MCP server registration.

Register a server entry that launches:

```powershell
python c:\Users\Mukul Prasad\Desktop\PROJECTS\New folder\an\githoppermain\backend\mcp_runtime_server.py
```

Working directory:

```powershell
c:\Users\Mukul Prasad\Desktop\PROJECTS\New folder\an\githoppermain\backend
```

Required env vars:

- `GITHUB_TOKEN`
- optional `MCP_TRANSPORT=stdio`

Then Antigravity can call MCP tools like:

- `continuous_scan`
- `get_unresolved_issues`

This is the cleanest “true MCP” integration.

Recommended Antigravity flow:

1. Claude changes code
2. Antigravity calls `sync_agent_change`
3. Antigravity reloads:
   - `repomemory://context/{repo_id}`
   - `repomemory://delta/{repo_id}`
   - `repomemory://commands/{repo_id}`

That makes MCP state reflect newly solved and newly arising issues after each command cycle.

### Option B. Antigravity keeps calling Flask, and Flask calls the MCP layer internally

Use this if Antigravity is already tightly coupled to your current API.

In that case:

- keep using `/api/analyze/continuous`
- keep the formal MCP server for testing and future host integrations
- let Antigravity talk to Flask for now

This is the fastest hackathon path.

## Recommended Path for You

For fastest success:

1. Test `backend/mcp_runtime_server.py` in Inspector first
2. Keep Antigravity connected to Flask for the demo
3. After demo validation, register the MCP server directly in Antigravity

## Full Antigravity Integration Plan

### Phase 1

- Run Flask app as main product backend
- Run MCP server separately for host-level validation

### Phase 2

- Register MCP server in Antigravity config
- Let Antigravity use MCP tools for memory-aware scans

### Phase 3

- Move watch mode and autofix invocation to Antigravity workflows
- Optionally replace direct Flask orchestration with MCP-first orchestration

## What I Need From You Before Full Antigravity Wiring

- How Antigravity loads MCP servers:
  - JSON config
  - desktop app settings
  - command registration
  - plugin manifest
- Whether Antigravity expects:
  - stdio MCP
  - streamable HTTP MCP
- Whether Antigravity should call the MCP server directly or via the Flask API first

## Honest Note

The MCP wrapper is now scaffolded correctly for the official Python SDK approach, but I have not installed the `mcp` package inside this repo here.

So:

- the code is ready
- the local test/install step still needs to be run on your machine

Once you tell me how Antigravity registers MCP servers, I can wire the final config exactly.
