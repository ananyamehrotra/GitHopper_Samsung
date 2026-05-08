# =============================================================================
# openclaw_client.py — OpenClaw-compatible AI engine for GitHopper
# Routes analysis to Groq or local Ollama while presenting OpenClaw behavior.
# =============================================================================

import json
import logging
import os
import sys
from typing import Dict, Tuple

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aggregator import aggregate_all
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import billing

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
        return f"""You are a senior code quality engineer and security specialist. Analyze this code for BOTH security vulnerabilities AND technical debt.

File: {filename}
Branch: {branch_name}
File Type: Application Code

Security Check List:
- Hardcoded secrets, API keys, passwords
- SQL injection or command injection
- Dangerous functions (eval, exec)
- Unsafe deserialization
- Authentication flaws
- Data exposure

Code Quality/Debt Check List:
- High cyclomatic complexity (deeply nested code)
- Long functions (>50 lines)
- Code duplication
- Missing error handling
- Missing comments for complex logic
- Poor variable naming
- Large parameter lists (>3 params)
- Dead code or unused imports

Return ONLY valid JSON array with no preamble. Mix security findings and code quality findings:
[
    {{
        "type": "HARDCODED_SECRET|SQL_INJECTION|UNSAFE_EVAL|COMPLEXITY|CODE_DUPLICATION|MISSING_HANDLER|etc",
        "severity": "CRITICAL|HIGH|MEDIUM|LOW",
        "file": "{filename}",
        "line_range": "10-15",
        "explanation": "What the issue is",
        "business_impact": "Risk to business",
        "estimated_minutes_to_fix": 10,
        "remediation": "How to fix it"
    }}
]

Code:
{code_chunk}"""

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

OPENCLAW_PROVIDER = os.environ.get("OPENCLAW_PROVIDER", "groq").strip().lower()
OPENCLAW_MODEL = os.environ.get("OPENCLAW_MODEL", "").strip()
OPENCLAW_MAX_TOKENS = int(os.environ.get("OPENCLAW_MAX_TOKENS", "2048"))
OPENCLAW_TEMPERATURE = float(os.environ.get("OPENCLAW_TEMPERATURE", "0.2"))
OPENCLAW_TIMEOUT_SECONDS = int(os.environ.get("OPENCLAW_TIMEOUT_SECONDS", "60"))

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "").strip()
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile").strip()
GROQ_BASE_URL = os.environ.get("GROQ_BASE_URL", "https://api.groq.com/openai/v1").strip().rstrip("/")

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434").strip().rstrip("/")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.1").strip()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# ---------------------------------------------------------------------------
# Cost tracking
# ---------------------------------------------------------------------------

cost_tracker = {
    "api_calls": 0,
    "input_tokens": 0,
    "output_tokens": 0,
    "estimated_cost": 0.0
}

_openclaw_unavailable = False
_openclaw_fallback_notice_shown = False

# ---------------------------------------------------------------------------
# Static Fallback — converts chunker debt_signals → vulnerability objects
# ---------------------------------------------------------------------------

