# 🦗 GitHopper

**Your intelligent Git repository analysis and insights platform**

**[Presentation](https://docs.google.com/presentation/d/1CSmJBo3YKx8wUpJAQLEz3bmbu31Gqo0U/edit?usp=sharing&ouid=100394359056483753626&rtpof=true&sd=true)** 
**[Video](https://drive.google.com/file/d/1duEMIEW_n8Vmok0jRB5xx1lBMr8fv_dT/view?usp=sharing)**
**[AI Disclosure](https://docs.google.com/document/d/1vnD8E_E_yJUvQlfH6V-CP6yfm85Xg-7U/edit?usp=sharing&ouid=100394359056483753626&rtpof=true&sd=true)**

## 🚨 Problem Statement

*“I know technical debt is piling up, but where do I even start? I am already broke.”*  
*“I don’t have hours to read massive audit report. I need to focus on my business.”*  
*“I just joined and this repo is older than me. How do I even fix this?”*  

GitHopper solves a major problem in modern security tools: **they detect issues but rarely explain them clearly.** Most scanners overwhelm developers with technical warnings like *“B105 hardcoded password string, HIGH severity.”* 

**GitHopper** takes the same finding and outputs: *"Your password is written directly in code. If this repo ever goes public, attackers have valid credentials instantly. Fix: move it to a .env file, load via python-dotenv, add .env to .gitignore. Takes ~15 minutes."*

Same finding. Completely different outcome.

---

## 🌟 Our Theme

- **On-Device:** When you're scanning for hardcoded secrets and exposed tokens, you cannot send that code to a cloud API — that is the vulnerability. Every scan runs locally via Ollama. Code never leaves the machine.
- **Productivity:** A developer who gets 47 findings with CVE IDs and no context closes the tab and ships anyway. GitHopper turns scanner noise into a 5-minute prioritized fix list.

---

## ❌ Current Solutions & Gaps

*What's missing?* None of these tools answer: **"I'm a junior developer with 3 hours this week — what do I fix, in what order, and how?"** Every existing tool is designed for security engineers to review findings. GitHopper is designed for developers to fix them. That difference shapes every decision from delivering alerts directly to developers’ devices, to generating plain-English fixes with estimated repair time, to continuous monitoring through OpenClaw automation instead of manually configured security pipelines.

| Tool | Does | Fails At |
|------|------|----------|
| **Snyk** | Dependency CVE matching | Expensive ($98/month), zero explanation, no tech debt coverage |
| **SonarQube** | Deep static analysis | Engineer-facing dashboards, painful to self-host, not beginner-friendly |
| **Gitleaks** | Fast secret detection | Only secrets, no explanation, no remediation, no monitoring |
| **Dependabot** | Auto PR for dependency updates | Only known CVEs, ignores everything else |
| **Semgrep** | Fast pattern matching | Requires rule-writing, raw output with no contextual explanation |

---

## 💡 Our Solution

GitHopper is a repo health monitoring skill built on **OpenClaw**. Connect your repo once — OpenClaw's agent runs persistently, rescanning automatically via HEARTBEAT scheduling. 

### Key Features
- **Parallel Dual Pipeline**: 
  - **Security pipeline:** Custom scan for hardcoded secrets, exposed tokens, and insecure configs pattern-matched against real credential formats like AWS key prefixes and GitHub token structures.
  - **Debt Analysis Pipeline:** Runs parallel to security scanning. Flags function bloat, cyclomatic complexity, outdated dependencies, and weak architecture patterns.
- **Entirely On-Device AI Inference**: Each confirmed finding goes to Ollama with the finding type, code context, and developer experience level. Returns a plain-English explanation, severity, fix time estimate, and remediation steps. Code never leaves the machine.
- **Continuous Monitoring & Zero Config**: Simply plug it in and it runs intelligently via MCP.
- **Health Cards & Real-Time Delivery**: All findings are packaged into one Health Card and pushed simultaneously to Discord, Slack, and other platforms in real time — formatted natively for each platform.

---

## 🚀 Quick Start & Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/ananyamehrotra/githoppermain.git
cd githoppermain
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

**Configure `backend/.env`:**
```env
GITHUB_TOKEN=your_github_token
# Run entirely on-device via Ollama
OPENCLAW_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1
DISCORD_WEBHOOK_URL=your_discord_webhook_url
DISCORD_REPORT_BASE_URL=https://drive.google.com/file/d/1zesrKhXqjfVjO_go-xRtm9Bm4flaX3ZS/view?usp=sharing
```

**Run the Backend:**
```bash
python app.py
```
*Backend runs on `http://localhost:5001`*

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*Frontend runs on `http://localhost:5173`*

---

## 🎮 How to Use (Product Walkthrough)

### 1. The Web Server (Dashboard)
- Navigate to `http://localhost:5173/dashboard` in your browser.
- Enter your GitHub repository URL and branch name.
- Click **"Analyse"** for a one-time scan or **"Watch Live"** to start Continuous Intelligence mode.
- Dive into the **Security Audit**, **Debt Report**, or **Health Score** to see detailed, plain-English fixes prioritizing your time based on severity.
- Generate and download PDF reports directly from the interface.

### 2. The MCP Server (Continuous Intelligence)
- In "Watch Live" mode, the MCP server tracks your repository in the background.
- It detects incremental changes, ensuring that it only rescans modified files.
- It automatically assesses code debt and generates **Health Cards** that are instantly pushed out to your connected webhooks (like Discord).

---

## 🛠️ Tech Stack

- **Frontend**: React 18, Vite, Three.js (Plasma UI), Firebase
- **Backend**: Python 3.8+, Flask, Model Context Protocol (MCP) Runtime
- **AI / LLM**: OpenClaw Framework, Ollama (Local AI Inference)
- **Integrations**: GitHub API, Discord Webhooks

---

## 🤝 Team
- **Ananya Mehrotra** & Team
- Built for Samsung PRISM OpenClaw Hackathon

---
**Happy Hopping! 🦘**


## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ananyamehrotra/githoppermain.git
cd githoppermain
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run backend
python app.py
```

The backend will start at `http://localhost:5000`

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
# or
yarn install

# Start development server
npm run dev
# or
yarn dev
```

The frontend will be available at `http://localhost:5173` (Vite default)

## 📁 Project Structure

```
githoppermain/
│
├── backend/                      # Flask Python backend
│   ├── app.py                   # Main application entry point
│   ├── requirements.txt          # Python dependencies
│   ├── requirements-mcp.txt     # MCP-specific dependencies
│   ├── ai/                      # AI/ML modules
│   │   ├── openclaw_client.py # OpenClaw-compatible LLM integration
│   │   ├── prompts.py          # AI prompts
│   │   └── synthesizer.py      # Response synthesis
│   ├── mcp_server/              # Model Context Protocol server
│   │   ├── analyzer.py         # Code analysis engine
│   │   ├── autofix.py          # Automated fixes
│   │   ├── continuous_pipeline.py
│   │   ├── diffing.py          # Diff analysis
│   │   └── watcher.py          # File watching
│   ├── lambdas/                 # AWS Lambda handlers
│   │   ├── fetcher/            # Data fetching
│   │   ├── processor/          # Data processing
│   │   └── scorer/             # Scoring engine
│   ├── utils/                   # Utility modules
│   ├── tests/                   # Test files
│   └── scan_results/            # Cached scan results
│
├── frontend/                     # React Vite frontend
│   ├── src/
│   │   ├── components/          # React components
│   │   │   ├── AppLayout.jsx
│   │   │   ├── Plasma.jsx       # 3D Plasma animation
│   │   │   ├── ThemeToggle.jsx
│   │   │   └── UserProfile.jsx
│   │   ├── context/             # React context
│   │   │   ├── ThemeContext.jsx
│   │   │   └── UserContext.jsx
│   │   ├── pages/               # Page components
│   │   │   ├── HomePage.jsx
│   │   │   ├── DashboardPage.jsx
│   │   │   ├── AnalyseBranchesPage.jsx
│   │   │   ├── HealthScorePage.jsx
│   │   │   ├── DebtReportPage.jsx
│   │   │   └── AuthPages.jsx
│   │   ├── services/            # API services
│   │   ├── main-home.jsx        # Main entry point
│   │   └── styles.css           # Global styles
│   ├── public/                  # Static assets
│   ├── package.json             # Node dependencies
│   ├── vite.config.js           # Vite configuration
│   ├── tailwind.config.js       # Tailwind configuration
│   └── postcss.config.js        # PostCSS configuration
│
├── mcp/                         # MCP documentation and workflow
│   ├── ANTIGRAVITY_WORKFLOW.md
│   ├── MCP_CONTINUOUS_INTELLIGENCE_PLAN.md
│   └── MCP_SERVER_TEST_AND_INTEGRATION.md
│
├── plugins/                     # Plugin and extension system
│   └── antigravity-reposcan-mcp/
│       ├── skills/             # Reusable skills
│       └── hooks.json
│
└── README.md                    # This file
```


## 📡 API Documentation

### Health Check
```
GET /api/health
```
Check if the backend is running.

### Scan Repository
```
POST /api/scan
Content-Type: application/json

{
  "repo_url": "https://github.com/username/repo"
}
```
Initiate a repository scan.

### Get Health Score
```
GET /api/health-score/:repo_id
```
Retrieve the health score for a repository.

### Get Technical Debt Report
```
GET /api/debt-report/:repo_id
```
Get the technical debt analysis.

### Analyze Branches
```
POST /api/analyze-branches
Content-Type: application/json

{
  "repo_url": "https://github.com/username/repo",
  "branches": ["main", "develop"]
}
```
Compare and analyze specific branches.

## 🏃 Running for Development

### Terminal 1: Backend
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

### Terminal 2: Frontend
```bash
cd frontend
npm run dev
```

### Build for Production

**Backend:**
```bash
# Create a production-ready distribution
pip freeze > requirements.txt
# Then deploy using Docker or cloud platform
```

**Frontend:**
```bash
npm run build
# Creates optimized build in dist/ directory
```


## 📚 Documentation

- [Backend README](./backend/README.md) - Detailed backend documentation
- [Frontend README](./frontend/README.md) - Frontend setup and components
- [MCP Workflow](./mcp/ANTIGRAVITY_WORKFLOW.md) - Model Context Protocol workflow
- [MCP Continuous Intelligence Plan](./mcp/MCP_CONTINUOUS_INTELLIGENCE_PLAN.md)

## 🔐 Security

- Never commit `.env` files
- Use environment variables for sensitive data
- Validate all user inputs
- Keep dependencies updated regularly

- OpenClaw-compatible LLM provider for AI capabilities
- GitHub for repository access API
- React, Vite, and Flask communities
- All open-source contributors

---

**Happy Hopping! 🦘**

Made with ❤️ by the GitHopper team
