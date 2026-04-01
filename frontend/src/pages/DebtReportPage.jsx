import React from "react";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import "./DashboardPage.css";
import "./DebtReportPage.css";

export function DebtReportPage() {

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
                <section className="scan-hero" aria-label="debt report section">
                    <div className="scan-content">
                        <h2 className="scan-title">
                            <span className="scan-word">DEBT</span>
                            <span className="scan-ampersand">&</span>
                            <span className="secure-word">REPORT</span>
                        </h2>
                    </div>
                </section>
            </div>
        </>
    );
}
