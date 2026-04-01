import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import "./DashboardPage.css";
import "./AnalyseBranchesPage.css";

// FileTree Component to display folder/file structure
const FileTree = ({ files, categoryName, categoryColor }) => {
    const [expanded, setExpanded] = useState({});

    // Group files by directory
    const buildTree = (fileList) => {
        const tree = {};
        fileList.forEach(file => {
            const parts = file.path.split('/');
            let current = tree;
            for (let i = 0; i < parts.length - 1; i++) {
                if (!current[parts[i]]) {
                    current[parts[i]] = {};
                }
                current = current[parts[i]];
            }
            current[parts[parts.length - 1]] = file;
        });
        return tree;
    };

    // Get icon based on language
    const getLanguageIcon = (language) => {
        const icons = {
            javascript: '[JS]',
            typescript: '[TS]',
            python: '[PY]',
            java: '[JAVA]',
            go: '[GO]',
            ruby: '[RB]',
            php: '[PHP]',
            cpp: '[C++]',
            json: '[JSON]',
            yaml: '[YAML]',
            markdown: '[MD]',
            html: '[HTML]',
            css: '[CSS]'
        };
        return icons[language?.toLowerCase()] || '[FILE]';
    };

    // Render tree recursively
    const renderTree = (obj, path = '') => {
        return Object.entries(obj).map(([key, value]) => {
            const fullPath = path ? `${path}/${key}` : key;
            const isDir = value && typeof value === 'object' && !value.path;
            const id = fullPath.replace(/\//g, '-');

            return (
                <div key={fullPath}>
                    {isDir ? (
                        <>
                            <div
                                onClick={() => setExpanded(prev => ({
                                    ...prev,
                                    [id]: !prev[id]
                                }))}
                                style={{
                                    padding: '8px 12px',
                                    cursor: 'pointer',
                                    display: 'flex',
                                    alignItems: 'center',
                                    color: categoryColor,
                                    fontWeight: 500
                                }}
                            >
                                <span style={{ marginRight: '8px' }}>
                                    {expanded[id] ? '[FOLDER-OPEN]' : '[FOLDER]'}
                                </span>
                                {key}/
                            </div>
                            {expanded[id] && (
                                <div style={{ marginLeft: '20px' }}>
                                    {renderTree(value, fullPath)}
                                </div>
                            )}
                        </>
                    ) : (
                        <div style={{
                            padding: '6px 12px',
                            display: 'flex',
                            alignItems: 'center',
                            color: '#d2ddb8',
                            fontSize: '14px'
                        }}>
                            <span style={{ marginRight: '8px', fontFamily: 'monospace', fontSize: '12px', color: '#72ea1e' }}>
                                {getLanguageIcon(value.language)}
                            </span>
                            <span>{key}</span>
                            <span style={{
                                marginLeft: '10px',
                                fontSize: '11px',
                                color: '#8f9a79',
                                padding: '2px 6px',
                                background: 'rgba(114, 234, 30, 0.1)',
                                borderRadius: '3px'
                            }}>
                                {value.language}
                            </span>
                        </div>
                    )}
                </div>
            );
        });
    };

    if (!files || files.length === 0) return null;

    const tree = buildTree(files);

    return (
        <div style={{
            background: "rgba(114, 234, 30, 0.05)",
            border: `1px solid ${categoryColor}`,
            borderRadius: "8px",
            padding: "20px",
            marginBottom: "20px"
        }}>
            <h3 style={{ color: categoryColor, marginTop: 0, marginBottom: "15px" }}>
                {categoryName} ({files.length})
            </h3>
            <div style={{
                background: "#000",
                borderRadius: "4px",
                padding: "12px",
                fontFamily: "monospace",
                fontSize: "13px",
                maxHeight: "400px",
                overflowY: "auto",
                color: "#d9ffb8"
            }}>
                {renderTree(tree)}
            </div>
        </div>
    );
};

export function AnalyseBranchesPage() {
    const location = useLocation();
    const navigate = useNavigate();
    const { isDark } = useTheme();
    const scanResult = location.state?.scanResult;
    const repoUrl = location.state?.repoUrl;
    const [expandedFile, setExpandedFile] = useState(null);

    if (!scanResult) {
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
                <div className="page-shell" style={{ padding: "40px", textAlign: "center" }}>
                    <h2 style={{ color: "#72ea1e" }}>No scan results available</h2>
                    <p>Please go back to the dashboard and scan a repository first.</p>
                    <button
                        onClick={() => navigate("/dashboard")}
                        style={{
                            marginTop: "20px",
                            padding: "10px 20px",
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
            </>
        );
    }

    const data = scanResult.data || {};

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
            <div className="page-shell" style={{ padding: "40px" }}>
                <section className="scan-hero" aria-label="analyse branches section">
                    <div className="scan-content">
                        <h2 className="scan-title" style={{ marginBottom: "30px" }}>
                            <span className="scan-word">ANALYSIS</span>
                            <span className="scan-ampersand">RESULTS</span>
                        </h2>

                        {/* Repository Info */}
                        <div style={{
                            background: "rgba(114, 234, 30, 0.1)",
                            border: "1px solid #72ea1e",
                            borderRadius: "8px",
                            padding: "20px",
                            marginBottom: "30px"
                        }}>
                            <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Repository</h3>
                            <p style={{ margin: "5px 0" }}><strong>URL:</strong> {repoUrl}</p>
                            <p style={{ margin: "5px 0" }}><strong>Status:</strong> <span style={{ color: "#72ea1e" }}>{scanResult.status}</span></p>
                            <p style={{ margin: "5px 0" }}><strong>Message:</strong> {scanResult.message}</p>
                        </div>

                        {/* Analysis Summary */}
                        {data.analysis_summary && (
                            <div style={{
                                background: "rgba(114, 234, 30, 0.1)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Debt Analysis Summary</h3>
                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "15px" }}>
                                    <div>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a" }}>Total Debt Signals:</p>
                                        <p style={{ margin: "0", fontSize: "24px", color: "#d9ffb8", fontWeight: "bold" }}>{data.analysis_summary.total_debt_signals}</p>
                                    </div>
                                    <div>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a" }}>Files with Signals:</p>
                                        <p style={{ margin: "0", fontSize: "24px", color: "#d9ffb8", fontWeight: "bold" }}>{data.analysis_summary.files_with_debt_signals}</p>
                                    </div>
                                    <div>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a" }}>Chunks to Analyze:</p>
                                        <p style={{ margin: "0", fontSize: "24px", color: "#d9ffb8", fontWeight: "bold" }}>{data.analysis_summary.cost_estimate.chunks_to_analyze}</p>
                                    </div>
                                    <div>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a" }}>Approx Tokens:</p>
                                        <p style={{ margin: "0", fontSize: "24px", color: "#d9ffb8", fontWeight: "bold" }}>{data.analysis_summary.cost_estimate.approx_tokens}</p>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Metrics Cards */}
                        <div style={{
                            display: "grid",
                            gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
                            gap: "20px",
                            marginBottom: "30px"
                        }}>
                            <div style={{
                                background: "rgba(114, 234, 30, 0.05)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#72ea1e", marginTop: 0 }}>Total Files</h4>
                                <p style={{ fontSize: "32px", color: "#d9ffb8", margin: "10px 0" }}>
                                    {data.total_files_fetched || 0}
                                </p>
                            </div>

                            <div style={{
                                background: "rgba(114, 234, 30, 0.05)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#72ea1e", marginTop: 0 }}>Configuration</h4>
                                <p style={{ fontSize: "32px", color: "#d9ffb8", margin: "10px 0" }}>
                                    {data.config_files || 0}
                                </p>
                            </div>

                            <div style={{
                                background: "rgba(114, 234, 30, 0.05)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#72ea1e", marginTop: 0 }}>Dependencies</h4>
                                <p style={{ fontSize: "32px", color: "#d9ffb8", margin: "10px 0" }}>
                                    {data.dependency_files || 0}
                                </p>
                            </div>

                            <div style={{
                                background: "rgba(114, 234, 30, 0.05)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#72ea1e", marginTop: 0 }}>Source Code</h4>
                                <p style={{ fontSize: "32px", color: "#d9ffb8", margin: "10px 0" }}>
                                    {data.source_files || 0}
                                </p>
                            </div>

                            <div style={{
                                background: "rgba(114, 234, 30, 0.05)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#72ea1e", marginTop: 0 }}>Code Chunks</h4>
                                <p style={{ fontSize: "32px", color: "#d9ffb8", margin: "10px 0" }}>
                                    {data.total_chunks || 0}
                                </p>
                            </div>
                        </div>

                        {/* Real-Time Analysis Progress Visualization */}
                        {scanResult.stages && scanResult.stages.analyze && (
                            <div style={{
                                background: "rgba(76, 175, 80, 0.05)",
                                border: "1px solid #4caf50",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#4caf50", marginTop: 0 }}>Analysis Progress Summary</h3>
                                
                                {/* Progress Bar */}
                                <div style={{ marginBottom: "20px" }}>
                                    <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "8px" }}>
                                        <span style={{ color: "#a1d96a", fontSize: "13px" }}>Files Analyzed</span>
                                        <span style={{ color: "#d2ddb8", fontSize: "13px" }}>{scanResult.stages.analyze.chunks_scanned} of {scanResult.stages.analyze.total_files}</span>
                                    </div>
                                    <div style={{
                                        width: "100%",
                                        height: "8px",
                                        background: "rgba(114, 234, 30, 0.2)",
                                        borderRadius: "4px",
                                        overflow: "hidden"
                                    }}>
                                        <div style={{
                                            height: "100%",
                                            width: `${Math.round((scanResult.stages.analyze.chunks_scanned / scanResult.stages.analyze.total_files) * 100)}%`,
                                            background: "linear-gradient(90deg, #4caf50, #9ccc65)",
                                            transition: "width 0.5s ease"
                                        }} />
                                    </div>
                                </div>

                                {/* File Tree Animation */}
                                <div style={{ background: "#000", borderRadius: "4px", padding: "15px", fontFamily: "monospace", fontSize: "12px" }}>
                                    <p style={{ color: "#4caf50", margin: "0 0 12px 0" }}>Scanning folder structure...</p>
                                    <div style={{ color: "#9ccc65", lineHeight: "1.8" }}>
                                        <div>. (root)</div>
                                        {data.files_by_category?.config?.length > 0 && (
                                            <div style={{ marginLeft: "20px", color: "#81c784" }}>
                                                ├─ config/
                                                {data.files_by_category.config.map((f, i) => (
                                                    <div key={i} style={{ marginLeft: "20px", color: "#c8e6c9" }}>
                                                        {i === data.files_by_category.config.length - 1 ? "└─" : "├─"} {f.path.split('/').pop()} [SCANNED]
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                        {data.files_by_category?.dependencies?.length > 0 && (
                                            <div style={{ marginLeft: "20px", color: "#81c784" }}>
                                                ├─ dependencies/
                                                {data.files_by_category.dependencies.map((f, i) => (
                                                    <div key={i} style={{ marginLeft: "20px", color: "#c8e6c9" }}>
                                                        {i === data.files_by_category.dependencies.length - 1 ? "└─" : "├─"} {f.path.split('/').pop()} [SCANNED]
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                        {data.files_by_category?.source_code?.length > 0 && (
                                            <div style={{ marginLeft: "20px", color: "#81c784" }}>
                                                └─ src/
                                                {data.files_by_category.source_code.map((f, i) => (
                                                    <div key={i} style={{ marginLeft: "20px", color: "#c8e6c9" }}>
                                                        {i === data.files_by_category.source_code.length - 1 ? "└─" : "├─"} {f.path.split('/').pop()} [SCANNED]
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                </div>

                                <p style={{ color: "#9ccc65", fontSize: "12px", margin: "12px 0 0 0", fontStyle: "italic" }}>
                                    Analysis completed with {scanResult.stages.analyze.cost_tracker?.api_calls || 0} API calls
                                </p>
                            </div>
                        )}

                        {/* Detailed Files Analysis */}
                        {data.detailed_files && data.detailed_files.length > 0 && (
                            <div style={{
                                background: "rgba(114, 234, 30, 0.05)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Detailed File Analysis</h3>
                                <div style={{ maxHeight: "800px", overflowY: "auto" }}>
                                    {data.detailed_files.map((file, idx) => (
                                        <div key={idx} style={{
                                            borderBottom: idx < data.detailed_files.length - 1 ? "1px solid #333" : "none",
                                            paddingBottom: "15px",
                                            marginBottom: "15px"
                                        }}>
                                            <div
                                                onClick={() => setExpandedFile(expandedFile === idx ? null : idx)}
                                                style={{
                                                    cursor: "pointer",
                                                    padding: "10px",
                                                    background: "rgba(114, 234, 30, 0.1)",
                                                    borderRadius: "4px",
                                                    marginBottom: "10px"
                                                }}
                                            >
                                                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                                                    <div>
                                                        <p style={{ margin: "0", color: "#72ea1e", fontWeight: "bold" }}>
                                                            {expandedFile === idx ? "[OPEN] " : "[+] "} {file.path}
                                                        </p>
                                                        <p style={{ margin: "5px 0 0 0", fontSize: "12px", color: "#8f9a79" }}>
                                                            {file.language} | {file.size_bytes} bytes | Debt Signals: {file.debt_signal_count}
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>

                                            {expandedFile === idx && (
                                                <div style={{ paddingLeft: "15px", color: "#d2ddb8" }}>
                                                    {/* Metrics */}
                                                    <div style={{ marginBottom: "10px", fontSize: "13px" }}>
                                                        <p style={{ margin: "5px 0", color: "#a1d96a" }}><strong>Metrics:</strong></p>
                                                        <p style={{ margin: "3px 0 3px 20px", fontSize: "12px" }}>
                                                            Lines: {file.metrics.total_lines} (Code: {file.metrics.code_lines}, Blank: {file.metrics.blank_lines}, Comments: {file.metrics.comment_lines})
                                                        </p>
                                                        <p style={{ margin: "3px 0 3px 20px", fontSize: "12px" }}>
                                                            Comment Ratio: {(file.metrics.comment_ratio * 100).toFixed(1)}% | Max Indent Depth: {file.metrics.max_indentation_depth}
                                                        </p>
                                                        {file.metrics.long_function_count > 0 && (
                                                            <p style={{ margin: "3px 0 3px 20px", fontSize: "12px", color: "#ff6b6b" }}>
                                                                Long Functions: {file.metrics.long_function_count}
                                                            </p>
                                                        )}
                                                    </div>

                                                    {/* Debt Signals */}
                                                    {file.debt_signal_count > 0 && (
                                                        <div style={{ marginBottom: "10px", fontSize: "13px" }}>
                                                            <p style={{ margin: "5px 0", color: "#ff9800" }}><strong>Debt Signals:</strong></p>
                                                            {file.debt_signals.map((signal, sidx) => (
                                                                <p key={sidx} style={{ margin: "3px 0 3px 20px", fontSize: "12px", color: "#ffb74d" }}>
                                                                    Line {signal.line_number}: [{signal.pattern}] {signal.line_snippet}
                                                                </p>
                                                            ))}
                                                        </div>
                                                    )}

                                                    <p style={{ margin: "5px 0", fontSize: "12px", color: "#8f9a79" }}>
                                                        Category Hint: <span style={{ color: "#72ea1e" }}>{file.debt_category_hint}</span>
                                                    </p>
                                                </div>
                                            )}
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* ============== BEDROCK AI ANALYSIS RESULTS ============== */}
                        {scanResult.stages && scanResult.stages.score && (
                            <>
                                {/* Health Score Card */}
                                <div style={{
                                    background: "rgba(114, 234, 30, 0.1)",
                                    border: "2px solid #72ea1e",
                                    borderRadius: "8px",
                                    padding: "30px",
                                    marginBottom: "30px",
                                    textAlign: "center"
                                }}>
                                    <h2 style={{ color: "#72ea1e", marginTop: 0 }}>HEALTH SCORE</h2>
                                    <div style={{
                                        fontSize: "72px",
                                        fontWeight: "bold",
                                        color: scanResult.stages.score.health_score >= 70 ? "#72ea1e" : scanResult.stages.score.health_score >= 40 ? "#ffb74d" : "#ff6b6b",
                                        margin: "20px 0"
                                    }}>
                                        {scanResult.stages.score.health_score}/100
                                    </div>
                                    <p style={{ color: "#d2ddb8", fontSize: "16px", margin: "15px 0" }}>
                                        {scanResult.stages.score.health_score >= 70 ? "[GOOD] Good overall health" : scanResult.stages.score.health_score >= 40 ? "[WARN] Needs attention" : "[CRITICAL] Critical issues detected"}
                                    </p>
                                </div>

                                {/* Cost Tracking & Service Alternatives */}
                                {scanResult.stages.analyze.cost_tracker && (
                                    <div style={{
                                        background: "rgba(76, 175, 80, 0.05)",
                                        border: "1px solid #4caf50",
                                        borderRadius: "8px",
                                        padding: "20px",
                                        marginBottom: "30px"
                                    }}>
                                        <h3 style={{ color: "#4caf50", marginTop: 0 }}>Analysis Metrics</h3>
                                        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "20px", marginBottom: "20px" }}>
                                            <div>
                                                <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "14px" }}>API Calls</p>
                                                <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>{scanResult.stages.analyze.cost_tracker.api_calls}</p>
                                            </div>
                                            <div>
                                                <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "14px" }}>Tokens Used</p>
                                                <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>{(scanResult.stages.analyze.cost_tracker.input_tokens + scanResult.stages.analyze.cost_tracker.output_tokens).toLocaleString()}</p>
                                            </div>
                                            <div>
                                                <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "14px" }}>Estimated Cost</p>
                                                <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>${scanResult.stages.analyze.cost_tracker.estimated_cost.toFixed(4)}</p>
                                            </div>
                                        </div>
                                        
                                        <div style={{ borderTop: "1px solid #4caf50", paddingTop: "15px" }}>
                                            <p style={{ margin: "0 0 15px 0", color: "#a1d96a", fontSize: "12px", fontWeight: "bold" }}>Alternative Services Comparison</p>
                                            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: "15px" }}>
                                                <div style={{ border: "1px solid #4caf50", borderRadius: "4px", padding: "12px", background: "rgba(76, 175, 80, 0.02)" }}>
                                                    <p style={{ margin: "0 0 8px 0", color: "#d2ddb8", fontWeight: "bold", fontSize: "13px" }}>Bedrock (Current)</p>
                                                    <p style={{ margin: "0", color: "#9ccc65", fontSize: "12px" }}>${scanResult.stages.analyze.cost_tracker.estimated_cost.toFixed(4)} per analysis</p>
                                                </div>
                                                <div style={{ border: "1px solid #ffc107", borderRadius: "4px", padding: "12px", background: "rgba(255, 193, 7, 0.02)" }}>
                                                    <p style={{ margin: "0 0 8px 0", color: "#d2ddb8", fontWeight: "bold", fontSize: "13px" }}>SonarQube</p>
                                                    <p style={{ margin: "0", color: "#ffc107", fontSize: "12px" }}>Free (community)</p>
                                                </div>
                                                <div style={{ border: "1px solid #2196f3", borderRadius: "4px", padding: "12px", background: "rgba(33, 150, 243, 0.02)" }}>
                                                    <p style={{ margin: "0 0 8px 0", color: "#d2ddb8", fontWeight: "bold", fontSize: "13px" }}>GitHub CodeQL</p>
                                                    <p style={{ margin: "0", color: "#64b5f6", fontSize: "12px" }}>Free (open source)</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                )}

                                {/* Architecture Archetype & Risk Radar */}
                                {scanResult.stages.score.archetype && (
                                    <div style={{
                                        background: "rgba(114, 234, 30, 0.05)",
                                        border: "1px solid #72ea1e",
                                        borderRadius: "8px",
                                        padding: "20px",
                                        marginBottom: "30px"
                                    }}>
                                        <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Repository Archetype</h3>
                                        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px" }}>
                                            <div>
                                                <p style={{ margin: "0 0 10px 0", color: "#a1d96a", fontWeight: "bold" }}>Type: {scanResult.stages.score.archetype}</p>
                                                <p style={{ margin: "0", color: "#d2ddb8", fontSize: "14px", lineHeight: "1.6" }}>
                                                    {scanResult.stages.score.archetype_description}
                                                </p>
                                            </div>
                                            <div>
                                                <p style={{ margin: "0 0 10px 0", color: "#a1d96a", fontWeight: "bold" }}>Risk Radar</p>
                                                {scanResult.stages.score.risk_radar && (
                                                    <div style={{ fontSize: "13px", fontFamily: "monospace" }}>
                                                        {Object.entries(scanResult.stages.score.risk_radar).map(([key, value]) => (
                                                            <div key={key} style={{ marginBottom: "8px" }}>
                                                                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "4px" }}>
                                                                    <span style={{ color: "#d2ddb8", textTransform: "capitalize" }}>{key}:</span>
                                                                    <span style={{ color: "#72ea1e", fontWeight: "bold" }}>{value}%</span>
                                                                </div>
                                                                <div style={{
                                                                    background: "#333",
                                                                    borderRadius: "4px",
                                                                    height: "6px",
                                                                    overflow: "hidden"
                                                                }}>
                                                                    <div style={{
                                                                        background: value >= 70 ? "#ff6b6b" : value >= 40 ? "#ffb74d" : "#72ea1e",
                                                                        height: "100%",
                                                                        width: `${value}%`,
                                                                        transition: "width 0.3s"
                                                                    }} />
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    </div>
                                )}

                                {/* Top 5 Recommended Actions */}
                                {scanResult.stages.score.top_5_actions && scanResult.stages.score.top_5_actions.length > 0 && (
                                    <div style={{
                                        background: "rgba(114, 234, 30, 0.05)",
                                        border: "1px solid #72ea1e",
                                        borderRadius: "8px",
                                        padding: "20px",
                                        marginBottom: "30px"
                                    }}>
                                        <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Top 5 Priority Actions</h3>
                                        {scanResult.stages.score.top_5_actions.map((action, idx) => {
                                            const severityColor = {
                                                'CRITICAL': '#ff6b6b',
                                                'HIGH': '#ffb74d',
                                                'MEDIUM': '#ffd54f',
                                                'LOW': '#72ea1e'
                                            }[action.severity] || '#d2ddb8';

                                            return (
                                                <div key={idx} style={{
                                                    background: "rgba(0,0,0,0.3)",
                                                    border: `1px solid ${severityColor}`,
                                                    borderRadius: "6px",
                                                    padding: "15px",
                                                    marginBottom: "15px"
                                                }}>
                                                    <div style={{ display: "flex", gap: "15px", marginBottom: "10px" }}>
                                                        <div style={{
                                                            background: severityColor,
                                                            color: "#000",
                                                            padding: "4px 10px",
                                                            borderRadius: "4px",
                                                            fontWeight: "bold",
                                                            fontSize: "12px",
                                                            minWidth: "80px",
                                                            textAlign: "center"
                                                        }}>
                                                            #{action.rank} {action.severity}
                                                        </div>
                                                        <span style={{ color: "#72ea1e", fontWeight: "bold" }}>{action.type}</span>
                                                        <span style={{ color: "#8f9a79", marginLeft: "auto" }}>{action.estimated_minutes} min</span>
                                                    </div>
                                                    <p style={{ margin: "8px 0", color: "#d2ddb8", fontSize: "14px" }}>
                                                        <strong>File:</strong> {action.file}
                                                    </p>
                                                    <p style={{ margin: "8px 0", color: "#d2ddb8", fontSize: "14px", lineHeight: "1.5" }}>
                                                        {action.explanation}
                                                    </p>
                                                    <p style={{ margin: "8px 0", color: "#a1d96a", fontSize: "13px" }}>
                                                        <strong>Fix:</strong> {action.fix}
                                                    </p>
                                                    {action.remediated_code && (
                                                        <pre style={{
                                                            background: "#000",
                                                            padding: "10px",
                                                            borderRadius: "4px",
                                                            overflow: "auto",
                                                            fontSize: "11px",
                                                            color: "#72ea1e",
                                                            margin: "8px 0"
                                                        }}>
{action.remediated_code}
                                                        </pre>
                                                    )}
                                                    <p style={{ margin: "8px 0", color: "#ffb74d", fontSize: "12px" }}>
                                                        💼 Business Impact: {action.business_impact}
                                                    </p>
                                                </div>
                                            );
                                        })}
                                    </div>
                                )}

                                {/* Security Findings */}
                                {scanResult.stages.analyze && scanResult.stages.analyze.security_findings && scanResult.stages.analyze.security_findings.length > 0 && (
                                    <div style={{
                                        background: "rgba(114, 234, 30, 0.05)",
                                        border: "1px solid #ff6b6b",
                                        borderRadius: "8px",
                                        padding: "20px",
                                        marginBottom: "30px"
                                    }}>
                                        <h3 style={{ color: "#ff6b6b", marginTop: 0 }}>Security Findings ({scanResult.stages.analyze.security_findings.length})</h3>
                                        {scanResult.stages.analyze.security_findings.map((finding, idx) => {
                                            const severityColor = {
                                                'CRITICAL': '#ff6b6b',
                                                'HIGH': '#ff9100',
                                                'MEDIUM': '#ffb74d',
                                                'LOW': '#ffd54f'
                                            }[finding.severity] || '#d2ddb8';

                                            return (
                                                <div key={idx} style={{
                                                    background: "rgba(0,0,0,0.2)",
                                                    border: `1px solid ${severityColor}`,
                                                    borderRadius: "6px",
                                                    padding: "12px",
                                                    marginBottom: "12px"
                                                }}>
                                                    <div style={{ display: "flex", gap: "10px", alignItems: "center", marginBottom: "8px" }}>
                                                        <span style={{
                                                            background: severityColor,
                                                            color: "#000",
                                                            padding: "2px 8px",
                                                            borderRadius: "3px",
                                                            fontSize: "11px",
                                                            fontWeight: "bold"
                                                        }}>
                                                            {finding.severity}
                                                        </span>
                                                        <span style={{ color: "#ff9100", fontWeight: "bold", fontSize: "13px" }}>{finding.type}</span>
                                                        <span style={{ color: "#8f9a79", fontSize: "12px", marginLeft: "auto" }}>{finding.file}:{finding.line}</span>
                                                    </div>
                                                    <p style={{ margin: "6px 0", color: "#d2ddb8", fontSize: "13px" }}>{finding.explanation}</p>
                                                    {finding.fix && <p style={{ margin: "6px 0", color: "#a1d96a", fontSize: "12px" }}><strong>Fix:</strong> {finding.fix}</p>}
                                                </div>
                                            );
                                        })}
                                    </div>
                                )}

                                {/* Debt Findings */}
                                {scanResult.stages.analyze && scanResult.stages.analyze.debt_findings && scanResult.stages.analyze.debt_findings.length > 0 && (
                                    <div style={{
                                        background: "rgba(114, 234, 30, 0.05)",
                                        border: "1px solid #ffb74d",
                                        borderRadius: "8px",
                                        padding: "20px",
                                        marginBottom: "30px"
                                    }}>
                                        <h3 style={{ color: "#ffb74d", marginTop: 0 }}>Technical Debt ({scanResult.stages.analyze.debt_findings.length})</h3>
                                        {scanResult.stages.analyze.debt_findings.map((finding, idx) => {
                                            const severityColor = {
                                                'CRITICAL': '#ff6b6b',
                                                'HIGH': '#ff9100',
                                                'MEDIUM': '#ffb74d',
                                                'LOW': '#ffd54f'
                                            }[finding.severity] || '#d2ddb8';

                                            return (
                                                <div key={idx} style={{
                                                    background: "rgba(0,0,0,0.2)",
                                                    border: `1px solid ${severityColor}`,
                                                    borderRadius: "6px",
                                                    padding: "12px",
                                                    marginBottom: "12px"
                                                }}>
                                                    <div style={{ display: "flex", gap: "10px", alignItems: "center", marginBottom: "8px" }}>
                                                        <span style={{
                                                            background: severityColor,
                                                            color: "#000",
                                                            padding: "2px 8px",
                                                            borderRadius: "3px",
                                                            fontSize: "11px",
                                                            fontWeight: "bold"
                                                        }}>
                                                            {finding.severity}
                                                        </span>
                                                        <span style={{ color: "#ffb74d", fontWeight: "bold", fontSize: "13px" }}>{finding.type}</span>
                                                        <span style={{ color: "#8f9a79", fontSize: "12px", marginLeft: "auto" }}>{finding.file}</span>
                                                    </div>
                                                    <p style={{ margin: "6px 0", color: "#d2ddb8", fontSize: "13px" }}>{finding.explanation}</p>
                                                    {finding.fix && <p style={{ margin: "6px 0", color: "#a1d96a", fontSize: "12px" }}><strong>Fix:</strong> {finding.fix}</p>}
                                                </div>
                                            );
                                        })}
                                    </div>
                                )}
                            </>
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
                                fontWeight: "bold",
                                marginTop: "20px"
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
