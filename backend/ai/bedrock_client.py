"""Compatibility shim for older imports.

This module now delegates to OpenClaw-backed logic in openclaw_client.
"""

try:
    from . import openclaw_client as _openclaw
except ImportError:
    import openclaw_client as _openclaw

classify_file = _openclaw.classify_file
generate_security_prompt = _openclaw.generate_security_prompt
invoke_bedrock = _openclaw.invoke_openclaw
invoke_openclaw = _openclaw.invoke_openclaw
scan_chunk = _openclaw.scan_chunk
scan_all_chunks = _openclaw.scan_all_chunks
reset_cost_tracker = _openclaw.reset_cost_tracker
cost_tracker = _openclaw.cost_tracker
_debt_signal_to_vulnerability = _openclaw._debt_signal_to_vulnerability

__all__ = [
    "classify_file",
    "generate_security_prompt",
    "invoke_bedrock",
    "invoke_openclaw",
    "scan_chunk",
    "scan_all_chunks",
    "reset_cost_tracker",
    "cost_tracker",
    "_debt_signal_to_vulnerability",
]
