# OpenClaw Heartbeat

Purpose: periodic status pings and lightweight summaries for demos.

## Schedule
- Interval: 30 minutes
- Active hours: 09:00-21:00 local time

## Payload Template
- Status: OK
- Provider: OpenClaw
- Provider backend: ${OPENCLAW_PROVIDER}
- Repo scanned: ${LAST_REPO_URL}
- Findings: ${LAST_TOTAL_FINDINGS}
- Health score: ${LAST_HEALTH_SCORE}
- Notes: ${LAST_NOTE}

## Behavior
- If no recent scan, report "idle" and keep findings/score empty.
- Do not send secrets or API keys.
- Keep output under 500 characters.