DEBT_SIGNAL_MAP = {
    "password\\s*=":   {"type": "HARDCODED_SECRET",    "severity": "CRITICAL", "minutes": 15,
                        "explanation": "Hardcoded password detected in source code.",
                        "business_impact": "Credential exposure — attackers can directly access databases or services.",
                        "remediation": "Move to environment variables or a secrets manager (AWS Secrets Manager, HashiCorp Vault)."},
    "secret\\s*=":     {"type": "HARDCODED_SECRET",    "severity": "CRITICAL", "minutes": 15,
                        "explanation": "Hardcoded secret/key detected in source code.",
                        "business_impact": "Secret exposure — any developer with repo access can compromise production systems.",
                        "remediation": "Use environment variables loaded via python-dotenv, never commit secrets to git."},
    "api_key\\s*=":    {"type": "HARDCODED_SECRET",    "severity": "CRITICAL", "minutes": 10,
                        "explanation": "Hardcoded API key detected.",
                        "business_impact": "API key exposure — attackers can make requests on your behalf, incur costs, or steal data.",
                        "remediation": "Store API keys in environment variables; rotate the exposed key immediately."},
    "token\\s*=":      {"type": "HARDCODED_SECRET",    "severity": "HIGH",     "minutes": 10,
                        "explanation": "Hardcoded token detected.",
                        "business_impact": "Token exposure — may allow unauthorized access to third-party services.",
                        "remediation": "Move token to .env file, add .env to .gitignore."},
    "hardcoded":       {"type": "HARDCODED_SECRET",    "severity": "HIGH",     "minutes": 10,
                        "explanation": "Hardcoded value flagged as potential secret.",
                        "business_impact": "Potential credential exposure in version control history.",
                        "remediation": "Audit this value and externalize if sensitive."},
    "eval\\(": {"type": "UNSAFE_EVAL",         "severity": "CRITICAL", "minutes": 20,
                "explanation": "Use of eval() allows arbitrary code execution.",
                "business_impact": "Remote code execution — attacker can run any Python/JS code on your server.",
                "remediation": "Remove eval(); use safe alternatives like ast.literal_eval() for Python."},
    "exec\\(": {"type": "UNSAFE_EXEC",         "severity": "CRITICAL", "minutes": 20,
                "explanation": "Use of exec() allows arbitrary code execution.",
                "business_impact": "Remote code execution risk if user input reaches exec().",
                "remediation": "Remove exec(); restructure logic to avoid dynamic code execution."},
    "sql_injection":   {"type": "SQL_INJECTION",       "severity": "CRITICAL", "minutes": 30,
                        "explanation": "SQL injection vulnerability — user input concatenated into query.",
                        "business_impact": "Data breach or full database compromise — attackers can read, modify, or delete all data.",
                        "remediation": "Use parameterized queries or an ORM. Never concatenate user input into SQL strings."},
    "print\\(":        {"type": "DEBUG_LOGGING",       "severity": "LOW",      "minutes": 5,
                        "explanation": "Debug print statements in production code.",
                        "business_impact": "May leak sensitive data to logs; indicates lack of structured logging.",
                        "remediation": "Replace print() with a structured logger (logging module)."},
    "TEMP":           {"type": "CODE_SMELL",           "severity": "LOW",      "minutes": 5,
                        "explanation": "Potential temporary/placeholder code detected.",
                        "business_impact": "Technical debt — placeholder code may indicate incomplete implementation.",
                        "remediation": "Review and replace temporary code with proper implementation."},
}


def _debt_signal_to_vulnerability(signal: dict, filename: str) -> dict:
    """Convert a chunker debt_signal dict into a structured vulnerability object."""
    pattern = signal.get("pattern", "")
    line_no = signal.get("line_number", "?")
    snippet = signal.get("line_snippet", "")

    meta = None
    for key, val in DEBT_SIGNAL_MAP.items():
        if key.lower() in pattern.lower() or pattern.lower() in key.lower():
            meta = val
            break

    if not meta:
        meta = {"type": "CODE_SMELL", "severity": "LOW", "minutes": 5,
                "explanation": f"Potential issue detected: {pattern}",
                "business_impact": "Code quality issue that may pose security risk.",
                "remediation": "Review this pattern and ensure it does not expose sensitive data."}

    return {
        "type": meta["type"],
        "severity": meta["severity"],
        "file": filename,
        "line_range": str(line_no),
        "code_snippet": snippet[:120] if snippet else "",
        "explanation": meta["explanation"],
        "business_impact": meta["business_impact"],
        "estimated_minutes_to_fix": meta["minutes"],
        "remediation": meta["remediation"],
        "source": "static_analysis"
    }


BILLING_THRESHOLD_CALLS = 100
BILLING_THRESHOLD_COST = 5.0


def reset_cost_tracker():
    global cost_tracker, _openclaw_fallback_notice_shown
    cost_tracker = {
        "api_calls": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "estimated_cost": 0.0
    }
    _openclaw_fallback_notice_shown = False


# ---------------------------------------------------------------------------
# OpenClaw invocation (Groq / Ollama)
# ---------------------------------------------------------------------------


