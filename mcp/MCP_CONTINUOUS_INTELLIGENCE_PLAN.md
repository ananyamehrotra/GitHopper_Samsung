# MCP Continuous Intelligence Layer for RepoScan AI

## Goal

Transform the current one-time RepoScan flow into a non-breaking extension layer that adds:

- Persistent memory
- Incremental scanning
- Context-aware Bedrock prompting
- Auto-fix generation
- Fix validation
- Continuous watch mode
- Better reporting for trends and quick wins

Tagline:

> From static analysis to continuous intelligent code improvement with memory and optimization.

## What I Added in This Repo

This implementation starts the extension as a plug-in style backend layer under `backend/mcp_server/`.

It does not replace the existing pipeline.
It adds a new parallel path and integration endpoints:

- New MCP memory store
- Incremental diff tracker
- Context injection wrapper for LLM analysis
- Prompt optimization layer
- Auto-fix generation and validation
- Watch mode manager
- New Flask APIs for continuous analysis

## Existing System Mapping

Current:

`fetch -> chunk -> Bedrock -> scoring -> UI`

Extended:

`fetch -> diff check -> MCP context injection -> optimized analysis -> scoring -> MCP memory update -> UI`

The original `/api/analyze` route remains available.
The extension uses new routes so existing behavior stays intact.

## New Files and Responsibilities

- `backend/mcp_server/storage.py`
  Lightweight SQLite memory store for scans, snapshots, issues, and fixes.
- `backend/mcp_server/diffing.py`
  Hash-based incremental scan logic.
- `backend/mcp_server/context.py`
  Builds history-aware context for the next analysis.
- `backend/mcp_server/prompting.py`
  Prompt profile routing and context injection helpers.
- `backend/mcp_server/analyzer.py`
  Wrapper over Bedrock/static analysis with strict JSON prompts and MCP context.
- `backend/mcp_server/autofix.py`
  Auto-fix proposal generation plus validation loop.
- `backend/mcp_server/watcher.py`
  Continuous scan manager using background polling.
- `backend/mcp_server/continuous_pipeline.py`
  Non-breaking orchestrator for continuous intelligence mode.

## Step-by-Step Architecture

### Step 1. Fetch Repo Metadata and Files

Uses the current GitHub fetch layer.

Inputs:

- `repo_url`
- `branch_name`
- optional `github_token`

No change needed from you yet.

Local in this repo now:

- Flask route receives the request.
- Python backend uses the existing fetch logic directly inside the app process.
- Files are pulled into local runtime memory for the duration of the scan.
- If a token is used, it is passed from local environment variables or request configuration.
- This is the fastest way to demo because there is no extra infrastructure between request and scan.

Future in AWS:

- API Gateway or an ALB can receive the request instead of a local Flask-only entrypoint.
- A Lambda function, ECS task, or containerized backend service can perform the GitHub fetch.
- GitHub credentials should move into AWS Secrets Manager instead of staying only in local `.env` style config.
- Large repo fetches can be queued through SQS so user requests do not wait on long scans synchronously.
- For webhook-driven scanning later, GitHub events can trigger EventBridge or an API endpoint instead of manual local polling.

### Step 2. Build Snapshot Metadata

For every fetched file we store metadata only:

- file path
- language
- size
- content hash
- debt signal count
- last seen time

We do not store the full repo code in MCP memory.

Local in this repo now:

- Snapshot metadata is created in Python in the same backend process that fetched the repo.
- Metadata is written into local SQLite through `backend/mcp_server/storage.py`.
- The database file lives on the local machine or local server disk.
- Hashing and signal counting happen inline during the scan request or watch cycle.
- This keeps setup simple and avoids cloud dependencies for the hackathon version.

Future in AWS:

