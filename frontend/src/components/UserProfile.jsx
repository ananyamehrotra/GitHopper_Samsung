import React, { useState, useRef, useEffect } from 'react';
import { useUser } from '../context/UserContext';
import { useNavigate } from 'react-router-dom';
import './UserProfile.css';

export function UserProfile() {
    const { user, logout } = useUser();
    const [showDropdown, setShowDropdown] = useState(false);
    const dropdownRef = useRef(null);
    const navigate = useNavigate();

    useEffect(() => {
        function handleClickOutside(event) {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
                setShowDropdown(false);
            }
        }

        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    const handleLogout = async () => {
        await logout();
        navigate('/login');
    };

    if (!user) return null;

    return (
        <div className="user-profile" ref={dropdownRef}>
            <button
                className="profile-button"
                onClick={() => setShowDropdown(!showDropdown)}
                aria-label="User profile"
            >
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="8" r="4" fill="currentColor" />
                    <path d="M 4 20 C 4 15.58 7.58 12 12 12 C 16.42 12 20 15.58 20 20" fill="currentColor" />
                </svg>
            </button>

            {showDropdown && (
                <div className="profile-dropdown">
                    <div className="dropdown-header">
                        <p className="user-email">{user.email}</p>
                    </div>
                    <button className="logout-button" onClick={handleLogout}>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M17 16L21 12M21 12L17 8M21 12H9M9 3H7C5.9 3 5 3.9 5 5V19C5 20.1 5.9 21 7 21H9" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                        </svg>
                        Logout
                    </button>
                </div>
            )}
        </div>
    );
}
