import json
import os
from datetime import datetime
from typing import Dict, Tuple

import requests

LOG_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(LOG_DIR, "discord.log")


def _get_mode(requested_mode: str | None) -> str:
    mode = (requested_mode or os.environ.get("DISCORD_MODE", "mock")).strip().lower()
    return "live" if mode == "live" else "mock"


def _get_webhook_url(override_url: str | None) -> str:
    return (override_url or os.environ.get("DISCORD_WEBHOOK_URL", "")).strip()


def _format_message(message: str, report_url: str) -> str:
    parts = []
    if message:
        parts.append(message.strip())
    if report_url:
        parts.append(f"Report: {report_url.strip()}")
    return "\n".join(parts).strip()


def _append_log(entry: Dict) -> None:
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry) + "\n")


def send_discord_notification(
    message: str,
    report_url: str = "",
    mode: str | None = None,
    webhook_url: str | None = None,
    username: str = "OpenClaw",
) -> Tuple[Dict, int]:
    payload_message = _format_message(message, report_url)
    if not payload_message:
        return {"error": "message or report_url is required"}, 400

    selected_mode = _get_mode(mode)
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "mode": selected_mode,
        "message": payload_message,
        "report_url": report_url,
    }

    if selected_mode == "mock":
        _append_log({**entry, "status": "mocked"})
        return {
            "status": "mocked",
            "delivered": False,
            "mode": "mock",
            "message": payload_message,
            "log_path": LOG_PATH,
        }, 200

    webhook = _get_webhook_url(webhook_url)
    if not webhook:
        return {"error": "DISCORD_WEBHOOK_URL is not set"}, 400

    response = requests.post(
        webhook,
        json={"content": payload_message, "username": username},
        timeout=20,
    )

    status_ok = 200 <= response.status_code < 300
    _append_log({
        **entry,
        "status": "sent" if status_ok else "failed",
        "status_code": response.status_code,
    })

    if not status_ok:
        return {
            "status": "failed",
            "delivered": False,
            "mode": "live",
            "status_code": response.status_code,
            "error": response.text[:500],
        }, 502

    return {
        "status": "sent",
        "delivered": True,
        "mode": "live",
    }, 200
