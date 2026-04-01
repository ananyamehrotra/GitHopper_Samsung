from typing import Dict

from ai.bedrock_client import classify_file, generate_security_prompt

from .context import render_context_block


def select_prompt_profile(chunk: Dict, file_path: str) -> str:
    filename = file_path or chunk.get("file", "unknown")
    file_type = classify_file(filename)
    if file_type == "deps":
        return "dependency_vulnerability"
    if file_type in {"iam", "iac"}:
        return "config_security"
    return "application_security_and_debt"


def build_contextual_prompt(chunk: Dict, repo_context: Dict, branch_name: str) -> str:
    file_path = chunk.get("file", "unknown")
    file_type = classify_file(file_path)
    base_prompt = generate_security_prompt(file_path, chunk.get("code", ""), file_type, branch_name)
    context_block = render_context_block(file_path, repo_context)
    chunk_note = chunk.get("context_note", "")
    profile = select_prompt_profile(chunk, file_path)

    return (
        f"You are operating in optimized profile: {profile}.\n"
        "Return strict JSON only. Do not include markdown fences.\n\n"
        f"{context_block}\n\n"
        f"CHUNK CONTEXT\n{chunk_note}\n\n"
        f"{base_prompt}"
    )