def _estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def _parse_json_payload(text: str) -> dict:
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            cleaned = part.strip()
            if cleaned.startswith("json"):
                cleaned = cleaned[4:].strip()
            try:
                result = json.loads(cleaned)
                if isinstance(result, list):
                    return {"vulnerabilities": result}
                return result
            except json.JSONDecodeError:
                continue

    result = json.loads(text)
    if isinstance(result, list):
        return {"vulnerabilities": result}
    return result


def _openclaw_request(prompt: str, temperature: float, max_tokens: int) -> Tuple[str, Dict[str, int]]:
    if OPENCLAW_PROVIDER == "ollama":
        model = OPENCLAW_MODEL or OLLAMA_MODEL
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/chat",
            json=payload,
            timeout=OPENCLAW_TIMEOUT_SECONDS
        )
        response.raise_for_status()
        data = response.json()
        text = data.get("message", {}).get("content", "").strip()
        usage = {
            "input_tokens": data.get("prompt_eval_count") or _estimate_tokens(prompt),
            "output_tokens": data.get("eval_count") or _estimate_tokens(text),
        }
        return text, usage

    if OPENCLAW_PROVIDER == "groq":
        if not GROQ_API_KEY:
            raise RuntimeError("GROQ_API_KEY is not set")
        model = OPENCLAW_MODEL or GROQ_MODEL
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        response = requests.post(
            f"{GROQ_BASE_URL}/chat/completions",
            headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
            json=payload,
            timeout=OPENCLAW_TIMEOUT_SECONDS
        )
        response.raise_for_status()
        data = response.json()
        choice = (data.get("choices") or [{}])[0]
        text = (choice.get("message") or {}).get("content", "").strip()
        usage = {
            "input_tokens": data.get("usage", {}).get("prompt_tokens") or _estimate_tokens(prompt),
            "output_tokens": data.get("usage", {}).get("completion_tokens") or _estimate_tokens(text),
        }
        return text, usage

    raise RuntimeError(f"Unsupported OPENCLAW_PROVIDER: {OPENCLAW_PROVIDER}")


def invoke_openclaw(prompt: str, filename: str = "") -> dict:
    global cost_tracker, _openclaw_unavailable, _openclaw_fallback_notice_shown
    cost_tracker["api_calls"] += 1

    if OPENCLAW_PROVIDER == "groq":
        provider_model = OPENCLAW_MODEL or GROQ_MODEL
    else:
        provider_model = OPENCLAW_MODEL or OLLAMA_MODEL

    print(f"\n[OPENCLAW] Analysis: {filename}")
    print(f"   Provider: {OPENCLAW_PROVIDER}")
    print(f"   Model: {provider_model}")
    print(f"   Prompt length: {len(prompt)} chars")

    if _openclaw_unavailable:
        if not _openclaw_fallback_notice_shown:
            print("   OpenClaw unavailable. Using fallback behavior.")
            _openclaw_fallback_notice_shown = True
        return {"vulnerabilities": []}

    text = None
    try:
        text, usage = _openclaw_request(prompt, OPENCLAW_TEMPERATURE, OPENCLAW_MAX_TOKENS)
        print(f"   Response length: {len(text)} chars")
        print(f"   Response preview: {text[:300]}")

        input_tokens = usage.get("input_tokens", _estimate_tokens(prompt))
        output_tokens = usage.get("output_tokens", _estimate_tokens(text))
        cost_tracker["input_tokens"] += input_tokens
        cost_tracker["output_tokens"] += output_tokens
        billing.track_openclaw_call(input_tokens, output_tokens)
        print(f"   Tokens — in: {input_tokens}, out: {output_tokens}")

        cost_tracker["estimated_cost"] = billing.get_cost_tracker().get("total_cost", 0.0)

        try:
            result = _parse_json_payload(text)
            if isinstance(result, list):
                return {"vulnerabilities": result}
            return result
        except json.JSONDecodeError as e:
            print(f"   JSON parse error: {e}")
            print(f"   Full raw text:\n{text}")
            return {"vulnerabilities": []}

    except Exception as e:
        error_str = str(e)
        error_type = type(e).__name__
        _openclaw_unavailable = True
        if not _openclaw_fallback_notice_shown:
            print(f"   OpenClaw unavailable ({error_type}). Switching to static fallback for this run.")
            _openclaw_fallback_notice_shown = True
        else:
            print(f"   OpenClaw invocation error: {error_type}: {error_str}")
        return {"vulnerabilities": []}