- The same metadata model can be stored in DynamoDB for shared, durable scan history.
- If report exports are needed, summaries can also be written to S3.
- Compute for hashing and metadata extraction can still run in Lambda, ECS, or EC2 workers.
- DynamoDB partitioning can be based on `repo_id`, branch, and snapshot timestamp for efficient history lookup.
- Encryption at rest and IAM-based access control become standard instead of relying on local machine security.

### Step 3. Compute Incremental Changes

The diff tracker compares the latest snapshot against the previous snapshot and marks:

- `new_files`
- `modified_files`
- `deleted_files`
- `unchanged_files`

Scan scope becomes:

- new files
- modified files
- files with unresolved issues from prior scans

This is where token and cost reduction happens.

Local in this repo now:

- `backend/mcp_server/diffing.py` compares the new local snapshot with the previous snapshot from SQLite.
- The comparison happens inside one Python process, so there is no network hop between memory and storage.
- The backend decides immediately which files need re-analysis before sending anything to Bedrock.
- This reduces tokens even in local mode because unchanged files are skipped.
- Watch mode can re-use the same logic repeatedly on the same machine.

Future in AWS:

- The diff operation can run in stateless workers that pull prior snapshot metadata from DynamoDB.
- Incremental scan jobs can be triggered by SQS messages, EventBridge schedules, or GitHub webhooks.
- For bigger repos, diffing can be split into background jobs instead of blocking the API request.
- The result of the diff step can be stored as a scan manifest in DynamoDB or S3 so downstream workers know exactly what to analyze.
- This makes horizontal scaling easier because workers do not depend on one local SQLite file.

### Step 4. Inject Historical Context

Before Bedrock is called, the wrapper adds:

- unresolved prior issues for the file
- recent resolved issues for the file
- repo trend summary
- chunk-local debt signals
- prompt profile based on file type

Example:

```text
Previously detected in auth.py:
- 2 issues total
- 1 resolved
- 1 unresolved: HARDCODED_SECRET
Analyze the current chunk with this history in mind.
```

Local in this repo now:

- `backend/mcp_server/context.py` reads prior issue history from local SQLite.
- Context is assembled in memory right before the prompt is sent.
- The current Flask app remains the orchestrator, so prompt enrichment is just a backend wrapper around the existing analysis flow.
- There is no separate cache layer yet; history lookup is local and lightweight.
- This is enough to prove memory-aware analysis without adding cloud architecture.

Future in AWS:

- Context retrieval can read from DynamoDB and optionally cache hot repo summaries in ElastiCache if needed later.
- Prompt assembly can run in Lambda/ECS workers close to the Bedrock calling layer.
- If multiple services need the same context, a dedicated context service or MCP API layer can expose normalized history lookups.
- Large trend summaries can be precomputed and stored instead of built every time on demand.
- IAM, audit logging, and centralized observability become easier once context generation is moved into AWS-managed infrastructure.

### Step 5. Dynamic Prompt Optimization

Prompt profile is selected by file kind:

- config and infra files -> configuration/security profile
- dependency manifests -> dependency vulnerability profile
- application source -> code logic + security profile

Output is forced into strict JSON-compatible structure.

Local in this repo now:

- `backend/mcp_server/prompting.py` can keep prompt templates and routing rules in local Python code.
- The local backend decides which profile to apply before each Bedrock request.
- Template edits are simple code changes in the repo, which is ideal while prompt strategy is still changing fast.
- Strict JSON output handling is validated in the backend before results continue to scoring.
- This keeps prompt experimentation easy during development.

Future in AWS:

- Prompt profiles can remain in code or move to a managed config source such as AppConfig, S3, or DynamoDB.
- Different environments can use different prompt versions without changing application code on every tweak.
- A/B testing of prompt variants becomes easier when workers read versioned config from AWS-managed storage.
- Centralized prompt config also helps if multiple scan workers or services need consistent behavior.
- Bedrock remains the model endpoint, but the prompt-governance layer becomes easier to manage at scale.

### Step 6. Score Without Breaking Existing Contracts

