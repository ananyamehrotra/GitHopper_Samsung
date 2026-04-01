# =============================================================================
# test_bedrock.py — Local test for Ananya's Bedrock engine
# Run: python test_bedrock.py
# Needs: AWS credentials configured (aws configure) + boto3 installed
# =============================================================================

import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../ai"))
from bedrock_client import scan_chunk, scan_all_chunks, classify_file

# ---------------------------------------------------------------------------
# Test chunks — planted vulnerabilities across all 4 types
# ---------------------------------------------------------------------------

APP_CODE_CHUNK = {
    "filename": "config/db.py",
    "content": """
import requests
import os

# Database config
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "admin123"
API_TOKEN = "sk-proj-abc123xyz"

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def process_data(data):
    result = eval(data)
    return result

def fetch_internal():
    url = "http://internal-api/data?user=" + input("enter user: ")
    return requests.get(url)
"""
}

IAC_CHUNK = {
    "filename": "infrastructure/main.tf",
    "content": """
resource "aws_s3_bucket" "data_bucket" {
  bucket = "my-company-data"
  acl    = "public-read"
}

resource "aws_security_group" "web_sg" {
  name = "web-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "main" {
  engine            = "mysql"
  instance_class    = "db.t3.micro"
  storage_encrypted = false
  publicly_accessible = true
  password          = "hardcoded_password_123"
}
"""
}

IAM_CHUNK = {
    "filename": "iam/admin_policy.json",
    "content": """{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreatePolicy",
        "iam:AttachUserPolicy",
        "iam:PassRole"
      ],
      "Resource": "*"
    }
  ]
}"""
}

DEPS_CHUNK = {
    "filename": "requirements.txt",
    "content": """
flask==0.12.0
requests==2.18.0
django==2.0.0
pillow==5.0.0
pyyaml==3.12
cryptography==2.1.0
sqlalchemy==1.2.0
"""
}

DEBT_CHUNK = {
    "filename": "utils/processor.py",
    "content": """
def process_everything(data, user, config, db, cache, logger, flags, retries, timeout, mode):
    try:
        if mode == 1:
            result = []
            for i in range(len(data)):
                if data[i] > 0:
                    result.append(data[i] * 2)
                elif data[i] < 0:
                    result.append(data[i] * -1)
                else:
                    result.append(0)
            for i in range(len(result)):
                if result[i] > 100:
                    result[i] = 100
                elif result[i] < 0:
                    result[i] = 0
            db.save(result)
            cache.set("result", result)
            logger.log(result)
            user.notify(result)
            config.update({"last_run": "now"})
            return result
        elif mode == 2:
            result = []
            for i in range(len(data)):
                if data[i] > 0:
                    result.append(data[i] * 2)
                elif data[i] < 0:
                    result.append(data[i] * -1)
                else:
                    result.append(0)
            for i in range(len(result)):
                if result[i] > 100:
                    result[i] = 100
                elif result[i] < 0:
                    result[i] = 0
            db.save(result)
            return result
    except:
        pass
"""
}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_classify():
    print("\n=== classify_file() ===")
    cases = [
        ("config/db.py", "app"),
        ("infrastructure/main.tf", "iac"),
        ("iam/admin_policy.json", "iam"),
        ("requirements.txt", "deps"),
        ("package.json", "deps"),
        ("cloudformation/template.yaml", "iac"),
    ]
    all_pass = True
    for filepath, expected in cases:
        got = classify_file(filepath)
        status = "✓" if got == expected else "✗"
        if got != expected:
            all_pass = False
        print(f"  {status} {filepath} → {got} (expected {expected})")
    return all_pass


def test_single_chunk(chunk, label):
    print(f"\n=== scan_chunk: {label} ===")
    result = scan_chunk(chunk)
    sec = result.get("security_findings", [])
    debt = result.get("debt_findings", [])
    print(f"  Security findings: {len(sec)}")
    for f in sec:
        print(f"    [{f.get('severity')}] {f.get('type')} — {f.get('explanation', '')[:80]}")
    print(f"  Debt findings: {len(debt)}")
    for f in debt:
        print(f"    [{f.get('severity')}] {f.get('type')} — {f.get('explanation', '')[:80]}")
    return result


def test_full_scan():
    print("\n=== scan_all_chunks: full repo simulation ===")
    all_chunks = [APP_CODE_CHUNK, IAC_CHUNK, IAM_CHUNK, DEPS_CHUNK, DEBT_CHUNK]
    result = scan_all_chunks(all_chunks)
    print(f"  Total security findings: {len(result['security_findings'])}")
    print(f"  Total debt findings:     {len(result['debt_findings'])}")
    print("\n  Full output JSON:")
    print(json.dumps(result, indent=2))
    return result


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("GitHopper — Bedrock Engine Test")
    print("=" * 50)

    # 1. classify_file (no AWS needed)
    classify_ok = test_classify()

    # 2. single chunk tests (needs AWS)
    print("\nRunning single chunk tests (needs AWS credentials)...")
    test_single_chunk(APP_CODE_CHUNK, "App code with secrets + injection")
    test_single_chunk(IAC_CHUNK, "Terraform with open S3 + SG")
    test_single_chunk(IAM_CHUNK, "IAM policy with wildcard")
    test_single_chunk(DEPS_CHUNK, "requirements.txt with old packages")

    # 3. full scan simulation
    test_full_scan()

    print("\n✓ All tests done.")