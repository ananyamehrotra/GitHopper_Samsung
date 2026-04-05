// Popup Script for GitHopper Extension

// DOM Elements
const repoUrl = document.getElementById('repoUrl');
const scanBtn = document.getElementById('scanBtn');
const loading = document.getElementById('loading');
const inputSection = document.getElementById('inputSection');
const errorSection = document.getElementById('errorSection');
const errorText = document.getElementById('errorText');
const resultsSection = document.getElementById('resultsSection');
const healthScore = document.getElementById('healthScore');
const statsGrid = document.getElementById('statsGrid');
const criticalSection = document.getElementById('criticalSection');
const criticalList = document.getElementById('criticalList');
const quickWinsSection = document.getElementById('quickWinsSection');
const quickWinsList = document.getElementById('quickWinsList');
const mediumSection = document.getElementById('mediumSection');
const mediumList = document.getElementById('mediumList');
const fullReportBtn = document.getElementById('fullReportBtn');
const newScanBtn = document.getElementById('newScanBtn');
const retryBtn = document.getElementById('retryBtn');

let currentScanData = null;

// Event Listeners
scanBtn.addEventListener('click', handleScan);
retryBtn.addEventListener('click', () => showSection('input'));
newScanBtn.addEventListener('click', () => showSection('input'));
fullReportBtn.addEventListener('click', openFullReport);

// Handle repository scan
async function handleScan() {
    const repo = repoUrl.value.trim();
    
    if (!repo) {
        showError('Please enter a repository URL');
        return;
    }

    // Validate repo format
    if (!repo.includes('/')) {
        showError('Please use format: username/repository');
        return;
    }

    showSection('loading');
    
    try {
        const fullUrl = `https://github.com/${repo}`;
        const response = await fetch('http://localhost:5000/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                repo_url: fullUrl
            })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        
        // Map the response to our display format
        const mappedData = mapAnalyzeResponse(data);
        currentScanData = mappedData;
        
        displayResults(mappedData);
        showSection('results');
        
        // Save to session storage for full report
        sessionStorage.setItem('lastScanData', JSON.stringify(mappedData));
        
    } catch (error) {
        console.error('Scan error:', error);
        showError(error.message || 'Failed to analyze repository. Make sure the backend is running on http://localhost:5000');
    }
}

// Map the backend response to our display format
function mapAnalyzeResponse(data) {
    // Extract health score
    const overallHealth = data.health_score?.overall_health || 0;
    
    // Extract security findings
    const securityFindings = data.security_audit?.findings || [];
    
    // Extract debt findings
    const debtFindings = data.debt_report?.findings || [];
    
    // Extract quick wins
    const quickWins = data.quick_wins || [];
    
    // Categorize all issues by severity
    const allIssues = [...securityFindings, ...debtFindings];
    
    const criticalIssues = allIssues.filter(i => i.severity === 'CRITICAL' || i.severity === 'HIGH');
    const mediumIssues = allIssues.filter(i => i.severity === 'MEDIUM');
    const lowIssues = allIssues.filter(i => i.severity === 'LOW');
    
    return {
        health_score: Math.round(overallHealth),
        repo_url: data.repo_url || 'Unknown Repository',
        critical_issues: criticalIssues,
        medium_issues: mediumIssues,
        low_issues: lowIssues,
        quick_wins: quickWins,
        raw_data: data
    };
}

// Display scan results
function displayResults(data) {
    // Update health score
    healthScore.textContent = data.health_score;
    
    // Update statistics grid
    statsGrid.innerHTML = `
        <div class="stat-item">
            <span class="stat-label">Critical Issues</span>
            <span class="stat-value critical">${data.critical_issues.length}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Medium Issues</span>
            <span class="stat-value warning">${data.medium_issues.length}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Quick Wins</span>
            <span class="stat-value success">${data.quick_wins.length}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Total Issues</span>
            <span class="stat-value">${data.critical_issues.length + data.medium_issues.length}</span>
        </div>
    `;
    
    // Display critical issues
    if (data.critical_issues.length > 0) {
        criticalList.innerHTML = '';
        data.critical_issues.forEach(issue => {
            criticalList.appendChild(createIssueElement(issue));
        });
        criticalSection.classList.remove('hidden');
    } else {
        criticalSection.classList.add('hidden');
    }
    
    // Display quick wins
    if (data.quick_wins.length > 0) {
        quickWinsList.innerHTML = '';
        data.quick_wins.forEach(win => {
            quickWinsList.appendChild(createIssueElement(win));
        });
        quickWinsSection.classList.remove('hidden');
    } else {
        quickWinsSection.classList.add('hidden');
    }
    
    // Display medium issues
    if (data.medium_issues.length > 0) {
        mediumList.innerHTML = '';
        data.medium_issues.forEach(issue => {
            mediumList.appendChild(createIssueElement(issue));
        });
        mediumSection.classList.remove('hidden');
    } else {
        mediumSection.classList.add('hidden');
    }
}

// Create an issue element
function createIssueElement(issue) {
    const div = document.createElement('div');
    div.className = 'issue-item';
    
    const severity = issue.severity || 'LOW';
    const severityClass = severity.toLowerCase();
    
    div.innerHTML = `
        <div class="issue-header">
            <span class="issue-severity ${severityClass}">${severity}</span>
            <span class="issue-type">${issue.type || 'Unknown Issue'}</span>
        </div>
        ${issue.file ? `<div class="issue-file">${issue.file}</div>` : ''}
        ${issue.explanation ? `<div class="issue-explanation">${issue.explanation}</div>` : ''}
    `;
    
    return div;
}

// Open full report in new tab
function openFullReport() {
    if (!currentScanData) return;
    
    // Store data and open report page
    sessionStorage.setItem('reportData', JSON.stringify(currentScanData));
    chrome.tabs.create({ 
        url: chrome.runtime.getURL('report.html')
    });
}

// Show/hide sections
function showSection(section) {
    loading.classList.add('hidden');
    inputSection.classList.add('hidden');
    errorSection.classList.add('hidden');
    resultsSection.classList.add('hidden');
    
    switch(section) {
        case 'loading':
            loading.classList.remove('hidden');
            break;
        case 'input':
            inputSection.classList.remove('hidden');
            repoUrl.value = '';
            repoUrl.focus();
            break;
        case 'error':
            errorSection.classList.remove('hidden');
            break;
        case 'results':
            resultsSection.classList.remove('hidden');
            break;
    }
}

// Show error message
function showError(message) {
    errorText.textContent = message;
    showSection('error');
}

// Load saved repository on popup open
document.addEventListener('DOMContentLoaded', () => {
    chrome.storage.local.get('lastRepo', (result) => {
        if (result.lastRepo) {
            repoUrl.value = result.lastRepo;
        }
    });
});

// Save repository on input change
repoUrl.addEventListener('change', () => {
    chrome.storage.local.set({ lastRepo: repoUrl.value });
});
