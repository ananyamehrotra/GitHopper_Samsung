import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import ShinyText from "../components/ShinyText";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import "./HomePage.css";
import "./DashboardPage.css";

export function DashboardPage() {
    const { isDark } = useTheme();
    const navigate = useNavigate();
    const [repoUrl, setRepoUrl] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleAnalyse = async () => {
        if (!repoUrl.trim()) {
            setError("Please enter a GitHub repository URL");
            return;
        }

        setLoading(true);
        setError("");

        try {
            const response = await fetch("http://localhost:5000/api/analyze", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    repo_url: repoUrl
                })
            });

            if (!response.ok) {
                throw new Error(`Failed to scan repository: ${response.status}`);
            }

            const data = await response.json();
            console.log("📊 Analysis complete:", data);

            // Navigate to analysis page with results
            navigate("/analyse-branches", {
                state: {
                    scanResult: data,
                    repoUrl: repoUrl
                }
            });
        } catch (err) {
            setError(err.message || "Failed to scan repository");
            console.error("Scan error:", err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <Plasma
                color="#72ea1e"
                speed={0.6}
                direction="forward"
                scale={1.1}
                opacity={0.1}
                mouseInteractive={true}
            />
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
                                >
                                    {loading ? "SCANNING..." : "ANALYSE"}
                                </button>
                            </div>
                            {error && <div style={{ color: "#ff6b6b", marginTop: "10px", fontSize: "14px" }}>{error}</div>}
                        </div>

                        <div className="scan-features">
                            <button className="feature-button" onClick={() => navigate('/analyse-branches')}>
                                <span className="feature-dot"></span>
                                ANALYSE BRANCHES
                            </button>
                            <button className="feature-button" onClick={() => navigate('/security-audit')}>
                                <span className="feature-dot"></span>
                                SECURITY AUDIT
                            </button>
                            <button className="feature-button" onClick={() => navigate('/debt-report')}>
                                <span className="feature-dot"></span>
                                DEBT REPORT
                            </button>
                            <button className="feature-button" onClick={() => navigate('/health-score')}>
                                <span className="feature-dot"></span>
                                HEALTH SCORE
                            </button>
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
