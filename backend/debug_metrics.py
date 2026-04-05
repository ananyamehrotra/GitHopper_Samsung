#!/usr/bin/env python
import requests
import json

resp = requests.post('http://localhost:5000/api/analyze', json={
    'repo_url': 'expressjs/express',
    'branch_name': 'main',
    'scan_mode': 'classic'
})

data = resp.json()
print("=== BRANCH ANALYSIS DATA ===")
ba = data.get('branch_analysis', {})
print(json.dumps(ba, indent=2)[:3000])
print("\n... (truncated)\n")

print("=== CHECKING STRUCTURE ===")
print(f"Keys in branch_analysis: {list(ba.keys())}")
if 'by_severity' in ba:
    print(f"by_severity: {ba['by_severity']}")
if 'findings' in ba:
    print(f"Number of findings: {len(ba['findings'])}")
if 'summary' in ba:
    print(f"summary: {ba['summary']}")
