import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import ShinyText from "../components/ShinyText";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import { LiveChangesModal } from "./LiveChangesModal";
import "./HomePage.css";
import "./DashboardPage.css";

export function DashboardPage() {
    const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://localhost:5001";
    const { isDark } = useTheme();
    const navigate = useNavigate();
    const [repoUrl, setRepoUrl] = useState("");
    const [branchName, setBranchName] = useState("main");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const [continuousMode, setContinuousMode] = useState(true);
    const [showLiveModal, setShowLiveModal] = useState(false);
    const [watchId, setWatchId] = useState("");
    const [watchStatus, setWatchStatus] = useState(null);
    const [watchError, setWatchError] = useState("");
    const [lastManualResult, setLastManualResult] = useState(() => {
        try {
            const saved = localStorage.getItem("githopper_last_scan");
            return saved ? JSON.parse(saved) : null;
        } catch (e) {
            return null;
        }
    });

    useEffect(() => {
        if (!watchId) {
            return undefined;
        }

        const loadStatus = async () => {
            try {
                const response = await fetch(`${API_BASE}/api/continuous/status/${watchId}`);
                const data = await response.json();
                if (!response.ok) {
                    throw new Error(data.error || "Failed to fetch watch status");
                }
                setWatchStatus(data);
                setWatchError("");
            } catch (err) {
                setWatchError(err.message || "Failed to fetch watch status");
            }
        };

        loadStatus();
        const intervalId = window.setInterval(loadStatus, 5000);
        return () => window.clearInterval(intervalId);
    }, [watchId]);

    const handleAnalyse = async () => {
        if (!repoUrl.trim()) {
            setError("Please enter a GitHub repository URL");
            return;
        }

        // Continuous mode → open Live Changes Modal (watch-based live feed)
        if (continuousMode) {
            setError("");
            setShowLiveModal(true);
            return;
        }

        // Classic mode → one-shot scan then navigate to results page
        setLoading(true);
        setError("");

        try {
            const response = await fetch(`${API_BASE}/api/analyze`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    repo_url: repoUrl,
                    branch_name: branchName || "main",
                    generate_fixes: false
                })
            });

            if (!response.ok) {
                throw new Error(`Failed to scan repository: ${response.status}`);
            }

            const data = await response.json();
            console.log("📊 Classic analysis complete:", data);

            setLastManualResult(data);
            localStorage.setItem("githopper_last_scan", JSON.stringify(data));
            localStorage.setItem("githopper_last_url", repoUrl);
            localStorage.setItem("githopper_last_branch", branchName || "main");
            localStorage.setItem("githopper_last_scan_mode", continuousMode ? "continuous" : "classic");

            navigate("/analyse-branches", {
                state: {
                    scanResult: data,
                    repoUrl: repoUrl,
                    scanMode: "classic"
                }
            });
        } catch (err) {
            setError(err.message || "Failed to scan repository");
            console.error("Scan error:", err);
        } finally {
            setLoading(false);
        }
    };

    const handleStartWatch = async () => {
        if (!repoUrl.trim()) {
            setError("Please enter a GitHub repository URL");
            return;
        }

        try {
            const response = await fetch(`${API_BASE}/api/continuous/start`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    repo_url: repoUrl,
                    branch_name: branchName || "main",
                    interval_seconds: 60
                })
            });

            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || "Failed to start watch mode");
            }

            setWatchId(data.watch_id);
            setWatchStatus({ ...data, run_count: 0, last_result: null });
            setWatchError("");
        } catch (err) {
            setWatchError(err.message || "Failed to start watch mode");
        }
    };

    const handleStopWatch = async () => {
        if (!watchId) {
            return;
        }

        try {
            const response = await fetch(`${API_BASE}/api/continuous/stop/${watchId}`, {
                method: "POST"
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || "Failed to stop watch mode");
            }
            setWatchStatus((prev) => prev ? { ...prev, status: data.status } : data);
        } catch (err) {
            setWatchError(err.message || "Failed to stop watch mode");
        }
    };

    return (
        <>
            {showLiveModal && (
                <LiveChangesModal
                    repoUrl={repoUrl}
                    branchName={branchName || "main"}
                    onClose={() => setShowLiveModal(false)}
                />
            )}
            <Plasma
                color="#72ea1e"
                speed={0.6}
                direction="forward"
                scale={1.1}
                opacity={0.1}
                mouseInteractive={true}
            />
            <div style={{ position: "fixed", top: "16px", right: "150px", display: "flex", gap: "10px", zIndex: 50 }}>
                <button
                    onClick={() => navigate("/analytics")}
                    style={{
                        padding: "8px 16px",
                        background: "rgba(114, 234, 30, 0.15)",
                        border: "1px solid #72ea1e",
                        color: "#72ea1e",
                        borderRadius: "6px",
                        fontSize: "12px",
                        fontWeight: "600",
                        cursor: "pointer",
                        transition: "all 0.3s ease",
                    }}
                    onMouseEnter={(e) => {
                        e.target.style.background = "rgba(114, 234, 30, 0.25)";
                        e.target.style.transform = "translateY(-2px)";
                    }}
                    onMouseLeave={(e) => {
                        e.target.style.background = "rgba(114, 234, 30, 0.15)";
                        e.target.style.transform = "translateY(0)";
                    }}
                >
                    📊 Analytics
                </button>
            </div>
            <ThemeToggle />
            <UserProfile />
            <div className="page-shell">
                <main className="home-hero" aria-label="landing hero">
                    <video className="hero-video-bg" autoPlay muted loop playsInline preload="auto" aria-hidden="true">
                        <source src={isDark ? "/assets/githopper.mp4" : "/assets/githopperlight.mp4"} type="video/mp4" />
                    </video>
                    <div className="hero-video-overlay" aria-hidden="true" />

                    <div className="hero-content">
                        <h1 className="git-lockup">
                            <ShinyText
                                text="GIT"
                                className="git-bold"
                                speed={2.1}
                                delay={0}
                                color="#72ea1e"
                                shineColor="#d9ffb8"
                                spread={122}
                                direction="left"
                                yoyo={false}
                                pauseOnHover={false}
                                disabled={false}
                            />
                            <ShinyText
                                text="HOPPER"
                                className="hopper-thin"
                                speed={2.2}
                                delay={0.08}
                                color="#69d31d"
                                shineColor="#d9ffb8"
                                spread={118}
                                direction="left"
                                yoyo={false}
                                pauseOnHover={false}
                                disabled={false}
                            />
                        </h1>

                        <p className="hero-tagline">
                            <em>One URL . Every vulnerability. No jargon.</em>
                        </p>
                    </div>
                </main>

                <section className="scan-hero" aria-label="scan and secure section">
                    <div className="scan-content">
                        <h2 className="scan-title">
                            <span className="scan-word">SCAN</span>
                            <span className="scan-ampersand">&</span>
                            <span className="secure-word">SECURE</span>
                        </h2>

                        <div className="scan-input-group">
                            <label htmlFor="repo-input" className="scan-label">SCAN YOUR REPO</label>
                            <div style={{ marginBottom: "14px", display: "flex", gap: "10px", flexWrap: "wrap" }}>
                                <button
                                    type="button"
                                    onClick={() => setContinuousMode(true)}
                                    disabled={loading}
                                    style={{
                                        padding: "8px 14px",
                                        borderRadius: "999px",
                                        border: "1px solid #72ea1e",
                                        background: continuousMode ? "#72ea1e" : "transparent",
                                        color: continuousMode ? "#000" : "#72ea1e",
                                        fontSize: "12px",
                                        fontWeight: "700",
                                        cursor: "pointer"
                                    }}
                                >
                                    CONTINUOUS INTELLIGENCE
                                </button>
                                <button
                                    type="button"
                                    onClick={() => setContinuousMode(false)}
                                    disabled={loading}
                                    style={{
                                        padding: "8px 14px",
                                        borderRadius: "999px",
                                        border: "1px solid #72ea1e",
                                        background: !continuousMode ? "#72ea1e" : "transparent",
                                        color: !continuousMode ? "#000" : "#72ea1e",
                                        fontSize: "12px",
                                        fontWeight: "700",
                                        cursor: "pointer"
                                    }}
                                >
                                    CLASSIC PIPELINE
                                </button>
                            </div>
                            <div className="input-wrapper">
                                <span className="input-prefix">github.com /</span>
                                <input
                                    id="repo-input"
                                    type="text"
                                    placeholder="username / repository"
                                    value={repoUrl}
                                    onChange={(e) => setRepoUrl(e.target.value)}
                                    className="repo-input"
                                    disabled={loading}
                                />
                                <button
                                    className="analyse-button"
                                    onClick={handleAnalyse}
                                    disabled={loading}
                                    style={continuousMode ? {
                                        background: "linear-gradient(90deg, #72ea1e, #89ff35)",
                                        position: "relative",
                                        overflow: "hidden"
                                    } : {}}
                                >
                                    {loading ? "SCANNING..." : continuousMode ? "▶ WATCH LIVE" : "ANALYSE"}
                                </button>
                            </div>
                            
                            <div style={{ marginTop: "12px", display: "flex", gap: "10px", alignItems: "center" }}>
                                <label htmlFor="branch-input" style={{ color: "#72ea1e", fontSize: "12px", fontWeight: "600" }}>BRANCH (optional):</label>
                                <input
                                    id="branch-input"
                                    type="text"
                                    placeholder="main"
                                    value={branchName}
                                    onChange={(e) => setBranchName(e.target.value)}
                                    style={{
                                        padding: "6px 10px",
                                        background: "rgba(114, 234, 30, 0.1)",
                                        border: "1px solid #72ea1e",
                                        borderRadius: "4px",
                                        color: "#d9ffb8",
                                        fontSize: "13px",
                                        fontFamily: "monospace",
                                        width: "150px",
                                        disabled: loading
                                    }}
                                    disabled={loading}
                                />
                            </div>
                            
                            {error && <div style={{ color: "#ff6b6b", marginTop: "10px", fontSize: "14px" }}>{error}</div>}
                            <div style={{ marginTop: "10px", color: "#a1d96a", fontSize: "12px", maxWidth: "720px" }}>
                                {continuousMode
                                    ? "▶ WATCH LIVE opens a real-time dialog that polls every commit — new issues, resolved & persisting are shown live as they happen."
                                    : "Classic mode uses the original RepoScan pipeline without the MCP extension layer."}
                            </div>

                            {continuousMode && (
                                <div style={{
                                    marginTop: "18px",
                                    border: "1px solid rgba(114, 234, 30, 0.45)",
                                    borderRadius: "10px",
                                    padding: "16px",
                                    background: "rgba(114, 234, 30, 0.06)",
                                    maxWidth: "780px"
                                }}>
                                    <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "center", flexWrap: "wrap" }}>
                                        <div>
                                            <div style={{ color: "#72ea1e", fontWeight: "700", fontSize: "13px" }}>WATCH MODE TESTER</div>
                                            <div style={{ color: "#a1d96a", fontSize: "12px", marginTop: "4px" }}>
                                                Start background incremental scans from the UI before wiring the plugin host.
                                            </div>
                                        </div>
                                        <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
                                            <button
                                                type="button"
                                                onClick={handleStartWatch}
                                                disabled={loading}
                                                style={{
                                                    padding: "8px 14px",
                                                    borderRadius: "999px",
                                                    border: "1px solid #72ea1e",
                                                    background: "#72ea1e",
                                                    color: "#000",
                                                    fontSize: "12px",
                                                    fontWeight: "700",
                                                    cursor: "pointer"
                                                }}
                                            >
                                                START WATCH
                                            </button>
                                            <button
                                                type="button"
                                                onClick={handleStopWatch}
                                                disabled={!watchId}
                                                style={{
                                                    padding: "8px 14px",
                                                    borderRadius: "999px",
                                                    border: "1px solid #ff9800",
                                                    background: "transparent",
                                                    color: !watchId ? "#777" : "#ff9800",
                                                    fontSize: "12px",
                                                    fontWeight: "700",
                                                    cursor: !watchId ? "not-allowed" : "pointer"
                                                }}
                                            >
                                                STOP WATCH
                                            </button>
                                        </div>
                                    </div>

                                    {(watchId || watchError) && (
                                            <div style={{ marginTop: "14px", display: "grid", gap: "10px" }}>
                                            {watchId && (
                                                <div style={{ color: "#d9ffb8", fontSize: "12px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                    watch_id: {watchId}
                                                </div>
                                            )}
                                            {watchStatus && (
                                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(140px, 1fr))", gap: "10px" }}>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>STATUS</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700", textTransform: "uppercase" }}>
                                                            {watchStatus.status || "running"}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>POLL COUNT</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700" }}>
                                                            {watchStatus.poll_count ?? 0}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>SCAN COUNT</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700" }}>
                                                            {watchStatus.run_count ?? 0}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>CHANGES DETECTED</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700" }}>
                                                            {watchStatus.change_detected_count ?? 0}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>LAST HEALTH SCORE</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700" }}>
                                                            {watchStatus.last_result?.summary?.health_score ?? "N/A"}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>LAST MODE</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700", textTransform: "uppercase" }}>
                                                            {watchStatus.last_result?.continuous_intelligence?.scan_mode ?? "N/A"}
                                                        </div>
                                                    </div>
                                                </div>
                                            )}
                                            {watchStatus?.last_seen_commit && (
                                                <div style={{ color: "#d9ffb8", fontSize: "12px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                    last_seen_commit: {watchStatus.last_seen_commit}
                                                </div>
                                            )}
                                            {watchStatus?.last_scanned_commit && (
                                                <div style={{ color: "#a1d96a", fontSize: "12px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                    last_scanned_commit: {watchStatus.last_scanned_commit}
                                                </div>
                                            )}
                                            <div style={{ color: "#a1d96a", fontSize: "12px" }}>
                                                Polling can continue in the background, but a new scan now only runs when the latest branch commit SHA changes.
                                            </div>
                                            {watchStatus?.last_error && (
                                                <div style={{ color: "#ff6b6b", fontSize: "12px" }}>
                                                    watch error: {watchStatus.last_error}
                                                </div>
                                            )}
                                            {watchError && (
                                                <div style={{ color: "#ff6b6b", fontSize: "12px" }}>
                                                    {watchError}
                                                </div>
                                            )}
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>

                        <p className="scan-tagline">
                            <em>One URL . Every vulnerability. <span className="highlight">No jargon.</span></em>
                        </p>
                    </div>
                </section>
            </div>
        </>
    );
}
