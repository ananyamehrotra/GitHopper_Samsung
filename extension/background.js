// Service Worker for Chrome Extension

// Listen for messages from content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'analyzeRepo') {
        // Forward to popup to handle the scan
        sendResponse({ status: 'received' });
    }
});

// Keep service worker alive
chrome.alarms.create('keepAlive', { periodInMinutes: 1 });

chrome.alarms.onAlarm.addListener((alarm) => {
    if (alarm.name === 'keepAlive') {
        // No-op to keep service worker alive
    }
});
