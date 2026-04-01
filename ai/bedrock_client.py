# =============================================================================
# bedrock_client.py — Core AI engine for GitHopper
# Owner: Ananya (AI / Bedrock Eng)
# =============================================================================

import boto3
import json
import logging

from prompts import (
    APP_SECURITY_PROMPT,
    IAC_SECURITY_PROMPT,
    IAM_PROMPT,
    DEBT_PROMPT,
    DEPENDENCY_PROMPT,
)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

MODEL_ID = "anthropic.claude-sonnet-4-5-20251001"
REGION = "us-east-1"
MAX_TOKENS = 2048

logger = logging.getLogger(__name__)

bedrock = boto3.client("bedrock-runtime", region_name="ap-south-2")

# ---------------------------------------------------------------------------
# File classification
# ---------------------------------------------------------------------------

IAC_EXTENSIONS = {".tf", ".tfvars"}
IAC_KEYWORDS = {"cloudformation", "template", "stack", "infra"}
IAM_KEYWORDS = {"iam", "policy", "role", "permission", "trust"}
DEP_FILES = {"requirements.txt", "package.json", "pipfile", "go.mod", "gemfile", "pom.xml"}
SKIP_DEBT_FOR = {".tf", ".tfvars", ".json"}  # IaC/IAM files don't need debt scan


def classify_file(filename: str) -> str:
    """
    Decides which prompt strategy to use for a given file.

    Returns one of: 'iam', 'iac', 'deps', 'app'
    """
    name = filename.lower()
    # get just the base filename (no path)
    base = name.rsplit("/", 1)[-1]
    ext = "." + base.rsplit(".", 1)[-1] if "." in base else ""

    # dependency files — check base filename exactly
    if base in DEP_FILES:
        return "deps"

    # IAM — JSON files that look like policies
    if ext == ".json" and any(kw in name for kw in IAM_KEYWORDS):
        return "iam"

    # IaC — Terraform files or CloudFormation templates
    if ext in IAC_EXTENSIONS:
        return "iac"
    if ext in {".yaml", ".yml"} and any(kw in name for kw in IAC_KEYWORDS):
        return "iac"

    # everything else is app code
    return "app"


# ---------------------------------------------------------------------------
# Bedrock invocation
# ---------------------------------------------------------------------------

def invoke_bedrock(prompt: str) -> dict:
    """
    Sends a prompt to Claude 3 Sonnet via Bedrock.
    Returns parsed JSON dict, or {"findings": []} on failure.
    """
    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": MAX_TOKENS,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            })
        )
        raw = json.loads(response["body"].read())
        text = raw["content"][0]["text"].strip()

        # strip markdown fences if Claude adds them despite instructions
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

def scan_chunk(chunk: dict) -> dict:
    """
    Scans a single code chunk and returns findings.

    Input:
        chunk = {
            "filename": "config/db.py",
            "content": "...raw code..."
        }

    Output:
        {
            "security_findings": [...],
            "debt_findings": [...]
        }
    """
    filename = chunk["filename"]
    content = chunk["content"]
    file_type = classify_file(filename)

    security_findings = []
    debt_findings = []

    if file_type == "iam":
        result = invoke_bedrock(
            IAM_PROMPT.format(filename=filename, code_chunk=content)
        )
        security_findings = result.get("findings", [])

    elif file_type == "iac":
        result = invoke_bedrock(
            IAC_SECURITY_PROMPT.format(filename=filename, code_chunk=content)
        )
        security_findings = result.get("findings", [])

    elif file_type == "deps":
        result = invoke_bedrock(
            DEPENDENCY_PROMPT.format(filename=filename, code_chunk=content)
        )
        security_findings = result.get("findings", [])

    else:
        # app code: run both security + debt scan
        sec = invoke_bedrock(
            APP_SECURITY_PROMPT.format(filename=filename, code_chunk=content)
        )
        debt = invoke_bedrock(
            DEBT_PROMPT.format(filename=filename, code_chunk=content)
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

def scan_all_chunks(chunks: list) -> dict:
    """
    Scans all chunks from a repo and aggregates findings.

    Input:
        chunks = [
            {"filename": "app.py", "content": "..."},
            {"filename": "terraform.tf", "content": "..."},
            ...
        ]

    Output:
        {
            "security_findings": [...],
            "debt_findings": [...]
        }
    """
    all_security = []
    all_debt = []

    for chunk in chunks:
        logger.info(f"Scanning: {chunk['filename']}")
        result = scan_chunk(chunk)
        all_security.extend(result["security_findings"])
        all_debt.extend(result["debt_findings"])

    return {
        "security_findings": all_security,
        "debt_findings": all_debt
    }