import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { HomePage } from "./pages/HomePage";
import { LoginPage } from "./pages/LoginPage";
import { SignUpPage } from "./pages/SignUpPage";
import { DashboardPage } from "./pages/DashboardPage";
import { AnalyseBranchesPage } from "./pages/AnalyseBranchesPage";
import { SecurityAuditPage } from "./pages/SecurityAuditPage";
import { DebtReportPage } from "./pages/DebtReportPage";
import { HealthScorePage } from "./pages/HealthScorePage";
import { AnalyticsPage } from "./pages/AnalyticsPage";
import { AppLayout } from "./components/AppLayout";
import { ThemeProvider } from "./context/ThemeContext";
import { UserProvider, useUser } from "./context/UserContext";
import "./styles.css";

function ProtectedRoute({ children }) {
    const { user, loading } = useUser();

    if (loading) {
        return <div style={{ background: 'var(--bg)', height: '100vh' }} />;
    }

    if (!user) {
        return <Navigate to="/login" />;
    }

    return children;
}

function App() {
    return (
        <AppLayout>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/signup" element={<SignUpPage />} />
                <Route path="/dashboard" element={<DashboardPage />} />
                <Route path="/analyse-branches" element={<AnalyseBranchesPage />} />
                <Route path="/security-audit" element={<SecurityAuditPage />} />
                <Route path="/debt-report" element={<DebtReportPage />} />
                <Route path="/health-score" element={<HealthScorePage />} />
                <Route path="/analytics" element={<AnalyticsPage />} />
            </Routes>
        </AppLayout>
    );
}

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <BrowserRouter>
            <ThemeProvider>
                <UserProvider>
                    <App />
                </UserProvider>
            </ThemeProvider>
        </BrowserRouter>
    </React.StrictMode>
);