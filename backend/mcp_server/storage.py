import json
import os
import sqlite3
import threading
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional


def utc_now() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


class MCPMemoryStore:
    """
    Lightweight persistent memory layer for continuous scans.
    Stores only metadata, summaries, and issue history.
    """

    def __init__(self, db_path: Optional[str] = None):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        data_dir = os.path.join(base_dir, "mcp_data")
        os.makedirs(data_dir, exist_ok=True)
        self.db_path = db_path or os.path.join(data_dir, "mcp_memory.db")
        self._lock = threading.Lock()
        self._init_db()

    def _connect(self):
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._lock:
            conn = self._connect()
            try:
                conn.executescript(
                    """
                    CREATE TABLE IF NOT EXISTS scans (
                        scan_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        repo_url TEXT NOT NULL,
                        branch_name TEXT NOT NULL,
                        scan_mode TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        summary_json TEXT NOT NULL,
                        scoring_json TEXT NOT NULL,
                        change_summary_json TEXT NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS snapshots (
                        snapshot_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        branch_name TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        file_count INTEGER NOT NULL,
                        files_json TEXT NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS issues (
                        issue_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        scan_id TEXT NOT NULL,
                        fingerprint TEXT NOT NULL,
                        file_path TEXT NOT NULL,
                        category TEXT NOT NULL,
                        issue_type TEXT NOT NULL,
                        severity TEXT NOT NULL,
                        status TEXT NOT NULL,
                        summary TEXT NOT NULL,
                        first_seen_at TEXT NOT NULL,
                        last_seen_at TEXT NOT NULL,
                        metadata_json TEXT NOT NULL
                    );

                    CREATE UNIQUE INDEX IF NOT EXISTS idx_issues_repo_fingerprint
                    ON issues(repo_id, fingerprint);

                    CREATE TABLE IF NOT EXISTS fixes (
                        fix_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        issue_fingerprint TEXT NOT NULL,
                        status TEXT NOT NULL,
                        validation_status TEXT NOT NULL,
                        explanation TEXT NOT NULL,
                        diff_patch TEXT NOT NULL,
                        remediated_code TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS scan_deltas (
                        delta_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        scan_id TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        new_issues_json TEXT NOT NULL,
                        resolved_issues_json TEXT NOT NULL,
                        persisting_issues_json TEXT NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS command_events (
                        event_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        command_name TEXT NOT NULL,
                        notes TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        metadata_json TEXT NOT NULL
                    );
                    """
                )
                conn.commit()
            finally:
                conn.close()

    def get_latest_snapshot(self, repo_id: str) -> Optional[Dict[str, Any]]:
        conn = self._connect()
        try:
            row = conn.execute(
                """
                SELECT snapshot_id, repo_id, branch_name, created_at, file_count, files_json
                FROM snapshots
                WHERE repo_id = ?
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (repo_id,),
            ).fetchone()
            if not row:
                return None
            return {
                "snapshot_id": row["snapshot_id"],
                "repo_id": row["repo_id"],
                "branch_name": row["branch_name"],
                "created_at": row["created_at"],
                "file_count": row["file_count"],
                "files": json.loads(row["files_json"]),
            }
        finally:
            conn.close()

    def store_snapshot(self, repo_id: str, branch_name: str, files_metadata: List[Dict[str, Any]]) -> Dict[str, Any]:
        snapshot_id = str(uuid.uuid4())
        created_at = utc_now()
        payload = json.dumps(files_metadata)
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    INSERT INTO snapshots (snapshot_id, repo_id, branch_name, created_at, file_count, files_json)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (snapshot_id, repo_id, branch_name, created_at, len(files_metadata), payload),
                )
                conn.commit()
            finally:
                conn.close()
        return {
            "snapshot_id": snapshot_id,
            "repo_id": repo_id,
            "branch_name": branch_name,
            "created_at": created_at,
            "file_count": len(files_metadata),
        }

    def get_unresolved_issues(self, repo_id: str) -> List[Dict[str, Any]]:
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM issues
                WHERE repo_id = ? AND status != 'RESOLVED'
                ORDER BY severity DESC, last_seen_at DESC
                """,
                (repo_id,),
            ).fetchall()
            return [self._row_to_issue(row) for row in rows]
        finally:
            conn.close()

    def get_recent_resolved_issues(self, repo_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM issues
                WHERE repo_id = ? AND status = 'RESOLVED'
                ORDER BY last_seen_at DESC
                LIMIT ?
                """,
                (repo_id, limit),
            ).fetchall()
            return [self._row_to_issue(row) for row in rows]
        finally:
            conn.close()

    def get_context(self, repo_id: str) -> Dict[str, Any]:
        latest_scan = self.get_latest_scan(repo_id)
        unresolved = self.get_unresolved_issues(repo_id)
        recent_resolved = self.get_recent_resolved_issues(repo_id)
        history = self.list_scans(repo_id, limit=10)
        latest_delta = self.get_latest_issue_delta(repo_id)
        recent_commands = self.list_recent_commands(repo_id, limit=10)

        file_history: Dict[str, Dict[str, Any]] = {}
        for issue in unresolved + recent_resolved:
            entry = file_history.setdefault(
                issue["file_path"],
                {"unresolved": [], "resolved": [], "last_seen_at": issue["last_seen_at"]},
            )
            bucket = "resolved" if issue["status"] == "RESOLVED" else "unresolved"
            entry[bucket].append(
                {
                    "issue_type": issue["issue_type"],
                    "severity": issue["severity"],
                    "summary": issue["summary"],
                    "fingerprint": issue["fingerprint"],
                }
            )

        return {
            "repo_id": repo_id,
            "latest_scan": latest_scan,
            "unresolved_issues": unresolved,
            "recent_resolved_issues": recent_resolved,
            "history": history,
            "latest_delta": latest_delta,
            "recent_commands": recent_commands,
            "file_history": file_history,
        }

    def get_latest_scan(self, repo_id: str) -> Optional[Dict[str, Any]]:
        scans = self.list_scans(repo_id, limit=1)
        return scans[0] if scans else None

    def list_scans(self, repo_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM scans
                WHERE repo_id = ?
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (repo_id, limit),
            ).fetchall()
            return [
                {
                    "scan_id": row["scan_id"],
                    "repo_id": row["repo_id"],
                    "repo_url": row["repo_url"],
                    "branch_name": row["branch_name"],
                    "scan_mode": row["scan_mode"],
                    "created_at": row["created_at"],
                    "summary": json.loads(row["summary_json"]),
                    "scoring": json.loads(row["scoring_json"]),
                    "change_summary": json.loads(row["change_summary_json"]),
                }
                for row in rows
            ]
        finally:
            conn.close()

    def store_scan_results(
        self,
        repo_id: str,
        repo_url: str,
        branch_name: str,
        scan_mode: str,
        issues: List[Dict[str, Any]],
        summary: Dict[str, Any],
        scoring: Dict[str, Any],
        change_summary: Dict[str, Any],
    ) -> Dict[str, Any]:
        scan_id = str(uuid.uuid4())
        created_at = utc_now()
        current_fingerprints = {issue["fingerprint"] for issue in issues}

        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    INSERT INTO scans (scan_id, repo_id, repo_url, branch_name, scan_mode, created_at,
                                       summary_json, scoring_json, change_summary_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        scan_id,
                        repo_id,
                        repo_url,
                        branch_name,
                        scan_mode,
                        created_at,
                        json.dumps(summary),
                        json.dumps(scoring),
                        json.dumps(change_summary),
                    ),
                )

                existing_rows = conn.execute(
                    "SELECT * FROM issues WHERE repo_id = ?",
                    (repo_id,),
                ).fetchall()

                existing = {row["fingerprint"]: row for row in existing_rows}
                new_count = 0
                persisting_count = 0
                resolved_count = 0
                new_issue_items: List[Dict[str, Any]] = []
                persisting_issue_items: List[Dict[str, Any]] = []
                resolved_issue_items: List[Dict[str, Any]] = []

                for issue in issues:
                    row = existing.get(issue["fingerprint"])
                    metadata_json = json.dumps(issue.get("metadata", {}))
                    if row:
                        persisting_count += 1
                        persisting_issue_items.append(self._issue_delta_item(issue))
                        conn.execute(
                            """
                            UPDATE issues
                            SET scan_id = ?, severity = ?, status = ?, summary = ?, last_seen_at = ?, metadata_json = ?
                            WHERE repo_id = ? AND fingerprint = ?
                            """,
                            (
                                scan_id,
                                issue["severity"],
                                issue["status"],
                                issue["summary"],
                                created_at,
                                metadata_json,
                                repo_id,
                                issue["fingerprint"],
                            ),
                        )
                    else:
                        new_count += 1
                        new_issue_items.append(self._issue_delta_item(issue))
                        conn.execute(
                            """
                            INSERT INTO issues (issue_id, repo_id, scan_id, fingerprint, file_path, category,
                                                issue_type, severity, status, summary, first_seen_at, last_seen_at, metadata_json)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                str(uuid.uuid4()),
                                repo_id,
                                scan_id,
                                issue["fingerprint"],
                                issue["file_path"],
                                issue["category"],
                                issue["issue_type"],
                                issue["severity"],
                                issue["status"],
                                issue["summary"],
                                created_at,
                                created_at,
                                metadata_json,
                            ),
                        )

                unresolved_existing = [
                    row for row in existing_rows
                    if row["status"] != "RESOLVED" and row["fingerprint"] not in current_fingerprints
                ]
                for row in unresolved_existing:
                    resolved_count += 1
                    resolved_issue_items.append(
                        {
                            "fingerprint": row["fingerprint"],
                            "file_path": row["file_path"],
                            "issue_type": row["issue_type"],
                            "severity": row["severity"],
                            "summary": row["summary"],
                        }
                    )
                    conn.execute(
                        """
                        UPDATE issues
                        SET status = 'RESOLVED', last_seen_at = ?
                        WHERE repo_id = ? AND fingerprint = ?
                        """,
                        (created_at, repo_id, row["fingerprint"]),
                    )

                conn.execute(
                    """
                    INSERT INTO scan_deltas (delta_id, repo_id, scan_id, created_at, new_issues_json, resolved_issues_json, persisting_issues_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        str(uuid.uuid4()),
                        repo_id,
                        scan_id,
                        created_at,
                        json.dumps(new_issue_items),
                        json.dumps(resolved_issue_items),
                        json.dumps(persisting_issue_items),
                    ),
                )

                conn.commit()
            finally:
                conn.close()

        return {
            "scan_id": scan_id,
            "created_at": created_at,
            "new_issues": new_count,
            "resolved_issues": resolved_count,
            "persisting_issues": persisting_count,
        }

    def get_latest_issue_delta(self, repo_id: str) -> Dict[str, Any]:
        conn = self._connect()
        try:
            row = conn.execute(
                """
                SELECT * FROM scan_deltas
                WHERE repo_id = ?
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (repo_id,),
            ).fetchone()
            if not row:
                return {
                    "repo_id": repo_id,
                    "new_issues": [],
                    "resolved_issues": [],
                    "persisting_issues": [],
                }
            return {
                "repo_id": repo_id,
                "scan_id": row["scan_id"],
                "created_at": row["created_at"],
                "new_issues": json.loads(row["new_issues_json"]),
                "resolved_issues": json.loads(row["resolved_issues_json"]),
                "persisting_issues": json.loads(row["persisting_issues_json"]),
            }
        finally:
            conn.close()

    def record_command_event(
        self,
        repo_id: str,
        command_name: str,
        notes: str = "",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        event_id = str(uuid.uuid4())
        created_at = utc_now()
        payload = json.dumps(metadata or {})
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    INSERT INTO command_events (event_id, repo_id, command_name, notes, created_at, metadata_json)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (event_id, repo_id, command_name, notes, created_at, payload),
                )
                conn.commit()
            finally:
                conn.close()
        return {
            "event_id": event_id,
            "repo_id": repo_id,
            "command_name": command_name,
            "notes": notes,
            "created_at": created_at,
            "metadata": metadata or {},
        }

    def list_recent_commands(self, repo_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM command_events
                WHERE repo_id = ?
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (repo_id, limit),
            ).fetchall()
            return [
                {
                    "event_id": row["event_id"],
                    "repo_id": row["repo_id"],
                    "command_name": row["command_name"],
                    "notes": row["notes"],
                    "created_at": row["created_at"],
                    "metadata": json.loads(row["metadata_json"]),
                }
                for row in rows
            ]
        finally:
            conn.close()

    def update_fix_status(
        self,
        repo_id: str,
        issue_fingerprint: str,
        status: str,
        validation_status: str,
        explanation: str = "",
        diff_patch: str = "",
        remediated_code: str = "",
    ) -> Dict[str, Any]:
        now = utc_now()
        with self._lock:
            conn = self._connect()
            try:
                row = conn.execute(
                    """
                    SELECT fix_id FROM fixes
                    WHERE repo_id = ? AND issue_fingerprint = ?
                    """,
                    (repo_id, issue_fingerprint),
                ).fetchone()
                if row:
                    fix_id = row["fix_id"]
                    conn.execute(
                        """
                        UPDATE fixes
                        SET status = ?, validation_status = ?, explanation = ?, diff_patch = ?,
                            remediated_code = ?, updated_at = ?
                        WHERE fix_id = ?
                        """,
                        (status, validation_status, explanation, diff_patch, remediated_code, now, fix_id),
                    )
                else:
                    fix_id = str(uuid.uuid4())
                    conn.execute(
                        """
                        INSERT INTO fixes (fix_id, repo_id, issue_fingerprint, status, validation_status,
                                           explanation, diff_patch, remediated_code, created_at, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            fix_id,
                            repo_id,
                            issue_fingerprint,
                            status,
                            validation_status,
                            explanation,
                            diff_patch,
                            remediated_code,
                            now,
                            now,
                        ),
                    )
                conn.commit()
            finally:
                conn.close()

        return {
            "fix_id": fix_id,
            "repo_id": repo_id,
            "issue_fingerprint": issue_fingerprint,
            "status": status,
            "validation_status": validation_status,
            "updated_at": now,
        }

    def _row_to_issue(self, row: sqlite3.Row) -> Dict[str, Any]:
        return {
            "issue_id": row["issue_id"],
            "repo_id": row["repo_id"],
            "scan_id": row["scan_id"],
            "fingerprint": row["fingerprint"],
            "file_path": row["file_path"],
            "category": row["category"],
            "issue_type": row["issue_type"],
            "severity": row["severity"],
            "status": row["status"],
            "summary": row["summary"],
            "first_seen_at": row["first_seen_at"],
            "last_seen_at": row["last_seen_at"],
            "metadata": json.loads(row["metadata_json"]),
        }

    def _issue_delta_item(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "fingerprint": issue["fingerprint"],
            "file_path": issue["file_path"],
            "issue_type": issue["issue_type"],
            "severity": issue["severity"],
            "summary": issue["summary"],
        }
