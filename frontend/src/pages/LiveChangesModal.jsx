import React, { useEffect, useRef, useState } from "react";

/* ─── helpers ─────────────────────────────────────────────────────────────── */
const fmt = (v, fallback = "—") => (v == null || v === "" ? fallback : String(v));
const badge = (sev) => {
    const map = { CRITICAL: "#ff4757", HIGH: "#ff9800", MEDIUM: "#ffb74d", LOW: "#4caf50" };
    return map[sev] || "#90caf9";
};
const ts = () => new Date().toLocaleTimeString("en-US", { hour12: false });

/* ─── Pulsing live dot ───────────────────────────────────────────────────── */
function LiveDot({ active, pending }) {
    const color = pending ? "#ffb74d" : active ? "#72ea1e" : "#555";
    const label = pending ? "SCANNING" : active ? "LIVE" : "IDLE";
    return (
        <span style={{ display: "inline-flex", alignItems: "center", gap: "6px" }}>
            <span style={{
                display: "inline-block", width: 10, height: 10, borderRadius: "50%",
                background: color, boxShadow: active || pending ? `0 0 8px ${color}` : "none",
                animation: active || pending ? "livePulse 1.2s ease-in-out infinite" : "none",
            }} />
            <span style={{ fontSize: 11, fontWeight: 700, letterSpacing: "0.12em", color }}>
                {label}
            </span>
        </span>
    );
}

/* ─── Stat card ──────────────────────────────────────────────────────────── */
function StatCard({ label, value, color = "#d9ffb8" }) {
    return (
        <div style={{
            background: "rgba(0,0,0,0.6)", border: `1px solid ${color}44`,
            borderRadius: 8, padding: "12px 16px", minWidth: 110,
        }}>
            <div style={{ color: "#a1d96a", fontSize: 10, letterSpacing: "0.12em", marginBottom: 5 }}>{label}</div>
            <div style={{ color, fontSize: 20, fontWeight: 700 }}>{value}</div>
        </div>
    );
}

/* ─── Issue row ──────────────────────────────────────────────────────────── */
function IssueRow({ item, kind }) {
    const [open, setOpen] = useState(false);
    const cfg = {
        new:        { label: "NEW",     color: "#ff6b6b", bg: "rgba(255,107,107,0.07)" },
        resolved:   { label: "FIXED",   color: "#4caf50", bg: "rgba(76,175,80,0.07)"  },
        persisting: { label: "PERSIST", color: "#ffb74d", bg: "rgba(255,152,0,0.07)"  },
    }[kind] || { label: kind, color: "#90caf9", bg: "rgba(144,202,249,0.07)" };

    const sev = item.severity || item.rule_id || "";
    return (
        <div onClick={() => setOpen(p => !p)} style={{
            background: cfg.bg, border: `1px solid ${cfg.color}33`,
            borderRadius: 6, padding: "10px 14px", cursor: "pointer",
        }}>
            <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
                <span style={{ padding: "2px 7px", borderRadius: 999, background: cfg.color, color: "#000", fontSize: 10, fontWeight: 700, flexShrink: 0 }}>
                    {cfg.label}
                </span>
                {sev && (
                    <span style={{ padding: "2px 7px", borderRadius: 999, background: badge(sev), color: "#000", fontSize: 10, fontWeight: 700, flexShrink: 0 }}>
                        {sev}
                    </span>
                )}
                <span style={{ color: "#d9ffb8", fontSize: 12, fontFamily: "monospace", wordBreak: "break-all", flex: 1 }}>
                    {item.file || item.check_id || item.fingerprint?.slice(0, 16) || "—"}
                </span>
                <span style={{ color: "#555", fontSize: 10, flexShrink: 0 }}>{open ? "▲" : "▼"}</span>
            </div>
            {open && (
                <div style={{ marginTop: 10, paddingTop: 10, borderTop: "1px solid #222" }}>
                    {item.message    && <p style={{ color: "#d2ddb8", fontSize: 12, margin: "0 0 6px" }}>{item.message}</p>}
                    {item.explanation && <p style={{ color: "#a1d96a", fontSize: 12, margin: "0 0 6px" }}>{item.explanation}</p>}
                    {item.remediation && (
                        <p style={{ color: "#90caf9", fontSize: 11, fontFamily: "monospace", whiteSpace: "pre-wrap", margin: 0 }}>
                            {item.remediation}
                        </p>
                    )}
                    {item.fingerprint && (
                        <p style={{ color: "#555", fontSize: 10, fontFamily: "monospace", margin: "8px 0 0" }}>
                            fp: {item.fingerprint}
                        </p>
                    )}
                </div>
            )}
        </div>
    );
}

