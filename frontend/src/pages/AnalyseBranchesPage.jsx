import React, { useState, useEffect, useRef, useCallback } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { jsPDF } from "jspdf";
import autoTable from "jspdf-autotable";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import "./DashboardPage.css";
import "./AnalyseBranchesPage.css";

/* ══════════════════════════════════════════════════════════
   STYLE TOKENS (moved above component to fix reference-before-declaration)
══════════════════════════════════════════════════════════ */

const CARD = {
  background: "#020c02",
  border: "1px solid #142014",
  borderRadius: "6px",
  padding: "22px",
  position: "relative",
};

const SEC_H = {
  margin: "0 0 18px",
  fontFamily: "'JetBrains Mono',monospace",
  fontSize: "12px",
  fontWeight: 800,
  letterSpacing: "2px",
  textTransform: "uppercase",
  color: "#b0d880",
};

const BTN = {
  padding: "10px 26px",
  background: "#72ea1e",
  color: "#000",
  border: "1px solid #72ea1e",
  borderRadius: "3px",
  cursor: "pointer",
  fontSize: "11px",
  fontWeight: 800,
  fontFamily: "'JetBrains Mono',monospace",
  letterSpacing: "1.5px",
  textTransform: "lowercase",
  transition: "all 0.2s ease",
};

/* ══════════════════════════════════════════════════════════
   GLOBAL CSS INJECTION
══════════════════════════════════════════════════════════ */

const CSS = `
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;0,800;0,900;1,400&display=swap');

  @keyframes lineGrow {
    from { transform: scaleX(0); }
    to   { transform: scaleX(1); }
  }
  @keyframes rowIn {
    from { opacity: 0; transform: translateX(-6px); }
    to   { opacity: 1; transform: translateX(0); }
  }
  @keyframes svgRipple {
    0%   { r: 8;  opacity: 0.55; }
    100% { r: 20; opacity: 0; }
  }
  @keyframes pulse {
    0%, 100% { opacity: 1;   transform: scale(1); }
    50%       { opacity: 0.4; transform: scale(1.12); }
  }
  .abp-cur {
    display: inline-block;
    animation: abpBlink 0.65s step-end infinite;
    margin-left: 1px;
  }
  @keyframes abpBlink {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0; }
  }

  [data-theme="dark"] {
    --color-text: #ffffff;
    --color-bg: #020c02;
    --color-border: #0a180a;
    --scrollbar-thumb: #142014;
  }

  [data-theme="light"] {
    --color-text: #020c02;
    --color-bg: #f8f8f8;
    --color-border: #d8d8d8;
    --scrollbar-thumb: #b0b0b0;
  }

  html, body {
    width: 100%;
    overflow-x: hidden;
  }

  img, video, iframe {
    max-width: 100%;
    height: auto;
    display: block;
  }

  @media (max-width: 768px) {
    button, a, [role="button"] {
      min-height: 44px;
      min-width: 44px;
      padding: clamp(8px, 2vw, 12px) clamp(12px, 3vw, 16px);
    }
  }

  * { cursor: default; }

  button, a, [role="button"], [style*="cursor: pointer"] {
    cursor: pointer;
    position: relative;
  }

  button:hover, a:hover, [role="button"]:hover {
    transition: all 0.25s ease;
  }

  body.pdf-downloading * {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
    transition: none !important;
  }

  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: var(--scrollbar-thumb, #142014); border-radius: 2px; }
`;

/* Inject CSS once */
if (typeof document !== "undefined" && !document.getElementById("abp-styles")) {
  const style = document.createElement("style");
  style.id = "abp-styles";
  style.textContent = CSS;
  document.head.appendChild(style);
}

/* ══════════════════════════════════════════════════════════
   HOOKS & UTILITIES
══════════════════════════════════════════════════════════ */

function useTypewriter(text = "", speed = 22, startDelay = 0) {
  const [displayed, setDisplayed] = useState("");
  const [done, setDone] = useState(false);
  useEffect(() => {
    setDisplayed("");
    setDone(false);
    if (!text) {
      setDone(true);
      return;
    }
    let i = 0;
    const t = setTimeout(() => {
      const id = setInterval(() => {
        i++;
        setDisplayed(text.slice(0, i));
        if (i >= text.length) {
          clearInterval(id);
          setDone(true);
        }
      }, speed);
      return () => clearInterval(id);
    }, startDelay);
    return () => clearTimeout(t);
  }, [text, speed, startDelay]);
  return { displayed, done };
}

function useCountUp(target, delay = 0, duration = 1100) {
  const [val, setVal] = useState(0);
  useEffect(() => {
    let start = null;
    const t = setTimeout(() => {
      const step = (ts) => {
        if (!start) start = ts;
        const p = Math.min((ts - start) / duration, 1);
        const ease = 1 - Math.pow(1 - p, 3);
        setVal(Math.floor(ease * target));
        if (p < 1) requestAnimationFrame(step);
        else setVal(target);
      };
      requestAnimationFrame(step);
    }, delay);
    return () => clearTimeout(t);
  }, [target, delay, duration]);
  return val;
}

/* ══════════════════════════════════════════════════════════
   PIPELINE SVG
══════════════════════════════════════════════════════════ */

