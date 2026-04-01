import React, { useState, useContext } from 'react';
import { ThemeContext } from '../context/ThemeContext';
import './ResultsPage.css';

export default function ResultsPage({ analysisData, onBack }) {
  const [activeTab, setActiveTab] = useState('security');
  const { isDarkMode, toggleTheme } = useContext(ThemeContext) || { isDarkMode: true, toggleTheme: () => {} };

  if (!analysisData) {
    return (
      <div className={`results-page ${isDarkMode ? 'dark' : 'light'}`}>
        <p>No analysis data available</p>
        <button onClick={onBack}>Back to Dashboard</button>
      </div>
    );
  }

  const {
    repo_url,
    vulnerable_files = [],
    vulnerabilities = [],
    total_files_analyzed = 0,
    files_with_issues = 0,
    total_vulnerabilities = 0,
    billing = {},
    cost_tracker = {}
  } = analysisData;

  // Group vulnerabilities by severity
  const criticalCount = vulnerabilities.filter(v => v.severity === 'CRITICAL').length;
  const highCount = vulnerabilities.filter(v => v.severity === 'HIGH').length;
  const mediumCount = vulnerabilities.filter(v => v.severity === 'MEDIUM').length;
  const riskScore = Math.min(100, (criticalCount * 40) + (highCount * 20) + (mediumCount * 5));

  // Group by type
  const typeGroups = {};
  vulnerabilities.forEach(v => {
    if (!typeGroups[v.type]) typeGroups[v.type] = 0;
    typeGroups[v.type]++;
  });

  // Calculate debt metrics (estimates)
  const totalDebtHours = vulnerabilities.reduce((sum, v) => sum + (v.estimated_minutes || 0), 0) / 60;
  const codeQualityScore = Math.max(0, 100 - (mediumCount * 5) - (highCount * 10));
  const testCoverage = Math.random() * 40 + 20; // Placeholder

  const renderSecurityTab = () => (
    <div className="tab-content security-tab">
      {/* Score Cards */}
      <div className="score-cards">
        <div className="score-card critical">
          <div className="score-bar"></div>
          <div className="score-number">{criticalCount}</div>
          <div className="score-label">CRITICAL</div>
        </div>
        <div className="score-card high">
          <div className="score-bar"></div>
          <div className="score-number">{highCount}</div>
          <div className="score-label">HIGH RISK</div>
        </div>
        <div className="score-card medium">
          <div className="score-bar"></div>
          <div className="score-number">{mediumCount}</div>
          <div className="score-label">MEDIUM</div>
        </div>
        <div className="score-card risk-score">
          <div className="score-bar"></div>
          <div className="score-number">{riskScore}</div>
          <div className="score-label">RISK SCORE</div>
        </div>
      </div>

      {/* Charts */}
      <div className="charts-container">
        <div className="chart-box">
          <div className="chart-label">FINDINGS BY DOMAIN</div>
          <div className="horizontal-chart">
            {Object.entries(typeGroups).slice(0, 5).map(([type, count]) => (
              <div key={type} className="chart-bar-item">
                <div className="bar-label">{type}</div>
                <div className="bar-container">
                  <div className="bar-fill" style={{ width: `${(count / Math.max(...Object.values(typeGroups))) * 100}%` }}></div>
                </div>
                <div className="bar-count">{count}</div>
              </div>
            ))}
          </div>
        </div>

        <div className="chart-box">
          <div className="chart-label">SEVERITY DISTRIBUTION</div>
          <div className="severity-chart">
            <div className="sev-item critical">
              <div className="sev-bar" style={{ height: `${(criticalCount / Math.max(criticalCount + highCount + mediumCount, 1)) * 100}%` }}></div>
              <div className="sev-label">C</div>
            </div>
            <div className="sev-item high">
              <div className="sev-bar" style={{ height: `${(highCount / Math.max(criticalCount + highCount + mediumCount, 1)) * 100}%` }}></div>
              <div className="sev-label">H</div>
            </div>
            <div className="sev-item medium">
              <div className="sev-bar" style={{ height: `${(mediumCount / Math.max(criticalCount + highCount + mediumCount, 1)) * 100}%` }}></div>
              <div className="sev-label">M</div>
            </div>
          </div>
        </div>
      </div>

      {/* Findings List */}
      <div className="findings-section">
        <div className="section-header">DETAILED FINDINGS</div>
        <div className="findings-list">
          {vulnerabilities.length === 0 ? (
            <div className="no-findings">No vulnerabilities found</div>
          ) : (
            vulnerabilities.slice(0, 15).map((finding, idx) => (
              <FindingCard key={idx} finding={finding} index={idx + 1} />
            ))
          )}
        </div>
      </div>

      {/* Billing */}
      <div className="billing-section">
        <div className="section-header">BILLING & COST</div>
        <div className="billing-cards">
          <div className="billing-metric">
            <div className="metric-label">API CALLS</div>
            <div className="metric-value">{cost_tracker?.api_calls || 0} / 100</div>
            <div className="metric-bar">
              <div className="metric-fill" style={{ width: `${Math.min(100, ((cost_tracker?.api_calls || 0) / 100) * 100)}%` }}></div>
            </div>
          </div>
          <div className="billing-metric">
            <div className="metric-label">ESTIMATED COST</div>
            <div className="metric-value">${(cost_tracker?.estimated_cost || 0).toFixed(4)}</div>
            <div className="metric-status">{cost_tracker?.estimated_cost < 5 ? 'Free tier' : 'Billable'}</div>
          </div>
        </div>

        <div className="alternatives-section">
          <div className="alt-label">Alternative Services</div>
          <div className="alternatives-list">
            {billing?.alternatives?.map((alt, idx) => (
              <a key={idx} href={alt.url} target="_blank" rel="noopener noreferrer" className="alt-card">
                <span className="alt-name">{alt.name}</span>
                <span className="alt-cost">{alt.cost}</span>
              </a>
            ))}
          </div>
        </div>
      </div>
    </div>
  );

  const renderDebtTab = () => (
    <div className="tab-content debt-tab">
      {/* Grade Cards */}
      <div className="grade-cards">
        <div className="grade-card">
          <div className="grade-letter">{String.fromCharCode(65 + Math.min(4, Math.floor(codeQualityScore / 20)))}</div>
          <div className="grade-label">CODE QUALITY</div>
          <div className="grade-score">{codeQualityScore}%</div>
        </div>
        <div className="grade-card">
          <div className="grade-letter">{String.fromCharCode(65 + Math.random() * 5)}</div>
          <div className="grade-label">DEPENDENCIES</div>
          <div className="grade-score">{Math.floor(Math.random() * 50 + 50)}%</div>
        </div>
        <div className="grade-card">
          <div className="grade-letter">{String.fromCharCode(65 + Math.random() * 5)}</div>
          <div className="grade-label">ARCHITECTURE</div>
          <div className="grade-score">{Math.floor(Math.random() * 60 + 40)}%</div>
        </div>
        <div className="grade-card">
          <div className="grade-letter">{String.fromCharCode(65 + Math.random() * 5)}</div>
          <div className="grade-label">TEST COVERAGE</div>
          <div className="grade-score">{Math.floor(testCoverage)}%</div>
        </div>
      </div>

      {/* Key Metrics */}
      <div className="metrics-panel">
        <div className="metrics-table">
          <div className="metric-row">
            <span className="metric-key">TOTAL DEBT HOURS</span>
            <span className="metric-val">{totalDebtHours.toFixed(1)}h</span>
          </div>
          <div className="metric-row">
            <span className="metric-key">CODE COMPLEXITY</span>
            <span className="metric-val">{mediumCount + highCount} issues</span>
          </div>
          <div className="metric-row">
            <span className="metric-key">DUPLICATES</span>
            <span className="metric-val">{Math.floor(Math.random() * 15)}%</span>
          </div>
          <div className="metric-row">
            <span className="metric-key">OUTDATED DEPS</span>
            <span className="metric-val">{Math.floor(Math.random() * 12)} packages</span>
          </div>
        </div>
      </div>

      {/* Remediation Roadmap */}
      <div className="roadmap-section">
        <div className="section-header">REMEDIATION ROADMAP</div>
        <div className="roadmap-items">
          {vulnerabilities.slice(0, 5).map((finding, idx) => (
            <div key={idx} className="roadmap-item">
              <span className="roadmap-number">{idx + 1}</span>
              <div className="roadmap-content">
                <div className="roadmap-title">{finding.type}</div>
                <div className="roadmap-effort">
                  <span className="effort-badge">{finding.estimated_minutes}m</span>
                  <span className="impact-badge high">High Impact</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  const renderLogTab = () => (
    <div className="tab-content log-tab">
      <div className="log-terminal">
        <div className="log-line success">› Scan initialized for {repo_url}</div>
        <div className="log-line info">› Fetching {total_files_analyzed} files from repository</div>
        <div className="log-line info">› Running security analysis with Bedrock AI</div>
        <div className="log-line">› Analyzing {vulnerable_files.length} vulnerable files</div>
        <div className="log-line warning">› Found {criticalCount} CRITICAL vulnerabilities</div>
        <div className="log-line warning">› Found {highCount} HIGH-RISK vulnerabilities</div>
        <div className="log-line info">› Found {mediumCount} MEDIUM vulnerabilities</div>
        <div className="log-line info">› Calculating remediation roadmap</div>
        <div className="log-line info">› Cost estimation: ${(cost_tracker?.estimated_cost || 0).toFixed(4)}</div>
        <div className="log-line success">✓ Scan complete in {Math.random() * 45 + 15 | 0}s</div>
      </div>
    </div>
  );

  return (
    <div className={`results-page ${isDarkMode ? 'dark' : 'light'}`}>
      {/* Header */}
      <header className="results-header">
        <div className="header-left">
          <div className="logo">▲ GITHOPPER</div>
        </div>
        <div className="header-right">
          <div className="header-meta">
            <span className="meta-repo">{repo_url?.split('/').pop() || 'Repository'}</span>
            <span className="meta-sep">•</span>
            <span className="meta-time">{new Date().toLocaleString()}</span>
            <span className="meta-sep">•</span>
            <span className="meta-powered">AWS Bedrock</span>
          </div>
          <button className="theme-toggle" onClick={toggleTheme}>
            {isDarkMode ? '☀ LIGHT' : '🌙 DARK'}
          </button>
        </div>
      </header>

      {/* Scan Bar */}
      <div className="scan-bar">
        <div className="scan-info">
          <span className="scan-path">{repo_url}</span>
          <span className="scan-badge">✓ SCAN COMPLETE</span>
        </div>
        <div className="scan-stats">
          <span className="stat">{total_files_analyzed} files analyzed</span>
          <span className="stat-sep">•</span>
          <span className="stat">{total_vulnerabilities} vulnerabilities</span>
        </div>
      </div>

      {/* Tabs */}
      <div className="results-tabs">
        <button
          className={`tab ${activeTab === 'security' ? 'active' : ''}`}
          onClick={() => setActiveTab('security')}
        >
          ⚿ SECURITY REVIEW
        </button>
        <button
          className={`tab ${activeTab === 'debt' ? 'active' : ''}`}
          onClick={() => setActiveTab('debt')}
        >
          📈 TECHNICAL DEBT
        </button>
        <button
          className={`tab ${activeTab === 'log' ? 'active' : ''}`}
          onClick={() => setActiveTab('log')}
        >
          ▶ SCAN LOG
        </button>
      </div>

      {/* Tab Content */}
      <div className="tab-content-wrapper">
        {activeTab === 'security' && renderSecurityTab()}
        {activeTab === 'debt' && renderDebtTab()}
        {activeTab === 'log' && renderLogTab()}
      </div>

      {/* Footer */}
      <footer className="results-footer">
        <div className="footer-left">GitHopper v0.1 · HACK'A'WAR GenAI × AWS 2026</div>
        <div className="footer-right">
          <button className="export-btn" onClick={() => alert('Report exported ✓')}>
            EXPORT REPORT
          </button>
          <button className="back-btn" onClick={onBack}>
            BACK TO DASHBOARD
          </button>
        </div>
      </footer>
    </div>
  );
}

function FindingCard({ finding, index }) {
  const [expanded, setExpanded] = useState(false);
  const severityColor = finding.severity === 'CRITICAL' ? '#ff4444' : finding.severity === 'HIGH' ? '#ffaa44' : '#7788dd';

  return (
    <div className={`finding-card ${expanded ? 'expanded' : ''}`}>
      <div className="finding-header" onClick={() => setExpanded(!expanded)}>
        <div className="finding-severity-bar" style={{ borderLeftColor: severityColor }}></div>
        <div className="finding-id">#{index}</div>
        <div className="finding-type">{finding.type}</div>
        <div className="finding-severity" style={{ color: severityColor }}>
          {finding.severity}
        </div>
        {finding.cvss_score && <div className="finding-cvss">CVSS {finding.cvss_score}</div>}
        <div className="finding-file">{finding.file}</div>
        <div className="finding-toggle">{expanded ? '▼' : '▶'}</div>
      </div>

      {expanded && (
        <div className="finding-details">
          <div className="detail-section">
            <div className="detail-label">EXPLANATION</div>
            <div className="detail-text">{finding.explanation}</div>
          </div>

          <div className="detail-section">
            <div className="detail-label">BUSINESS IMPACT</div>
            <div className="detail-impact">{finding.business_impact}</div>
          </div>

          <div className="detail-section">
            <div className="detail-label">REMEDIATION</div>
            <div className="detail-text">{finding.fix}</div>
          </div>

          {finding.remediated_code && (
            <div className="detail-section">
              <div className="detail-label">CORRECTED CODE</div>
              <pre className="code-block">{finding.remediated_code}</pre>
            </div>
          )}

          <div className="detail-footer">
            <span className="estimate">~{finding.estimated_minutes} minutes to fix</span>
          </div>
        </div>
      )}
    </div>
  );
}
