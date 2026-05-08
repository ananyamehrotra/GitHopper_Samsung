import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useTheme } from "../context/ThemeContext";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";

const CSS = `
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800;900&display=swap');
  @keyframes fadeUp { from { opacity:0; transform:translateY(14px);} to { opacity:1; transform:translateY(0);} }
  @keyframes scanPulse { 0%,100%{box-shadow:0 0 0 0 #ff8c0040;} 50%{box-shadow:0 0 0 8px #ff8c0000;} }
  @keyframes blink { 0%,100%{opacity:1;} 50%{opacity:0;} }
  .dr-blink { animation: blink 0.7s step-end infinite; }
`;
if (typeof document !== "undefined" && !document.getElementById("dr-styles")) {
  const s = document.createElement("style");
  s.id = "dr-styles";
  s.textContent = CSS;
  document.head.appendChild(s);
}

const SEV_COLOR = { HIGH:"#ff5050", MEDIUM:"#ff8c00", LOW:"#c8b400" };
const SEV_BG = { HIGH:"rgba(255,80,80,0.1)", MEDIUM:"rgba(255,140,0,0.08)", LOW:"rgba(200,180,0,0.08)" };

function Badge({ sev }) {
  const c = SEV_COLOR[sev] || "#c8b400";
  return (
    <span style={{ display:"inline-flex", alignItems:"center", gap:6, padding:"3px 10px",
      borderRadius:3, fontSize:10, fontWeight:900, letterSpacing:"1.8px",
      fontFamily:"'JetBrains Mono',monospace",
      background: SEV_BG[sev] || "transparent", border:`1px solid ${c}`, color:c, flexShrink:0 }}>
      <span style={{ width:5, height:5, borderRadius:"50%", background:c, boxShadow:`0 0 5px ${c}` }} />
      {sev}
    </span>
  );
}

function CountUp({ to, delay=0 }) {
  const [v, setV] = useState(0);
  useEffect(() => {
    const t = setTimeout(() => {
      let start = null;
      const step = ts => {
        if (!start) start = ts;
        const p = Math.min((ts - start) / 900, 1);
        setV(Math.floor((1 - Math.pow(1 - p, 3)) * to));
        if (p < 1) requestAnimationFrame(step);
        else setV(to);
      };
      requestAnimationFrame(step);
    }, delay);
    return () => clearTimeout(t);
  }, [to, delay]);
  return <>{v}</>;
}