/* ─── Commit event card ──────────────────────────────────────────────────── */
function CommitEvent({ event, index }) {
    const [open, setOpen] = useState(index === 0);
    const ci   = event.continuous_intelligence || {};
    const data = event.data || {};
    const newI      = ci.new_issues       ?? 0;
    const resolved  = ci.resolved_issues  ?? 0;
    const persisting = ci.persisting_issues ?? 0;

    return (
        <div style={{ border: "1px solid #72ea1e33", borderRadius: 10, marginBottom: 12, overflow: "hidden" }}>
            {/* header row */}
            <div onClick={() => setOpen(p => !p)} style={{
                display: "flex", alignItems: "center", gap: 12,
                padding: "12px 16px", background: "rgba(114,234,30,0.06)",
                cursor: "pointer", flexWrap: "wrap",
            }}>
                <span style={{ color: "#72ea1e", fontFamily: "monospace", fontSize: 12 }}>
                    #{event.commit?.slice(0, 8) || "—"}
                </span>
                <span style={{ color: "#a1d96a", fontSize: 11, flex: 1 }}>{event.scannedAt}</span>
                <span style={{ color: "#ff6b6b", fontWeight: 700, fontSize: 12, background: "rgba(255,107,107,0.12)", padding: "2px 8px", borderRadius: 999 }}>
                    +{newI} new
                </span>
                <span style={{ color: "#4caf50", fontWeight: 700, fontSize: 12, background: "rgba(76,175,80,0.12)", padding: "2px 8px", borderRadius: 999 }}>
                    -{resolved} fixed
                </span>
                <span style={{ color: "#ffb74d", fontWeight: 700, fontSize: 12, background: "rgba(255,152,0,0.12)", padding: "2px 8px", borderRadius: 999 }}>
                    {persisting} persist
                </span>
                <span style={{ color: "#555", fontSize: 10 }}>{open ? "▲" : "▼"}</span>
            </div>

            {open && (
                <div style={{ padding: "14px 16px" }}>
                    {/* mini-stats */}
                    <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginBottom: 14 }}>
                        <StatCard label="HEALTH SCORE" value={fmt(event.summary?.health_score)} color="#72ea1e" />
                        <StatCard label="SCORE DELTA"  value={ci.trend?.delta == null ? "N/A" : `${ci.trend.delta > 0 ? "+" : ""}${ci.trend.delta}`} color="#90caf9" />
                        <StatCard label="SCAN MODE"    value={fmt(ci.scan_mode, "full").toUpperCase()} color="#a1d96a" />
                        <StatCard label="FIX TIME"     value={`${ci.estimated_fix_minutes ?? 0}m`} color="#64b5f6" />
                    </div>

                    {/* new issues */}
                    {(ci.new_issue_details || []).length > 0 && (
                        <div style={{ marginBottom: 12 }}>
                            <div style={{ color: "#ff6b6b", fontSize: 11, fontWeight: 700, letterSpacing: "0.1em", marginBottom: 6 }}>
                                NEW ISSUES ({ci.new_issue_details.length})
                            </div>
                            <div style={{ display: "grid", gap: 6 }}>
                                {ci.new_issue_details.map((it, i) => <IssueRow key={i} item={it} kind="new" />)}
                            </div>
                        </div>
                    )}

                    {/* resolved */}
                    {(ci.resolved_issue_details || []).length > 0 && (
                        <div style={{ marginBottom: 12 }}>
                            <div style={{ color: "#4caf50", fontSize: 11, fontWeight: 700, letterSpacing: "0.1em", marginBottom: 6 }}>
                                RESOLVED ({ci.resolved_issue_details.length})
                            </div>
                            <div style={{ display: "grid", gap: 6 }}>
                                {ci.resolved_issue_details.map((it, i) => <IssueRow key={i} item={it} kind="resolved" />)}
                            </div>
                        </div>
                    )}

                    {/* security findings */}
                    {(data.security_findings || []).length > 0 && (
                        <div style={{ marginBottom: 12 }}>
                            <div style={{ color: "#ffb74d", fontSize: 11, fontWeight: 700, letterSpacing: "0.1em", marginBottom: 6 }}>
                                SECURITY FINDINGS ({data.security_findings.length})
                            </div>
                            <div style={{ display: "grid", gap: 6 }}>
                                {data.security_findings.slice(0, 6).map((it, i) => <IssueRow key={i} item={it} kind="persisting" />)}
                            </div>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}

/* ─── MAIN MODAL ─────────────────────────────────────────────────────────── */
export function LiveChangesModal({ repoUrl, branchName, onClose }) {
    // ── state ──
    const [phase,      setPhase]      = useState("starting"); // starting | watching | stopped | error
    const [watchId,    setWatchId]    = useState(null);
    const [status,     setStatus]     = useState(null);
    const [events,     setEvents]     = useState([]);
    const [err,        setErr]        = useState("");
    const [log,        setLog]        = useState([]);
    const [pending,    setPending]    = useState(false); // new commit seen — scan in progress

    // ── refs (never stale in callbacks) ──
    const watchIdRef      = useRef(null);
    const phaseRef        = useRef("starting");
    const lastScannedRef  = useRef(null);   // ← KEY FIX: no stale closure
    const lastSeenRef     = useRef(null);
    const intervalRef     = useRef(null);
    const eventsEndRef    = useRef(null);
    const logEndRef       = useRef(null);

    // keep phase ref up to date
    useEffect(() => { phaseRef.current = phase; }, [phase]);

    // auto-scroll
    useEffect(() => { eventsEndRef.current?.scrollIntoView({ behavior: "smooth" }); }, [events]);
    useEffect(() => { logEndRef.current?.scrollIntoView({ behavior: "smooth" }); }, [log]);

    const addLog = (msg) => setLog(prev => [...prev.slice(-150), `[${ts()}] ${msg}`]);

    /* ── poll — all comparisons done via refs, never stale ── */
    const doPoll = async () => {
        const wid = watchIdRef.current;
        if (!wid || phaseRef.current === "stopped") return;
        try {
            const r = await fetch(`http://localhost:5000/api/continuous/status/${wid}`);
            const d = await r.json();
            if (!r.ok) throw new Error(d.error || "Status fetch failed");
            setStatus(d);

            const seenSHA    = d.last_seen_commit;
            const scannedSHA = d.last_scanned_commit;

            // Detect new commit seen by backend (not yet scanned) → show "SCANNING" badge
            if (seenSHA && seenSHA !== lastSeenRef.current) {
                lastSeenRef.current = seenSHA;
                addLog(`📡 New commit detected: ${seenSHA.slice(0, 12)} — waiting for scan...`);
                setPending(true);
            }

            // Detect completed scan of a new commit
            if (scannedSHA && scannedSHA !== lastScannedRef.current) {
                lastScannedRef.current = scannedSHA;
                setPending(false);
                if (d.last_result) {
                    const ci = d.last_result.continuous_intelligence || {};
                    addLog(`✅ Scan complete for ${scannedSHA.slice(0, 12)}`);
                    addLog(`   ↳ +${ci.new_issues ?? 0} new  -${ci.resolved_issues ?? 0} fixed  ${ci.persisting_issues ?? 0} persist`);
                    setEvents(prev => [{
                        ...d.last_result,
                        commit: scannedSHA,
                        scannedAt: ts(),
                    }, ...prev]);
                }
            }

            // Clear error if poll succeeded
            setErr("");
        } catch (e) {
            addLog(`⚠️  Poll error: ${e.message}`);
            setErr(e.message);
        }
    };

    /* ── start watch + kick off single interval ── */
    useEffect(() => {
        const start = async () => {
            addLog(`🚀 Starting continuous watch for ${repoUrl} @ ${branchName || "main"}`);
            try {
                const r = await fetch("http://localhost:5000/api/continuous/start", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        repo_url:         repoUrl,
                        branch_name:      branchName || "main",
                        interval_seconds: 15,   // backend polls GitHub every 15s
                    }),
                });
                const d = await r.json();
                if (!r.ok) throw new Error(d.error || "Failed to start watch");

                watchIdRef.current = d.watch_id;
                setWatchId(d.watch_id);
                setPhase("watching");
                addLog(`✅ Watch started — id: ${d.watch_id}`);
                addLog(`   Backend will poll GitHub every 15 s and scan on new commits.`);

                // first poll immediately, then every 3 seconds
                doPoll();
                intervalRef.current = window.setInterval(doPoll, 3000);
            } catch (e) {
                setPhase("error");
                setErr(e.message);
                addLog(`❌ Start failed: ${e.message}`);
            }
        };

        start();

        return () => {
            if (intervalRef.current) window.clearInterval(intervalRef.current);
        };
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []); // intentionally empty — start once, use refs inside doPoll

    /* ── force scan now ── */
    const handleForceScan = async () => {
        const wid = watchIdRef.current;
        if (!wid) return;
        addLog("⚡ Forcing immediate scan…");
        try {
            const r = await fetch(`http://localhost:5000/api/continuous/force-scan/${wid}`, { method: "POST" });
            const d = await r.json();
            if (r.status === 409) { addLog("⚠️  Scan already in progress — please wait."); return; }
            if (!r.ok) throw new Error(d.error || "Force scan failed");
            addLog("✅ Force scan triggered — check feed in a moment.");
            setPending(true);
        } catch (e) {
            addLog(`❌ Force scan error: ${e.message}`);
        }
    };

    /* ── stop watch ── */
    const handleStop = async () => {
        if (intervalRef.current) window.clearInterval(intervalRef.current);
        phaseRef.current = "stopped";
        setPhase("stopped");
        setPending(false);
        addLog("⏹ Stopping watch...");
        if (!watchIdRef.current) return;
        try {
            await fetch(`http://localhost:5000/api/continuous/stop/${watchIdRef.current}`, { method: "POST" });
            addLog("✅ Watch stopped.");
        } catch (e) {
            addLog(`⚠️  Stop error: ${e.message}`);
        }
    };

    const isLive = phase === "watching";

    return (
        <>
            <style>{`
                @keyframes livePulse   { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.5;transform:scale(1.35)} }
                @keyframes modalFadeIn { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
                @keyframes scanLine    { 0%{top:0} 100%{top:100%} }
                @keyframes spin        { to{transform:rotate(360deg)} }
                .lcm-sb::-webkit-scrollbar       { width:4px }
                .lcm-sb::-webkit-scrollbar-track { background:#111 }
                .lcm-sb::-webkit-scrollbar-thumb { background:#72ea1e44; border-radius:2px }
            `}</style>

            {/* backdrop */}
            <div
                onClick={e => { if (e.target === e.currentTarget) { if (isLive) handleStop().then(onClose); else onClose(); } }}
                style={{ position:"fixed", inset:0, zIndex:9999, background:"rgba(0,0,0,0.87)", backdropFilter:"blur(6px)", display:"flex", alignItems:"center", justifyContent:"center" }}
            >
                {/* modal box */}
                <div style={{
                    position:"relative", width:"min(1060px,96vw)", maxHeight:"92vh",
                    background:"linear-gradient(135deg,#0a0f0a 0%,#081208 100%)",
                    border:"1px solid #72ea1e55", borderRadius:14, overflow:"hidden",
                    display:"flex", flexDirection:"column",
                    animation:"modalFadeIn 0.25s ease", boxShadow:"0 0 60px rgba(114,234,30,0.12)",
                }}>
                    {/* scan-line sweep */}
                    {isLive && (
                        <div style={{
                            position:"absolute", left:0, right:0, height:2,
                            background:"linear-gradient(90deg,transparent,#72ea1e66,transparent)",
                            animation:"scanLine 3s linear infinite", pointerEvents:"none", zIndex:10,
                        }} />
                    )}

                    {/* ── header ── */}
                    <div style={{ padding:"18px 24px", borderBottom:"1px solid #72ea1e22", display:"flex", alignItems:"center", gap:16, flexWrap:"wrap", background:"rgba(114,234,30,0.04)" }}>
                        <LiveDot active={isLive} pending={pending} />
                        <div style={{ flex:1 }}>
                            <div style={{ color:"#72ea1e", fontFamily:"Bebas Neue,sans-serif", fontSize:22, letterSpacing:"0.1em" }}>
                                CONTINUOUS INTELLIGENCE — LIVE FEED
                            </div>
                            <div style={{ color:"#a1d96a", fontSize:11, fontFamily:"monospace", marginTop:2, wordBreak:"break-all" }}>
                                {repoUrl} @ {branchName || "main"}
                            </div>
                        </div>
                        <div style={{ display:"flex", gap:10, alignItems:"center" }}>
                            {isLive && (
                                <button onClick={handleForceScan} disabled={pending}
                                    style={{ padding:"7px 16px", borderRadius:999, border:"1px solid #72ea1e", background: pending ? "transparent" : "rgba(114,234,30,0.12)", color: pending ? "#555" : "#72ea1e", fontSize:11, fontWeight:700, cursor: pending ? "not-allowed" : "pointer", letterSpacing:"0.06em" }}>
                                    ⚡ FORCE SCAN NOW
                                </button>
                            )}
                            {isLive && (
                                <button onClick={handleStop} style={{ padding:"7px 16px", borderRadius:999, border:"1px solid #ff9800", background:"transparent", color:"#ff9800", fontSize:12, fontWeight:700, cursor:"pointer", letterSpacing:"0.06em" }}>
                                    ⏹ STOP WATCH
                                </button>
                            )}
                            <button onClick={() => { if (isLive) handleStop().then(onClose); else onClose(); }}
                                style={{ padding:"7px 14px", borderRadius:999, border:"1px solid #555", background:"transparent", color:"#aaa", fontSize:12, fontWeight:700, cursor:"pointer" }}>
                                ✕ CLOSE
                            </button>
                        </div>
                    </div>

                    {/* ── stat bar ── */}
                    {status && (
                        <div style={{ padding:"12px 24px", display:"flex", gap:10, flexWrap:"wrap", borderBottom:"1px solid #72ea1e22", background:"rgba(0,0,0,0.3)" }}>
                            <StatCard label="STATUS"        value={(status.status || "—").toUpperCase()}
                                color={status.status==="running"?"#72ea1e":status.status==="idle"?"#a1d96a":status.status==="stopped"?"#ff9800":"#ff6b6b"} />
                            <StatCard label="POLL COUNT"    value={fmt(status.poll_count,  "0")} color="#90caf9" />
                            <StatCard label="SCANS RUN"     value={fmt(status.run_count,   "0")} color="#a1d96a" />
                            <StatCard label="CHANGES FOUND" value={fmt(status.change_detected_count,"0")} color="#ffb74d" />
                            <StatCard label="LAST HEALTH"   value={fmt(status.last_result?.summary?.health_score)} color="#72ea1e" />
                        </div>
                    )}

                    {/* ── commit SHA bar ── */}
                    {(status?.last_seen_commit || status?.last_scanned_commit) && (
                        <div style={{ padding:"8px 24px", display:"flex", gap:20, flexWrap:"wrap", background:"rgba(0,0,0,0.2)", borderBottom:"1px solid #72ea1e11", fontSize:11, fontFamily:"monospace" }}>
                            {status.last_seen_commit && (
                                <span>
                                    <span style={{ color:"#555" }}>latest commit: </span>
                                    <span style={{ color: pending ? "#ffb74d" : "#d9ffb8" }}>
                                        {status.last_seen_commit.slice(0, 16)}
                                    </span>
                                    {pending && <span style={{ color:"#ffb74d", marginLeft:8 }}>⏳ scanning…</span>}
                                </span>
                            )}
                            {status.last_scanned_commit && (
                                <span>
                                    <span style={{ color:"#555" }}>last scanned: </span>
                                    <span style={{ color:"#72ea1e" }}>{status.last_scanned_commit.slice(0, 16)}</span>
                                </span>
                            )}
                            <span style={{ color:"#555" }}>frontend polls every 3 s · backend checks GitHub every 15 s</span>
                        </div>
                    )}

                    {/* ── error banner ── */}
                    {(err || status?.last_error) && (
                        <div style={{ padding:"10px 24px", background:"rgba(255,71,87,0.1)", borderBottom:"1px solid #ff475722", color:"#ff6b6b", fontSize:12 }}>
                            ⚠️ {err || status.last_error}
                        </div>
                    )}

                    {/* ── body: feed + log ── */}
                    <div style={{ flex:1, display:"grid", gridTemplateColumns:"1fr 300px", minHeight:0, overflow:"hidden" }}>

                        {/* commit events feed */}
                        <div className="lcm-sb" style={{ overflowY:"auto", padding:"16px 20px", borderRight:"1px solid #72ea1e11" }}>

                            {phase === "starting" && (
                                <div style={{ display:"flex", flexDirection:"column", alignItems:"center", justifyContent:"center", height:200, gap:16 }}>
                                    <div style={{ width:36, height:36, border:"3px solid #72ea1e33", borderTop:"3px solid #72ea1e", borderRadius:"50%", animation:"spin 0.8s linear infinite" }} />
                                    <div style={{ color:"#a1d96a", fontSize:13 }}>Connecting to continuous watch...</div>
                                </div>
                            )}

                            {events.length === 0 && phase === "watching" && (
                                <div style={{ textAlign:"center", color:"#555", fontSize:13, marginTop:60 }}>
                                    <div style={{ fontSize:32, marginBottom:12 }}>👁</div>
                                    <div>Watching for commits...</div>
                                    <div style={{ marginTop:6, fontSize:11 }}>
                                        A scan triggers when the branch HEAD SHA changes.
                                    </div>
                                    <div style={{ marginTop:4, fontSize:11, color:"#72ea1e88" }}>
                                        Frontend polls every 3 s — backend checks GitHub every 15 s
                                    </div>
                                    {pending && (
                                        <div style={{ marginTop:16, padding:"10px 20px", background:"rgba(255,183,77,0.1)", border:"1px solid #ffb74d44", borderRadius:8, color:"#ffb74d", fontSize:12 }}>
                                            ⏳ New commit detected — scan in progress…
                                        </div>
                                    )}
                                </div>
                            )}

                            {events.map((ev, i) => <CommitEvent key={i} event={ev} index={i} />)}
                            <div ref={eventsEndRef} />
                        </div>

                        {/* activity log */}
                        <div style={{ display:"flex", flexDirection:"column", background:"#050e05" }}>
                            <div style={{ padding:"10px 14px", color:"#72ea1e", fontSize:10, fontWeight:700, letterSpacing:"0.12em", borderBottom:"1px solid #72ea1e11" }}>
                                ACTIVITY LOG
                            </div>
                            <div className="lcm-sb" style={{ flex:1, overflowY:"auto", padding:"10px 14px", fontFamily:"monospace", fontSize:10, color:"#6a996a", lineHeight:1.75 }}>
                                {log.map((line, i) => (
                                    <div key={i} style={{ color: line.includes("❌") ? "#ff6b6b" : line.includes("⚠️") ? "#ffb74d" : line.includes("✅") ? "#72ea1e" : line.includes("📡") ? "#ffb74d" : "#6a996a" }}>
                                        {line}
                                    </div>
                                ))}
                                <div ref={logEndRef} />
                            </div>
                        </div>
                    </div>

                    {/* footer */}
                    <div style={{ padding:"8px 24px", borderTop:"1px solid #72ea1e11", display:"flex", gap:12, alignItems:"center", background:"rgba(0,0,0,0.4)" }}>
                        <span style={{ color:"#555", fontSize:10, flex:1 }}>
                            {watchId ? `watch_id: ${watchId}` : "watch not started"}
                        </span>
                        <span style={{ color:"#555", fontSize:10 }}>
                            {events.length} commit scan{events.length !== 1 ? "s" : ""} captured
                        </span>
                    </div>
                </div>
            </div>
        </>
    );
}