The extension prepares scoring input compatible with the existing scorer:

- `security_findings`
- `debt_findings`
- `repo_id`
- `repo_url`

It then returns the original-style score block plus a new `continuous_intelligence` section.

Local in this repo now:

- The current backend can call the existing scorer directly after the MCP-enhanced analysis step.
- Response shaping happens inside the same Flask request lifecycle.
- Frontend compatibility is protected because the original response fields remain unchanged.
- The added `continuous_intelligence` block is generated locally and returned immediately.
- This is the safest integration path because it does not force frontend rewrites.

Future in AWS:

- The scoring service can stay embedded in one backend or be separated into its own Lambda/service if traffic grows.
- API Gateway can expose the same contract externally while internal workers generate the payload.
- Shared schemas can be versioned so old clients keep working while new clients consume extra fields.
- If analytics grow, score history can also be pushed into S3, DynamoDB, or an analytics store for trend dashboards.
- The contract remains the same, but transport and persistence become cloud-managed.

### Step 7. Auto-Fix and Validation Loop

For issues found in the latest scan:

1. Generate fix proposal
2. Build remediated code and diff patch
3. Re-analyze remediated code
4. Mark fix status:
   - `VALIDATED`
   - `PARTIAL`
   - `FAILED`

The current implementation includes heuristic fixes for:

- hardcoded secrets
- unsafe `eval`
- some dependency upgrade cases

And leaves room for Bedrock-powered fix generation when AWS credentials are active.

Local in this repo now:

- `backend/mcp_server/autofix.py` can generate heuristic patches directly in the backend process.
- Validation can re-run analysis locally against the remediated content before marking status.
- Patch preview can stay in memory or be stored in SQLite with fix status metadata.
- This is good for demoing safe suggestion loops without needing GitHub write access yet.
- If Bedrock credentials are already configured locally, the same flow can later switch from heuristics to LLM-assisted fixes.

Future in AWS:

- Fix generation can run as queued jobs using SQS plus Lambda/ECS workers, especially for expensive model calls.
- Validation can be expanded into isolated workers or CodeBuild jobs that run tests, linters, and policy checks.
- Generated patches can be stored in S3, DynamoDB, or a fix-history table for auditing.
- Secrets Manager should hold GitHub tokens if the system later opens PRs automatically.
- This step benefits a lot from AWS because fix generation and validation are the most bursty and compute-heavy parts of the pipeline.

### Step 8. Continuous Watch Mode

Background polling loop:

1. Fetch latest repo state
2. Run incremental scan
3. Update memory
4. Expose status to UI

This is demo-friendly and hackathon-safe.

Local in this repo now:

- `backend/mcp_server/watcher.py` can run a background polling thread inside the Flask backend process.
- Watch state can be tracked in local memory and/or SQLite.
- The UI can query the backend directly for status using the new watch endpoints.
- This is simple to build and works well while one demo server is running.
- The tradeoff is that watch jobs disappear if the local process restarts.

Future in AWS:

- EventBridge Scheduler can trigger periodic scans without depending on one always-on local process.
- SQS can buffer watch jobs so scans are resilient and retryable.
- Lambda, ECS, or Step Functions can execute each scheduled scan independently.
- CloudWatch Logs and metrics can track failures, durations, and scan frequency centrally.
- This is the right long-term model if multiple repos, users, or organizations need reliable continuous monitoring.

## New APIs

Implemented or scaffolded:

- `POST /api/analyze/continuous`
- `POST /api/continuous/start`
- `GET /api/continuous/status/<watch_id>`
- `POST /api/continuous/stop/<watch_id>`
- `GET /api/mcp/context/<repo_id>`
- `GET /api/mcp/unresolved/<repo_id>`
- `POST /api/mcp/fix-status`

Core MCP storage methods:

- `store_scan_results()`
- `get_context()`
- `get_unresolved_issues()`
- `update_fix_status()`

