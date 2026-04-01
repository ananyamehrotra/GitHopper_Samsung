import React from "react";
import { useNavigate } from "react-router-dom";
import ShinyText from "../components/ShinyText";
import { ThemeToggle } from "../components/ThemeToggle";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import "./HomePage.css";

export function HomePage() {
    const { isDark } = useTheme();
    const navigate = useNavigate();

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

                        <button
                            className="cta-btn"
                            onClick={() => navigate('/dashboard')}
                        >
                            Get Started →
                        </button>
                    </div>

                    <button
                        className="auth-nav-button"
                        onClick={() => navigate('/login')}
                    >
                        LOGIN / SIGN UP
                    </button>
                </main>
            </div>
        </>
    );
}
