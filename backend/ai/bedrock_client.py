# =============================================================================
# bedrock_client.py — Core AI engine for GitHopper
# Dynamic prompts generated per repo based on actual file content
# =============================================================================

import boto3
import json
import logging
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# File Classification
# ---------------------------------------------------------------------------

IAC_EXTENSIONS = {".tf", ".tfvars"}
IAC_KEYWORDS = {"cloudformation", "template", "stack", "infra"}
IAM_KEYWORDS = {"iam", "policy", "role", "permission", "trust"}
DEP_FILES = {
    "requirements.txt", "package.json", "pipfile",
    "go.mod", "gemfile", "pom.xml"
}

def classify_file(filename: str) -> str:
    name = filename.lower()
    base = name.rsplit("/", 1)[-1]
    ext = "." + base.rsplit(".", 1)[-1] if "." in base else ""

    if base in DEP_FILES:
        return "deps"
    if ext == ".json" and any(kw in name for kw in IAM_KEYWORDS):
        return "iam"
    if ext in IAC_EXTENSIONS:
        return "iac"
    if ext in {".yaml", ".yml"} and any(kw in name for kw in IAC_KEYWORDS):
        return "iac"

    return "app"

# ---------------------------------------------------------------------------
# Dynamic Prompt Generation
# ---------------------------------------------------------------------------

def generate_security_prompt(filename: str, code_chunk: str, file_type: str, branch_name: str) -> str:

    if file_type == "iam":
        return f"""You are an IAM security specialist. Analyze this IAM policy for overly permissive permissions.

File: {filename}
Branch: {branch_name}
File Type: IAM Policy

Check for:
- Wildcard actions (Action: "*") or wildcard resources (Resource: "*")
- Principal "*" allowing public access
- Missing conditions on sensitive actions
- arn:* or overly broad resource access

Return ONLY valid JSON with no preamble:
{{
  "vulnerabilities": [
    {{
      "type": "OVERLY_PERMISSIVE",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "explanation": "What is the issue",
      "business_impact": "What risk this poses to the business",
      "estimated_minutes_to_fix": 15,
      "remediation": "How to fix"
    }}
  ]
}}

IAM Policy:
{code_chunk}"""

    elif file_type == "iac":
        return f"""You are a cloud security engineer. Analyze this infrastructure code for misconfigurations.

File: {filename}
Branch: {branch_name}
File Type: Infrastructure-as-Code

Check for:
- Public S3 buckets or unencrypted storage
- Security groups exposed to 0.0.0.0/0
- Unencrypted databases or volumes
- Missing logging or monitoring
- Hardcoded credentials

Return ONLY valid JSON with no preamble:
{{
  "vulnerabilities": [
    {{
      "type": "MISCONFIG_TYPE",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "explanation": "What is misconfigured",
      "business_impact": "Operational/security risk",
      "estimated_minutes_to_fix": 20,
      "remediation": "Step-by-step fix"
    }}
  ]
}}

Infrastructure Code:
{code_chunk}"""

    elif file_type == "deps":
        return f"""You are a dependency security analyst. Analyze this dependency file.

File: {filename}
Branch: {branch_name}
File Type: Dependency File (requirements.txt/package.json/etc)

Check for:
- Severely outdated packages (major versions behind)
- Packages with known CVEs
- Unpinned versions (*)
- Unmaintained dependencies

Return ONLY valid JSON with no preamble:
{{
  "vulnerabilities": [
    {{
      "package": "package_name==version",
      "type": "OUTDATED|VULNERABLE|UNPINNED",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "current_version": "1.2.3",
      "recommended_version": "2.0.0",
      "explanation": "Why this is a problem",
      "business_impact": "What issues this causes",
      "estimated_minutes_to_fix": 5,
      "remediation": "How to update"
    }}
  ]
}}

Dependencies:
{code_chunk}"""

    else:
        return f"""You are a senior security engineer. Analyze this code for vulnerabilities.

File: {filename}
Branch: {branch_name}
File Type: Application Code

Check for:
- Hardcoded secrets, API keys, passwords
- SQL injection or command injection
- Dangerous functions (eval, exec)
- Unsafe deserialization
- Authentication flaws
- Data exposure

Return ONLY valid JSON with no preamble:
{{
  "vulnerabilities": [
    {{
      "type": "HARDCODED_SECRET|SQL_INJECTION|UNSAFE_EVAL|etc",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "line_range": "10-15",
      "explanation": "What the vulnerability is",
      "business_impact": "Risk to business (data breach, account compromise, etc)",
      "estimated_minutes_to_fix": 10,
      "remediation": "How to fix it"
    }}
  ]
}}

Code:
{code_chunk}"""

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
MODEL_ID = "us.anthropic.claude-haiku-4-5-20251001-v1:0"
REGION = "us-east-1"
MAX_TOKENS = 2048

logger = logging.getLogger(__name__)

session = boto3.Session(profile_name="default")
bedrock = session.client("bedrock-runtime", region_name=REGION)

# ---------------------------------------------------------------------------
# Cost tracking
# ---------------------------------------------------------------------------

cost_tracker = {
    "api_calls": 0,
    "input_tokens": 0,
    "output_tokens": 0,
    "estimated_cost": 0.0
}

CLAUDE_HAIKU_INPUT_COST = 0.000001
CLAUDE_HAIKU_OUTPUT_COST = 0.000005

BILLING_THRESHOLD_CALLS = 100
BILLING_THRESHOLD_COST = 5.0

def reset_cost_tracker():
    global cost_tracker
    cost_tracker = {
        "api_calls": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "estimated_cost": 0.0
    }

