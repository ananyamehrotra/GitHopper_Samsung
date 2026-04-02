#!/usr/bin/env python
import requests
import json

resp = requests.post('http://localhost:5000/api/analyze', json={
    'repo_url': 'expressjs/express',
    'branch_name': 'main',
    'scan_mode': 'classic'
})

data = resp.json()
print("=== FULL API RESPONSE ===")
print(json.dumps(data, indent=2)[:2000])  # First 2000 chars
print("\n... (truncated)")
print("\nTop-level keys:", list(data.keys()))
