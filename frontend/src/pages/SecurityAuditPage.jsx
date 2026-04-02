import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useTheme } from "../context/ThemeContext";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";

/* ── inject styles once ── */
const CSS = `
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800;900&display=swap');
  @keyframes fadeUp { from { opacity:0; transform:translateY(14px);} to { opacity:1; transform:translateY(0);} }
  @keyframes barGrow { from { width:0; } to { width:var(--bar-w); } }
  @keyframes scanPulse { 0%,100%{box-shadow:0 0 0 0 #ff323240;} 50%{box-shadow:0 0 0 8px #ff323200;} }
  @keyframes blink { 0%,100%{opacity:1;} 50%{opacity:0;} }
  .sa-blink { animation: blink 0.7s step-end infinite; }
`;
if (typeof document !== "undefined" && !document.getElementById("sa-styles")) {
  const s = document.createElement("style"); s.id = "sa-styles"; s.textContent = CSS;
  document.head.appendChild(s);
}

/* ── helpers ── */
const SEV_COLOR = { CRITICAL:"#ff3232", HIGH:"#ff8c00", MEDIUM:"#c8b400", LOW:"#3cb43c" };
const SEV_BG    = { CRITICAL:"rgba(255,50,50,0.1)", HIGH:"rgba(255,140,0,0.1)", MEDIUM:"rgba(200,180,0,0.08)", LOW:"rgba(60,180,60,0.08)" };

function Badge({ sev }) {
  const c = SEV_COLOR[sev] || "#3cb43c";
  return (
    <span style={{ display:"inline-flex", alignItems:"center", gap:6, padding:"3px 10px",
      borderRadius:3, fontSize:10, fontWeight:900, letterSpacing:"1.8px",
      fontFamily:"'JetBrains Mono',monospace",
      background: SEV_BG[sev]||"transparent", border:`1px solid ${c}`, color:c, flexShrink:0 }}>
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
        const p = Math.min((ts-start)/900,1);
        setV(Math.floor((1-Math.pow(1-p,3))*to));
        if (p<1) requestAnimationFrame(step); else setV(to);
      };
      requestAnimationFrame(step);
    }, delay);
    return ()=>clearTimeout(t);
  }, [to, delay]);
  return <>{v}</>;
}

function SeverityBar({ label, count, max, color, delay }) {
  const [show, setShow] = useState(false);
  useEffect(() => { const t=setTimeout(()=>setShow(true),delay); return()=>clearTimeout(t); }, [delay]);
  const pct = max ? `${Math.round(count/max*100)}%` : "0%";
  return (
    <div style={{ marginBottom:10 }}>
      <div style={{ display:"flex", justifyContent:"space-between", marginBottom:4 }}>
        <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:10, color:"#3a5220", letterSpacing:"1.5px", textTransform:"uppercase" }}>{label}</span>
        <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:11, fontWeight:800, color }}>
          <CountUp to={count} delay={delay} />
        </span>
      </div>
      <div style={{ height:3, background:"#0a180a", borderRadius:2, overflow:"hidden" }}>
        <div style={{
          height:"100%", borderRadius:2, background:color,
          width: show ? pct : "0%",
          transition:"width 0.9s cubic-bezier(0.4,0,0.2,1)",
          boxShadow:`0 0 8px ${color}80`
        }} />
      </div>
    </div>
  );
}

