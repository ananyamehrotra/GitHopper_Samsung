// Report Page Script

// DOM Elements
const scoreNumber = document.getElementById('scoreNumber');
const repoName = document.getElementById('repoName');
const criticalCount = document.getElementById('criticalCount');
const mediumCount = document.getElementById('mediumCount');
const quickWinsCount = document.getElementById('quickWinsCount');

const criticalSection = document.getElementById('criticalSection');
const quickWinsSection = document.getElementById('quickWinsSection');
const mediumSection = document.getElementById('mediumSection');

const criticalIssuesList = document.getElementById('criticalIssuesList');
const quickWinsIssuesList = document.getElementById('quickWinsIssuesList');
const mediumIssuesList = document.getElementById('mediumIssuesList');

const actionTimeline = document.getElementById('actionTimeline');
const closeBtn = document.getElementById('closeBtn');

// Load report data
let reportData = null;
document.addEventListener('DOMContentLoaded', () => {
    const data = sessionStorage.getItem('reportData');
    if (data) {
        reportData = JSON.parse(data);
        renderReport(reportData);
    } else {
        scoreNumber.textContent = '--';
        repoName.textContent = 'No scan data available';
    }
});

// Create issue card
function createIssueCard(issue) {
    const card = document.createElement('div');
    card.className = `issue-card ${issue.severity.toLowerCase()}`;
    
    const severityLabel = {
        'CRITICAL': 'Critical',
        'HIGH': 'High',
        'MEDIUM': 'Medium',
        'LOW': 'Low'
    }[issue.severity] || issue.severity;
    
    card.innerHTML = `
        <div class="issue-header">
            <div class="issue-type">${issue.type}</div>
            <div class="issue-severity ${issue.severity.toLowerCase()}">${severityLabel}</div>
        </div>
        <div class="issue-location">
            <strong>${issue.file || 'Unknown'}</strong> (Line ${issue.line || 'N/A'})
        </div>
        <div class="issue-description">
            ${issue.explanation}
        </div>
        ${issue.fix ? `
        <div class="issue-fix">
            <div class="issue-fix-label">Suggested Fix:</div>
            <div class="issue-fix-text">${issue.fix}</div>
        </div>
        ` : ''}
        <div class="issue-footer">
            <div class="issue-time">⏱️ ~${issue.estimated_minutes} minutes to fix</div>
            <div class="issue-impact">Impact: ${issue.business_impact ? issue.business_impact.substring(0, 30) + '...' : 'High'}</div>
        </div>
    `;
    
    return card;
}

// Render results
function renderReport(data) {
    // Header
    scoreNumber.textContent = Math.round(data.health_score);
    repoName.textContent = data.repo_url;
    
    // Counts
    const criticalLen = data.critical_issues?.length || 0;
    const mediumLen = data.medium_issues?.length || 0;
    const quickWinsLen = data.quick_wins?.length || 0;
    
    criticalCount.textContent = criticalLen;
    mediumCount.textContent = mediumLen;
    quickWinsCount.textContent = quickWinsLen;
    
    // Critical Issues
    if (criticalLen > 0) {
        criticalIssuesList.innerHTML = '';
        data.critical_issues.forEach(issue => {
            criticalIssuesList.appendChild(createIssueCard(issue));
        });
        criticalSection.style.display = 'block';
    } else {
        criticalSection.style.display = 'none';
    }
    
    // Quick Wins
    if (quickWinsLen > 0) {
        quickWinsIssuesList.innerHTML = '';
        data.quick_wins.forEach(issue => {
            quickWinsIssuesList.appendChild(createIssueCard(issue));
        });
        quickWinsSection.style.display = 'block';
    } else {
        quickWinsSection.style.display = 'none';
    }
    
    // Medium Issues
    if (mediumLen > 0) {
        mediumIssuesList.innerHTML = '';
        data.medium_issues.forEach(issue => {
            mediumIssuesList.appendChild(createIssueCard(issue));
        });
        mediumSection.style.display = 'block';
    } else {
        mediumSection.style.display = 'none';
    }
    
    // Generate action timeline
    generateActionTimeline(data);
}

// Generate action timeline
function generateActionTimeline(data) {
    const allIssues = [
        ...(data.critical_issues || []),
        ...(data.medium_issues || []),
        ...(data.quick_wins || [])
    ];
    
    // Sort by estimated time
    allIssues.sort((a, b) => a.estimated_minutes - b.estimated_minutes);
    
    actionTimeline.innerHTML = '';
    
    let totalTime = 0;
    allIssues.forEach((issue, index) => {
        totalTime += issue.estimated_minutes;
        
        const item = document.createElement('div');
        item.className = 'timeline-item';
        
        item.innerHTML = `
            <div class="timeline-marker">
                <div class="timeline-dot"></div>
            </div>
            <div class="timeline-content">
                <div class="timeline-time">${totalTime} total minutes</div>
                <div class="timeline-title">${issue.type}</div>
                <div class="timeline-description">${issue.explanation.substring(0, 60)}...</div>
            </div>
        `;
        
        actionTimeline.appendChild(item);
    });
}

// Load data on startup
chrome.storage.local.get(['lastScanData'], (result) => {
    if (result.lastScanData) {
        renderReport(result.lastScanData);
    }
});

// Close button
closeBtn.addEventListener('click', () => {
    window.close();
});
