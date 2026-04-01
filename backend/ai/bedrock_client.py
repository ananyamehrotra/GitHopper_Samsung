# =============================================================================
# bedrock_client.py — Core AI engine for GitHopper
# Dynamic prompts generated per repo based on actual file content
# =============================================================================

import boto3
import json
import logging
import sys
import os

# Add ai directory to path for prompts imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# File Classification (copied from utils to avoid import issues)
# ---------------------------------------------------------------------------

IAC_EXTENSIONS = {".tf", ".tfvars"}
IAC_KEYWORDS = {"cloudformation", "template", "stack", "infra"}
IAM_KEYWORDS = {"iam", "policy", "role", "permission", "trust"}
DEP_FILES = {
    "requirements.txt", "package.json", "pipfile",
    "go.mod", "gemfile", "pom.xml"
}

def classify_file(filename: str) -> str:
    """
    Routes a file to the correct scan prompt.
    
    Returns one of:
        'iam'   → IAM policy scan
        'iac'   → Infrastructure-as-code scan
        'deps'  → Dependency health scan
        'app'   → App code security + debt scan
    """
    name = filename.lower()
    base = name.rsplit("/", 1)[-1]
    ext = "." + base.rsplit(".", 1)[-1] if "." in base else ""

    # dependency files
    if base in DEP_FILES:
        return "deps"

    # IAM — JSON files with policy-related names
    if ext == ".json" and any(kw in name for kw in IAM_KEYWORDS):
        return "iam"

    # IaC — Terraform
    if ext in IAC_EXTENSIONS:
        return "iac"

    # IaC — CloudFormation YAML
    if ext in {".yaml", ".yml"} and any(kw in name for kw in IAC_KEYWORDS):
        return "iac"

    return "app"

# ---------------------------------------------------------------------------
# Dynamic Prompt Generation (based on actual file content)
# ---------------------------------------------------------------------------

def generate_security_prompt(filename: str, code_chunk: str, file_type: str, branch_name: str) -> str:
    """Generate dynamic security prompt based on actual file content and type"""
    
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
    
    else:  # app code
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
MODEL_ID = "anthropic.claude-opus-4-6-v1"
REGION = "ap-south-2"
MAX_TOKENS = 2048

logger = logging.getLogger(__name__)

# Use session with default profile to ensure correct credentials
session = boto3.Session(profile_name="default")
bedrock = session.client("bedrock-runtime", region_name=REGION)

# ---------------------------------------------------------------------------
# Bedrock invocation
# ---------------------------------------------------------------------------

# Track cost metrics
cost_tracker = {
    "api_calls": 0,
    "input_tokens": 0,
    "output_tokens": 0,
    "estimated_cost": 0.0
}

# Opus 4.6 pricing: $3 per 1M input tokens, $15 per 1M output tokens
CLAUDE_OPUS_INPUT_COST = 0.000003
CLAUDE_OPUS_OUTPUT_COST = 0.000015

# Billing threshold - when user gets charged
BILLING_THRESHOLD_CALLS = 100  # After 100 calls
BILLING_THRESHOLD_COST = 5.0   # After $5 spent

def reset_cost_tracker():
    """Reset cost metrics for new analysis"""
    global cost_tracker
    cost_tracker = {
        "api_calls": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "estimated_cost": 0.0
    }

def invoke_bedrock(prompt: str) -> dict:
    """
    Sends a prompt to Claude via Bedrock.
    Returns parsed JSON dict with vulnerabilities.
    """
    global cost_tracker
    cost_tracker["api_calls"] += 1
    
    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps({
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": MAX_TOKENS,
                "temperature": 0.2
            })
        )
        raw = json.loads(response["body"].read())
        text = raw['content'][0]['text'].strip()
        
        # Track token usage
        if 'usage' in raw:
            cost_tracker["input_tokens"] += raw['usage'].get('input_tokens', 0)
            cost_tracker["output_tokens"] += raw['usage'].get('output_tokens', 0)
        else:
            # Estimate
            cost_tracker["input_tokens"] += len(prompt) // 4
            cost_tracker["output_tokens"] += len(text) // 4
        
        # Calculate cost
        cost_tracker["estimated_cost"] = (
            (cost_tracker["input_tokens"] * CLAUDE_OPUS_INPUT_COST) +
            (cost_tracker["output_tokens"] * CLAUDE_OPUS_OUTPUT_COST)
        )

        # Strip markdown if needed
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]

        return json.loads(text)

    except json.JSONDecodeError as e:
        logger.error(f"JSON parse error: {e}")
        return {"vulnerabilities": []}
    except Exception as e:
        logger.error(f"Bedrock error: {e}")
        return {"vulnerabilities": []}

