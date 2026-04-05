import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useTheme } from "../context/ThemeContext";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  AreaChart,
  Area
} from "recharts";
import "./AnalyticsPage.css";

const COLORS = ["#72ea1e", "#ec4899", "#f59e0b", "#ef4444", "#06b6d4", "#8b5cf6"];

export function AnalyticsPage() {
  const { isDark } = useTheme();
  const navigate = useNavigate();
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAnalytics();
  }, []);

  const fetchAnalytics = async () => {
    setLoading(true);
    try {
      const mockData = generateAnalyticsData();
      setAnalytics(mockData);
    } catch (err) {
      console.error("Failed to fetch analytics:", err);
    } finally {
      setLoading(false);
    }
  };

  const generateAnalyticsData = () => {
    return {
      keyMetrics: {
        totalRepos: 24,
        avgHealthScore: 87,
        totalIssuesFound: 156,
        criticalIssues: 12,
        securityIssues: 34,
        debtIssues: 110
      },
      healthScoreTrend: [
        { date: "Apr 2", score: 72 },
        { date: "Apr 3", score: 75 },
        { date: "Apr 4", score: 78 },
        { date: "Apr 5", score: 82 },
        { date: "Apr 6", score: 81 },
        { date: "Apr 7", score: 85 },
        { date: "Apr 8", score: 87 }
      ],
      issueDistribution: [
        { name: "Critical", value: 12 },
        { name: "Security", value: 34 },
        { name: "Debt", value: 110 }
      ],
      repositoryStats: [
        { name: "GitHopper", health: 95, issues: 8 },
        { name: "RepoScan", health: 88, issues: 12 },
        { name: "CodeAudit", health: 82, issues: 18 },
        { name: "DebtTracker", health: 76, issues: 24 },
        { name: "SecureFlow", health: 90, issues: 11 }
      ],
      issuesByType: [
        { type: "Memory Leak", count: 15 },
        { type: "SQL Injection", count: 8 },
        { type: "Dead Code", count: 32 },
        { type: "Unhandled Error", count: 18 },
        { type: "Performance", count: 22 },
        { type: "Dependency", count: 25 }
      ],
      timeSeriesIssues: [
        { week: "W1", critical: 8, security: 12, debt: 45 },
        { week: "W2", critical: 6, security: 14, debt: 48 },
        { week: "W3", critical: 5, security: 16, debt: 52 },
        { week: "W4", critical: 4, security: 18, debt: 38 },
        { week: "W5", critical: 3, security: 15, debt: 32 },
        { week: "W6", critical: 2, security: 12, debt: 28 },
        { week: "W7", critical: 12, security: 34, debt: 110 }
      ]
    };
  };

  if (loading || !analytics) {
    return (
      <div className={`min-h-screen ${isDark ? "bg-slate-950" : "bg-white"}`}>
        <Plasma color="#72ea1e" speed={0.5} opacity={0.08} mouseInteractive />
        <div className="flex items-center justify-center h-screen">
          <div className="text-center">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-lime-500"></div>
            <p className={`mt-4 ${isDark ? "text-gray-400" : "text-gray-600"}`}>Loading Analytics...</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`min-h-screen ${isDark ? "bg-slate-950" : "bg-slate-50"}`}>
      <Plasma color="#72ea1e" speed={0.5} opacity={0.08} mouseInteractive />
      
      {/* Header */}
      <div className={`border-b ${isDark ? "border-slate-800 bg-slate-900/50" : "border-slate-200 bg-white"} backdrop-blur-xl w-full`}>
        <div className="max-w-7xl mx-auto px-6 py-6 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <h1 className={`text-3xl font-bold ${isDark ? "text-lime-400" : "text-lime-600"}`}>
              📊 Analytics
            </h1>
          </div>
          <div className="flex items-center gap-4">
            <button
              onClick={() => navigate("/")}
              className={`px-4 py-2 rounded-lg font-medium transition ${isDark ? "bg-slate-800 text-gray-300 hover:bg-slate-700" : "bg-slate-200 text-slate-700 hover:bg-slate-300"}`}
            >
              ← Back
            </button>
            <ThemeToggle />
            <UserProfile />
          </div>
        </div>
      </div>

      <div className="w-full px-6 py-12">
        <div className="max-w-7xl mx-auto">
          {/* Key Metrics */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
            <MetricCard 
              label="Avg Health Score" 
              value={`${analytics.keyMetrics.avgHealthScore}`}
              subtitle="repositories"
              isDark={isDark}
              color="text-lime-400"
            />
            <MetricCard 
              label="Total Issues Found" 
              value={analytics.keyMetrics.totalIssuesFound.toString()}
              subtitle="across all scans"
              isDark={isDark}
              color="text-rose-400"
            />
            <MetricCard 
              label="Repositories Analyzed" 
              value={analytics.keyMetrics.totalRepos.toString()}
              subtitle="monitored"
              isDark={isDark}
              color="text-cyan-400"
            />
          </div>

          {/* Critical Issues Alert */}
          <div className={`p-6 rounded-xl mb-12 border ${isDark ? "bg-rose-950/20 border-rose-800/50" : "bg-rose-50 border-rose-200"}`}>
            <div className="flex items-center gap-3">
              <span className="text-2xl">⚠️</span>
              <div>
                <h3 className={`font-bold ${isDark ? "text-rose-400" : "text-rose-600"}`}>
                  {analytics.keyMetrics.criticalIssues} Critical Issues Detected
                </h3>
                <p className={`text-sm ${isDark ? "text-rose-300/70" : "text-rose-600/70"}`}>
                  Requires immediate attention
                </p>
              </div>
            </div>
          </div>

          {/* Charts Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
            {/* Health Score Trend */}
            <ChartCard isDark={isDark} title="Health Score Trend">
              <ResponsiveContainer width="100%" height={300}>
                <AreaChart data={analytics.healthScoreTrend}>
                  <defs>
                    <linearGradient id="colorScore" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#72ea1e" stopOpacity={0.8}/>
                      <stop offset="95%" stopColor="#72ea1e" stopOpacity={0}/>
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" stroke={isDark ? "#334155" : "#cbd5e1"} />
                  <XAxis stroke={isDark ? "#94a3b8" : "#64748b"} />
                  <YAxis stroke={isDark ? "#94a3b8" : "#64748b"} />
                  <Tooltip contentStyle={{ background: isDark ? "#1e293b" : "#f8fafc", border: `1px solid ${isDark ? "#334155" : "#cbd5e1"}` }} />
                  <Area type="monotone" dataKey="score" stroke="#72ea1e" fillOpacity={1} fill="url(#colorScore)" />
                </AreaChart>
              </ResponsiveContainer>
            </ChartCard>

            {/* Issue Distribution Pie */}
            <ChartCard isDark={isDark} title="Issue Distribution">
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={analytics.issueDistribution}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, value }) => `${name}: ${value}`}
                    outerRadius={80}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {analytics.issueDistribution.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </ChartCard>
          </div>

          {/* Repository Performance */}
          <ChartCard isDark={isDark} title="Repository Health Scores">
            <ResponsiveContainer width="100%" height={350}>
              <BarChart data={analytics.repositoryStats}>
                <CartesianGrid strokeDasharray="3 3" stroke={isDark ? "#334155" : "#cbd5e1"} />
                <XAxis stroke={isDark ? "#94a3b8" : "#64748b"} />
                <YAxis stroke={isDark ? "#94a3b8" : "#64748b"} />
                <Tooltip contentStyle={{ background: isDark ? "#1e293b" : "#f8fafc", border: `1px solid ${isDark ? "#334155" : "#cbd5e1"}` }} />
                <Legend />
                <Bar dataKey="health" fill="#72ea1e" name="Health Score" />
                <Bar dataKey="issues" fill="#ec4899" name="Issues Count" />
              </BarChart>
            </ResponsiveContainer>
          </ChartCard>

          {/* Issues Over Time */}
          <ChartCard isDark={isDark} title="Issue Breakdown Over Time">
            <ResponsiveContainer width="100%" height={350}>
              <LineChart data={analytics.timeSeriesIssues}>
                <CartesianGrid strokeDasharray="3 3" stroke={isDark ? "#334155" : "#cbd5e1"} />
                <XAxis stroke={isDark ? "#94a3b8" : "#64748b"} />
                <YAxis stroke={isDark ? "#94a3b8" : "#64748b"} />
                <Tooltip contentStyle={{ background: isDark ? "#1e293b" : "#f8fafc", border: `1px solid ${isDark ? "#334155" : "#cbd5e1"}` }} />
                <Legend />
                <Line type="monotone" dataKey="critical" stroke="#ef4444" strokeWidth={2} name="Critical" />
                <Line type="monotone" dataKey="security" stroke="#f59e0b" strokeWidth={2} name="Security" />
                <Line type="monotone" dataKey="debt" stroke="#06b6d4" strokeWidth={2} name="Debt" />
              </LineChart>
            </ResponsiveContainer>
          </ChartCard>

          {/* Top Issues by Type */}
          <ChartCard isDark={isDark} title="Most Common Issue Types">
            <ResponsiveContainer width="100%" height={350}>
              <BarChart
                data={analytics.issuesByType}
                layout="vertical"
                margin={{ top: 5, right: 30, left: 150, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" stroke={isDark ? "#334155" : "#cbd5e1"} />
                <XAxis type="number" stroke={isDark ? "#94a3b8" : "#64748b"} />
                <YAxis dataKey="type" type="category" stroke={isDark ? "#94a3b8" : "#64748b"} width={140} />
                <Tooltip contentStyle={{ background: isDark ? "#1e293b" : "#f8fafc", border: `1px solid ${isDark ? "#334155" : "#cbd5e1"}` }} />
                <Bar dataKey="count" fill="#72ea1e" />
              </BarChart>
            </ResponsiveContainer>
          </ChartCard>
        </div>
      </div>
    </div>
  );
}

function MetricCard({ label, value, subtitle, isDark, color }) {
  return (
    <div className={`p-6 rounded-xl border ${isDark ? "bg-slate-800/50 border-slate-700" : "bg-white border-slate-200"} hover:border-lime-500 transition`}>
      <p className={`text-sm font-medium ${isDark ? "text-gray-400" : "text-gray-600"} mb-2`}>{label}</p>
      <p className={`text-3xl font-bold ${color} mb-2`}>{value}</p>
      <p className={`text-xs ${isDark ? "text-gray-500" : "text-gray-500"}`}>{subtitle}</p>
    </div>
  );
}

function ChartCard({ isDark, title, children }) {
  return (
    <div className={`p-6 rounded-xl border ${isDark ? "bg-slate-800/50 border-slate-700" : "bg-white border-slate-200"}`}>
      <h3 className={`text-lg font-bold mb-6 ${isDark ? "text-white" : "text-slate-900"}`}>{title}</h3>
      {children}
    </div>
  );
}
