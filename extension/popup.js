// Configuration
const API_BASE_URL = 'http://localhost:5001';

// DOM Elements
const inputSection = document.getElementById('inputSection');
const loadingSection = document.getElementById('loading');
const errorSection = document.getElementById('errorSection');
const resultsSection = document.getElementById('resultsSection');

const repoUrlInput = document.getElementById('repoUrl');
const scanBtn = document.getElementById('scanBtn');
const retryBtn = document.getElementById('retryBtn');
const newScanBtn = document.getElementById('newScanBtn');
const fullReportBtn = document.getElementById('fullReportBtn');
const errorText = document.getElementById('errorText');

// Statistics and Issues Elements
const healthScore = document.getElementById('healthScore');
const statsGrid = document.getElementById('statsGrid');
const criticalSection = document.getElementById('criticalSection');
const criticalList = document.getElementById('criticalList');
const quickWinsSection = document.getElementById('quickWinsSection');
const quickWinsList = document.getElementById('quickWinsList');
const mediumSection = document.getElementById('mediumSection');
const mediumList = document.getElementById('mediumList');

// Load saved repo URL on startup
function loadSavedUrl() {
    chrome.storage.local.get(['lastRepoUrl'], (result) => {
        if (result.lastRepoUrl) {
            repoUrlInput.value = result.lastRepoUrl;
        }
    });
}

// Extract repo URL from GitHub page if on GitHub
function extractGitHubUrl() {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const url = tabs[0].url;
        if (url && url.includes('github.com/')) {
            const match = url.match(/github\.com\/([^/]+)\/([^/]+)/);
            if (match) {
                repoUrlInput.value = `${match[1]}/${match[2]}`;
            }
        }
    });
}

// Show section
function showSection(section) {
    inputSection.classList.add('hidden');
    loadingSection.classList.add('hidden');
    errorSection.classList.add('hidden');
    resultsSection.classList.add('hidden');
    section.classList.remove('hidden');
}

// Format repository URL
function formatRepoUrl(input) {
    if (input.startsWith('https://github.com/')) {
        return input;
    }
    if (input.startsWith('github.com/')) {
        return 'https://' + input;
    }
    return `https://github.com/${input}`;
}

// Create issue item element
function createIssueElement(issue) {
    const div = document.createElement('div');
    div.className = `issue-item ${issue.severity.toLowerCase()}`;
    
    div.innerHTML = `
        <div class="issue-type">${issue.type}</div>
        <div class="issue-description">${issue.explanation}</div>
        <div class="issue-time">⏱️ ~${issue.estimated_minutes} minutes to fix</div>
    `;
    
    return div;
}

// Render results
function renderResults(data) {
    // Health Score
    healthScore.textContent = Math.round(data.health_score);
    
    // Statistics
    statsGrid.innerHTML = '';
    const stats = data.statistics || {};
    
    const statItems = [
        { label: 'Critical Issues', value: data.critical_issues?.length || 0 },
        { label: 'Quick Wins', value: data.quick_wins?.length || 0 },
        { label: 'Medium Issues', value: data.medium_issues?.length || 0 },
        { label: 'Total Findings', value: (data.critical_issues?.length || 0) + (data.quick_wins?.length || 0) + (data.medium_issues?.length || 0) }
    ];
    
    statItems.forEach(stat => {
        const element = document.createElement('div');
        element.className = 'stat';
        element.innerHTML = `
            <div class="stat-value">${stat.value}</div>
            <div class="stat-label">${stat.label}</div>
        `;
        statsGrid.appendChild(element);
    });
    
    // Critical Issues
    if (data.critical_issues && data.critical_issues.length > 0) {
        criticalList.innerHTML = '';
        data.critical_issues.forEach(issue => {
            criticalList.appendChild(createIssueElement(issue));
        });
        criticalSection.classList.remove('hidden');
    } else {
        criticalSection.classList.add('hidden');
    }
    
    // Quick Wins
    if (data.quick_wins && data.quick_wins.length > 0) {
        quickWinsList.innerHTML = '';
        data.quick_wins.forEach(issue => {
            quickWinsList.appendChild(createIssueElement(issue));
        });
        quickWinsSection.classList.remove('hidden');
    } else {
        quickWinsSection.classList.add('hidden');
    }
    
    // Medium Issues
    if (data.medium_issues && data.medium_issues.length > 0) {
        mediumList.innerHTML = '';
        data.medium_issues.forEach(issue => {
            mediumList.appendChild(createIssueElement(issue));
        });
        mediumSection.classList.remove('hidden');
    } else {
        mediumSection.classList.add('hidden');
    }
    
    showSection(resultsSection);
}

// Perform scan
async function performScan(repoUrl) {
    try {
        showSection(loadingSection);
        
        const formattedUrl = formatRepoUrl(repoUrl);
        
        // Save the repo URL
        chrome.storage.local.set({ lastRepoUrl: repoUrl });
        
        const response = await fetch(`${API_BASE_URL}/api/scan`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ repo_url: formattedUrl })
        });
        
        if (!response.ok) {
            throw new Error(`API returned status ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        // Store results for full report
        chrome.storage.local.set({ lastScanData: data });
        
        renderResults(data);
    } catch (error) {
        console.error('Scan error:', error);
        errorText.textContent = error.message || 'Failed to scan repository. Make sure the backend server is running on http://localhost:5001';
        showSection(errorSection);
    }
}

// Event Listeners
scanBtn.addEventListener('click', () => {
    const url = repoUrlInput.value.trim();
    if (url) {
        performScan(url);
    } else {
        errorText.textContent = 'Please enter a valid GitHub repository URL (e.g., username/repository)';
        showSection(errorSection);
    }
});

repoUrlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        scanBtn.click();
    }
});

retryBtn.addEventListener('click', () => {
    showSection(inputSection);
});

newScanBtn.addEventListener('click', () => {
    repoUrlInput.value = '';
    showSection(inputSection);
    repoUrlInput.focus();
});

fullReportBtn.addEventListener('click', () => {
    chrome.storage.local.get(['lastScanData'], (result) => {
        if (result.lastScanData) {
            // Open a new window with the full report
            chrome.windows.create({
                url: `chrome-extension://${chrome.runtime.id}/report.html`,
                type: 'popup',
                width: 1200,
                height: 800
            });
        }
    });
});

// Initialize
loadSavedUrl();
extractGitHubUrl();