function PipelineSVG({ containerRef, nodeRefs }) {
  const [totalH, setTotalH] = useState(0);
  const [nodeYs, setNodeYs] = useState([]);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const measure = () => {
      const c = containerRef.current;
      if (!c) return;
      setTotalH(c.offsetHeight);
      const ys = nodeRefs.current
        .map((r) => (r ? r.offsetTop + 18 : null))
        .filter((y) => y !== null);
      setNodeYs(ys);
    };
    measure();
    window.addEventListener("resize", measure);
    const tid = setTimeout(measure, 800);
    return () => {
      window.removeEventListener("resize", measure);
      clearTimeout(tid);
    };
  }, []);

  useEffect(() => {
    const onScroll = () => {
      const c = containerRef.current;
      if (!c) return;
      const rect = c.getBoundingClientRect();
      const revealed = window.innerHeight - rect.top;
      setProgress(
        Math.max(0, Math.min(1, revealed / (rect.height + window.innerHeight * 0.25)))
      );
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  if (!nodeYs.length || !totalH) return null;

  const x = 7;
  const first = nodeYs[0];
  const last = nodeYs[nodeYs.length - 1];
  const drawnTo = first + progress * (last - first);

  return (
    <svg
      aria-hidden="true"
      style={{
        position: "absolute",
        left: 0,
        top: 0,
        width: "14px",
        height: `${totalH}px`,
        pointerEvents: "none",
        overflow: "visible",
        zIndex: 1,
      }}
    >
      <line x1={x} y1={first} x2={x} y2={last} stroke="#0f200a" strokeWidth="1.5" />
      <line
        x1={x}
        y1={first}
        x2={x}
        y2={Math.min(drawnTo, last)}
        stroke="#72ea1e"
        strokeWidth="1.5"
        style={{ filter: "drop-shadow(0 0 3px #72ea1e88)" }}
      />
      {nodeYs.map((y, i) => {
        const lit = drawnTo >= y - 4;
        return (
          <g key={i}>
            {lit && (
              <circle
                cx={x}
                cy={y}
                r="10"
                fill="none"
                stroke="#72ea1e33"
                style={{ animation: "svgRipple 1.2s ease-out forwards" }}
              />
            )}
            <circle
              cx={x}
              cy={y}
              r="4.5"
              fill={lit ? "#72ea1e" : "#050a05"}
              stroke={lit ? "#72ea1e" : "#1a2e0a"}
              strokeWidth="1.5"
              style={{
                filter: lit ? "drop-shadow(0 0 6px #72ea1e)" : "none",
                transition: "fill 0.45s ease, filter 0.45s ease",
              }}
            />
          </g>
        );
      })}
    </svg>
  );
}

/* ══════════════════════════════════════════════════════════
   SEVERITY
══════════════════════════════════════════════════════════ */

const SEV = {
  CRITICAL: { bg: "rgba(255,50,50,0.12)", border: "#ff3232", text: "#ff6464", dot: "#ff3232" },
  HIGH: { bg: "rgba(255,140,0,0.12)", border: "#ff8c00", text: "#ffaa44", dot: "#ff8c00" },
  MEDIUM: { bg: "rgba(220,190,0,0.1)", border: "#c8b400", text: "#e8d040", dot: "#c8b400" },
  LOW: { bg: "rgba(60,180,60,0.1)", border: "#3cb43c", text: "#60d060", dot: "#3cb43c" },
};

function Badge({ sev }) {
  const c = SEV[sev] || SEV.LOW;
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "6px",
        padding: "4px 12px",
        borderRadius: "3px",
        fontSize: "11px",
        fontWeight: 900,
        letterSpacing: "2px",
        fontFamily: "'JetBrains Mono',monospace",
        background: c.bg,
        border: `1px solid ${c.border}`,
        color: c.text,
        flexShrink: 0,
      }}
    >
      <span
        style={{
          width: "6px",
          height: "6px",
          borderRadius: "50%",
          background: c.dot,
          display: "inline-block",
          boxShadow: `0 0 6px ${c.dot}`,
        }}
      />
      {sev}
    </span>
  );
}

/* ══════════════════════════════════════════════════════════
   FIELD LABEL + CURSOR
══════════════════════════════════════════════════════════ */

function FL({ color, children, mb = "8px" }) {
  return (
    <p
      style={{
        margin: `0 0 ${mb}`,
        fontFamily: "'JetBrains Mono',monospace",
        fontSize: "11px",
        letterSpacing: "2.5px",
        textTransform: "uppercase",
        color,
        fontWeight: 900,
      }}
    >
      {children}
    </p>
  );
}

function Cur({ color = "#72ea1e" }) {
  return <span className="abp-cur" style={{ color }}>▌</span>;
}

/* ══════════════════════════════════════════════════════════
   STAT TILE
══════════════════════════════════════════════════════════ */

function StatTile({ label, value, accent, delay }) {
  const n = useCountUp(value, delay);
  const [hov, setHov] = useState(false);
  const { isDark } = useTheme();
  return (
    <div
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{
        padding: "clamp(16px, 4vw, 24px) clamp(14px, 3vw, 20px)",
        border: `1px solid ${hov ? accent + "66" : accent + "33"}`,
        borderRadius: "6px",
        background: hov ? accent + "06" : "transparent",
        transition: "all 0.25s ease",
        cursor: "default",
      }}
    >
      <p
        style={{
          margin: "0 0 clamp(8px, 2vw, 12px)",
          fontFamily: "'JetBrains Mono',monospace",
          fontSize: "clamp(8px, 1.5vw, 10px)",
          letterSpacing: "1px",
          textTransform: "uppercase",
          fontWeight: 700,
          color: accent,
        }}
      >
        {label}
      </p>
      <p
        style={{
          margin: 0,
          fontFamily: "'JetBrains Mono',monospace",
          fontSize: "clamp(32px, 8vw, 48px)",
          fontWeight: 700,
          lineHeight: 1,
          color: isDark ? "#ffffff" : "#020c02",
          transition: "color 0.22s",
        }}
      >
        {n}
      </p>
    </div>
  );
}