def invoke_bedrock(prompt: str) -> dict:
    """
    Sends a prompt to Claude via Bedrock.
    Returns parsed JSON dict, or {"findings": []} on failure.
    Also tracks API calls and token usage for cost calculation.
    """
    global cost_tracker
    cost_tracker["api_calls"] += 1
    
    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps({
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": MAX_TOKENS,
                "temperature": 0.1
            })
        )
        raw = json.loads(response["body"].read())
        text = raw['choices'][0]['message']['content'].strip()
        
        # Track token usage if available in response
        if 'usage' in raw:
            cost_tracker["input_tokens"] += raw['usage'].get('input_tokens', 0)
            cost_tracker["output_tokens"] += raw['usage'].get('output_tokens', 0)
        else:
            # Estimate token count (rough approximation)
            prompt_tokens = len(prompt) // 4
            response_tokens = len(text) // 4
            cost_tracker["input_tokens"] += prompt_tokens
            cost_tracker["output_tokens"] += response_tokens
        
        # Calculate estimated cost
        cost_tracker["estimated_cost"] = (
            (cost_tracker["input_tokens"] * CLAUDE_OPUS_INPUT_COST) +
            (cost_tracker["output_tokens"] * CLAUDE_OPUS_OUTPUT_COST)
        )

        # strip markdown fences if model adds them
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]

        return json.loads(text)

    except json.JSONDecodeError as e:
        logger.error(f"JSON parse error from Bedrock: {e}")
        return {"findings": []}
    except Exception as e:
        logger.error(f"Bedrock invocation error: {e}")
        return {"findings": []}


# ---------------------------------------------------------------------------
# Per-chunk scanning
# ---------------------------------------------------------------------------

def scan_chunk(chunk: dict, branch_name: str = "main") -> dict:
    """
    Analyzes a single code chunk using dynamic Bedrock prompt.
    
    Input: chunk {"file": "app.py", "code": "..."}
    Output: {
        "file": "app.py",
        "file_type": "app",
        "vulnerabilities": [...],
        "has_issues": bool
    }
    """
    filename = chunk.get("file") or chunk.get("filename", "unknown")
    content = chunk.get("code") or chunk.get("content", "")
    file_type = classify_file(filename)
    
    # Generate dynamic prompt based on file type and content
    prompt = generate_security_prompt(filename, content, file_type, branch_name)
    
    # Invoke Bedrock with dynamic prompt
    result = invoke_bedrock(prompt)
    vulnerabilities = result.get("vulnerabilities", [])
    
    return {
        "file": filename,
        "file_type": file_type,
        "vulnerabilities": vulnerabilities,
        "has_issues": len(vulnerabilities) > 0,
        "vulnerability_count": len(vulnerabilities)
    }


def scan_all_chunks(chunks: list, branch_name: str = "main") -> dict:
    """
    Scans all chunks with dynamic per-repo prompts.
    Returns summary of vulnerable files + detailed analysis.
    """
    reset_cost_tracker()
    
    vulnerable_files = []
    all_vulnerabilities = []
    unique_files_analyzed = set()  # Track unique files (not chunks)
    
    for chunk in chunks:
        filename = chunk.get("file") or chunk.get("filename", "unknown")
        unique_files_analyzed.add(filename)
        logger.info(f"Analyzing: {filename}")
        
        result = scan_chunk(chunk, branch_name)
        
        # Collect vulnerable files (deduplicate by filename)
        if result["has_issues"]:
            # Check if this file is already in the list
            existing = next((f for f in vulnerable_files if f["file"] == filename), None)
            if existing:
                # Add to count for this file
                existing["count"] += result["vulnerability_count"]
                all_vulnerabilities.extend(result["vulnerabilities"])
            else:
                # New file with issues
                vulnerable_files.append({
                    "file": filename,
                    "type": result["file_type"],
                    "count": result["vulnerability_count"]
                })
                all_vulnerabilities.extend(result["vulnerabilities"])
    
    return {
        "vulnerable_files": vulnerable_files,
        "vulnerabilities": all_vulnerabilities,
        "total_files_analyzed": len(unique_files_analyzed),
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