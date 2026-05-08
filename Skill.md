# OpenClaw Skill: Repo Analysis Digest

## Overview
Generate a concise repository analysis digest and prepare it for delivery.

## Inputs
- repo_url (string)
- branch (string, optional, default: main)
- include_top_actions (boolean, default: true)

## Output
- A markdown summary with:
  - total findings
  - top 5 actions (if available)
  - health score
  - notable risks

## Constraints
- No secrets in output.
- Keep under 1,000 characters.
- Always mention provider as OpenClaw.

## Example Output
Repo: https://github.com/org/repo
Branch: main
Provider: OpenClaw (groq)
Findings: 12 (CRITICAL: 2, HIGH: 4)
Health score: 71
Top actions:
1) Rotate hardcoded API keys in config/db.py
2) Fix SQL injection in src/user.py
3) Lock S3 bucket policy in infra/main.tf