/* ══════════════════════════════════════════════════════════
   SECTION WRAPPER
══════════════════════════════════════════════════════════ */

const PSection = React.forwardRef(function PSection({ children, label, isLast = false }, ref) {
  const inner = useRef(null);
  const [vis, setVis] = useState(false);

  useEffect(() => {
    const el = inner.current;
    if (!el) return;
    const obs = new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting) {
          setVis(true);
          obs.disconnect();
        }
      },
      { rootMargin: "-5% 0px -5% 0px" }
    );
    obs.observe(el);
    return () => obs.disconnect();
  }, []);

  return (
    <div
      ref={(el) => {
        inner.current = el;
        if (typeof ref === "function") ref(el);
        else if (ref) ref.current = el;
      }}
      style={{
        position: "relative",
        marginBottom: isLast ? 0 : "52px",
        opacity: vis ? 1 : 0,
        transform: vis ? "translateX(0)" : "translateX(-10px)",
        transition: "opacity 0.5s ease, transform 0.5s ease",
      }}
    >
      <span
        style={{
          position: "absolute",
          left: "-120px",
          top: "16px",
          fontFamily: "'JetBrains Mono',monospace",
          fontSize: "8px",
          letterSpacing: "1.5px",
          color: vis ? "#2a4020" : "#111",
          textTransform: "uppercase",
          textAlign: "right",
          width: "108px",
          display: "block",
          userSelect: "none",
          transition: "color 0.6s ease",
        }}
      >
        {label}
      </span>
      {children}
    </div>
  );
});

/* tiny inline count (avoids hooks-in-loops) */
function InlineCount({ target, delay }) {
  const v = useCountUp(target, delay);
  return <>{v}</>;
}

/* dim chip */
function Chip({ children }) {
  return (
    <span
      style={{
        marginLeft: "8px",
        fontFamily: "'JetBrains Mono',monospace",
        fontSize: "11px",
        fontWeight: 500,
        color: "#243a14",
        letterSpacing: "1.2px",
      }}
    >
      [ {children} ]
    </span>
  );
}

/* ══════════════════════════════════════════════════════════
   DETAILED ANALYSIS SECTION (extracted to its own component
   so hooks are called at the top level — fixes Rules of Hooks)
══════════════════════════════════════════════════════════ */