## Response Additions

The extension returns a new block like:

```json
{
  "continuous_intelligence": {
    "scan_mode": "full_or_incremental",
    "files_considered": 12,
    "files_scanned": 4,
    "new_issues": 3,
    "resolved_issues": 1,
    "persisting_issues": 2,
    "estimated_fix_minutes": 55,
    "history_depth": 4,
    "trend": {
      "previous_health_score": 71,
      "current_health_score": 78,
      "delta": 7
    }
  }
}
```

This is safe for the frontend because it is additive.

## What I Still Need From You

These are not blockers for the starter implementation, but they will improve the final hackathon version:

### Needed Soon

- A decision on whether MCP memory should stay local SQLite for demo, or move to managed AWS storage.
- Confirmation on whether watch mode can be simple polling, or if you want webhook/event-driven behavior.
- Confirmation on whether fix patches should be preview-only, or later pushed into GitHub PRs.

### Needed For Production-Like Version

- AWS account access details for the final deployment target
- Bedrock model preference:
  - Claude on Bedrock only
  - Claude + Gemini abstraction
  - fully provider-agnostic model gateway
- Whether you want issue/fix history stored per branch or only per repo
- Whether GitHub App auth is available for richer repo polling and PR automation

### Needed If You Want PR Automation Next

- GitHub token or GitHub App credentials
- repo write permissions
- preferred branch naming convention for generated fix branches

## AWS / Tech Stack by Phase

### Phase 1. Hackathon-Minimum

Already sufficient:

- Flask
- Python stdlib `sqlite3`
- existing Bedrock integration
- background polling thread in backend process

Optional AWS:

- none required

### Phase 2. Better Demo Stability

Recommended:

- Amazon EventBridge Scheduler for periodic scans
- DynamoDB instead of SQLite for shared history
- S3 for scan summaries and exported reports
- CloudWatch Logs for watch-mode observability

### Phase 3. Production Upgrade

Recommended:

- API Gateway + Lambda for MCP API layer
- DynamoDB for scan memory
- SQS for queued scan jobs
- EventBridge for continuous scheduling
- Secrets Manager for tokens
- Step Functions for multi-stage scan/fix/validate orchestration

### Phase 4. Auto-Fix PR Workflow

Recommended:

- GitHub App
- SQS or Step Functions for queued fix runs
- Lambda workers for patch generation
- optional CodeBuild for validation/test execution

## Suggested Delivery Plan

### Milestone 1

- MCP storage
- incremental scans
- context injection
- continuous analysis endpoint

### Milestone 2

- watch mode
- auto-fix generation
- validation loop
- enhanced reporting payload

### Milestone 3

- frontend dashboard widgets for:
  - new vs resolved
  - trend chart
  - quick wins
  - total fix time

### Milestone 4

- GitHub PR automation
- managed AWS persistence
- event-driven scanning

## Risks and How This Starter Handles Them

### Risk: MCP failure breaks scanning

Mitigation:

- extension catches MCP errors
- scan can still continue with best-effort analysis

### Risk: Full repo re-scan cost

Mitigation:

- hash-based changed file detection
- unresolved issue carry-forward only

### Risk: Storing sensitive code

Mitigation:

- snapshot store keeps metadata, hashes, summaries
- full code stays transient in request-time memory only

### Risk: Auto-fix is unreliable

Mitigation:

- validation loop
- explicit status: `VALIDATED`, `PARTIAL`, `FAILED`

## Recommended Next Input From You

Reply with any of these if you want me to take the next step:

1. "Keep it hackathon-local" -> I will keep SQLite + polling and extend the UI next.
2. "Make it AWS-ready" -> I will add deployment-oriented config and managed-service adapters.
3. "Add GitHub PR autofix" -> I will scaffold PR branch/patch flow next.
4. "Build the UI cards now" -> I will connect frontend pages to the new continuous endpoints.