function DistributionChart({ findings, isDark }) {
  const severityCounts = { CRITICAL: 0, HIGH: 0, MEDIUM: 0, LOW: 0 };
  const severityOrder = ["CRITICAL", "HIGH", "MEDIUM", "LOW"];
  
  findings.forEach(f => {
    const sev = f.severity || "LOW";
    if (severityCounts.hasOwnProperty(sev)) {
      severityCounts[sev]++;
    }
  });

  const total = findings.length;
  const chartColors = { CRITICAL: "#ff2a2a", HIGH: "#ff5050", MEDIUM: "#ff8c00", LOW: "#c8b400" };

  // Calculate pie chart angles
  const segments = [];
  let currentAngle = -90;
  
  severityOrder.forEach(sev => {
    const count = severityCounts[sev];
    const sliceAngle = (count / total) * 360;
    segments.push({
      sev,
      count,
      sliceAngle,
      startAngle: currentAngle,
      endAngle: currentAngle + sliceAngle,
      color: chartColors[sev],
      pct: total > 0 ? Math.round((count / total) * 100) : 0
    });
    currentAngle += sliceAngle;
  });

  // SVG pie chart path calculation
  const radius = 80;
  const centerX = 120;
  const centerY = 120;

  const angleToPoint = (angle, r) => {
    const rad = (angle * Math.PI) / 180;
    return {
      x: centerX + r * Math.cos(rad),
      y: centerY + r * Math.sin(rad)
    };
  };

  const arcPath = (startAngle, endAngle) => {
    const start = angleToPoint(startAngle, radius);
    const end = angleToPoint(endAngle, radius);
    const largeArc = endAngle - startAngle > 180 ? 1 : 0;
    return `M ${centerX} ${centerY} L ${start.x} ${start.y} A ${radius} ${radius} 0 ${largeArc} 1 ${end.x} ${end.y} Z`;
  };

  return (
    <div style={{ marginBottom: 48, padding: "24px 28px", background: isDark?"#020a02":"#fafafa",
      border: isDark?"1px solid #142014":"1px solid #e0e0e0", borderRadius:6,
      animation:"fadeUp 0.5s ease both" }}>
      <p style={{ margin:"0 0 24px", fontFamily:"'JetBrains Mono',monospace", fontSize:10, fontWeight:800, 
        letterSpacing:2, textTransform:"uppercase", color: isDark?"#b0d880":"#142014" }}>
        <span style={{ color:"#ff8c00" }}>◉</span> Severity Distribution
      </p>

      <div style={{ display:"flex", gap:40, alignItems:"center", justifyContent:"center", flexWrap:"wrap" }}>
        {/* Pie Chart */}
        <div style={{ position:"relative", width:280, height:280 }}>
          <svg width="280" height="280" style={{ filter: isDark ? "drop-shadow(0 0 20px rgba(255,140,0,0.15))" : "drop-shadow(0 0 15px rgba(0,0,0,0.1))" }}>
            {segments.map((seg, idx) => (
              seg.sliceAngle > 0 && (
                <g key={seg.sev}>
                  <path
                    d={arcPath(seg.startAngle, seg.endAngle)}
                    fill={seg.color}
                    opacity="0.85"
                    style={{ transition:"opacity 0.2s", cursor:"pointer" }}
                  />
                  <path
                    d={arcPath(seg.startAngle, seg.endAngle)}
                    fill="none"
                    stroke={isDark ? "#0a140a" : "#fff"}
                    strokeWidth="2"
                  />
                </g>
              )
            ))}
          </svg>
          <div style={{ position:"absolute", top:"50%", left:"50%", transform:"translate(-50%, -50%)", textAlign:"center" }}>
            <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:32, fontWeight:900, color: isDark?"#fff":"#000" }}>
              {total}
            </p>
            <p style={{ margin:"2px 0 0", fontFamily:"'JetBrains Mono',monospace", fontSize:9, color: isDark?"#888":"#999", letterSpacing:1, textTransform:"uppercase" }}>
              Total Findings
            </p>
          </div>
        </div>

        {/* Legend and Stats */}
        <div style={{ display:"flex", flexDirection:"column", gap:12, minWidth:200 }}>
          {segments.map(seg => (
            seg.sliceAngle > 0 && (
              <div key={seg.sev} style={{ display:"flex", alignItems:"center", gap:12, padding:"10px 12px", 
                borderRadius:4, background: isDark?"#0a140a":"#f5f5f5", transition:"all 0.2s",
                border: `1px solid ${seg.color}40`, cursor:"pointer" }}
                onMouseEnter={e=>{ e.currentTarget.style.borderColor = seg.color; e.currentTarget.style.boxShadow = `0 0 8px ${seg.color}30`; }}
                onMouseLeave={e=>{ e.currentTarget.style.borderColor = `${seg.color}40`; e.currentTarget.style.boxShadow = "none"; }}>
                <span style={{ width:12, height:12, borderRadius:"50%", background: seg.color, flexShrink:0, boxShadow: `0 0 6px ${seg.color}` }} />
                <div style={{ flex:1 }}>
                  <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:10, fontWeight:800, color: seg.color, letterSpacing:1, textTransform:"uppercase" }}>
                    {seg.sev}
                  </p>
                  <p style={{ margin:"2px 0 0", fontFamily:"'JetBrains Mono',monospace", fontSize:9, color: isDark?"#888":"#999" }}>
                    {seg.count} issues
                  </p>
                </div>
                <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:13, fontWeight:900, color: isDark?"#fff":"#000", minWidth:30, textAlign:"right" }}>
                  {seg.pct}%
                </span>
              </div>
            )
          ))}
        </div>
      </div>
    </div>
  );
}

