import threading
import uuid
from typing import Any, Dict

from github_client import get_latest_commit_sha

from .continuous_pipeline import ContinuousIntelligencePipeline


class ContinuousWatchManager:
    def __init__(self, pipeline: ContinuousIntelligencePipeline = None):
        self.pipeline = pipeline or ContinuousIntelligencePipeline()
        self._watches: Dict[str, Dict[str, Any]] = {}
        self._lock = threading.Lock()

    def start(self, repo_url: str, branch_name: str = "main", interval_seconds: int = 60, github_token: str = None) -> Dict[str, Any]:
        watch_id = str(uuid.uuid4())
        state = {
            "watch_id": watch_id,
            "repo_url": repo_url,
            "branch_name": branch_name,
            "interval_seconds": max(10, interval_seconds),
            "github_token": github_token,
            "status": "running",
            "poll_count": 0,
            "run_count": 0,
            "change_detected_count": 0,
            "last_result": None,
            "last_error": None,
            "last_seen_commit": None,
            "last_scanned_commit": None,
            "stop_event": threading.Event(),
        }

        def _runner():
            first_poll = True
            while not state["stop_event"].is_set():
                try:
                    state["poll_count"] += 1
                    commit_info = get_latest_commit_sha(
                        repo_url,
                        github_token=github_token,
                        branch_name=branch_name,
                    )
                    latest_commit   = commit_info.get("commit_sha")
                    resolved_branch = commit_info.get("branch_name", branch_name)
                    state["branch_name"]       = resolved_branch
                    state["last_seen_commit"]  = latest_commit

                    if first_poll:
                        # On the very first poll, seed last_scanned_commit so we
                        # only scan FUTURE commits, not the current HEAD on startup.
                        state["last_scanned_commit"] = latest_commit
                        state["status"] = "running"
                        first_poll = False
                    elif state["last_scanned_commit"] != latest_commit:
                        # New commit detected — run incremental scan
                        state["status"] = "scanning"
                        result = self.pipeline.run(
                            repo_url=repo_url,
                            github_token=github_token,
                            branch_name=resolved_branch,
                            generate_fixes=True,
                        )
                        state["last_result"]          = result
                        state["run_count"]            += 1
                        state["change_detected_count"] += 1
                        state["last_scanned_commit"]  = latest_commit
                        state["status"] = "running"
                    else:
                        state["status"] = "idle"

                    state["last_error"] = None
                except Exception as exc:
                    state["last_error"] = str(exc)
                    state["status"]     = "error"

                state["stop_event"].wait(state["interval_seconds"])

            state["status"] = "stopped"


        thread = threading.Thread(target=_runner, daemon=True)
        state["thread"] = thread

        with self._lock:
            self._watches[watch_id] = state
        thread.start()

        return {
            "watch_id": watch_id,
            "status": "running",
            "interval_seconds": state["interval_seconds"],
        }

    def status(self, watch_id: str) -> Dict[str, Any]:
        with self._lock:
            state = self._watches.get(watch_id)
        if not state:
            return {"error": "watch_not_found"}
        return {
            "watch_id": watch_id,
            "status": state["status"],
            "poll_count": state["poll_count"],
            "run_count": state["run_count"],
            "change_detected_count": state["change_detected_count"],
            "last_error": state["last_error"],
            "last_seen_commit": state["last_seen_commit"],
            "last_scanned_commit": state["last_scanned_commit"],
            "last_result": state["last_result"],
        }

    def stop(self, watch_id: str) -> Dict[str, Any]:
        with self._lock:
            state = self._watches.get(watch_id)
        if not state:
            return {"error": "watch_not_found"}
        state["stop_event"].set()
        return {
            "watch_id": watch_id,
            "status": "stopping",
        }

    def force_scan(self, watch_id: str) -> Dict[str, Any]:
        """Immediately run a scan for the given watch, ignoring the interval."""
        with self._lock:
            state = self._watches.get(watch_id)
        if not state:
            return {"error": "watch_not_found"}
        if state["status"] == "scanning":
            return {"error": "scan_already_in_progress"}

        def _run():
            try:
                state["status"] = "scanning"
                commit_info = get_latest_commit_sha(
                    state["repo_url"],
                    github_token=state["github_token"],
                    branch_name=state["branch_name"],
                )
                latest_commit   = commit_info.get("commit_sha")
                resolved_branch = commit_info.get("branch_name", state["branch_name"])
                state["last_seen_commit"] = latest_commit

                result = self.pipeline.run(
                    repo_url=state["repo_url"],
                    github_token=state["github_token"],
                    branch_name=resolved_branch,
                    generate_fixes=True,
                )
                state["last_result"]           = result
                state["run_count"]            += 1
                state["change_detected_count"] += 1
                state["last_scanned_commit"]   = latest_commit
                state["last_error"]            = None
                state["status"]                = "running"
            except Exception as exc:
                state["last_error"] = str(exc)
                state["status"]     = "error"

        threading.Thread(target=_run, daemon=True).start()
        return {"watch_id": watch_id, "status": "scan_triggered"}
