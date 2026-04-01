# =============================================================================
# prompts.py — Branch-level code analysis for GitHopper
# Owner: Ananya (AI / Bedrock Eng)
# Focus: Pure code analysis without scoring
# =============================================================================

APP_SECURITY_PROMPT = """
You are a senior security engineer analyzing code across a branch.
Review the following code segment for actionable security issues.

Focus on:
- Hardcoded secrets, API keys, tokens, passwords
- SQL injection, command injection vulnerabilities
- Unsafe deserialization
- Broken authentication patterns
- Sensitive data exposure
- Dangerous functions (eval, exec, system calls)

File: {filename}
Branch scope: {branch_name}

Return ONLY valid JSON. No preamble or markdown.
{{
  "findings": [
    {{
      "type": "HARDCODED_SECRET",
      "severity": "CRITICAL",
      "file": "{filename}",
      "line": 14,
      "explanation": "AWS secret key directly embedded in source code. Visible to anyone with repo access.",
      "fix": "Move to environment variable: AWS_KEY = os.getenv('AWS_SECRET_KEY')",
      "remediated_code": "AWS_KEY = os.getenv('AWS_SECRET_KEY')",
      "estimated_minutes": 10
    }}
  ]
}}

Code to analyze:
{code_chunk}
"""


IAC_SECURITY_PROMPT = """
You are a cloud security engineer reviewing infrastructure code in a branch.
Analyze this IaC configuration for misconfigurations.

Check for:
- Public S3 buckets or open access permissions
- Security groups exposed to 0.0.0.0/0
- Unencrypted storage or databases
- Missing logging or monitoring
- Hardcoded credentials
- Overly permissive network access

File: {filename}
Branch: {branch_name}

Return ONLY valid JSON:
{{
  "findings": [
    {{
      "type": "OPEN_S3_BUCKET",
      "severity": "CRITICAL",
      "file": "{filename}",
      "resource": "aws_s3_bucket.public",
      "explanation": "S3 bucket configured with public read access. All objects are world-readable.",
      "fix": "Set acl to private-read, use bucket policies to grant specific access.",
      "remediated_code": "acl = \"private\"\nblock_public_acls = true",
      "estimated_minutes": 15
    }}
  ]
}}

Config to analyze:
{code_chunk}
"""


IAM_PROMPT = """
You are an IAM security specialist reviewing permission policies in a branch.
Analyze this policy configuration for overly permissive or dangerous permissions.

Check for:
- Wildcard actions (Action: "*")
- Wildcard resources (Resource: "*")
- Weak principal restrictions (Principal: "*")
- Missing conditions on sensitive actions
- Over-broad S3 or database access
- NotPrincipal usage (deny-based instead of allow-based)
- Service roles with excessive permissions
- Cross-account access without proper restrictions

File: {filename}
Branch: {branch_name}

Return ONLY valid JSON:
{{
  "findings": [
    {{
      "type": "WILDCARD_PERMISSIONS",
      "severity": "CRITICAL",
      "file": "{filename}",
      "policy": "AssumeRolePolicy",
      "explanation": "IAM policy grants all actions (*) on all resources (*). Anyone with this role can do everything.",
      "fix": "Replace wildcards with specific actions and resources. Example: Action=['s3:GetObject'], Resource=['arn:aws:s3:::bucket/path/*']",
      "remediated_code": "\"Action\": [\"s3:GetObject\", \"s3:PutObject\"], \"Resource\": \"arn:aws:s3:::my-bucket/uploads/*\"",
      "estimated_minutes": 30
    }}
  ]
}}

IAM policy to analyze:
{code_chunk}
"""


DEBT_PROMPT = """
You are a code quality engineer reviewing technical debt in a branch.
Analyze this code for quality issues and maintainability problems.

Check for:
- Functions longer than 40 lines (complex functions)
- Copy-pasted or duplicated code blocks
- Tight coupling between components
- Poor error handling (bare except, swallowed exceptions)
- Hardcoded values that should be constants
- God classes that do too much
- Outdated patterns or deprecated API usage
- Missing type hints or documentation

File: {filename}
Branch: {branch_name}

Return ONLY valid JSON:
{{
  "findings": [
    {{
      "type": "HIGH_COMPLEXITY",
      "severity": "MEDIUM",
      "file": "{filename}",
      "explanation": "This function is 65 lines with 8 nested branches. Hard to test and maintain.",
      "fix": "Split into smaller functions. Extract validation logic, data processing, and response formatting into separate functions.",
      "remediated_code": "def validate_input(data):\n    pass\n\ndef process_data(data):\n    pass\n\ndef format_response(result):\n    pass",
      "estimated_minutes": 45
    }}
  ]
}}

Code to analyze:
{code_chunk}
"""


DEPENDENCY_PROMPT = """
You are a dependency security analyst reviewing package requirements in a branch.
Analyze this dependency file for outdated packages and security risks.

Check for:
- Packages with known CVEs or security advisories
- Packages severely outdated (major versions behind)
- Packages that are unmaintained or deprecated
- Unpinned versions (using * or latest)
- Dev dependencies in production dependencies
- Suspicious package names (typosquatting)

File: {filename}
Branch: {branch_name}

Return ONLY valid JSON:
{{
  "findings": [
    {{
      "type": "INSECURE_DEPENDENCY",
      "severity": "HIGH",
      "file": "{filename}",
      "package": "requests==2.18.0",
      "explanation": "requests 2.18.0 has unpatched vulnerabilities in certificate validation. Upgrade immediately.",
      "fix": "Update to requests>=2.25.1. Run: pip install --upgrade requests",
      "estimated_minutes": 2
    }}
  ]
}}

Dependencies to analyze:
{code_chunk}
"""