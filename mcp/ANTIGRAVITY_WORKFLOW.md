# Antigravity MCP Workflow for RepoScan Continuous Intelligence

## Goal

Make Antigravity keep MCP memory in sync whenever the main Claude agent changes code, fixes issues, or introduces new ones.

## Required MCP Server

Register the RepoScan MCP server using either:

- [antigravity.mcp.template.json](c:/Users/Mukul%20Prasad/Desktop/PROJECTS/New%20folder/an/githoppermain/plugins/antigravity-reposcan-mcp/antigravity.mcp.template.json#L1)
- or the plugin-managed server entry in [plugins/antigravity-reposcan-mcp/.mcp.json](c:/Users/Mukul%20Prasad/Desktop/PROJECTS/New%20folder/an/githoppermain/plugins/antigravity-reposcan-mcp/.mcp.json#L1)

## Core MCP Calls

### Tools

- `continuous_scan(repo_url, branch_name, generate_fixes)`
- `sync_agent_change(repo_url, branch_name, command_name, notes, generate_fixes)`
- `get_issue_delta(repo_id)`
- `get_unresolved_issues(repo_id)`

### Resources

- `repomemory://context/{repo_id}`
- `repomemory://delta/{repo_id}`
- `repomemory://commands/{repo_id}`
- `repomemory://unresolved/{repo_id}`

## Recommended Antigravity Lifecycle

### 1. Session start

When Antigravity opens a repo or starts a task:

1. call `continuous_scan`
2. store returned `repo_id`
3. load:
   - `repomemory://context/{repo_id}`
   - `repomemory://delta/{repo_id}`
   - `repomemory://unresolved/{repo_id}`

Purpose:

- seed Claude with prior unresolved issues
- seed Claude with recent fixes and trend context

### 2. After Claude edits code

Whenever the main Claude agent:

- edits files
- applies a patch
- resolves a bug
- changes dependencies
- modifies configuration

Antigravity should immediately call:

```json
{
  "tool": "sync_agent_change",
  "arguments": {
    "repo_url": "https://github.com/owner/repo",
    "branch_name": "main",
    "command_name": "apply_patch",
    "notes": "Claude updated auth middleware and removed unsafe eval usage.",
    "generate_fixes": true
  }
}
```

Then reload:

- `repomemory://context/{repo_id}`
- `repomemory://delta/{repo_id}`
- `repomemory://commands/{repo_id}`

Purpose:

- MCP reflects new issues introduced by the latest change
- MCP reflects solved issues from the latest change
- Claude gets refreshed repo memory after its own actions

### 3. Before Claude plans next action

Antigravity should inject the refreshed MCP context into Claude’s next reasoning cycle:

- unresolved issues
- latest issue delta
- recent command events
- per-file history from `context`

That makes the system self-updating instead of static.

## Practical Host Rules

Antigravity should call `sync_agent_change` when:

- a write/edit tool succeeds
- a commit is created
- a dependency file changes
- a config/security-sensitive file changes
- Claude explicitly says an issue was fixed

Antigravity should not call it when:

- Claude only reads files
- Claude only chats/explains
- no code or repo state changed

## Minimal Orchestration Template

Use this host-side sequence:

```text
On repo open:
  1. MCP tool: continuous_scan
  2. MCP resource: repomemory://context/{repo_id}
  3. MCP resource: repomemory://delta/{repo_id}

On successful Claude write/edit:
  1. MCP tool: sync_agent_change
  2. MCP resource: repomemory://context/{repo_id}
  3. MCP resource: repomemory://delta/{repo_id}
  4. MCP resource: repomemory://commands/{repo_id}

On follow-up reasoning:
  Include latest delta + unresolved issue context in Claude prompt.
```

## Antigravity Config Shape

If Antigravity supports an MCP server registry config, use something like:

```json
{
  "mcpServers": {
    "reposcan-continuous-intelligence": {
      "command": "python",
      "args": [
        "c:/Users/Mukul Prasad/Desktop/PROJECTS/New folder/an/githoppermain/backend/mcp_runtime_server.py"
      ],
      "cwd": "c:/Users/Mukul Prasad/Desktop/PROJECTS/New folder/an/githoppermain/backend",
      "env": {
        "MCP_TRANSPORT": "stdio",
        "GITHUB_TOKEN": "REPLACE_WITH_YOUR_TOKEN"
      }
    }
  }
}
```

## Suggested Event Mapping

Map Antigravity events to MCP calls like this:

- `session_started` -> `continuous_scan`
- `file_write_completed` -> `sync_agent_change`
- `patch_applied` -> `sync_agent_change`
- `commit_created` -> `sync_agent_change`
- `task_completed` -> reload `repomemory://delta/{repo_id}`

## What Antigravity Should Show in UI

After every sync cycle, display:

- new issues
- resolved issues
- persisting issues
- last synced command
- latest health score
- latest scanned commit

## Recommended Prompt Injection Block

Antigravity can prepend something like this to Claude after every sync:

```text
Repo memory refreshed.
Latest delta:
- New issues: 2
- Resolved issues: 1
- Persisting issues: 3

Recent command:
- apply_patch: Claude updated auth middleware

Use this updated repo memory before making the next code change.
```

## Final Recommendation

For your setup:

1. Keep UI testing through Flask
2. Keep plugin registration for Antigravity
3. Make Antigravity call `sync_agent_change` after every successful write action
4. Reload `context`, `delta`, and `commands` resources right after that

That gives you the “live MCP intelligence layer” behavior you were asking for.

