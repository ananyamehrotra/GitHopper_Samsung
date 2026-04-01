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

                        {/* Full JSON Response */}
                        <div style={{
                            background: "rgba(114, 234, 30, 0.05)",
                            border: "1px solid #72ea1e",
                            borderRadius: "8px",
                            padding: "20px",
                            marginBottom: "30px"
                        }}>
                            <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Full JSON Response</h3>
                            <pre style={{
                                background: "#000",
                                padding: "15px",
                                borderRadius: "4px",
                                overflow: "auto",
                                fontSize: "12px",
                                color: "#d9ffb8",
                                maxHeight: "400px"
                            }}>
                                {JSON.stringify(scanResult, null, 2)}
                            </pre>
                        </div>

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
                            [BACK] Back to Dashboard
                        </button>
                    </div>
                </section>
            </div>
        </>
    );
}