function DebtItem({ d, idx }) {
  const { isDark } = useTheme();
  const c = SEV_COLOR[d.severity] || "#ff8c00";
  return (
    <div style={{ padding:"20px 24px", background: isDark?"#020a02":"#fafafa",
      border: isDark?"1px solid #142014":"1px solid #e0e0e0", borderRadius:6,
      marginBottom:16, animation:`fadeUp 0.4s ease ${idx * 40}ms both`,
      position:"relative", overflow:"hidden" }}>
      <div style={{ position:"absolute", top:0, left:0, width:3, height:"100%", background:c }} />

      <div style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-start", marginBottom:14, gap:20 }}>
        <div>
          <div style={{ display:"flex", alignItems:"center", gap:14, marginBottom:8 }}>
            <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:11, color: isDark?"#648a44":"#3a5220", fontWeight:800, letterSpacing:1 }}>
              {d.type}
            </span>
            <Badge sev={d.severity} />
          </div>
          <h3 style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:15, color:c, letterSpacing:0.5 }}>
            {d.file}
          </h3>
        </div>
        <div style={{ textAlign:"right" }}>
          <p style={{ margin:"0 0 4px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, color:"#ff8c00", letterSpacing:2, textTransform:"uppercase" }}>
            EST. EFFORT
          </p>
          <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:24, fontWeight:900, color: isDark?"#fff":"#000" }}>
            {d.estimated_minutes_to_fix || 0} <span style={{ fontSize:12, color:"#648a44" }}>min</span>
          </p>
        </div>
      </div>

      <div style={{ display:"flex", flexDirection:"column", gap:12 }}>
        <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:12, color: isDark?"#88c460":"#2a5010", lineHeight:1.8 }}>
          {d.explanation || d.description}
        </p>

        {(d.remediation || d.refactoring_suggestion) && (
          <div style={{ marginTop:8, padding:"12px 16px", background: isDark?"#0a140a":"#f0f5f0", borderRadius:4, borderLeft:`2px solid ${c}60` }}>
            <p style={{ margin:"0 0 6px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:"2px", color:c, fontWeight:900, textTransform:"uppercase" }}>
              REFACTORING PLAN
            </p>
            <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:11, color: isDark?"#a0e080":"#1a4010", lineHeight:1.8 }}>
              {d.remediation || d.refactoring_suggestion}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export function DebtReportPage() {
  const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://localhost:5001";
  const location = useLocation();
  const navigate = useNavigate();
  const { isDark } = useTheme();
  const [data, setData] = useState(location.state?.debtReport || null);
  const [repoUrl, setRepoUrl] = useState(location.state?.repoUrl || "");
  const [loading, setLoading] = useState(!location.state?.debtReport);
  const [error, setError] = useState("");

  const CARD = { background: isDark?"#020a02":"#f8f8f8", border: isDark?"1px solid #142014":"1px solid #d8d8d8", borderRadius:6, padding:22 };

  useEffect(() => {
    if (location.state?.debtReport) {
      setData(location.state.debtReport);
      setRepoUrl(location.state?.repoUrl || "");
      setLoading(false);
      setError("");
      return;
    }

    const savedRepoUrl = location.state?.repoUrl || localStorage.getItem("githopper_last_url") || "";
    const savedBranch = localStorage.getItem("githopper_last_branch") || "main";
    const savedScanMode = localStorage.getItem("githopper_last_scan_mode") || "classic";

    if (!savedRepoUrl) {
      setLoading(false);
      setError("No repository found. Run an analysis first from the dashboard.");
      return;
    }

    let cancelled = false;

    async function loadDebtReport() {
      setLoading(true);
      setError("");
      setRepoUrl(savedRepoUrl);

      try {
        const response = await fetch(`${API_BASE}/api/debt-report`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            repo_url: savedRepoUrl,
            branch_name: savedBranch,
            scan_mode: savedScanMode,
            generate_fixes: savedScanMode === "continuous",
          }),
        });

        const payload = await response.json();
        if (!response.ok) {
          throw new Error(payload.error || "Failed to load technical debt report");
        }

        if (!cancelled) {
          setData(payload.debt_report || null);
          setRepoUrl(payload.repo_url || savedRepoUrl);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message || "Failed to load technical debt report");
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadDebtReport();

    return () => {
      cancelled = true;
    };
  }, [location.state]);

  if (loading) return (
    <>
      <Plasma color="#ff8c00" speed={0.5} opacity={0.08} mouseInteractive />
      <ThemeToggle /><UserProfile />
      <div style={{ padding:40, textAlign:"center" }}>
        <p style={{ color:"#ff8c00", fontFamily:"'JetBrains Mono',monospace" }}>Loading technical debt report...</p>
      </div>
    </>
  );

  if (!data) return (
    <>
      <Plasma color="#ff8c00" speed={0.5} opacity={0.08} mouseInteractive />
      <ThemeToggle /><UserProfile />
      <div style={{ padding:40, textAlign:"center" }}>
        <p style={{ color:"#ff8c00", fontFamily:"'JetBrains Mono',monospace" }}>
          {error || "No technical debt data available."}
        </p>
        <button onClick={()=>navigate("/analyse-branches", { state: { scanResult: location.state?.scanResult, repoUrl: location.state?.repoUrl } })} style={BTN}>← back</button>
      </div>
    </>
  );

  const { findings=[], summary={}, effort_estimate={} } = data;
  const hours = Math.floor((effort_estimate.total_minutes || 0) / 60);
  const mins = (effort_estimate.total_minutes || 0) % 60;

  return (
    <>
      <Plasma color="#ff8c00" speed={0.5} opacity={0.07} mouseInteractive />
      <ThemeToggle /><UserProfile />

      <div style={{ padding:"clamp(20px,5vw,60px) clamp(16px,4vw,60px) 80px", maxWidth:1040, margin:"0 auto" }}>

        <div style={{ marginBottom:52 }}>
          <p style={{ margin:"0 0 8px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:4, color:"#ff8c0060", textTransform:"uppercase" }}>
            quality insights
          </p>
          <h1 style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:"clamp(24px,6vw,52px)",
            fontWeight:900, letterSpacing:2, color:"#ff8c00",
            textShadow:"0 0 50px rgba(255,140,0,0.2)", lineHeight:1.05 }}>
            TECHNICAL DEBT
            <span className="dr-blink" style={{ color:"#ff8c00" }}> ▌</span>
          </h1>
          {repoUrl && <p style={{ margin:"10px 0 0", fontFamily:"'JetBrains Mono',monospace", fontSize:11, color:"#4a3210" }}>{repoUrl}</p>}
          <div style={{ marginTop:16, height:1, background:"linear-gradient(90deg,#ff8c00,#ff8c0018,transparent)" }} />
        </div>

        <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(180px,1fr))", gap:16, marginBottom:40 }}>
          <div style={{ ...CARD, animation:"fadeUp 0.4s ease both", borderLeft:"3px solid #ff8c00" }}>
            <p style={{ margin:"0 0 8px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:1, textTransform:"uppercase", color:"#ff8c00", fontWeight:700 }}>
              Total Debt Effort
            </p>
            <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:36, fontWeight:900, color: isDark?"#fff":"#000", lineHeight:1 }}>
              <CountUp to={hours} />h <CountUp to={mins} delay={200} />m
            </p>
          </div>
          <div style={{ ...CARD, animation:"fadeUp 0.4s ease 100ms both", borderLeft:"3px solid #ff5050" }}>
            <p style={{ margin:"0 0 8px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:1, textTransform:"uppercase", color:"#ff5050", fontWeight:700 }}>
              High Priority Return
            </p>
            <div style={{ display:"flex", alignItems:"flex-end", gap:8 }}>
              <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:36, fontWeight:900, color: isDark?"#fff":"#000", lineHeight:1 }}>
                {Math.round(summary.total_issues > 0 ? (((summary.critical || 0) + (summary.high || 0)) / summary.total_issues) * 100 : 0)}%
              </p>
              <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:11, color:"#ff5050", paddingBottom:4 }}>ROI Focus</span>
            </div>
          </div>
          <div style={{ ...CARD, animation:"fadeUp 0.4s ease 200ms both", borderLeft:"3px solid #243a14" }}>
            <p style={{ margin:"0 0 8px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:1, textTransform:"uppercase", color:"#648a44", fontWeight:700 }}>
              Debt Categories
            </p>
            <div style={{ display:"flex", flexDirection:"column", gap:6, marginTop:12 }}>
              {Object.entries(summary.categories || {}).slice(0,3).map(([k, v]) => (
                <div key={k} style={{ display:"flex", justifyContent:"space-between", fontFamily:"'JetBrains Mono',monospace", fontSize:11 }}>
                  <span style={{ color: isDark?"#88c460":"#2a5010" }}>{k.replace(/_/g," ")}</span>
                  <span style={{ fontWeight:800, color: isDark?"#fff":"#000" }}>{v}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div style={{ marginBottom:48 }}>
          <p style={{ margin:"0 0 18px", fontFamily:"'JetBrains Mono',monospace", fontSize:10, fontWeight:800, letterSpacing:2, textTransform:"uppercase", color: isDark?"#b0d880":"#142014" }}>
            <span style={{ color:"#ff8c00" }}>◈</span> Debt Register
            <span style={{ marginLeft:8, color:"#243a14", fontWeight:500 }}>[ {findings.length} ]</span>
          </p>
          {findings.length === 0
            ? <p style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:12, color:"#243a14", padding:"20px 0" }}>No technical debt found.</p>
            : findings.map((d, i) => <DebtItem key={i} d={d} idx={i} />)
          }
        </div>

        {findings.length > 0 && <DistributionChart findings={findings} isDark={isDark} />}

        <div>
          <button onClick={()=>navigate("/analyse-branches", { state: { scanResult: location.state?.scanResult, repoUrl: location.state?.repoUrl } })} style={BTN}
            onMouseEnter={e=>{ e.currentTarget.style.background="transparent"; e.currentTarget.style.color="#ff8c00"; }}
            onMouseLeave={e=>{ e.currentTarget.style.background="#ff8c00"; e.currentTarget.style.color="#000"; }}>
            ← back to analysis
          </button>
        </div>
      </div>
    </>
  );
}

const BTN = {
  padding:"10px 26px", background:"#ff8c00", color:"#000",
  border:"1px solid #ff8c00", borderRadius:3, cursor:"pointer",
  fontSize:11, fontWeight:800, fontFamily:"'JetBrains Mono',monospace",
  letterSpacing:"1.5px", textTransform:"lowercase", transition:"all 0.2s ease",
};