function DetailedAnalysisSection({ vulnerabilities, expandedVulnerability, setExpandedVulnerability, nodeRef }) {
  const { isDark } = useTheme(); // ✅ hook at top level of a real component

  const textColor = isDark ? "#ffffff" : "#020c02";
  const secondaryText = isDark ? "#cccccc" : "#142014";
  const dimText = isDark ? "#888888" : "#243a14";
  const borderColor = isDark ? "#0a180a" : "#d0d0d0";
  const hoverBg = isDark ? "rgba(114,234,30,0.05)" : "rgba(114,234,30,0.08)";
  const cardBg = isDark ? "#010801" : "#f5f5f5";
  const cardBorder = isDark ? "#0a180a" : "#e0e0e0";

  /* Deduplicate vulnerabilities by type */
  const uniqueVulns = [];
  const seenTypes = new Set();
  vulnerabilities.forEach((v) => {
    if (!seenTypes.has(v.type)) {
      seenTypes.add(v.type);
      uniqueVulns.push(v);
    }
  });

  return (
    <PSection ref={nodeRef} label="analysis">
      <div style={{ ...CARD, padding: "24px", background: cardBg, borderColor: cardBorder }}>
        <p style={SEC_H}>
          <span style={{ color: "#ff9800" }}>◈</span> Detailed Analysis
          <Chip>{uniqueVulns.length} unique types</Chip>
        </p>

        <div style={{ display: "flex", flexDirection: "column", gap: "16px", marginTop: "20px" }}>
          {uniqueVulns.map((vuln, idx) => {
            const isUnique = !["DEBUG_LOGGING", "INFO_LOGGING", "WARN_LOGGING"].includes(vuln.type);
            const count = vulnerabilities.filter((v) => v.type === vuln.type).length;
            const accentColor = isUnique ? "#ff9800" : "#72ea1e";

            return (
              <div
                key={idx}
                onClick={() =>
                  setExpandedVulnerability(expandedVulnerability === idx ? null : idx)
                }
                style={{
                  display: "flex",
                  alignItems: "flex-start",
                  gap: "14px",
                  padding: "16px 18px",
                  cursor: "pointer",
                  userSelect: "none",
                  background: expandedVulnerability === idx ? hoverBg : "transparent",
                  border: `1px solid ${expandedVulnerability === idx ? borderColor : "transparent"}`,
                  borderRadius: "6px",
                  transition: "all 0.25s ease",
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.background = hoverBg;
                  e.currentTarget.style.border = `1px solid ${borderColor}`;
                }}
                onMouseLeave={(e) => {
                  if (expandedVulnerability !== idx) {
                    e.currentTarget.style.background = "transparent";
                    e.currentTarget.style.border = "1px solid transparent";
                  }
                }}
              >
                <span style={{ color: accentColor, fontSize: "18px", lineHeight: 1, flexShrink: 0, marginTop: "2px" }}>
                  •
                </span>

                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "8px" }}>
                    <span
                      style={{
                        fontFamily: "'JetBrains Mono',monospace",
                        fontSize: isUnique ? "14px" : "13px",
                        fontWeight: 800,
                        color: accentColor,
                        textShadow: isUnique ? `0 0 10px ${accentColor}30` : "none",
                        letterSpacing: "1px",
                        textTransform: "uppercase",
                      }}
                    >
                      {isUnique && "✦ "}{vuln.type}
                    </span>
                    {count > 1 && (
                      <span
                        style={{
                          fontFamily: "'JetBrains Mono',monospace",
                          fontSize: "11px",
                          color: isDark ? "#72ea1e" : "#142014",
                          background: isDark ? "rgba(114,234,30,0.08)" : "rgba(114,234,30,0.15)",
                          padding: "2px 8px",
                          borderRadius: "3px",
                          fontWeight: 700,
                          letterSpacing: "0.5px",
                        }}
                      >
                        {count}x
                      </span>
                    )}
                  </div>

                  <p
                    style={{
                      margin: "0 0 10px",
                      fontFamily: "'JetBrains Mono',monospace",
                      fontSize: "11px",
                      color: dimText,
                      letterSpacing: "0.5px",
                    }}
                  >
                    {vuln.file}
                  </p>

                  <Badge sev={vuln.severity} />

                  {expandedVulnerability === idx && (
                    <div style={{ marginTop: "16px", paddingTop: "16px", borderTop: `1px solid ${borderColor}` }}>
                      {vuln.explanation && (
                        <div style={{ marginBottom: "14px" }}>
                          <FL color="#72ea1e">what is this</FL>
                          <p
                            style={{
                              margin: 0,
                              fontFamily: "'JetBrains Mono',monospace",
                              fontSize: "13px",
                              color: secondaryText,
                              lineHeight: 1.8,
                            }}
                          >
                            {vuln.explanation}
                          </p>
                        </div>
                      )}

                      {vuln.business_impact && (
                        <div style={{ marginBottom: "14px", borderLeft: "2px solid #ff606033", paddingLeft: "14px" }}>
                          <FL color="#ff8080">why it matters</FL>
                          <p
                            style={{
                              margin: 0,
                              fontFamily: "'JetBrains Mono',monospace",
                              fontSize: "13px",
                              color: secondaryText,
                              lineHeight: 1.8,
                            }}
                          >
                            {vuln.business_impact}
                          </p>
                        </div>
                      )}

                      {vuln.remediation && (
                        <div>
                          <FL color="#60d060">how to fix</FL>
                          <pre
                            style={{
                              margin: 0,
                              padding: "12px 14px",
                              background: cardBg,
                              border: `1px solid ${cardBorder}`,
                              borderRadius: "4px",
                              fontFamily: "'JetBrains Mono',monospace",
                              fontSize: "12px",
                              color: isDark ? "#72ea1e" : "#142014",
                              lineHeight: 1.8,
                              whiteSpace: "pre-wrap",
                              wordBreak: "break-word",
                            }}
                          >
                            {vuln.remediation}
                          </pre>
                        </div>
                      )}
                    </div>
                  )}
                </div>

                <span
                  style={{
                    color: accentColor,
                    fontSize: "16px",
                    fontFamily: "'JetBrains Mono',monospace",
                    transition: "transform 0.3s",
                    transform: expandedVulnerability === idx ? "rotate(90deg)" : "rotate(0)",
                    flexShrink: 0,
                    marginTop: "2px",
                    cursor: "pointer",
                  }}
                >
                  ›
                </span>
              </div>
            );
          })}
        </div>
      </div>
    </PSection>
  );
}

/* ══════════════════════════════════════════════════════════
   MAIN PAGE
══════════════════════════════════════════════════════════ */

