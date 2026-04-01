import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import "./DashboardPage.css";
import "./AnalyseBranchesPage.css";

export function AnalyseBranchesPage() {
    const location = useLocation();
    const navigate = useNavigate();
    useTheme();
    const scanResult = location.state?.scanResult;
    const repoUrl = location.state?.repoUrl;
    const scanMode = location.state?.scanMode;
    const [expandedVulnerability, setExpandedVulnerability] = useState(null);

    if (!scanResult) {
        return (
            <>
                <Plasma color="#72ea1e" speed={0.6} direction="forward" scale={1.1} opacity={0.1} mouseInteractive={true} />
                <ThemeToggle />
                <UserProfile />
                <div className="page-shell" style={{ padding: "40px", textAlign: "center" }}>
                    <h2 style={{ color: "#72ea1e" }}>No scan results available</h2>
                    <p>Please go back to the dashboard and scan a repository first.</p>
                    <button onClick={() => navigate("/dashboard")} style={{
                        marginTop: "20px",
                        padding: "10px 20px",
                        background: "#72ea1e",
                        color: "#000",
                        border: "none",
                        borderRadius: "4px",
                        cursor: "pointer",
                        fontSize: "16px",
                        fontWeight: "bold"
                    }}>
                        Back to Dashboard
                    </button>
                </div>
            </>
        );
    }

    const isContinuous = scanResult.pipeline === "continuous_intelligence_extension" || scanMode === "continuous";
    const analyze = scanResult.stages?.analyze || {};
    const continuous = scanResult.continuous_intelligence || {};
    const data = scanResult.data || {};
    const vulnerableFiles = isContinuous ? (data.vulnerable_files || []) : (analyze.vulnerable_files || []);
    const vulnerabilities = isContinuous ? (data.security_findings || []) : (analyze.vulnerabilities || []);
    const debtFindings = isContinuous ? (data.debt_findings || []) : [];
    const autofixSuggestions = isContinuous ? (data.autofix_suggestions || []) : [];
    const billing = analyze.billing || {};
    const filesSummary = {
        total: isContinuous ? (data.total_files_fetched || 0) : (analyze.total_files_analyzed || 0),
        withIssues: isContinuous ? vulnerableFiles.length : (analyze.files_with_issues || 0),
        totalVulnerabilities: isContinuous ? vulnerabilities.length : (analyze.total_vulnerabilities || 0)
    };

    return (
        <>
            <Plasma color="#72ea1e" speed={0.6} direction="forward" scale={1.1} opacity={0.1} mouseInteractive={true} />
            <ThemeToggle />
            <UserProfile />
            <div className="page-shell" style={{ padding: "40px" }}>
                <section className="scan-hero" aria-label="analyse branches section">
                    <div className="scan-content">
                        <h2 className="scan-title" style={{ marginBottom: "30px" }}>
                            <span className="scan-word">BEDROCK</span>
                            <span className="scan-ampersand">&</span>
                            <span className="secure-word">ANALYSIS</span>
                        </h2>

                        {/* Repository Info */}
                        <div style={{
                            background: "rgba(114, 234, 30, 0.1)",
                            border: "1px solid #72ea1e",
                            borderRadius: "8px",
                            padding: "20px",
                            marginBottom: "20px"
                        }}>
                            <p style={{ margin: "0 0 10px 0", color: "#a1d96a", fontSize: "12px" }}>Repository</p>
                            <p style={{ margin: "0 0 15px 0", color: "#d9ffb8", fontSize: "14px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                {repoUrl || scanResult.repo_url || analyze.repo_url}
                            </p>
                            <p style={{ margin: "0 0 10px 0", color: "#a1d96a", fontSize: "12px" }}>Branch</p>
                            <p style={{ margin: "0", color: "#d9ffb8", fontSize: "14px", fontFamily: "monospace" }}>
                                {scanResult.branch_name || analyze.branch_name || "main"}
                            </p>
                        </div>

                        {isContinuous && (
                            <div style={{
                                background: "rgba(76, 175, 80, 0.08)",
                                border: "1px solid #4caf50",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "20px"
                            }}>
                                <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Continuous Intelligence</h3>
                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: "14px" }}>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>SCAN MODE</p>
                                        <p style={{ margin: 0, color: "#d9ffb8", fontSize: "18px", fontWeight: "bold", textTransform: "uppercase" }}>{continuous.scan_mode || "full"}</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>NEW ISSUES</p>
                                        <p style={{ margin: 0, color: "#ff9999", fontSize: "18px", fontWeight: "bold" }}>{continuous.new_issues ?? 0}</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>RESOLVED</p>
                                        <p style={{ margin: 0, color: "#9ccc65", fontSize: "18px", fontWeight: "bold" }}>{continuous.resolved_issues ?? 0}</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>PERSISTING</p>
                                        <p style={{ margin: 0, color: "#ffb74d", fontSize: "18px", fontWeight: "bold" }}>{continuous.persisting_issues ?? 0}</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>FIX TIME</p>
                                        <p style={{ margin: 0, color: "#90caf9", fontSize: "18px", fontWeight: "bold" }}>{continuous.estimated_fix_minutes ?? 0}m</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>SCORE DELTA</p>
                                        <p style={{ margin: 0, color: "#d9ffb8", fontSize: "18px", fontWeight: "bold" }}>
                                            {continuous.trend?.delta == null ? "N/A" : `${continuous.trend.delta > 0 ? "+" : ""}${continuous.trend.delta}`}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        )}

                        <div style={{ marginBottom: "30px", textAlign: "left" }}>
                            <button
                                onClick={() => navigate("/dashboard")}
                                style={{
                                    padding: "8px 20px",
                                    background: "transparent",
                                    color: "#72ea1e",
                                    border: "1px solid #72ea1e",
                                    borderRadius: "4px",
                                    cursor: "pointer",
                                    fontSize: "14px",
                                    fontWeight: "bold",
                                    transition: "all 0.2s ease-in-out"
                                }}
                                onMouseEnter={(e) => {
                                    e.target.style.background = "#72ea1e";
                                    e.target.style.color = "#000";
                                }}
                                onMouseLeave={(e) => {
                                    e.target.style.background = "transparent";
                                    e.target.style.color = "#72ea1e";
                                }}
                            >
                                ← Back to Dashboard
                            </button>
                        </div>

                        {/* Summary Cards */}
                        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "20px", marginBottom: "30px" }}>
                            <div style={{
                                background: "rgba(114, 234, 30, 0.1)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#72ea1e", marginTop: 0 }}>Total Files</h4>
                                <p style={{ fontSize: "32px", color: "#d9ffb8", margin: "10px 0" }}>{filesSummary.total}</p>
                            </div>
                            <div style={{
                                background: "rgba(255, 107, 107, 0.1)",
                                border: "1px solid #ff6b6b",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#ff6b6b", marginTop: 0 }}>Files with Issues</h4>
                                <p style={{ fontSize: "32px", color: "#ff9999", margin: "10px 0" }}>{filesSummary.withIssues}</p>
                            </div>
                            <div style={{
                                background: "rgba(255, 152, 0, 0.1)",
                                border: "1px solid #ff9800",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#ff9800", marginTop: 0 }}>Vulnerabilities Found</h4>
                                <p style={{ fontSize: "32px", color: "#ffb74d", margin: "10px 0" }}>{filesSummary.totalVulnerabilities}</p>
                            </div>
                        </div>

                        {isContinuous && debtFindings.length > 0 && (
                            <div style={{
                                background: "rgba(114, 234, 30, 0.05)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Technical Debt Signals ({debtFindings.length})</h3>
                                <div style={{ display: "grid", gap: "12px" }}>
                                    {debtFindings.slice(0, 8).map((item, idx) => (
                                        <div key={idx} style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "14px" }}>
                                            <p style={{ margin: "0 0 4px 0", color: "#d9ffb8", fontFamily: "monospace", fontSize: "12px" }}>{item.file}</p>
                                            <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "12px" }}>{item.type}</p>
                                            <p style={{ margin: 0, color: "#d2ddb8", fontSize: "13px" }}>{item.summary}</p>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* Vulnerable Files List */}
                        {vulnerableFiles.length > 0 && (
                            <div style={{
                                background: "rgba(255, 107, 107, 0.05)",
                                border: "1px solid #ff6b6b",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#ff6b6b", marginTop: 0 }}>Vulnerable Files ({vulnerableFiles.length})</h3>
                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))", gap: "15px" }}>
                                    {vulnerableFiles.map((file, idx) => (
                                        <div key={idx} style={{
                                            background: "#000",
                                            border: "1px solid #ff9999",
                                            borderRadius: "4px",
                                            padding: "15px"
                                        }}>
                                            <p style={{ margin: "0 0 8px 0", color: "#ff6b6b", fontWeight: "bold", fontSize: "13px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                {file.file}
                                            </p>
                                            <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px" }}>
                                                Type: <span style={{ color: "#d9ffb8" }}>{file.type}</span>
                                            </p>
                                            <p style={{ margin: "0", color: "#ff9800", fontSize: "12px" }}>
                                                Vulnerabilities: <span style={{ color: "#ffb74d", fontWeight: "bold" }}>{file.count}</span>
                                            </p>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* Detailed Vulnerabilities - Bedrock Analysis */}
                        {vulnerabilities.length > 0 && (
                            <div style={{
                                background: "rgba(255, 152, 0, 0.05)",
                                border: "1px solid #ff9800",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#ff9800", marginTop: 0 }}>Detailed Analysis ({vulnerabilities.length})</h3>
                                <div style={{ maxHeight: "1000px", overflowY: "auto" }}>
                                    {vulnerabilities.map((vuln, idx) => (
                                        <div key={idx} style={{
                                            borderBottom: idx < vulnerabilities.length - 1 ? "1px solid #333" : "none",
                                            paddingBottom: "20px",
                                            marginBottom: "20px",
                                            cursor: "pointer"
                                        }} onClick={() => setExpandedVulnerability(expandedVulnerability === idx ? null : idx)}>
                                            {/* Header */}
                                            <div style={{
                                                display: "flex",
                                                justifyContent: "space-between",
                                                alignItems: "start",
                                                padding: "12px",
                                                background: "rgba(255, 152, 0, 0.1)",
                                                borderRadius: "4px",
                                                marginBottom: "10px"
                                            }}>
                                                <div style={{ flex: 1 }}>
                                                    <p style={{ margin: "0 0 5px 0", color: "#ff6b6b", fontWeight: "bold", fontSize: "14px" }}>
                                                        {expandedVulnerability === idx ? "[OPEN]" : "[+]"} {vuln.type || "Unknown"}
                                                    </p>
                                                    <p style={{ margin: "0", color: "#d9ffb8", fontSize: "12px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                        {vuln.file}
                                                    </p>
                                                </div>
                                                <div style={{
                                                    padding: "4px 8px",
                                                    borderRadius: "4px",
                                                    fontSize: "11px",
                                                    fontWeight: "bold",
                                                    background: vuln.severity === "CRITICAL" ? "#ff6b6b" : vuln.severity === "HIGH" ? "#ff9800" : vuln.severity === "MEDIUM" ? "#ffb74d" : "#4caf50",
                                                    color: "#000"
                                                }}>
                                                    {vuln.severity}
                                                </div>
                                            </div>

                                            {/* Expanded Details */}
                                            {expandedVulnerability === idx && (
                                                <div style={{ paddingLeft: "12px", color: "#d2ddb8" }}>
                                                    {/* Explanation */}
                                                    <div style={{ marginBottom: "15px" }}>
                                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px", fontWeight: "bold" }}>EXPLANATION</p>
                                                        <p style={{ margin: "0", color: "#d2ddb8", fontSize: "13px", lineHeight: "1.5" }}>
                                                            {vuln.explanation || "No explanation provided"}
                                                        </p>
                                                    </div>

                                                    {/* Business Impact */}
                                                    <div style={{ marginBottom: "15px",  padding: "10px", background: "rgba(255, 107, 107, 0.1)", borderLeft: "3px solid #ff6b6b", borderRadius: "4px" }}>
                                                        <p style={{ margin: "0 0 5px 0", color: "#ff6b6b", fontSize: "12px", fontWeight: "bold" }}>BUSINESS IMPACT</p>
                                                        <p style={{ margin: "0", color: "#ff9999", fontSize: "13px", lineHeight: "1.5" }}>
                                                            {vuln.business_impact || "Impact information not available"}
                                                        </p>
                                                    </div>

                                                    {/* Remediation */}
                                                    <div style={{ marginBottom: "15px" }}>
                                                        <p style={{ margin: "0 0 5px 0", color: "#4caf50", fontSize: "12px", fontWeight: "bold" }}>REMEDIATION</p>
                                                        <p style={{ margin: "0", color: "#9ccc65", fontSize: "13px", lineHeight: "1.5", fontFamily: "monospace", whiteSpace: "pre-wrap", wordBreak: "break-word" }}>
                                                            {vuln.remediation || "See explanation above"}
                                                        </p>
                                                    </div>

                                                    {/* Fix Time Estimate */}
                                                    {vuln.estimated_minutes_to_fix && (
                                                        <div>
                                                            <p style={{ margin: "0 0 5px 0", color: "#64b5f6", fontSize: "12px", fontWeight: "bold" }}>ESTIMATED FIX TIME</p>
                                                            <p style={{ margin: "0", color: "#90caf9", fontSize: "13px" }}>
                                                                ~{vuln.estimated_minutes_to_fix} minutes
                                                            </p>
                                                        </div>
                                                    )}
                                                </div>
                                            )}
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {isContinuous && autofixSuggestions.length > 0 && (
                            <div style={{
                                background: "rgba(100, 181, 246, 0.06)",
                                border: "1px solid #64b5f6",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#64b5f6", marginTop: 0 }}>AutoFix Suggestions ({autofixSuggestions.length})</h3>
                                <div style={{ display: "grid", gap: "16px" }}>
                                    {autofixSuggestions.slice(0, 6).map((fix, idx) => (
                                        <div key={idx} style={{ background: "#000", border: "1px solid #64b5f6", borderRadius: "6px", padding: "16px" }}>
                                            <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "start" }}>
                                                <div>
                                                    <p style={{ margin: "0 0 6px 0", color: "#d9ffb8", fontFamily: "monospace", fontSize: "12px" }}>{fix.file_path}</p>
                                                    <p style={{ margin: 0, color: "#d2ddb8", fontSize: "13px" }}>{fix.issue}</p>
                                                </div>
                                                <div style={{
                                                    padding: "4px 8px",
                                                    borderRadius: "999px",
                                                    background: fix.validation_status === "VALIDATED" ? "#4caf50" : "#ff9800",
                                                    color: "#000",
                                                    fontWeight: "bold",
                                                    fontSize: "11px"
                                                }}>
                                                    {fix.validation_status}
                                                </div>
                                            </div>
                                            <div style={{ marginTop: "12px" }}>
                                                <p style={{ margin: "0 0 6px 0", color: "#90caf9", fontSize: "12px", fontWeight: "bold" }}>EXPLANATION</p>
                                                <p style={{ margin: "0 0 10px 0", color: "#d2ddb8", fontSize: "13px" }}>{fix.explanation}</p>
                                                <p style={{ margin: "0 0 6px 0", color: "#90caf9", fontSize: "12px", fontWeight: "bold" }}>PATCH PREVIEW</p>
                                                <pre style={{
                                                    margin: 0,
                                                    whiteSpace: "pre-wrap",
                                                    wordBreak: "break-word",
                                                    fontSize: "11px",
                                                    color: "#b3e5fc",
                                                    background: "rgba(100, 181, 246, 0.08)",
                                                    padding: "10px",
                                                    borderRadius: "4px",
                                                    maxHeight: "180px",
                                                    overflow: "auto"
                                                }}>
                                                    {fix.diff || "No patch generated"}
                                                </pre>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* Billing & Cost Information */}
                        {billing && (
                            <div style={{
                                background: "rgba(76, 175, 80, 0.05)",
                                border: "1px solid #4caf50",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#4caf50", marginTop: 0 }}>Analysis Cost & Billing</h3>
                                
                                {/* Cost Metrics */}
                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: "15px", marginBottom: "20px" }}>
                                    <div style={{ background: "#000", padding: "15px", borderRadius: "4px", border: "1px solid #4caf50" }}>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px" }}>API Calls Used</p>
                                        <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>
                                            {billing.calls_made || 0}
                                        </p>
                                    </div>
                                    <div style={{ background: "#000", padding: "15px", borderRadius: "4px", border: "1px solid #4caf50" }}>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px" }}>Estimated Cost</p>
                                        <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>
                                            ${(analyze.cost_tracker?.estimated_cost || 0).toFixed(4)}
                                        </p>
                                    </div>
                                    <div style={{ background: "#000", padding: "15px", borderRadius: "4px", border: "1px solid #4caf50" }}>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px" }}>Free Calls Remaining</p>
                                        <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>
                                            {billing.free_calls_remaining >= 0 ? billing.free_calls_remaining : "N/A"}
                                        </p>
                                    </div>
                                </div>

                                {/* Billing Status */}
                                <div style={{
                                    background: billing.will_be_charged ? "rgba(255, 107, 107, 0.1)" : "rgba(76, 175, 80, 0.1)",
                                    border: `1px solid ${billing.will_be_charged ? "#ff6b6b" : "#4caf50"}`,
                                    borderRadius: "4px",
                                    padding: "15px",
                                    marginBottom: "20px"
                                }}>
                                    <p style={{
                                        margin: "0",
                                        color: billing.will_be_charged ? "#ff6b6b" : "#4caf50",
                                        fontSize: "13px",
                                        fontWeight: "bold"
                                    }}>
                                        Status: {billing.will_be_charged ? "WARNING - You will be charged for additional analyses" : "Within free tier"}
                                    </p>
                                </div>

                                {/* Alternative Services */}
                                {billing.alternatives && billing.alternatives.length > 0 && (
                                    <div>
                                        <p style={{ margin: "0 0 15px 0", color: "#a1d96a", fontSize: "12px", fontWeight: "bold" }}>Alternative Services Comparison</p>
                                        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "12px" }}>
                                            {billing.alternatives.map((alt, idx) => (
                                                <a key={idx} href={alt.url} target="_blank" rel="noopener noreferrer" style={{
                                                    background: "#000",
                                                    border: "1px solid #72ea1e",
                                                    borderRadius: "4px",
                                                    padding: "12px",
                                                    textDecoration: "none",
                                                    transition: "all 0.3s"
                                                }} onMouseEnter={(e) => e.target.style.background = "rgba(114, 234, 30, 0.1)"} onMouseLeave={(e) => e.target.style.background = "#000"}>
                                                    <p style={{ margin: "0 0 5px 0", color: "#72ea1e", fontWeight: "bold", fontSize: "13px" }}>
                                                        {alt.name}
                                                    </p>
                                                    <p style={{ margin: "0", color: "#a1d96a", fontSize: "12px" }}>
                                                        {alt.cost}
                                                    </p>
                                                </a>
                                            ))}
                                        </div>
                                    </div>
                                )}
                            </div>
                        )}

                        {/* No Vulnerabilities Message */}
                        {vulnerabilities.length === 0 && (
                            <div style={{
                                background: "rgba(76, 175, 80, 0.1)",
                                border: "1px solid #4caf50",
                                borderRadius: "8px",
                                padding: "30px",
                                textAlign: "center",
                                marginBottom: "30px"
                            }}>
                                <p style={{ margin: "0", color: "#4caf50", fontSize: "16px", fontWeight: "bold" }}>
                                    No vulnerabilities found in this repository
                                </p>
                                <p style={{ margin: "5px 0 0 0", color: "#9ccc65", fontSize: "14px" }}>
                                    Code appears to be secure in the analyzed branch
                                </p>
                            </div>
                        )}

                        {/* Back Button */}
                        <button
                            onClick={() => navigate("/dashboard")}
                            style={{
                                padding: "12px 30px",
                                background: "#72ea1e",
                                color: "#000",
                                border: "none",
                                borderRadius: "4px",
                                cursor: "pointer",
                                fontSize: "16px",
                                fontWeight: "bold"
                            }}
                        >
                            Back to Dashboard
                        </button>
                    </div>
                </section>
            </div>
        </>
    );
}
