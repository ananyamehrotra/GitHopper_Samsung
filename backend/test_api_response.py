#!/usr/bin/env python
import requests
import json

resp = requests.post('http://localhost:5000/api/analyze', json={
    'repo_url': 'expressjs/express',
    'branch_name': 'main',
    'scan_mode': 'classic'
})

data = resp.json()
dr = data.get('debt_report', {})
print('=== DEBT REPORT CONTENT ===')
print('Summary:', dr.get('summary'))
print('\nNumber of findings:', len(dr.get('findings', [])))
print('\nFirst 3 findings:')
for f in dr.get('findings', [])[:3]:
    print(f'  - {f.get("type")}: {f.get("severity")} ({f.get("file")})')

print('\n\n=== FULL DEBT REPORT ===')
print(json.dumps(dr, indent=2))
