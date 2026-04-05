#!/usr/bin/env python
import requests
import json

resp = requests.post('http://localhost:5000/api/analyze', json={
    'repo_url': 'expressjs/express',
    'branch_name': 'main',
    'scan_mode': 'classic'
})

data = resp.json()
print("=== TOP LEVEL KEYS ===")
print(list(data.keys()))

print("\n=== CHECKING FILES WITH ISSUES ===")
print(f"Files with issues: {data.get('files_with_issues')}")
print(f"Vulnerable files: {len(data.get('vulnerable_files', []))}")

print("\n=== BY SEVERITY ===")
ba = data.get('branch_analysis', {})
by_sev = ba.get('by_severity', {})
total = sum(by_sev.values())
print(f"Total from by_severity: {total}")
print(f"Breakdown: {by_sev}")

print("\n=== SUMMARY ===")
print(f"Summary: {ba.get('summary')}")

# Count unique files
findings = ba.get('findings', [])
files = set()
for f in findings:
    files.add(f.get('file'))
print(f"\nUnique files with issues: {len(files)}")
print(f"Total findings: {len(findings)}")
