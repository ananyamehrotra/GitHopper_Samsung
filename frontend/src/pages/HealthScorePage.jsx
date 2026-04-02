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
  @keyframes blink { 0%,100%{opacity:1;} 50%{opacity:0;} }
  .hs-blink { animation: blink 0.7s step-end infinite; }
`;
if (typeof document !== "undefined" && !document.getElementById("hs-styles")) {
  const s = document.createElement("style"); s.id = "hs-styles"; s.textContent = CSS;
  document.head.appendChild(s);
}

function CountUp({ to, delay=0, suffix="", prefix="" }) {
  const [v, setV] = useState(0);
  useEffect(() => {
    const t = setTimeout(() => {
      let start = null;
      const step = ts => {
        if (!start) start = ts;
        const p = Math.min((ts-start)/1200,1);
        setV(Math.floor((1-Math.pow(1-p,4))*to));
        if (p<1) requestAnimationFrame(step); else setV(to);
      };
      requestAnimationFrame(step);
    }, delay);
    return ()=>clearTimeout(t);
  }, [to, delay]);
  return <>{prefix}{v}{suffix}</>;
}

export function HealthScorePage() {
  const location = useLocation();
  const navigate = useNavigate();
  const { isDark } = useTheme();

  const data = location.state?.healthScore;
  const repoUrl = location.state?.repoUrl;

  const CARD = { background: isDark?"#030e03":"#f4fdf4", border: isDark?"1px solid #1a2c1a":"1px solid #d0ebd0", borderRadius:6, padding:22 };

  if (!data) return (
    <>
      <Plasma color="#72ea1e" speed={0.5} opacity={0.08} mouseInteractive />
      <ThemeToggle /><UserProfile />
      <div style={{ padding:40, textAlign:"center" }}>
        <p style={{ color:"#72ea1e", fontFamily:"'JetBrains Mono',monospace" }}>No health score data available.</p>
        <button onClick={()=>navigate("/analyse-branches", { state: { scanResult: location.state?.scanResult, repoUrl: location.state?.repoUrl } })} style={BTN}>← back</button>
      </div>
    </>
  );

  const { overall_health = 0, dimension_scores = {}, issue_summary = {}, recommendations = [] } = data;
  const overall_score = overall_health;
  const summary = { health_grade: overall_score >= 90 ? "A" : overall_score >= 75 ? "B" : overall_score >= 60 ? "C" : overall_score >= 40 ? "D" : "F" };

  const getScoreColor = s => {
    if(s>=90) return "#3cb43c"; if(s>=75) return "#72ea1e"; if(s>=60) return "#c8b400"; if(s>=40) return "#ff8c00"; return "#ff3232";
  };
  const mainColor = getScoreColor(overall_score);

  return (
    <>
      <Plasma color={mainColor} speed={0.5} opacity={0.07} mouseInteractive />
      <ThemeToggle /><UserProfile />

      <div style={{ padding:"clamp(20px,5vw,60px) clamp(16px,4vw,60px) 80px", maxWidth:1040, margin:"0 auto" }}>

        <div style={{ marginBottom:52, display:"flex", justifyContent:"space-between", alignItems:"flex-end", flexWrap:"wrap", gap:20 }}>
          <div>
            <p style={{ margin:"0 0 8px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, letterSpacing:4, color:`${mainColor}60`, textTransform:"uppercase" }}>
              system vitality
            </p>
            <h1 style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:"clamp(24px,6vw,52px)",
              fontWeight:900, letterSpacing:2, color:mainColor,
              textShadow:`0 0 50px ${mainColor}33`, lineHeight:1.05 }}>
              HEALTH SCORE
              <span className="hs-blink" style={{ color:mainColor }}> █</span>
            </h1>
            {repoUrl && <p style={{ margin:"10px 0 0", fontFamily:"'JetBrains Mono',monospace", fontSize:11, color:"#2a401a" }}>{repoUrl}</p>}
          </div>

          <div style={{ textAlign:"right", animation:"fadeUp 0.6s cubic-bezier(0.3,0,0.2,1) both" }}>
            <div style={{ display:"inline-flex", alignItems:"flex-end", gap:4 }}>
              <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:80, fontWeight:900, color:mainColor, lineHeight:0.8 }}>
                <CountUp to={Math.round(overall_score)} />
              </span>
              <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:18, color:`${mainColor}80`, fontWeight:700, paddingBottom:8 }}>/100</span>
            </div>
            <p style={{ margin:"6px 0 0", fontFamily:"'JetBrains Mono',monospace", fontSize:11, color: isDark?"#a0d880":"#3a5220", letterSpacing:1, textTransform:"uppercase", fontWeight:700 }}>
              {summary.health_grade || "Overall Grade"}
            </p>
          </div>
        </div>

        <div style={{ marginBottom:32, height:1, background:`linear-gradient(90deg,${mainColor},${mainColor}18,transparent)` }} />

        <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(200px,1fr))", gap:16, marginBottom:40 }}>
          {[
            { label:"App Security", val:dimension_scores.security, color:"#ff8c00" },
            { label:"Infrastructure", val:dimension_scores.infrastructure, color:"#3cb43c" },
            { label:"IAM Security", val:dimension_scores.iam_security, color:"#c8b400" },
            { label:"Code Quality", val:dimension_scores.code_quality, color:"#72ea1e" },
            { label:"Dependencies", val:dimension_scores.dependencies, color:"#3a8ec4" },
          ].map(({ label, val, color }, i) => (
            <div key={label} style={{ ...CARD, animation:`fadeUp 0.4s ease ${(i+1)*80}ms both` }}>
              <div style={{ display:"flex", justifyContent:"space-between", alignItems:"center", marginBottom:14 }}>
                <span style={{ fontFamily:"'JetBrains Mono',monospace", fontSize:10, letterSpacing:1, textTransform:"uppercase", color: isDark?"#88c460":"#3a5220", fontWeight:700 }}>
                  {label}
                </span>
                <span style={{ width:8, height:8, borderRadius:"50%", background:color, boxShadow:`0 0 8px ${color}` }} />
              </div>
              <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:32, fontWeight:900, color: isDark?"#fff":"#000", lineHeight:1 }}>
                <CountUp to={Math.round(val||0)} delay={150+i*100} />
              </p>
              <div style={{ marginTop:14, height:4, background: isDark?"#0a180a":"#eaeaea", borderRadius:2, overflow:"hidden" }}>
                <div style={{ height:"100%", background:color, width:`${val||0}%`, transition:"width 1.2s cubic-bezier(0.2,0,0.1,1)" }} />
              </div>
            </div>
          ))}
        </div>

        <div style={{ ...CARD, animation:"fadeUp 0.5s ease 300ms both", marginBottom:48 }}>
          <p style={{ margin:"0 0 20px", fontFamily:"'JetBrains Mono',monospace", fontSize:10, fontWeight:800, letterSpacing:2, textTransform:"uppercase", color: isDark?"#b0d880":"#1a301a" }}>
            <span style={{ color:mainColor }}>◈</span> Security Profile & Recommendations
          </p>
          <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(140px,1fr))", gap:12 }}>
            {[
              { k:"Total Issues", v:issue_summary.total_issues },
              { k:"Critical", v:issue_summary.critical, highlight:true },
              { k:"High", v:issue_summary.high, highlight:true },
              { k:"Medium", v:issue_summary.medium },
              { k:"Low", v:issue_summary.low },
            ].map(({ k, v, highlight }, i) => (
              <div key={k} style={{ padding:"12px 16px", background: isDark?"#010801":"#f9fcf9", border: isDark?"1px solid #142014":"1px solid #ddd", borderRadius:4 }}>
                <p style={{ margin:"0 0 6px", fontFamily:"'JetBrains Mono',monospace", fontSize:9, color: isDark?"#5a8030":"#3a5220", textTransform:"uppercase", letterSpacing:1 }}>{k}</p>
                <p style={{ margin:0, fontFamily:"'JetBrains Mono',monospace", fontSize:20, fontWeight:800, color: (highlight && v > 0)?"#ff5050":(isDark?"#fff":"#000") }}>
                  {typeof v==="number" && Number.isInteger(v) ? <CountUp to={v} delay={300+i*50} /> : v}
                </p>
              </div>
            ))}
          </div>

          {recommendations && recommendations.length > 0 && (
            <div style={{ marginTop: 24, padding: "16px 20px", background: isDark ? "#061006" : "#f2f8f2", borderLeft: `3px solid ${mainColor}`, borderRadius: 4 }}>
              <p style={{ margin: "0 0 10px", fontFamily: "'JetBrains Mono',monospace", fontSize: 10, letterSpacing: 2, textTransform: "uppercase", color: mainColor, fontWeight: 900 }}>
                Action Plan
              </p>
              <ul style={{ margin: 0, paddingLeft: 18, color: isDark ? "#a0d880" : "#2a5010", fontSize: 13, lineHeight: 1.8, fontFamily: "'JetBrains Mono',monospace" }}>
                {recommendations.map((rec, i) => <li key={i}>{rec}</li>)}
              </ul>
            </div>
          )}
        </div>

        <div>
          <button onClick={()=>navigate("/analyse-branches", { state: { scanResult: location.state?.scanResult, repoUrl: location.state?.repoUrl } })} style={{ ...BTN, background:mainColor, borderColor:mainColor }}
            onMouseEnter={e=>{ e.currentTarget.style.background="transparent"; e.currentTarget.style.color=mainColor; }}
            onMouseLeave={e=>{ e.currentTarget.style.background=mainColor; e.currentTarget.style.color="#000"; }}>
            ← back to analysis
          </button>
        </div>
      </div>
    </>
  );
}

const BTN = {
  padding:"10px 26px", color:"#000",
  borderRadius:3, cursor:"pointer",
  fontSize:11, fontWeight:800, fontFamily:"'JetBrains Mono',monospace",
  letterSpacing:"1.5px", textTransform:"lowercase", transition:"all 0.2s ease",
};
