#!/usr/bin/env python
"""
Quick test to verify that OpenClaw is returning code quality/debt findings.
"""
import sys
import json
from ai.openclaw_client import scan_chunk

# Sample Python code with code quality issues
test_code = '''
def process_data(a, b, c, d, e):
    """A function with too many parameters"""
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        result = a + b + c + d + e
                        result = result * 2
                        result = result / 3
                        return result  # Very deep nesting
    return None

def helper_function():
    x = 1
    return x

def helper_function_2():
    y = 1
    return y

def helper_function_3():
    z = 1
    return z

# Lots of similar code (duplication)
print("duplicated code")
print("duplicated code")
print("duplicated code")
'''

test_chunk = {
    "file": "test_complex.py",
    "code": test_code,
    "filename": "test_complex.py"
}

print("Testing OpenClaw code quality analysis...")
print(f"Scanning {test_chunk['file']}")
print("=" * 60)

result = scan_chunk(test_chunk, branch_name="test")

print("\n" + "=" * 60)
print("SCAN RESULT:")
print(json.dumps(result, indent=2))

# Check if code quality findings were detected
vulns = result.get("vulnerabilities", [])
print(f"\nTotal findings: {len(vulns)}")

code_quality_findings = [v for v in vulns if "complexity" in v.get("type", "").lower() or "duplication" in v.get("type", "").lower()]
print(f"Code quality/debt findings: {len(code_quality_findings)}")

if code_quality_findings:
    print("\n✓ SUCCESS: OpenClaw returned code quality findings!")
    for f in code_quality_findings:
        print(f"  - {f.get('type')}: {f.get('severity')} - {f.get('explanation', 'N/A')[:50]}")
else:
    print("\n✗ ISSUE: No code quality findings detected.")
    print("This means either:")
    print("  1. OpenClaw isn't being invoked properly")
    print("  2. The prompt wasn't updated in the running process")
    print("  3. OpenClaw is returning an empty response")