function FindingRow({ finding, idx, isOpen, onToggle }) {
  const { isDark } = useTheme();
  const c = SEV_COLOR[finding.severity] || "#3cb43c";
  return (
    <div style={{ borderBottom:`1px solid ${isDark?"#0a180a":"#e0e0e0"}`, animation:`fadeUp 0.3s ease ${idx*30}ms both` }}>
      <div onClick={onToggle} style={{ display:"flex", alignItems:"center", gap:12, padding:"14px 18px",
        cursor:"pointer", userSelect:"none",
        background: isOpen ? `${c}06` : "transparent", transition:"background 0.2s" }}
        onMouseEnter={e=>e.currentTarget.style.background=`${c}08`}
        onMouseLeave={e=>e.currentTarget.style.background=isOpen?`${c}06`:"transparent"}>
        <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:10, color:"#243a14", width:24, flexShrink:0 }}>
          {String(idx+1).padStart(2,"0")}
        </span>
        <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:12, fontWeight:800,
          color:c, flex:1, overflow:"hidden", textOverflow:"ellipsis", whiteSpace:"nowrap", letterSpacing:"0.5px" }}>
          {finding.type || "UNKNOWN"}
        </span>
        <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:10, color:"#2a3e1a",
          flex:"0 1 200px", overflow:"hidden", textOverflow:"ellipsis", whiteSpace:"nowrap", textAlign:"right", paddingRight:12 }}>
          {finding.file}
        </span>
        <Badge sev={finding.severity} />
        <span style={{ color:c, fontSize:14, fontFamily:"'JetBrains Mono',monospace",
          transition:"transform 0.3s", transform:isOpen?"rotate(90deg)":"rotate(0)", flexShrink:0 }}>›</span>
      </div>
      <div style={{ maxHeight:isOpen?"600px":"0", overflow:"hidden", transition:"max-height 0.45s cubic-bezier(0.4,0,0.2,1)" }}>
        <div style={{ padding:"4px 18px 22px 52px", display:"flex", flexDirection:"column", gap:14 }}>
          {finding.explanation && (
            <div>
              <p style={{ margin:"0 0 6px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:"2px", textTransform:"uppercase", color:"#72ea1e", fontWeight:900 }}>EXPLANATION</p>
              <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:12, color: isDark?"#88c460":"#2a5010", lineHeight:1.9 }}>{finding.explanation}</p>
            </div>
          )}
          {finding.business_impact && (
            <div style={{ borderLeft:"2px solid #ff606033", paddingLeft:14 }}>
              <p style={{ margin:"0 0 6px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:"2px", textTransform:"uppercase", color:"#ff8080", fontWeight:900 }}>BUSINESS IMPACT</p>
              <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:12, color: isDark?"#c07070":"#8b3030", lineHeight:1.9 }}>{finding.business_impact}</p>
            </div>
          )}
          {finding.remediation && (
            <div>
              <p style={{ margin:"0 0 6px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:"2px", textTransform:"uppercase", color:"#60d060", fontWeight:900 }}>REMEDIATION</p>
              <pre style={{ margin:0, padding:"12px 14px", background: isDark?"#010801":"#f0f8f0",
                border: isDark?"1px solid #162816":"1px solid #c0dcc0", borderRadius:4,
                fontFamily:"'JetBrains Mono',monospace", fontSize:11, color: isDark?"#72ea1e":"#1a4010",
                lineHeight:1.9, whiteSpace:"pre-wrap", wordBreak:"break-word" }}>{finding.remediation}</pre>
            </div>
          )}
          {finding.estimated_minutes_to_fix && (
            <div style={{ display:"flex", alignItems:"center", gap:10 }}>
              <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:"2px", textTransform:"uppercase", color:"#60a0d0", fontWeight:900 }}>EST. FIX</span>
              <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:11, color:"#7ac0f0",
                padding:"2px 12px", background:"rgba(96,160,208,0.07)", border:"1px solid rgba(96,160,208,0.18)", borderRadius:20 }}>
                ~{finding.estimated_minutes_to_fix} min
              </span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export function SecurityAuditPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const { isDark } = useTheme();
  const [openIdx, setOpenIdx] = useState(null);
  const [filterSev, setFilterSev] = useState("ALL");

  const data = location.state?.securityAudit;
  const repoUrl = location.state?.repoUrl;

  const CARD = { background: isDark?"#020c02":"#f8f8f8", border: isDark?"1px solid #142014":"1px solid #d8d8d8", borderRadius:6, padding:22 };

  if (!data) return (
    <>
      <Plasma color="#ff3232" speed={0.5} opacity={0.08} mouseInteractive />
      <ThemeToggle /><UserProfile />
      <div style={{ padding:40, textAlign:"center" }}>
        <p style={{ color:"#ff6060", fontFamily:"'JetBrains Mono',monospace" }}>No security audit data available.</p>
        <button onClick={()=>navigate("/analyse-branches", { state: { scanResult: location.state?.scanResult, repoUrl: location.state?.repoUrl } })} style={BTN}>← back</button>
      </div>
    </>
  );

  const { findings=[], summary={}, risk_indicators={} } = data;
  const total = summary.total_issues || 0;

  const filtered = filterSev === "ALL" ? findings : findings.filter(f=>f.severity===filterSev);

  const SEVS = ["CRITICAL","HIGH","MEDIUM","LOW"];

  return (
    <>
      <Plasma color="#ff3232" speed={0.5} opacity={0.07} mouseInteractive />
      <ThemeToggle /><UserProfile />

      <div style={{ padding:"clamp(20px,5vw,60px) clamp(16px,4vw,60px) 80px", maxWidth:1040, margin:"0 auto" }}>

        <div style={{ marginBottom:52 }}>
          <p style={{ margin:"0 0 8px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:4, color:"#ff323260", textTransform:"uppercase" }}>
            security report
          </p>
          <h1 style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:"clamp(24px,6vw,52px)",
            fontWeight:900, letterSpacing:2, color:"#ff5050",
            textShadow:"0 0 50px rgba(255,50,50,0.2)", lineHeight:1.05 }}>
            SECURITY AUDIT
            <span className="sa-blink" style={{ color:"#ff3232" }}> ▌</span>
          </h1>
          {repoUrl && <p style={{ margin:"10px 0 0", fontFamily:"'JetBrains Mono',monospace", fontSize:11, color:"#3a2020" }}>{repoUrl}</p>}
          <div style={{ marginTop:16, height:1, background:"linear-gradient(90deg,#ff3232,#ff323218,transparent)" }} />
        </div>

        {risk_indicators.has_critical && (
          <div style={{ marginBottom:28, padding:"14px 20px", borderRadius:6,
            background:"rgba(255,50,50,0.06)", border:"1px solid #ff323240",
            animation:"scanPulse 2.5s ease infinite", display:"flex", alignItems:"center", gap:12 }}>
            <span style={{ fontSize:18 }}>⚠</span>
            <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:11, fontWeight:800, color:"#ff6060", letterSpacing:1 }}>
              CRITICAL VULNERABILITIES DETECTED — DO NOT DEPLOY
            </span>
            <span style={{ marginLeft:"auto", fontFamily:"'JetBrains Mono',monospace", fontSize:10, color:"#ff404060" }}>
              {risk_indicators.critical_percentage?.toFixed(1)}% critical rate
            </span>
          </div>
        )}

        <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(140px,1fr))", gap:10, marginBottom:32 }}>
          {[
            { label:"Total Issues", val:total, color:"#ff5050" },
            { label:"Critical", val:summary.critical||0, color:"#ff3232" },
            { label:"High", val:summary.high||0, color:"#ff8c00" },
            { label:"Medium", val:summary.medium||0, color:"#c8b400" },
            { label:"Low", val:summary.low||0, color:"#3cb43c" },
          ].map(({ label, val, color }, i) => (
            <div key={label} style={{ ...CARD, animation:`fadeUp 0.4s ease ${i*80}ms both` }}>
              <p style={{ margin:"0 0 8px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:1, textTransform:"uppercase", color, fontWeight:700 }}>{label}</p>
              <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:36, fontWeight:900, color: isDark?"#fff":"#020c02", lineHeight:1 }}>
                <CountUp to={val} delay={i*80+200} />
              </p>
            </div>
          ))}
        </div>

        <div style={{ ...CARD, marginBottom:28 }}>
          <p style={{ margin:"0 0 18px", fontFamily:"'JetBrains Mono',monospace", fontSize:10, fontWeight:800, letterSpacing:2, textTransform:"uppercase", color: isDark?"#b0d880":"#142014" }}>
            ◈ Severity Distribution
          </p>
          {SEVS.map((s,i) => (
            <SeverityBar key={s} label={s} count={summary[s.toLowerCase()]||0} max={total||1} color={SEV_COLOR[s]} delay={200+i*100} />
          ))}
          <div style={{ marginTop:18, display:"grid", gridTemplateColumns:"repeat(3,1fr)", gap:10 }}>
            {Object.entries(summary.categories||{}).map(([k,v]) => (
              <div key={k} style={{ padding:"10px 14px", background: isDark?"#010801":"#f0f0f0", border: isDark?"1px solid #142014":"1px solid #ddd", borderRadius:4 }}>
                <p style={{ margin:"0 0 4px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, color:"#3a5220", textTransform:"uppercase", letterSpacing:1 }}>{k.replace(/_/g," ")}</p>
                <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:20, fontWeight:800, color:"#ff5050" }}>{v}</p>
              </div>
            ))}
          </div>
        </div>

        <div style={CARD}>
          <div style={{ display:"flex", alignItems:"center", justifyContent:"space-between", marginBottom:18, flexWrap:"wrap", gap:10 }}>
            <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:10, fontWeight:800, letterSpacing:2, textTransform:"uppercase", color: isDark?"#b0d880":"#142014" }}>
              <span style={{ color:"#ff5050" }}>◈</span> Findings
              <span style={{ marginLeft:8, color:"#243a14", fontWeight:500 }}>[ {filtered.length} ]</span>
            </p>
            <div style={{ display:"flex", gap:6 }}>
              {["ALL",...SEVS].map(s => (
                <button key={s} onClick={()=>setFilterSev(s)} style={{
                  padding:"4px 10px", borderRadius:3, cursor:"pointer",
                  fontFamily:"'JetBrains Mono',monospace", fontSize:9, fontWeight:800, letterSpacing:1,
                  background: filterSev===s ? (SEV_COLOR[s]||"#ff5050") : "transparent",
                  color: filterSev===s ? "#000" : (SEV_COLOR[s]||"#ff5050"),
                  border:`1px solid ${SEV_COLOR[s]||"#ff5050"}`,
                  transition:"all 0.2s"
                }}>{s}</button>
              ))}
            </div>
          </div>
          {filtered.length === 0
            ? <p style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:12, color:"#243a14", padding:"20px 0" }}>No findings for this filter.</p>
            : filtered.map((f,i) => (
                <FindingRow key={i} finding={f} idx={i} isOpen={openIdx===i} onToggle={()=>setOpenIdx(openIdx===i?null:i)} />
              ))
          }
        </div>

        <div style={{ marginTop:48 }}>
          <button onClick={()=>navigate("/analyse-branches", { state: { scanResult: location.state?.scanResult, repoUrl: location.state?.repoUrl } })} style={BTN}
            onMouseEnter={e=>{ e.currentTarget.style.background="transparent"; e.currentTarget.style.color="#ff5050"; }}
            onMouseLeave={e=>{ e.currentTarget.style.background="#ff5050"; e.currentTarget.style.color="#000"; }}>
            ← back to analysis
          </button>
        </div>
      </div>
    </>
  );
}

const BTN = {
  padding:"10px 26px", background:"#ff5050", color:"#000",
  border:"1px solid #ff5050", borderRadius:3, cursor:"pointer",
  fontSize:11, fontWeight:800, fontFamily:"'JetBrains Mono',monospace",
  letterSpacing:"1.5px", textTransform:"lowercase", transition:"all 0.2s ease",
};
