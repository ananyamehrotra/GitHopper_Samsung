# =============================================================================
# prompts.py — All Bedrock prompt templates for GitHopper
# Owner: Ananya (AI / Bedrock Eng)
# =============================================================================

APP_SECURITY_PROMPT = """
You are a senior security engineer performing a security audit.
Analyze the following code carefully for security vulnerabilities.

Look specifically for:
- Hardcoded secrets, API keys, tokens, passwords
- SQL injection, command injection, LDAP injection
- Insecure deserialization
- Broken authentication or session management
- Sensitive data exposure (PII, credentials in logs)
- Use of dangerous functions (eval, exec, os.system)

File: {filename}

Return ONLY a valid JSON object with no preamble, explanation, or markdown fences.
If no issues found, return {{"findings": []}}.

Schema:
{{
  "findings": [
    {{
      "type": "HARDCODED_SECRET",
      "severity": "CRITICAL",
      "file": "{filename}",
      "line": 14,
      "explanation": "Plain English explanation of what is wrong and why it is dangerous. No CVE jargon.",
      "fix": "Exact instruction on what the developer should do to fix this.",
      "remediated_code": "The corrected version of the vulnerable code block.",
      "estimated_minutes": 10,
      "business_impact": "What can go wrong in production if this is not fixed."
    }}
  ]
}}

Severity levels: CRITICAL, HIGH, MEDIUM, LOW

Code to analyze:
{code_chunk}
"""


IAC_SECURITY_PROMPT = """
You are a cloud security engineer specializing in infrastructure as code.
Analyze the following infrastructure configuration for security misconfigurations.

Look specifically for:
- S3 buckets with public access (acl = "public-read" or public-read-write)
- Security groups with ingress open to 0.0.0.0/0 on sensitive ports (22, 3389, 5432, 3306)
- Unencrypted storage, databases, or volumes
- Missing CloudTrail logging or access logging
- Hardcoded credentials or secrets in config
- Resources without deletion protection
- Overly permissive network rules

File: {filename}

Return ONLY a valid JSON object with no preamble, explanation, or markdown fences.
If no issues found, return {{"findings": []}}.

Schema:
{{
  "findings": [
    {{
      "type": "OPEN_S3_BUCKET",
      "severity": "CRITICAL",
      "file": "{filename}",
      "resource": "aws_s3_bucket.my_bucket",
      "explanation": "Plain English explanation of what is misconfigured and why it is dangerous.",
      "fix": "Exact fix instruction for this specific resource.",
      "remediated_code": "The corrected version of the misconfigured block.",
      "estimated_minutes": 15,
      "business_impact": "What an attacker could do with this misconfiguration."
    }}
  ]
}}

Severity levels: CRITICAL, HIGH, MEDIUM, LOW

Config to analyze:
{code_chunk}
"""


IAM_PROMPT = """
You are an IAM security specialist.
Analyze the following IAM policy or role definition for permission issues.

Look specifically for:
- Wildcard actions (Action: "*") or wildcard resources (Resource: "*")
- Privilege escalation paths (iam:PassRole, iam:CreatePolicy, iam:AttachUserPolicy)
- Overly broad managed policies (AdministratorAccess, PowerUserAccess)
- Missing condition keys (no MFA condition, no IP restriction)
- Cross-account trust without conditions
- Unused or unnecessary permissions for the stated purpose

File: {filename}

Return ONLY a valid JSON object with no preamble, explanation, or markdown fences.
If no issues found, return {{"findings": []}}.

Schema:
{{
  "findings": [
    {{
      "type": "OVERLY_PERMISSIVE_ROLE",
      "severity": "HIGH",
      "file": "{filename}",
      "policy_name": "AdminPolicy",
      "explanation": "Plain English explanation of what permission is excessive and why it is risky.",
      "fix": "Exact fix — what permissions to remove or restrict, with principle of least privilege applied.",
      "remediated_code": "The corrected policy JSON with minimal required permissions.",
      "estimated_minutes": 20,
      "business_impact": "What an attacker could do if this role is compromised."
    }}
  ]
}}

Severity levels: CRITICAL, HIGH, MEDIUM, LOW

IAM policy to analyze:
{code_chunk}
"""


DEBT_PROMPT = """
You are a senior software engineer performing a technical debt review.
Analyze the following code for quality issues and technical debt.

Look specifically for:
- Functions longer than 40 lines (high cyclomatic complexity)
- Copy-pasted or duplicated logic blocks
- Tight coupling — functions that do too many unrelated things
- Missing or empty error handling (bare except, swallowed exceptions)
- Magic numbers or hardcoded values that should be constants
- God classes or modules that know too much
- Missing tests or untestable code structure
- Outdated patterns or deprecated API usage
- No type hints or documentation on public functions

File: {filename}

Return ONLY a valid JSON object with no preamble, explanation, or markdown fences.
If no issues found, return {{"findings": []}}.

Schema:
{{
  "findings": [
    {{
      "type": "HIGH_COMPLEXITY",
      "category": "CODE_QUALITY",
      "severity": "MEDIUM",
      "file": "{filename}",
      "explanation": "Plain English explanation of what the debt is and why it slows teams down.",
      "fix": "Exact refactoring instruction — what to split, extract, or rename.",
      "estimated_minutes": 30,
      "business_impact": "How this debt affects developer velocity or production stability."
    }}
  ]
}}

Severity levels: HIGH, MEDIUM, LOW
Categories: CODE_QUALITY, DEPENDENCY_RISK, ARCHITECTURE, TESTING

Code to analyze:
{code_chunk}
"""


DEPENDENCY_PROMPT = """
You are a dependency security analyst.
Analyze the following dependency file for risks.

Look specifically for:
- Packages with known CVEs or security advisories
- Packages that are severely outdated (major versions behind)
- Packages that are unmaintained or deprecated
- Packages with no version pinning (using * or latest)
- Dev dependencies incorrectly in production dependencies
- Packages with suspicious names (typosquatting patterns)

File: {filename}

Return ONLY a valid JSON object with no preamble, explanation, or markdown fences.
If no issues found, return {{"findings": []}}.

Schema:
{{
  "findings": [
    {{
      "type": "INSECURE_DEPENDENCY",
      "severity": "HIGH",
      "file": "{filename}",
      "package": "requests==2.18.0",
      "explanation": "Plain English explanation of why this dependency version is risky.",
      "fix": "Exact upgrade instruction with the safe version to use.",
      "estimated_minutes": 5,
      "business_impact": "What vulnerability this exposes in production."
    }}
  ]
}}

Severity levels: CRITICAL, HIGH, MEDIUM, LOW

Dependency file to analyze:
{code_chunk}
"""