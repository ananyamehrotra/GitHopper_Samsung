from typing import Any, Dict, List

from ai.bedrock_client import _debt_signal_to_vulnerability, classify_file, invoke_bedrock

from .prompting import build_contextual_prompt


def normalize_vulnerability(vulnerability: Dict[str, Any], chunk: Dict[str, Any]) -> Dict[str, Any]:
    return {
        **vulnerability,
        "file": chunk.get("file", "unknown"),
        "category": "security",
        "line_range": vulnerability.get("line_range") or f"{chunk.get('start_line', '?')}-{chunk.get('end_line', '?')}",
    }


def scan_chunk_with_context(chunk: Dict[str, Any], repo_context: Dict[str, Any], branch_name: str = "main") -> Dict[str, Any]:
    prompt = build_contextual_prompt(chunk, repo_context, branch_name)
    result = invoke_bedrock(prompt, chunk.get("file", "unknown"))
    vulnerabilities = [
        normalize_vulnerability(vulnerability, chunk)
        for vulnerability in result.get("vulnerabilities", [])
    ]

    if not vulnerabilities and chunk.get("debt_signals"):
        vulnerabilities = [
            normalize_vulnerability(_debt_signal_to_vulnerability(signal, chunk.get("file", "unknown")), chunk)
            for signal in chunk.get("debt_signals", [])
        ]

    return {
        "file": chunk.get("file", "unknown"),
        "file_type": classify_file(chunk.get("file", "unknown")),
        "vulnerabilities": vulnerabilities,
        "has_issues": bool(vulnerabilities),
        "vulnerability_count": len(vulnerabilities),
    }


def scan_all_chunks_with_context(chunks: List[Dict[str, Any]], repo_context: Dict[str, Any], branch_name: str = "main") -> Dict[str, Any]:
    all_vulnerabilities: List[Dict[str, Any]] = []
    vulnerable_files: List[Dict[str, Any]] = []

    for chunk in chunks:
        result = scan_chunk_with_context(chunk, repo_context, branch_name)
        if result["has_issues"]:
            vulnerable_files.append(
                {
                    "file": result["file"],
                    "type": result["file_type"],
                    "count": result["vulnerability_count"],
                }
            )
            all_vulnerabilities.extend(result["vulnerabilities"])

    return {
        "vulnerabilities": all_vulnerabilities,
        "vulnerable_files": vulnerable_files,
        "total_files_analyzed": len(chunks),
        "files_with_issues": len(vulnerable_files),
        "total_vulnerabilities": len(all_vulnerabilities),
        "context_applied": True,
    }


def build_debt_findings_from_files(files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    for file in files:
        for signal in file.get("debt_signals", []):
            findings.append(
                {
                    "type": "DEBT_SIGNAL",
                    "severity": "MEDIUM" if file.get("debt_signal_count", 0) > 2 else "LOW",
                    "file": file["path"],
                    "line_range": str(signal.get("line_number", "?")),
                    "summary": signal.get("line_snippet", "Technical debt signal"),
                    "estimated_minutes": 10,
                    "estimated_minutes_to_fix": 10,
                    "metadata": {
                        "pattern": signal.get("pattern"),
                        "line_snippet": signal.get("line_snippet"),
                        "category_hint": file.get("debt_category_hint", "code_quality"),
                    },
                }
            )

        for long_fn in file.get("metrics", {}).get("long_functions_detected", []):
            findings.append(
                {
                    "type": "LONG_FUNCTION",
                    "severity": "MEDIUM",
                    "file": file["path"],
                    "line_range": str(long_fn.get("approximate_start_line", "?")),
                    "summary": long_fn.get("first_line", "Large function detected"),
                    "estimated_minutes": 20,
                    "estimated_minutes_to_fix": 20,
                    "metadata": {
                        "approximate_length_lines": long_fn.get("approximate_length_lines", 0),
                        "category_hint": file.get("debt_category_hint", "code_quality"),
                    },
                }
            )

    return findings