export function AnalyseBranchesPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const { isDark } = useTheme();

  const scanResult = location.state?.scanResult || {};
  const repoUrl = location.state?.repoUrl;

  const [expandedVulnerability, setExpandedVulnerability] = useState(null);
  const [isDownloading, setIsDownloading] = useState(false);

  const handleDownloadPdf = async () => {
    setIsDownloading(true);

    try {
      const doc = new jsPDF();
      let y = 20;

      // Report Header
      doc.setFontSize(22);
      doc.setTextColor(34, 139, 34); // Green Theme
      doc.text("GitHopper Security & Debt Report", 14, y);
      
      y += 10;
      doc.setFontSize(11);
      doc.setTextColor(60, 60, 60);
      doc.text(`Repository: ${repoUrl || analyze.repo_url || "Unknown"}`, 14, y);
      y += 6;
      doc.text(`Branch: ${analyze.branch_name || "main"}`, 14, y);
      y += 6;
      doc.text(`Date Generated: ${new Date().toLocaleString()}`, 14, y);
      
      y += 14;

      // Executive Summary
      doc.setFontSize(16);
      doc.setTextColor(0, 0, 0);
      doc.text("Executive Summary", 14, y);
      y += 6;

      autoTable(doc, {
        startY: y,
        head: [["Metric", "Value"]],
        body: [
          ["Total Files Analyzed", (filesSummary.total || 0).toString()],
          ["Files with Issues", (filesSummary.withIssues || 0).toString()],
          ["Total Vulnerabilities", (filesSummary.totalVulnerabilities || 0).toString()],
        ],
        theme: "grid",
        headStyles: { fillColor: [40, 40, 40] },
        styles: { fontSize: 11, cellPadding: 4 },
      });

      y = doc.lastAutoTable.finalY + 15;

      // Detailed Findings
      doc.setFontSize(16);
      doc.setTextColor(0, 0, 0);
      doc.text("Detailed Analysis", 14, y);
      y += 6;

      if (vulnerabilities && vulnerabilities.length > 0) {
        vulnerabilities.forEach((vuln, idx) => {
          // Check if we need to add a new page before drawing
          if (y > 250) {
            doc.addPage();
            y = 20;
          }

          // Determine header color based on severity
          let headColor = [100, 100, 100];
          if (vuln.severity === "CRITICAL") headColor = [220, 53, 69];
          else if (vuln.severity === "HIGH") headColor = [253, 126, 20];
          else if (vuln.severity === "MEDIUM") headColor = [255, 193, 7];
          else if (vuln.severity === "LOW") headColor = [40, 167, 69];

          const tableBody = [
            ["Severity", vuln.severity || "N/A"],
            ["File", vuln.file || "N/A"],
          ];

          if (vuln.explanation) tableBody.push(["Explanation", vuln.explanation]);
          if (vuln.business_impact) tableBody.push(["Impact", vuln.business_impact]);
          if (vuln.remediation) tableBody.push(["Remediation", vuln.remediation]);

          autoTable(doc, {
            startY: y,
            head: [[`Finding #${idx + 1}: ${vuln.type}`, ""]],
            body: tableBody,
            theme: "grid",
            headStyles: { fillColor: headColor, fontSize: 12 },
            styles: { overflow: "linebreak", cellPadding: 4, fontSize: 10 },
            columnStyles: {
              0: { cellWidth: 35, fontStyle: "bold", textColor: [50, 50, 50] },
              1: { cellWidth: "auto" }
            }
          });

          y = doc.lastAutoTable.finalY + 10;
        });
      } else {
        doc.setFontSize(11);
        doc.setTextColor(40, 167, 69);
        doc.text("No vulnerabilities detected! Codebase is secure.", 14, y);
      }

      doc.save(`GitHopper_Analysis_${analyze?.branch_name || "report"}.pdf`);
    } catch (err) {
      console.error("PDF generation failed:", err);
    } finally {
      setIsDownloading(false);
    }
  };

  /* refs for pipeline */
  const pipelineRoot = useRef(null);
  const nodeRefs = useRef([]);
  const setNode = (i) => (el) => {
    nodeRefs.current[i] = el;
  };

  /* title typewriter */
  const { displayed: titleOut, done: titleDone } = useTypewriter("BEDROCK & ANALYSIS", 58, 220);

  /* ── THEME-AWARE STYLES ── */
  const THEME_CARD = {
    background: isDark ? "#020c02" : "#f8f8f8",
    border: isDark ? "1px solid #142014" : "1px solid #d8d8d8",
    borderRadius: "6px",
    padding: "22px",
    position: "relative",
  };

  const THEME_SEC_H = {
    margin: "0 0 18px",
    fontFamily: "'JetBrains Mono',monospace",
    fontSize: "12px",
    fontWeight: 800,
    letterSpacing: "2px",
    textTransform: "uppercase",
    color: isDark ? "#b0d880" : "#142014",
  };

  /* ── no results ── */
  if (Object.keys(scanResult).length === 0 && !location.state?.branchAnalysis) {
    return (
      <>
        <Plasma color="#72ea1e" speed={0.6} direction="forward" scale={1.1} opacity={0.1} mouseInteractive />
        <ThemeToggle />
        <UserProfile />
        <div className="page-shell" style={{ padding: "40px", textAlign: "center" }}>
          <h2 style={{ color: "#72ea1e", fontFamily: "'JetBrains Mono',monospace" }}>
            No scan results available
          </h2>
          <p style={{ color: "#3d5c22", fontFamily: "'JetBrains Mono',monospace", fontSize: "13px" }}>
            Go back to the dashboard and scan a repository first.
          </p>
          <button onClick={() => navigate("/dashboard")} style={BTN}>
            ← back
          </button>
        </div>
      </>
    );
  }

  /* ── data extraction ── */
  const analyze = location.state?.branchAnalysis || scanResult.branch_analysis || scanResult.stages?.analyze || {};
  const vulnerableFiles = []; // Old fallback logic not easily portable, we use vulnerabilities below.
  const vulnerabilities = analyze.findings || analyze.vulnerabilities || [];
  const billing = analyze.billing || {};
  
  // Calculate unique files with issues from findings
  const uniqueFilesWithIssues = new Set(
    vulnerabilities.map(v => v.file).filter(f => f)
  ).size;
  
  const filesSummary = {
    total: vulnerabilities.length || analyze.summary?.total_issues || analyze.total_vulnerabilities || 0,
    withIssues: uniqueFilesWithIssues,
    totalVulnerabilities: vulnerabilities.length || analyze.summary?.total_issues || analyze.total_vulnerabilities || 0,
  };

  /* node index counter */
  let nIdx = 0;
  const N = () => nIdx++;

  return (
    <>
      <Plasma color="#72ea1e" speed={0.6} direction="forward" scale={1.1} opacity={0.1} mouseInteractive={true} />
      <ThemeToggle />
      <UserProfile />

      <div
        className="page-shell"
        style={{
          padding: "clamp(20px, 5vw, 64px) clamp(16px, 4vw, 64px) clamp(60px, 20vh, 100px)",
          maxWidth: "clamp(320px, 100%, 1060px)",
          margin: "0 auto",
          width: "100%",
        }}
      >
        {/* ── TITLE ── */}
        <div style={{ marginBottom: "clamp(32px, 10vw, 64px)" }}>
          <p
            style={{
              margin: "0 0 clamp(6px, 2vw, 10px)",
              fontFamily: "'JetBrains Mono',monospace",
              fontSize: "clamp(8px, 1.5vw, 9px)",
              letterSpacing: "clamp(2px, 1vw, 4px)",
              color: isDark ? "#243a14" : "#72ea1e",
              textTransform: "uppercase",
            }}
          >
            security report
          </p>
          <h1
            style={{
              margin: 0,
              fontFamily: "'JetBrains Mono',monospace",
              fontSize: "clamp(20px, 6vw, 52px)",
              fontWeight: 900,
              letterSpacing: "clamp(1px, 1vw, 3px)",
              color: "#72ea1e",
              textShadow: "0 0 50px rgba(114,234,30,0.25)",
              lineHeight: 1.05,
              minHeight: "1.15em",
            }}
          >
            {titleOut}
            {!titleDone && <Cur />}
          </h1>
          <div
            style={{
              marginTop: "clamp(12px, 5vw, 20px)",
              height: "1px",
              background: "linear-gradient(90deg,#72ea1e,#72ea1e18,transparent)",
              animation: "lineGrow 1s ease 1.6s both",
              transformOrigin: "left",
            }}
          />
        </div>

        {/* ── NEW FEATURE BUTTONS ── */}
        <div style={{ marginBottom: "40px", display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "16px" }}>
          <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
            {[{ id:"/security-audit", label:"SECURITY AUDIT", stateKey:"securityAudit", dataKey:"security_audit" },
              { id:"/debt-report", label:"DEBT REPORT", stateKey:"debtReport", dataKey:"debt_report" },
              { id:"/health-score", label:"HEALTH SCORE", stateKey:"healthScore", dataKey:"health_score" }].map(b => {
              return (
              <button key={b.id} onClick={() => navigate(b.id, {
                state: { 
                  [b.stateKey]: scanResult?.[b.dataKey] || scanResult, 
                  scanResult: scanResult, 
                  repoUrl: repoUrl || localStorage.getItem("githopper_last_url") || "Recent Repository" 
                }
              })}
              style={{
                padding: "8px 14px",
                borderRadius: "999px",
                border: "1px solid #72ea1e",
                background: "transparent",
                color: "#72ea1e",
                fontSize: "12px",
                fontWeight: "700",
                transition: "all 0.2s"
              }}
              onMouseEnter={e=>{e.currentTarget.style.background="#72ea1e"; e.currentTarget.style.color="#000"}}
              onMouseLeave={e=>{e.currentTarget.style.background="transparent"; e.currentTarget.style.color="#72ea1e"}}>
                <span style={{ 
                  display: "inline-block", width: "6px", height: "6px", borderRadius: "50%", background: "#72ea1e", marginRight: "8px", 
                  boxShadow: "0 0 5px #72ea1e" 
                }}></span>
                {b.label}
              </button>
            )})}
          </div>

          <button 
            onClick={handleDownloadPdf}
            disabled={isDownloading}
            style={{
              padding: "8px 20px",
              borderRadius: "4px",
              background: isDark ? "#020c02" : "#f8f8f8",
              border: "1px dashed #72ea1e",
              color: "#72ea1e",
              fontSize: "12px",
              fontWeight: "700",
              fontFamily: "'JetBrains Mono',monospace",
              cursor: isDownloading ? "wait" : "pointer",
              transition: "all 0.2s",
              opacity: isDownloading ? 0.7 : 1
            }}
            onMouseEnter={e=>{ if(!isDownloading) { e.currentTarget.style.background="#72ea1e"; e.currentTarget.style.color="#000"; } }}
            onMouseLeave={e=>{ if(!isDownloading) { e.currentTarget.style.background=isDark?"#020c02":"#f8f8f8"; e.currentTarget.style.color="#72ea1e"; } }}
          >
            {isDownloading ? "GENERATING PDF..." : "⬇ DOWNLOAD REPORT"}
          </button>
        </div>

        <div id="report-content" style={{ position: "relative", paddingBottom: "20px", paddingTop: "10px", margin: "-10px 0 0" }}>
        {/* ── PIPELINE ROOT ── */}
        <div ref={pipelineRoot} style={{ position: "relative", paddingLeft: "clamp(20px, 5vw, 40px)" }}>
          <PipelineSVG containerRef={pipelineRoot} nodeRefs={nodeRefs} />

          {/* SECTION: REPOSITORY */}
          <PSection ref={setNode(N())} label="repository">
            <div style={THEME_CARD}>
              <div style={{ display: "flex", flexDirection: "column", gap: "clamp(16px, 4vw, 24px)" }}>
                <div>
                  <p
                    style={{
                      margin: "0 0 clamp(6px, 1.5vw, 8px)",
                      fontFamily: "'JetBrains Mono',monospace",
                      fontSize: "clamp(8px, 1.5vw, 10px)",
                      letterSpacing: "1px",
                      textTransform: "uppercase",
                      color: "#72ea1e",
                      fontWeight: 700,
                    }}
                  >
                    URL
                  </p>
                  <p
                    style={{
                      margin: 0,
                      fontFamily: "'JetBrains Mono',monospace",
                      fontSize: "clamp(14px, 3vw, 18px)",
                      color: isDark ? "#ffffff" : "#020c02",
                      wordBreak: "break-all",
                      lineHeight: 1.5,
                      fontWeight: 400,
                    }}
                  >
                    {repoUrl || analyze.repo_url}
                  </p>
                </div>
                <div>
                  <p
                    style={{
                      margin: "0 0 clamp(6px, 1.5vw, 8px)",
                      fontFamily: "'JetBrains Mono',monospace",
                      fontSize: "clamp(8px, 1.5vw, 10px)",
                      letterSpacing: "1px",
                      textTransform: "uppercase",
                      color: "#72ea1e",
                      fontWeight: 700,
                    }}
                  >
                    Branch
                  </p>
                  <p
                    style={{
                      margin: 0,
                      fontFamily: "'JetBrains Mono',monospace",
                      fontSize: "clamp(14px, 3vw, 18px)",
                      color: isDark ? "#ffffff" : "#020c02",
                      fontWeight: 400,
                    }}
                  >
                    {analyze.branch_name || "main"}
                  </p>
                </div>
              </div>
            </div>
          </PSection>

          {/* SECTION: METRICS */}
          <PSection ref={setNode(N())} label="metrics">
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fit,minmax(clamp(140px, 30vw, 175px),1fr))",
                gap: "clamp(8px, 2vw, 12px)",
              }}
            >
              <StatTile label="Total Files" value={filesSummary.total} accent="#72ea1e" delay={180} />
              <StatTile label="Files w/ Issues" value={filesSummary.withIssues} accent="#ff6060" delay={320} />
              <StatTile label="Vulnerabilities" value={filesSummary.totalVulnerabilities} accent="#ff9800" delay={460} />
            </div>
          </PSection>

          {/* SECTION: VULNERABLE FILES */}
          {vulnerableFiles.length > 0 && (
            <PSection ref={setNode(N())} label="vuln_files">
              <div style={THEME_CARD}>
                <p style={THEME_SEC_H}>
                  <span style={{ color: "#ff6060" }}>⚠</span> Vulnerable Files
                  <Chip>{vulnerableFiles.length}</Chip>
                </p>
                <div style={{ marginTop: "clamp(12px, 3vw, 16px)", display: "flex", flexDirection: "column", gap: "clamp(8px, 2vw, 12px)" }}>
                  {vulnerableFiles.map((file, i) => (
                    <div
                      key={i}
                      style={{
                        padding: "clamp(10px, 2vw, 14px) clamp(12px, 3vw, 16px)",
                        background: isDark ? "#010801" : "#f5f5f5",
                        border: isDark ? "1px solid #142014" : "1px solid #e8e8e8",
                        borderRadius: "5px",
                        animation: `rowIn 0.3s ease ${i * 45}ms both`,
                        transition: "all 0.25s ease",
                        cursor: "default",
                      }}
                      onMouseEnter={(e) => {
                        e.currentTarget.style.borderColor = isDark ? "#ff606055" : "#ff6060";
                        e.currentTarget.style.background = isDark ? "#180000" : "#fff0f0";
                      }}
                      onMouseLeave={(e) => {
                        e.currentTarget.style.borderColor = isDark ? "#142014" : "#e8e8e8";
                        e.currentTarget.style.background = isDark ? "#010801" : "#f5f5f5";
                      }}
                    >
                      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", gap: "12px" }}>
                        <div style={{ flex: 1, minWidth: 0 }}>
                          <p
                            style={{
                              margin: "0 0 4px",
                              fontFamily: "'JetBrains Mono',monospace",
                              fontSize: "13px",
                              fontWeight: 500,
                              color: isDark ? "#ffffff" : "#020c02",
                              wordBreak: "break-all",
                            }}
                          >
                            {file.file}
                          </p>
                          <p style={{ margin: 0, fontFamily: "'JetBrains Mono',monospace", fontSize: "10px", color: isDark ? "#888" : "#999" }}>
                            {file.type}
                          </p>
                        </div>
                        <span
                          style={{
                            fontFamily: "'JetBrains Mono',monospace",
                            fontSize: "10px",
                            fontWeight: 700,
                            padding: "4px 10px",
                            background: isDark ? "rgba(255,96,96,0.08)" : "rgba(255,96,96,0.12)",
                            color: isDark ? "#ff9090" : "#d84040",
                            borderRadius: "3px",
                            whiteSpace: "nowrap",
                            flexShrink: 0,
                          }}
                        >
                          {file.count} issues
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </PSection>
          )}

          {/* SECTION: DETAILED ANALYSIS — now a proper component, no hook-in-IIFE */}
          {vulnerabilities.length > 0 && (
            <DetailedAnalysisSection
              vulnerabilities={vulnerabilities}
              expandedVulnerability={expandedVulnerability}
              setExpandedVulnerability={setExpandedVulnerability}
              nodeRef={setNode(N())}
            />
          )}

          {/* SECTION: NO VULNS */}
          {vulnerabilities.length === 0 && (
            <PSection ref={setNode(N())} label="result">
              <div style={{ ...THEME_CARD, textAlign: "center", padding: "48px 24px" }}>
                <div style={{ fontSize: "34px", marginBottom: "12px", animation: "pulse 2.5s ease infinite" }}>✓</div>
                <p style={{ margin: "0 0 5px", fontFamily: "'JetBrains Mono',monospace", fontSize: "15px", fontWeight: 700, color: "#4caf50" }}>
                  No vulnerabilities detected
                </p>
                <p style={{ margin: 0, fontFamily: "'JetBrains Mono',monospace", fontSize: "10px", color: isDark ? "#243a14" : "#666" }}>
                  Code appears secure in this branch
                </p>
              </div>
            </PSection>
          )}

          {/* SECTION: BILLING */}
          {billing && (
            <PSection ref={setNode(N())} label="billing" isLast>
              <div style={THEME_CARD}>
                <p style={THEME_SEC_H}>
                  <span style={{ color: "#4caf50" }}>◉</span> Cost & Billing
                </p>

                <div
                  style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(auto-fit,minmax(155px,1fr))",
                    gap: "10px",
                    marginBottom: "14px",
                  }}
                >
                  {[
                    { label: "api_calls", raw: false, val: billing.calls_made || 0 },
                    {
                      label: "est_cost",
                      raw: true,
                      val: `$${(analyze.cost_tracker?.estimated_cost || 0).toFixed(4)}`,
                    },
                    {
                      label: "free_remaining",
                      raw: billing.free_calls_remaining < 0,
                      val: billing.free_calls_remaining >= 0 ? billing.free_calls_remaining : "N/A",
                    },
                  ].map(({ label, val, raw }, i) => (
                    <div
                      key={label}
                      style={{
                        background: isDark ? "#010801" : "#f0f0f0",
                        border: isDark ? "1px solid #142014" : "1px solid #ddd",
                        borderRadius: "4px",
                        padding: "12px 14px",
                      }}
                    >
                      <FL color={isDark ? "#243a14" : "#666"}>{label}</FL>
                      <p style={{ margin: 0, fontFamily: "'JetBrains Mono',monospace", fontSize: "20px", fontWeight: 800, color: "#72ea1e" }}>
                        {raw ? val : <InlineCount target={Number(val)} delay={300 + i * 100} />}
                      </p>
                    </div>
                  ))}
                </div>

                <div
                  style={{
                    display: "inline-flex",
                    alignItems: "center",
                    gap: "8px",
                    padding: "8px 16px",
                    borderRadius: "4px",
                    background: billing.will_be_charged ? "rgba(255,96,96,0.05)" : "rgba(76,175,80,0.05)",
                    border: `1px solid ${billing.will_be_charged ? "#ff606030" : "#4caf5030"}`,
                    marginBottom: billing.alternatives?.length ? "18px" : 0,
                  }}
                >
                  <span style={{ fontSize: "13px" }}>{billing.will_be_charged ? "⚡" : "✓"}</span>
                  <span
                    style={{
                      fontFamily: "'JetBrains Mono',monospace",
                      fontSize: "10px",
                      fontWeight: 700,
                      color: billing.will_be_charged ? "#ff6060" : "#4caf50",
                      letterSpacing: "0.5px",
                    }}
                  >
                    {billing.will_be_charged
                      ? "WARNING — additional analyses will incur charges"
                      : "within free tier — no charges"}
                  </span>
                </div>

                {billing.alternatives?.length > 0 && (
                  <div>
                    <FL color={isDark ? "#243a14" : "#666"} mb="10px">alternatives</FL>
                    <div
                      style={{
                        display: "grid",
                        gridTemplateColumns: "repeat(auto-fit,minmax(175px,1fr))",
                        gap: "9px",
                      }}
                    >
                      {billing.alternatives.map((alt, i) => (
                        <a
                          key={i}
                          href={alt.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          style={{
                            background: isDark ? "#010801" : "#f0f0f0",
                            border: isDark ? "1px solid #142014" : "1px solid #ddd",
                            borderRadius: "4px",
                            padding: "10px 14px",
                            textDecoration: "none",
                            display: "block",
                            transition: "all 0.2s",
                          }}
                          onMouseEnter={(e) => {
                            e.currentTarget.style.borderColor = isDark ? "#72ea1e40" : "#72ea1e80";
                            e.currentTarget.style.background = isDark ? "rgba(114,234,30,0.04)" : "rgba(114,234,30,0.08)";
                          }}
                          onMouseLeave={(e) => {
                            e.currentTarget.style.borderColor = isDark ? "#142014" : "#ddd";
                            e.currentTarget.style.background = isDark ? "#010801" : "#f0f0f0";
                          }}
                        >
                          <p style={{ margin: "0 0 3px", fontFamily: "'JetBrains Mono',monospace", fontSize: "12px", fontWeight: 700, color: "#72ea1e" }}>
                            {alt.name} ↗
                          </p>
                          <p style={{ margin: 0, fontFamily: "'JetBrains Mono',monospace", fontSize: "9px", color: isDark ? "#243a14" : "#666" }}>
                            {alt.cost}
                          </p>
                        </a>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </PSection>
          )}
        </div>
        </div> {/* END #report-content */}

        {/* ── BACK ── */}
        <div style={{ marginTop: "60px", paddingLeft: "40px" }}>
          <button
            onClick={() => navigate("/dashboard")}
            style={BTN}
            onMouseEnter={(e) => {
              e.currentTarget.style.background = "transparent";
              e.currentTarget.style.color = "#72ea1e";
              e.currentTarget.style.boxShadow = "0 0 16px rgba(114,234,30,0.2)";
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.background = "#72ea1e";
              e.currentTarget.style.color = "#000";
              e.currentTarget.style.boxShadow = "none";
            }}
          >
            ← back to dashboard
          </button>
        </div>
      </div>
    </>
  );
}