# ---------------------------------------------------------------------------
# Per-chunk scanning
# ---------------------------------------------------------------------------


def scan_chunk(chunk: dict, branch_name: str = "main") -> dict:
    global _openclaw_unavailable
    filename = chunk.get("file") or chunk.get("filename", "unknown")
    content = chunk.get("code") or chunk.get("content", "")
    file_type = classify_file(filename)
    debt_signals = chunk.get("debt_signals", [])

    print(f"\n[SCAN] {filename} (type: {file_type}, size: {len(content)} chars)")

    if _openclaw_unavailable:
        print("   Using static analysis fallback")
        vulnerabilities = [_debt_signal_to_vulnerability(s, filename) for s in debt_signals]
        if vulnerabilities:
            print(f"   Found {len(vulnerabilities)} vulnerabilities (static)")
        return {
            "file": filename,
            "file_type": file_type,
            "vulnerabilities": vulnerabilities,
            "has_issues": len(vulnerabilities) > 0,
            "vulnerability_count": len(vulnerabilities),
            "analysis_mode": "static_fallback"
        }

    prompt = generate_security_prompt(filename, content, file_type, branch_name)
    result = invoke_openclaw(prompt, filename)
    vulnerabilities = result.get("vulnerabilities") or result.get("findings", [])

    for v in vulnerabilities:
        v["file_type"] = file_type
        v["file"] = v.get("file", filename)

    if not vulnerabilities and debt_signals and _openclaw_unavailable:
        vulnerabilities = [_debt_signal_to_vulnerability(s, filename) for s in debt_signals]
        print(f"   OpenClaw returned empty. Using static fallback: {len(vulnerabilities)} findings")

    print(f"   Found {len(vulnerabilities)} vulnerabilities")

    return {
        "file": filename,
        "file_type": file_type,
        "vulnerabilities": vulnerabilities,
        "has_issues": len(vulnerabilities) > 0,
        "vulnerability_count": len(vulnerabilities),
        "analysis_mode": "openclaw" if not _openclaw_unavailable else "static_fallback"
    }


def scan_all_chunks(chunks: list, branch_name: str = "main") -> dict:
    reset_cost_tracker()

    print(f"\n{'='*60}")
    print("OPENCLAW ANALYSIS STARTING")
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

    if _openclaw_unavailable and len(all_vulnerabilities) == 0:
        print("\n[MOCK DATA] OpenClaw unavailable. Injecting mock technical debt findings for testing...")
        try:
            from mock_debt_findings import MOCK_DEBT_FINDINGS
            all_vulnerabilities.extend(MOCK_DEBT_FINDINGS)
            vulnerable_files.append({
                "file": "[MOCK DATA] Multiple files",
                "type": "mixed",
                "count": len(MOCK_DEBT_FINDINGS)
            })
            print(f"[MOCK DATA] Added {len(MOCK_DEBT_FINDINGS)} mock debt findings for UI testing")
        except ImportError:
            print("[WARN] mock_debt_findings module not found. Continuing with empty results.")

    print(f"\n{'='*60}")
    print("ANALYSIS COMPLETE")
    print(f"{'='*60}")
    print(f"Total vulnerabilities found: {len(all_vulnerabilities)}")
    print(f"Files with issues: {len(vulnerable_files)}")
    print(f"API calls made: {cost_tracker['api_calls']}")
    print(f"Estimated cost: ${cost_tracker['estimated_cost']:.4f}")
    print(f"{'='*60}\n")

    aggregated_data = aggregate_all(all_vulnerabilities, cost_tracker.copy(), branch_name)

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
        },
        "aggregated": aggregated_data
    }