# ---------------------------------------------------------------------------
# Bedrock invocation
# ---------------------------------------------------------------------------

def invoke_bedrock(prompt: str, filename: str = "") -> dict:
    global cost_tracker
    cost_tracker["api_calls"] += 1

    print(f"\n🔍 BEDROCK ANALYSIS: {filename}")
    print(f"   Prompt length: {len(prompt)} chars")

    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": MAX_TOKENS,
                "temperature": 0.2
            })
        )

        raw = json.loads(response["body"].read())
        text = raw['content'][0]['text'].strip()

        print(f"   Response length: {len(text)} chars")
        print(f"   Response preview: {text[:200]}...")

        if 'usage' in raw:
            cost_tracker["input_tokens"] += raw['usage'].get('input_tokens', 0)
            cost_tracker["output_tokens"] += raw['usage'].get('output_tokens', 0)
        else:
            cost_tracker["input_tokens"] += len(prompt) // 4
            cost_tracker["output_tokens"] += len(text) // 4

        cost_tracker["estimated_cost"] = (
            (cost_tracker["input_tokens"] * CLAUDE_HAIKU_INPUT_COST) +
            (cost_tracker["output_tokens"] * CLAUDE_HAIKU_OUTPUT_COST)
        )

        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
            text = text.rstrip("`").strip()

        result = json.loads(text)
        print(f"   ✅ Parsed JSON successfully. Found {len(result.get('vulnerabilities', []))} vulnerabilities")
        return result

    except json.JSONDecodeError as e:
        print(f"   ❌ JSON parse error: {e}")
        print(f"   Raw text: {text[:300] if 'text' in locals() else 'N/A'}")
        return {"vulnerabilities": []}
    except Exception as e:
        print(f"   ❌ Bedrock error: {e}")
        import traceback
        traceback.print_exc()
        return {"vulnerabilities": []}

# ---------------------------------------------------------------------------
# Per-chunk scanning
# ---------------------------------------------------------------------------

def scan_chunk(chunk: dict, branch_name: str = "main") -> dict:
    filename = chunk.get("file") or chunk.get("filename", "unknown")
    content = chunk.get("code") or chunk.get("content", "")
    file_type = classify_file(filename)

    print(f"\n📄 Scanning: {filename} (type: {file_type}, size: {len(content)} chars)")

    prompt = generate_security_prompt(filename, content, file_type, branch_name)
    result = invoke_bedrock(prompt, filename)
    vulnerabilities = result.get("vulnerabilities", [])

    print(f"   Found {len(vulnerabilities)} vulnerabilities")

    return {
        "file": filename,
        "file_type": file_type,
        "vulnerabilities": vulnerabilities,
        "has_issues": len(vulnerabilities) > 0,
        "vulnerability_count": len(vulnerabilities)
    }


def scan_all_chunks(chunks: list, branch_name: str = "main") -> dict:
    reset_cost_tracker()

    print(f"\n{'='*60}")
    print(f"🔬 BEDROCK ANALYSIS STARTING")
    print(f"{'='*60}")
    print(f"Total chunks to analyze: {len(chunks)}")
    print(f"Branch: {branch_name}")
    print(f"{'='*60}")

    vulnerable_files = []
    all_vulnerabilities = []

    for i, chunk in enumerate(chunks, 1):
        filename = chunk.get("file") or chunk.get("filename", "unknown")
        print(f"\n[{i}/{len(chunks)}] Processing: {filename}")
        logger.info(f"Analyzing chunk {i}/{len(chunks)}: {filename}")

        result = scan_chunk(chunk, branch_name)

        if result["has_issues"]:
            vulnerable_files.append({
                "file": filename,
                "type": result["file_type"],
                "count": result["vulnerability_count"]
            })
            all_vulnerabilities.extend(result["vulnerabilities"])

    print(f"\n{'='*60}")
    print(f"📊 ANALYSIS COMPLETE")
    print(f"{'='*60}")
    print(f"Total vulnerabilities found: {len(all_vulnerabilities)}")
    print(f"Files with issues: {len(vulnerable_files)}")
    print(f"API calls made: {cost_tracker['api_calls']}")
    print(f"Estimated cost: ${cost_tracker['estimated_cost']:.4f}")
    print(f"{'='*60}\n")

    return {
        "vulnerable_files": vulnerable_files,
        "vulnerabilities": all_vulnerabilities,
        "total_files_analyzed": len(chunks),
        "files_with_issues": len(vulnerable_files),
        "total_vulnerabilities": len(all_vulnerabilities),
        "cost_tracker": cost_tracker.copy(),
        "billing": {
            "calls_made": cost_tracker["api_calls"],
            "free_calls_remaining": max(0, BILLING_THRESHOLD_CALLS - cost_tracker["api_calls"]),
            "estimated_cost": cost_tracker["estimated_cost"],
            "will_be_charged": cost_tracker["estimated_cost"] >= BILLING_THRESHOLD_COST or cost_tracker["api_calls"] >= BILLING_THRESHOLD_CALLS,
            "alternatives": [
                {"name": "SonarQube Community", "cost": "Free", "url": "https://www.sonarqube.org/"},
                {"name": "GitHub CodeQL", "cost": "Free (open source)", "url": "https://codeql.github.com/"},
                {"name": "Snyk", "cost": "$50+/month", "url": "https://snyk.io/"},
                {"name": "Checkmarx", "cost": "Enterprise pricing", "url": "https://checkmarx.com/"}
            ]
        }
    }