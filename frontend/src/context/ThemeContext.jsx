import React, { createContext, useContext, useState, useEffect } from 'react';

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
    const [isDark, setIsDark] = useState(() => {
        // Check localStorage for saved theme preference
        const saved = localStorage.getItem('theme');
        if (saved) {
            return saved === 'dark';
        }
        // Default to dark mode
        return true;
    });

    useEffect(() => {
        // Update localStorage and DOM immediately
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        const root = document.documentElement;

        // Force immediate attribute update
        root.removeAttribute('data-theme');
        setTimeout(() => {
            root.setAttribute('data-theme', isDark ? 'dark' : 'light');
        }, 0);

        // Also add/remove class for extra specificity
        if (isDark) {
            root.classList.remove('light-mode');
            root.classList.add('dark-mode');
        } else {
            root.classList.remove('dark-mode');
            root.classList.add('light-mode');
        }
    }, [isDark]);

    const toggleTheme = () => {
        setIsDark(prev => !prev);
    };

    return (
        <ThemeContext.Provider value={{ isDark, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

export function useTheme() {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error('useTheme must be used within ThemeProvider');
    }
    return context;
}
