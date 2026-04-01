# =============================================================================
# bedrock_client.py — Core AI engine for GitHopper
# Owner: Ananya (AI / Bedrock Eng)
# =============================================================================

import boto3
import json
import logging
import sys
import os

# Add ai directory to path for prompts imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from prompts import (
    APP_SECURITY_PROMPT,
    IAC_SECURITY_PROMPT,
    IAM_PROMPT,
    DEBT_PROMPT,
    DEPENDENCY_PROMPT,
)

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
# Config
# ---------------------------------------------------------------------------
MODEL_ID = "nvidia.nemotron-nano-12b-v2"  # Use available model
REGION = "us-east-1"  # Match CLI region
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

# Opus 4.6 pricing (approximate): $3 per 1M input tokens, $15 per 1M output tokens
CLAUDE_OPUS_INPUT_COST = 0.000003  # $3 per 1M tokens
CLAUDE_OPUS_OUTPUT_COST = 0.000015  # $15 per 1M tokens

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
    Scans a single code chunk and returns findings.

    Input:
        chunk = {
            "file": "config/db.py",
            "code": "...raw code..."
        }
        branch_name = "feature/auth" (optional, defaults to "main")

    Output:
        {
            "security_findings": [...],
            "debt_findings": [...]
        }
    """
    filename = chunk.get("file") or chunk.get("filename")
    content = chunk.get("code") or chunk.get("content")
    file_type = classify_file(filename)

    security_findings = []
    debt_findings = []

    if file_type == "iam":
        result = invoke_bedrock(
            IAM_PROMPT.format(filename=filename, branch_name=branch_name, code_chunk=content)
        )
        security_findings = result.get("findings", [])

    elif file_type == "iac":
        result = invoke_bedrock(
            IAC_SECURITY_PROMPT.format(filename=filename, branch_name=branch_name, code_chunk=content)
        )
        security_findings = result.get("findings", [])

    elif file_type == "deps":
        result = invoke_bedrock(
            DEPENDENCY_PROMPT.format(filename=filename, branch_name=branch_name, code_chunk=content)
        )
        security_findings = result.get("findings", [])

    else:
        # app code: run both security + debt scan
        sec = invoke_bedrock(
            APP_SECURITY_PROMPT.format(filename=filename, branch_name=branch_name, code_chunk=content)
        )
        debt = invoke_bedrock(
            DEBT_PROMPT.format(filename=filename, branch_name=branch_name, code_chunk=content)
        )
        security_findings = sec.get("findings", [])
        debt_findings = debt.get("findings", [])

    return {
        "security_findings": security_findings,
        "debt_findings": debt_findings
    }


# ---------------------------------------------------------------------------
# Full repo scan — called by lambda_processor
# ---------------------------------------------------------------------------

def scan_all_chunks(chunks: list, branch_name: str = "main") -> dict:
    """
    Scans all chunks from a repo and aggregates findings.

    Input:
        chunks = [
            {"file": "app.py", "code": "..."},
            {"file": "terraform.tf", "code": "..."},
            ...
        ]
        branch_name = "feature/auth" (optional, defaults to "main")

    Output:
        {
            "security_findings": [...],
            "debt_findings": [...],
            "cost_tracker": {
                "api_calls": 12,
                "input_tokens": 45000,
                "output_tokens": 12000,
                "estimated_cost": 0.23
            }
        }
    """
    reset_cost_tracker()
    all_security = []
    all_debt = []

    for chunk in chunks:
        filename = chunk.get("file") or chunk.get("filename", "unknown")
        logger.info(f"Scanning: {filename}")
        result = scan_chunk(chunk, branch_name)
        all_security.extend(result["security_findings"])
        all_debt.extend(result["debt_findings"])

    return {
        "security_findings": all_security,
        "debt_findings": all_debt,
        "cost_tracker": cost_tracker.copy()
    }