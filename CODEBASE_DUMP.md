# 📚 GitHopper Complete Codebase Dump

**Generated:** 2026-04-01 23:57:26
**Repository:** githoppermain
**Total Files:** 89

---

## 📑 Table of Contents

- **.agents\plugins/**
  - marketplace.json
- **./**
  - CODEBASE_DUMPER_GUIDE.md
  - README.md
- **backend/**
  - README.md
- **backend\ai/**
  - bedrock_client.py
  - prompts.py
  - synthesizer.py
- **backend/**
  - ananya_flagged_files.json
  - app.py
  - chunker.py
  - flagged_files.json
  - github_client.py
- **backend\lambdas\fetcher/**
  - handler.py
- **backend\lambdas\processor/**
  - handler.py
- **backend\lambdas\scorer/**
  - handler.py
- **backend/**
  - mcp_runtime_server.py
- **backend\mcp_server/**
  - __init__.py
  - analyzer.py
  - autofix.py
  - context.py
  - continuous_pipeline.py
  - diffing.py
  - prompting.py
  - storage.py
  - watcher.py
- **backend/**
  - package-lock.json
  - pipeline.py
  - requirements-mcp.txt
  - requirements.txt
- **backend\tests/**
  - local_test.py
- **backend\tests\test_chunks/**
  - requirements.txt
  - sample_app.py
  - sample_iam.json
- **backend\utils/**
  - chunker.py
  - file_classifier.py
  - github_client.py
- **./**
  - codebase_dumper.py
- **frontend/**
  - README.md
  - components.json
  - index.html
  - jsconfig.json
  - package-lock.json
  - package.json
  - postcss.config.js
- **frontend\src\components/**
  - AppLayout.jsx
  - Plasma.css
  - Plasma.jsx
  - PlasmaBackground.css
  - PlasmaBackground.jsx
  - ShinyText.css
  - ShinyText.jsx
  - ThemeToggle.css
  - ThemeToggle.jsx
  - UserProfile.css
  - UserProfile.jsx
- **frontend\src\context/**
  - ThemeContext.jsx
  - UserContext.jsx
- **frontend\src/**
  - main-home.jsx
- **frontend\src\pages/**
  - AnalyseBranchesPage.css
  - AnalyseBranchesPage.jsx
  - AuthPages.css
  - DashboardPage.css
  - DashboardPage.jsx
  - DebtReportPage.css
  - DebtReportPage.jsx
  - HealthScorePage.css
  - HealthScorePage.jsx
  - HomePage.css
  - HomePage.jsx
  - LoginPage.jsx
  - SecurityAuditPage.css
  - SecurityAuditPage.jsx
  - SignUpPage.jsx
- **frontend\src\services/**
  - firebase.js
- **frontend\src/**
  - styles.css
- **frontend/**
  - tailwind.config.js
  - vite.config.js
- **mcp/**
  - ANTIGRAVITY_WORKFLOW.md
  - MCP_CONTINUOUS_INTELLIGENCE_PLAN.md
  - MCP_SERVER_TEST_AND_INTEGRATION.md
- **plugins\antigravity-reposcan-mcp/**
  - .app.json
- **plugins\antigravity-reposcan-mcp\.codex-plugin/**
  - plugin.json
- **plugins\antigravity-reposcan-mcp/**
  - .mcp.json
  - README.md
  - antigravity.mcp.template.json
  - antigravity.sync.template.json
  - hooks.json
- **plugins\antigravity-reposcan-mcp\skills/**
  - README.md
- **./**
  - update_codebase_dump.sh

---

# 📂 File Contents

## [1] .agents/plugins/marketplace.json
**Size:** 452.0B

```json
{
  "name": "antigravity-local-marketplace",
  "interface": {
    "displayName": "Antigravity Local Marketplace"
  },
  "plugins": [
    {
      "name": "antigravity-reposcan-mcp",
      "source": {
        "source": "local",
        "path": "./plugins/antigravity-reposcan-mcp"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}

```

---

## [2] CODEBASE_DUMPER_GUIDE.md
**Size:** 4.9KB

```markdown
# 📚 Codebase Dumper Guide

This tool automatically consolidates your entire codebase into a single, easy-to-read markdown file.

## What It Does

The codebase dumper scans your entire project and creates `CODEBASE_DUMP.md` containing:
- ✨ A complete table of contents
- 📂 All source code files with proper syntax highlighting
- 📊 File sizes and organization
- 🔍 Easy searchable reference of your entire codebase

## Setup

### First Time Setup

The dumper scripts are already included in the repository:

- **Windows:** `update_codebase_dump.bat`
- **macOS/Linux:** `update_codebase_dump.sh`
- **Python Script:** `codebase_dumper.py`

No additional installation needed!

## How to Use

### Windows Users

Simply double-click the batch file:
```
update_codebase_dump.bat
```

Or run from command prompt:
```cmd
update_codebase_dump.bat
```

### macOS/Linux Users

Run the shell script from terminal:
```bash
bash update_codebase_dump.sh
```

Or make it executable first:
```bash
chmod +x update_codebase_dump.sh
./update_codebase_dump.sh
```

### Manual Python Execution (All Platforms)

```bash
python3 codebase_dumper.py
```

## Output

After running, you'll get:
- ✅ `CODEBASE_DUMP.md` - Complete codebase in one file
- 📊 File count and total size information
- ⏱️ Generation timestamp

## What Gets Included

**Included file types:**
- Python files (`.py`)
- JavaScript/TypeScript (`.js`, `.jsx`, `.ts`, `.tsx`)
- Web files (`.html`, `.css`, `.scss`)
- Configuration (`.json`, `.yaml`, `.yml`, `.toml`)
- Documentation (`.md`, `.txt`)
- Scripts (`.sh`, `.bat`, `.dockerfile`)

**Excluded directories:**
- `node_modules/` - npm dependencies
- `venv/` / `env/` - Python virtual environments
- `.git/` - Git history
- `__pycache__/` - Python cache
- `dist/` / `build/` - Build outputs
- `mcp_data/` - Data files
- `scan_results/` - Result files
- `.env` - Secret environment files
- `public/` - Static assets

## Automation

### Auto-Update on Commit (Git Hook)

Create a `.git/hooks/post-commit` file (no extension):

**For macOS/Linux:**
```bash
#!/bin/bash
python3 codebase_dumper.py
git add CODEBASE_DUMP.md
```

**For Windows PowerShell:**
```powershell
python3 codebase_dumper.py
git add CODEBASE_DUMP.md
```

Then make it executable:
```bash
chmod +x .git/hooks/post-commit
```

### Scheduled Updates

**Windows Task Scheduler:**
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Daily at your preferred time
4. Action: `update_codebase_dump.bat`

**macOS/Linux Cron:**
```bash
# Daily at 2 AM
0 2 * * * cd /path/to/githoppermain && bash update_codebase_dump.sh
```

## Using CODEBASE_DUMP.md

### View in VS Code
- Open `CODEBASE_DUMP.md` in the editor
- Use Ctrl+F (Cmd+F on Mac) to search
- Use breadcrumbs to navigate sections

### View in Browser
- Open the file with your markdown renderer
- Many online viewers support markdown files
- GitHub automatically renders it

### Share with Team
- Commit to repository for team access
- Use as documentation reference
- Share with AI assistants for context

## Troubleshooting

### "Python not found"
Install Python 3.8+ from [python.org](https://www.python.org)

### File is too large
The dump can be large for big projects. You can:
- Open in VS Code (optimized for large files)
- Use a markdown viewer that handles large files
- Search within VS Code using Ctrl+F

### Permissions Error (macOS/Linux)
```bash
chmod +x update_codebase_dump.sh
./update_codebase_dump.sh
```

## Performance Notes

- **Small projects (<1000 files):** < 1 second
- **Medium projects:** 1-5 seconds
- **Large projects:** 5-30 seconds

The dump is read-only and won't modify your source code.

## Examples

### Search for a Function
Open `CODEBASE_DUMP.md` and use Ctrl+F to find your function:
```
Ctrl+F → "def my_function"
```

### Browse Organization
Check the table of contents to see project structure at a glance.

### Share with AI
Copy relevant sections of the dump to:
- GitHub Copilot
- Claude
- ChatGPT
- Other AI assistants

## Pro Tips

1. **Commit regularly** - The dump shows code at generation time
2. **Use with version control** - Compare dumps to see what changed
3. **Share with new team members** - Great onboarding reference
4. **Include in documentation** - Link to specific sections
5. **Archive old dumps** - Keep history of project evolution

## Advanced Configuration

To customize what gets included, edit `codebase_dumper.py`:

```python
# Line ~20: Add extensions to INCLUDE_EXTENSIONS
INCLUDE_EXTENSIONS = {
    '.py', '.js', '.ts',  # Add your custom extensions here
}

# Line ~30: Add folders to EXCLUDE_DIRS
EXCLUDE_DIRS = {
    'folder_to_skip',
    'another_folder',
}
```

---

**Happy coding!** 🚀

For updates to the dumper, check the main repository.

```

---

## [3] README.md
**Size:** 10.4KB

```markdown
# 🦘 GitHopper

**Your intelligent Git repository analysis and insights platform**

GitHopper is a comprehensive full-stack application that provides deep analysis, code health scoring, and debt reporting for GitHub repositories. It combines advanced ML/AI capabilities with an intuitive, modern web interface to help you understand and improve your codebase.

## ✨ Key Features

- **Repository Scanning & Analysis**: Deep code analysis across branches and commits
- **Health Score Calculation**: Get actionable metrics on code quality and health
- **Technical Debt Reporting**: Identify and track technical debt in your repositories
- **Branch Analysis**: Compare and analyze multiple branches
- **Code Insights**: Historical trends, pattern detection, and recommendations
- **Real-time Monitoring**: Continuous intelligence gathering via MCP (Model Context Protocol)
- **AI-Powered Synthesis**: Leverage AWS Bedrock for intelligent code analysis
- **Beautiful Dashboard**: Modern, responsive UI with theme support

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Client-side routing
- **Three.js** - 3D graphics
- **Firebase** - Authentication and services
- **GSAP & Lenis** - Animation libraries
- **Motion** - Animation framework

### Backend
- **Python 3.8+** - Core language
- **Flask 2.3** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **boto3** - AWS SDK (for Bedrock AI integration)
- **MCP Runtime** - Model Context Protocol server

### Additional Tools
- **Docker** - Containerization
- **AWS Services** - Bedrock, Lambda, S3
- **GitHub API** - Repository access

## 📋 Prerequisites

Before you begin, ensure you have:

- **Node.js 16+** and npm/yarn (for frontend)
- **Python 3.8+** (for backend)
- **Git** (for version control)
- **AWS Account** (optional, for full AI features)
- **GitHub Account** and personal access token (for repository access)

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
│   │   ├── bedrock_client.py   # AWS Bedrock integration
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

## 🔧 Configuration

### Backend Environment Variables

Create a `.env` file in the `backend` directory:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# GitHub Configuration
GITHUB_TOKEN=your_github_token_here
GITHUB_USERNAME=your_username

# AWS Configuration
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

# Bedrock Configuration
BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0

# Server Configuration
HOST=0.0.0.0
PORT=5000
```

### Frontend Environment Variables

Create a `.env` file in the `frontend` directory:

```env
VITE_API_BASE_URL=http://localhost:5000
VITE_FIREBASE_CONFIG={}
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

## 🐳 Docker Support

Build and run using Docker:

```bash
# Build image
docker build -t githopper:latest .

# Run container
docker run -p 5000:5000 -p 5173:5173 githopper:latest
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes** and commit
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

## 📝 Branching Strategy

- **main** - Production-ready code
- **develop** - Development branch
- **feature/*** - Feature branches
- **bugfix/*** - Bug fix branches
- **mukul** - Personal development branch

## 🐛 Known Issues & Roadmap

### Current Limitations
- MCP integration is still in development
- Some AI features require AWS Bedrock access
- Real-time monitoring has latency considerations

### Planned Features
- Real-time WebSocket updates
- Advanced code pattern detection
- Team collaboration features
- GitHub Actions integration
- Metrics export and reporting

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

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Ananya Mehrotra** - Original creator
- **Contributors** - See GitHub contributors page

## 🆘 Support

For issues, questions, or suggestions:

1. Check existing [GitHub Issues](https://github.com/ananyamehrotra/githoppermain/issues)
2. Create a new issue with detailed information
3. Join our community discussions

## 🎉 Acknowledgments

- AWS Bedrock for AI capabilities
- GitHub for repository access API
- React, Vite, and Flask communities
- All open-source contributors

---

**Happy Hopping! 🦘**

Made with ❤️ by the GitHopper team

```

---

## [4] backend/README.md
**Size:** 4.3KB

```markdown
# GitHopper Backend

Python Flask backend server for GitHopper - connects to the frontend React application and provides API endpoints for repository scanning.

## Overview

The backend provides:
- REST API for repository scanning
- Health check endpoint
- CORS support for frontend communication
- Serving the frontend static files
- Repository analysis endpoints (placeholder for future implementation)

## Project Structure

```
backend/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env.example        # Environment configuration template
└── README.md           # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
```

## Running the Backend

### Development Server

```bash
python app.py
```

The server will start at `http://localhost:5000`

### With Flask CLI

```bash
flask run
```

## API Endpoints

### Health Check
- **GET** `/api/health`
- **Description**: Check if backend is running
- **Response**: 
  ```json
  {
    "status": "healthy",
    "message": "GitHopper backend is running",
    "version": "1.0.0"
  }
  ```

### Scan Repository
- **POST** `/api/scan`
- **Description**: Initiate a repository scan
- **Request Body**:
  ```json
  {
    "repo_url": "https://github.com/username/repo"
  }
  ```
- **Response** (202 Accepted):
  ```json
  {
    "status": "pending",
    "repo_url": "https://github.com/username/repo",
    "message": "Scan initiated for repository",
    "scan_id": "scan_123456"
  }
  ```

### Get Scan Status
- **GET** `/api/scan/status/<scan_id>`
- **Description**: Get the status of an ongoing or completed scan
- **Response**:
  ```json
  {
    "scan_id": "scan_123456",
    "status": "completed",
    "progress": 100,
    "result": {
      "security_issues": 5,
      "technical_debt": 3,
      "health_score": 78
    }
  }
  ```

## Frontend Integration

The backend serves the frontend static files automatically. Once you build the frontend:

```bash
cd ../frontend
npm run build
```

The built files will be served from `/` and the backend will handle routing.

## CORS Configuration

CORS is enabled to allow the frontend (running on separate port during development) to communicate with the backend. 

- Frontend: `http://localhost:5173` (Vite dev server)
- Backend: `http://localhost:5000` (Flask server)

## Development Workflow

### Terminal 1 - Frontend Development
```bash
cd frontend
npm install
npm run dev
```
Frontend will be available at: `http://localhost:5173`

### Terminal 2 - Backend Development
```bash
cd backend
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Backend will be available at: `http://localhost:5000`

## Environment Variables

See `.env.example` for available configuration:

| Variable | Description | Default |
|----------|-------------|---------|
| FLASK_ENV | Environment type | development |
| FLASK_DEBUG | Enable debug mode | True |
| FLASK_APP | Entry point file | app.py |
| SECRET_KEY | Secret key for sessions | your-secret-key-here |

## Future Implementation

This backend is prepared for:
- Actual repository scanning logic
- Database integration for storing scan results
- Authentication and authorization
- Advanced analysis features
- Caching layer for performance
- Logging and monitoring

## Troubleshooting

### Port Already in Use
```bash
# Change the port in app.py
app.run(host='0.0.0.0', port=5001, debug=True)
```

### Module Not Found
```bash
# Ensure virtual environment is activated and dependencies installed
pip install -r requirements.txt
```

### CORS Issues
Ensure `Flask-CORS` is installed and that routes use `@CORS(app)` or `@cross_origin()`

## License

MIT

```

---

## [5] backend/ai/bedrock_client.py
**Size:** 20.8KB

```python
# =============================================================================
# bedrock_client.py — Core AI engine for GitHopper
# Dynamic prompts generated per repo based on actual file content
# =============================================================================

import boto3
import json
import logging
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# File Classification
# ---------------------------------------------------------------------------

IAC_EXTENSIONS = {".tf", ".tfvars"}
IAC_KEYWORDS = {"cloudformation", "template", "stack", "infra"}
IAM_KEYWORDS = {"iam", "policy", "role", "permission", "trust"}
DEP_FILES = {
    "requirements.txt", "package.json", "pipfile",
    "go.mod", "gemfile", "pom.xml"
}

def classify_file(filename: str) -> str:
    name = filename.lower()
    base = name.rsplit("/", 1)[-1]
    ext = "." + base.rsplit(".", 1)[-1] if "." in base else ""

    if base in DEP_FILES:
        return "deps"
    if ext == ".json" and any(kw in name for kw in IAM_KEYWORDS):
        return "iam"
    if ext in IAC_EXTENSIONS:
        return "iac"
    if ext in {".yaml", ".yml"} and any(kw in name for kw in IAC_KEYWORDS):
        return "iac"

    return "app"

# ---------------------------------------------------------------------------
# Dynamic Prompt Generation
# ---------------------------------------------------------------------------

def generate_security_prompt(filename: str, code_chunk: str, file_type: str, branch_name: str) -> str:

    if file_type == "iam":
        return f"""You are an IAM security specialist. Analyze this IAM policy for overly permissive permissions.

File: {filename}
Branch: {branch_name}
File Type: IAM Policy

Check for:
- Wildcard actions (Action: "*") or wildcard resources (Resource: "*")
- Principal "*" allowing public access
- Missing conditions on sensitive actions
- arn:* or overly broad resource access

Return ONLY valid JSON with no preamble:
{{
  "vulnerabilities": [
    {{
      "type": "OVERLY_PERMISSIVE",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "explanation": "What is the issue",
      "business_impact": "What risk this poses to the business",
      "estimated_minutes_to_fix": 15,
      "remediation": "How to fix"
    }}
  ]
}}

IAM Policy:
{code_chunk}"""

    elif file_type == "iac":
        return f"""You are a cloud security engineer. Analyze this infrastructure code for misconfigurations.

File: {filename}
Branch: {branch_name}
File Type: Infrastructure-as-Code

Check for:
- Public S3 buckets or unencrypted storage
- Security groups exposed to 0.0.0.0/0
- Unencrypted databases or volumes
- Missing logging or monitoring
- Hardcoded credentials

Return ONLY valid JSON with no preamble:
{{
  "vulnerabilities": [
    {{
      "type": "MISCONFIG_TYPE",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "explanation": "What is misconfigured",
      "business_impact": "Operational/security risk",
      "estimated_minutes_to_fix": 20,
      "remediation": "Step-by-step fix"
    }}
  ]
}}

Infrastructure Code:
{code_chunk}"""

    elif file_type == "deps":
        return f"""You are a dependency security analyst. Analyze this dependency file.

File: {filename}
Branch: {branch_name}
File Type: Dependency File (requirements.txt/package.json/etc)

Check for:
- Severely outdated packages (major versions behind)
- Packages with known CVEs
- Unpinned versions (*)
- Unmaintained dependencies

Return ONLY valid JSON with no preamble:
{{
  "vulnerabilities": [
    {{
      "package": "package_name==version",
      "type": "OUTDATED|VULNERABLE|UNPINNED",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "current_version": "1.2.3",
      "recommended_version": "2.0.0",
      "explanation": "Why this is a problem",
      "business_impact": "What issues this causes",
      "estimated_minutes_to_fix": 5,
      "remediation": "How to update"
    }}
  ]
}}

Dependencies:
{code_chunk}"""

    else:
        return f"""You are a senior security engineer. Analyze this code for vulnerabilities.

File: {filename}
Branch: {branch_name}
File Type: Application Code

Check for:
- Hardcoded secrets, API keys, passwords
- SQL injection or command injection
- Dangerous functions (eval, exec)
- Unsafe deserialization
- Authentication flaws
- Data exposure

Return ONLY valid JSON with no preamble:
{{
  "vulnerabilities": [
    {{
      "type": "HARDCODED_SECRET|SQL_INJECTION|UNSAFE_EVAL|etc",
      "severity": "CRITICAL|HIGH|MEDIUM|LOW",
      "line_range": "10-15",
      "explanation": "What the vulnerability is",
      "business_impact": "Risk to business (data breach, account compromise, etc)",
      "estimated_minutes_to_fix": 10,
      "remediation": "How to fix it"
    }}
  ]
}}

Code:
{code_chunk}"""

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
# Use stable cross-region inference profile (Claude 3 Haiku - broadly available)
MODEL_ID = "us.anthropic.claude-3-haiku-20240307-v1:0"
REGION = "us-east-1"
MAX_TOKENS = 2048

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

try:
    try:
        session = boto3.Session(profile_name="default")
    except Exception:
        session = boto3.Session()
    bedrock = session.client("bedrock-runtime", region_name=REGION)
    print(f"[BEDROCK] Client initialized. Model: {MODEL_ID} | Region: {REGION}")
except Exception as init_err:
    print(f"[BEDROCK] Failed to initialize boto3 client: {init_err}")
    bedrock = None

# ---------------------------------------------------------------------------
# Cost tracking
# ---------------------------------------------------------------------------

cost_tracker = {
    "api_calls": 0,
    "input_tokens": 0,
    "output_tokens": 0,
    "estimated_cost": 0.0
}

# Global flag: set True when AWS payment/access is denied — skips all further Bedrock calls
_bedrock_access_denied = False
_bedrock_fallback_notice_shown = False

# ---------------------------------------------------------------------------
# Static Fallback — converts chunker debt_signals → vulnerability objects
# Used when Bedrock is unavailable (no payment, no access, etc.)
# ---------------------------------------------------------------------------

DEBT_SIGNAL_MAP = {
    "password\\s*=":   {"type": "HARDCODED_SECRET",    "severity": "CRITICAL", "minutes": 15,
                        "explanation": "Hardcoded password detected in source code.",
                        "business_impact": "Credential exposure — attackers can directly access databases or services.",
                        "remediation": "Move to environment variables or a secrets manager (AWS Secrets Manager, HashiCorp Vault)."},
    "secret\\s*=":     {"type": "HARDCODED_SECRET",    "severity": "CRITICAL", "minutes": 15,
                        "explanation": "Hardcoded secret/key detected in source code.",
                        "business_impact": "Secret exposure — any developer with repo access can compromise production systems.",
                        "remediation": "Use environment variables loaded via python-dotenv, never commit secrets to git."},
    "api_key\\s*=":    {"type": "HARDCODED_SECRET",    "severity": "CRITICAL", "minutes": 10,
                        "explanation": "Hardcoded API key detected.",
                        "business_impact": "API key exposure — attackers can make requests on your behalf, incur costs, or steal data.",
                        "remediation": "Store API keys in environment variables; rotate the exposed key immediately."},
    "token\\s*=":      {"type": "HARDCODED_SECRET",    "severity": "HIGH",     "minutes": 10,
                        "explanation": "Hardcoded token detected.",
                        "business_impact": "Token exposure — may allow unauthorized access to third-party services.",
                        "remediation": "Move token to .env file, add .env to .gitignore."},
    "hardcoded":       {"type": "HARDCODED_SECRET",    "severity": "HIGH",     "minutes": 10,
                        "explanation": "Hardcoded value flagged as potential secret.",
                        "business_impact": "Potential credential exposure in version control history.",
                        "remediation": "Audit this value and externalize if sensitive."},
    "eval\\(": {"type": "UNSAFE_EVAL",         "severity": "CRITICAL", "minutes": 20,
                "explanation": "Use of eval() allows arbitrary code execution.",
                "business_impact": "Remote code execution — attacker can run any Python/JS code on your server.",
                "remediation": "Remove eval(); use safe alternatives like ast.literal_eval() for Python."},
    "exec\\(": {"type": "UNSAFE_EXEC",         "severity": "CRITICAL", "minutes": 20,
                "explanation": "Use of exec() allows arbitrary code execution.",
                "business_impact": "Remote code execution risk if user input reaches exec().",
                "remediation": "Remove exec(); restructure logic to avoid dynamic code execution."},
    "sql_injection":   {"type": "SQL_INJECTION",       "severity": "CRITICAL", "minutes": 30,
                        "explanation": "SQL injection vulnerability — user input concatenated into query.",
                        "business_impact": "Data breach or full database compromise — attackers can read, modify, or delete all data.",
                        "remediation": "Use parameterized queries or an ORM. Never concatenate user input into SQL strings."},
    "print\\(":        {"type": "DEBUG_LOGGING",       "severity": "LOW",      "minutes": 5,
                        "explanation": "Debug print statements in production code.",
                        "business_impact": "May leak sensitive data to logs; indicates lack of structured logging.",
                        "remediation": "Replace print() with a structured logger (logging module)."},
    "TEMP":           {"type": "CODE_SMELL",           "severity": "LOW",      "minutes": 5,
                        "explanation": "Potential temporary/placeholder code detected.",
                        "business_impact": "Technical debt — placeholder code may indicate incomplete implementation.",
                        "remediation": "Review and replace temporary code with proper implementation."},
}

def _debt_signal_to_vulnerability(signal: dict, filename: str) -> dict:
    """Convert a chunker debt_signal dict into a structured vulnerability object."""
    pattern = signal.get("pattern", "")
    line_no = signal.get("line_number", "?")
    snippet = signal.get("line_snippet", "")

    # Find best matching map entry
    meta = None
    for key, val in DEBT_SIGNAL_MAP.items():
        if key.lower() in pattern.lower() or pattern.lower() in key.lower():
            meta = val
            break

    if not meta:
        meta = {"type": "CODE_SMELL", "severity": "LOW", "minutes": 5,
                "explanation": f"Potential issue detected: {pattern}",
                "business_impact": "Code quality issue that may pose security risk.",
                "remediation": "Review this pattern and ensure it does not expose sensitive data."}

    return {
        "type": meta["type"],
        "severity": meta["severity"],
        "file": filename,
        "line_range": str(line_no),
        "code_snippet": snippet[:120] if snippet else "",
        "explanation": meta["explanation"],
        "business_impact": meta["business_impact"],
        "estimated_minutes_to_fix": meta["minutes"],
        "remediation": meta["remediation"],
        "source": "static_analysis"
    }

CLAUDE_HAIKU_INPUT_COST = 0.000001
CLAUDE_HAIKU_OUTPUT_COST = 0.000005

BILLING_THRESHOLD_CALLS = 100
BILLING_THRESHOLD_COST = 5.0

def reset_cost_tracker():
    global cost_tracker, _bedrock_fallback_notice_shown
    cost_tracker = {
        "api_calls": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "estimated_cost": 0.0
    }
    _bedrock_fallback_notice_shown = False

# ---------------------------------------------------------------------------
# Bedrock invocation
# ---------------------------------------------------------------------------

def invoke_bedrock(prompt: str, filename: str = "") -> dict:
    global cost_tracker, _bedrock_access_denied, _bedrock_fallback_notice_shown
    cost_tracker["api_calls"] += 1

    print(f"\n[BEDROCK] Analysis: {filename}")
    print(f"   Model: {MODEL_ID}")
    print(f"   Prompt length: {len(prompt)} chars")

    if bedrock is None:
        if not _bedrock_fallback_notice_shown:
            print("   Bedrock client not initialized. Using fallback behavior.")
            _bedrock_fallback_notice_shown = True
        return {"vulnerabilities": []}

    text = None
    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": MAX_TOKENS,
                "temperature": 0.2
            })
        )

        raw = json.loads(response["body"].read())
        print(f"   Raw response keys: {list(raw.keys())}")
        print(f"   Stop reason: {raw.get('stop_reason', 'N/A')}")

        content = raw.get('content', [])
        if not content:
            print(f"   Empty content in response: {raw}")
            return {"vulnerabilities": []}

        text = content[0].get('text', '').strip()
        print(f"   Response length: {len(text)} chars")
        print(f"   Response preview: {text[:300]}")

        if 'usage' in raw:
            cost_tracker["input_tokens"] += raw['usage'].get('input_tokens', 0)
            cost_tracker["output_tokens"] += raw['usage'].get('output_tokens', 0)
            print(f"   Tokens — in: {raw['usage'].get('input_tokens', 0)}, out: {raw['usage'].get('output_tokens', 0)}")
        else:
            cost_tracker["input_tokens"] += len(prompt) // 4
            cost_tracker["output_tokens"] += len(text) // 4
            print("   No 'usage' key in response. Estimating tokens.")

        cost_tracker["estimated_cost"] = (
            (cost_tracker["input_tokens"] * CLAUDE_HAIKU_INPUT_COST) +
            (cost_tracker["output_tokens"] * CLAUDE_HAIKU_OUTPUT_COST)
        )

        # Strip markdown code fences if present
        if "```" in text:
            parts = text.split("```")
            for part in parts:
                part = part.strip()
                if part.startswith("json"):
                    part = part[4:].strip()
                try:
                    result = json.loads(part)
                    print(f"   Parsed JSON from code fence. Found {len(result.get('vulnerabilities', []))} vulnerabilities")
                    return result
                except json.JSONDecodeError:
                    continue

        # Try parsing the raw text directly
        result = json.loads(text)
        print(f"   Parsed JSON directly. Found {len(result.get('vulnerabilities', []))} vulnerabilities")
        return result

    except json.JSONDecodeError as e:
        print(f"   JSON parse error: {e}")
        print(f"   Full raw text:\n{text}")
        return {"vulnerabilities": []}
    except Exception as e:
        error_str = str(e)
        error_type = type(e).__name__
        known_fallback_error = (
            "AccessDeniedException" in error_type
            or "INVALID_PAYMENT_INSTRUMENT" in error_str
            or "AccessDenied" in error_str
            or error_type == "NoCredentialsError"
            or "Unable to locate credentials" in error_str
        )
        if known_fallback_error:
            _bedrock_access_denied = True
            if not _bedrock_fallback_notice_shown:
                print(f"   Bedrock unavailable ({error_type}). Switching to static fallback for this run.")
                _bedrock_fallback_notice_shown = True
        else:
            print(f"   Bedrock invocation error: {error_type}: {error_str}")
        return {"vulnerabilities": []}

# ---------------------------------------------------------------------------
# Per-chunk scanning
# ---------------------------------------------------------------------------

def scan_chunk(chunk: dict, branch_name: str = "main") -> dict:
    global _bedrock_access_denied
    filename = chunk.get("file") or chunk.get("filename", "unknown")
    content = chunk.get("code") or chunk.get("content", "")
    file_type = classify_file(filename)
    debt_signals = chunk.get("debt_signals", [])

    print(f"\n[SCAN] {filename} (type: {file_type}, size: {len(content)} chars)")

    # If Bedrock access is blocked, use static fallback immediately
    if _bedrock_access_denied:
        print("   Using static analysis fallback")
        vulnerabilities = [_debt_signal_to_vulnerability(s, filename) for s in debt_signals]
        if vulnerabilities:
            print(f"   Found {len(vulnerabilities)} vulnerabilities (static)")
        return {
            "file": filename,
            "file_type": file_type,
            "vulnerabilities": vulnerabilities,
            "has_issues": len(vulnerabilities) > 0,
            "vulnerability_count": len(vulnerabilities),
            "analysis_mode": "static_fallback"
        }

    prompt = generate_security_prompt(filename, content, file_type, branch_name)
    result = invoke_bedrock(prompt, filename)
    vulnerabilities = result.get("vulnerabilities", [])

    # If Bedrock returned nothing AND we have debt signals, also inject static findings
    if not vulnerabilities and debt_signals and _bedrock_access_denied:
        vulnerabilities = [_debt_signal_to_vulnerability(s, filename) for s in debt_signals]
        print(f"   Bedrock returned empty. Using static fallback: {len(vulnerabilities)} findings")

    print(f"   Found {len(vulnerabilities)} vulnerabilities")

    return {
        "file": filename,
        "file_type": file_type,
        "vulnerabilities": vulnerabilities,
        "has_issues": len(vulnerabilities) > 0,
        "vulnerability_count": len(vulnerabilities),
        "analysis_mode": "bedrock" if not _bedrock_access_denied else "static_fallback"
    }


def scan_all_chunks(chunks: list, branch_name: str = "main") -> dict:
    reset_cost_tracker()

    print(f"\n{'='*60}")
    print("BEDROCK ANALYSIS STARTING")
    print(f"{'='*60}")
    print(f"Total chunks to analyze: {len(chunks)}")
    print(f"Branch: {branch_name}")
    print(f"{'='*60}")

    vulnerable_files = []
    all_vulnerabilities = []

    for i, chunk in enumerate(chunks, 1):
        filename = chunk.get("file") or chunk.get("filename", "unknown")
        print(f"\n[{i}/{len(chunks)}] Processing: {filename}")
        logger.info(f"Analyzing chunk {i}/{len(chunks)}: {filename}")

        result = scan_chunk(chunk, branch_name)

        if result["has_issues"]:
            vulnerable_files.append({
                "file": filename,
                "type": result["file_type"],
                "count": result["vulnerability_count"]
            })
            all_vulnerabilities.extend(result["vulnerabilities"])

    print(f"\n{'='*60}")
    print("ANALYSIS COMPLETE")
    print(f"{'='*60}")
    print(f"Total vulnerabilities found: {len(all_vulnerabilities)}")
    print(f"Files with issues: {len(vulnerable_files)}")
    print(f"API calls made: {cost_tracker['api_calls']}")
    print(f"Estimated cost: ${cost_tracker['estimated_cost']:.4f}")
    print(f"{'='*60}\n")

    return {
        "vulnerable_files": vulnerable_files,
        "vulnerabilities": all_vulnerabilities,
        "total_files_analyzed": len(chunks),
        "files_with_issues": len(vulnerable_files),
        "total_vulnerabilities": len(all_vulnerabilities),
        "cost_tracker": cost_tracker.copy(),
        "billing": {
            "calls_made": cost_tracker["api_calls"],
            "free_calls_remaining": max(0, BILLING_THRESHOLD_CALLS - cost_tracker["api_calls"]),
            "estimated_cost": cost_tracker["estimated_cost"],
            "will_be_charged": cost_tracker["estimated_cost"] >= BILLING_THRESHOLD_COST or cost_tracker["api_calls"] >= BILLING_THRESHOLD_CALLS,
            "alternatives": [
                {"name": "SonarQube Community", "cost": "Free", "url": "https://www.sonarqube.org/"},
                {"name": "GitHub CodeQL", "cost": "Free (open source)", "url": "https://codeql.github.com/"},
                {"name": "Snyk", "cost": "$50+/month", "url": "https://snyk.io/"},
                {"name": "Checkmarx", "cost": "Enterprise pricing", "url": "https://checkmarx.com/"}
            ]
        }
    }

```

---

## [6] backend/ai/prompts.py
**Size:** 12.6KB

```python
# =============================================================================
# prompts.py — Branch-level code analysis for GitHopper
# Owner: Ananya (AI / Bedrock Eng)
# Focus: Pure code analysis without scoring
# =============================================================================

APP_SECURITY_PROMPT = """
You are a senior security engineer performing DEEP code security analysis.
Analyze EVERY line of this code for security issues. Be THOROUGH and STRICT.

CRITICAL CHECKS (highest priority - report ALL instances):
1. SQL INJECTION patterns:
   - query = "SELECT * FROM users WHERE id = " + user_input
   - f"SELECT * FROM table WHERE id={id}"
   - .format() or % with user data in SQL strings
   - string concatenation in SQL queries
   - parameterized queries NOT used (should use ? or %s placeholders)
   - Any SQL string containing variables without parameterization

2. COMMAND INJECTION:
   - os.system(user_input)
   - subprocess.call(cmd) with string concatenation
   - shell=True in subprocess
   - eval(), exec(), compile() with user data
   - Any shell command built from user input

3. HARDCODED SECRETS:
   - password = "some_password"
   - api_key = "sk_live_..."
   - AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"
   - db_password in code
   - Any string that looks like a token/key/credential

4. AUTHENTICATION/AUTHORIZATION BYPASS:
   - if admin: (checking request.user without validation)
   - No validation of user_id from request
   - Missing CSRF tokens
   - No rate limiting on login
   - Plaintext passwords (should be hashed)

5. UNSAFE OPERATIONS:
   - pickle.loads(untrusted_data)
   - yaml.load() without Loader
   - json.loads() on unsanitized input
   - Input not validated before use
   - No bounds checking on arrays/loops

6. PATH TRAVERSAL:
   - file_path = uploads_dir + request.filename
   - open(filename) where filename comes from user
   - No sanitization of file paths

7. XSS/INJECTION in responses:
   - return user_data without escaping
   - render_template with unsanitized variables
   - Direct HTML generation from user input

File: {filename}
Branch: {branch_name}

IMPORTANT: Report ALL vulnerabilities found, even if there are many.
Return ONLY valid JSON with ALL findings:
{{
  "vulnerabilities": [
    {{
      "type": "SQL_INJECTION",
      "severity": "CRITICAL",
      "file": "{filename}",
      "line": 45,
      "explanation": "User input directly concatenated into SQL query. Attacker can inject SQL commands.",
      "vulnerable_code": "query = f'SELECT * FROM users WHERE username = {{username}}'",
      "fix": "Use parameterized queries: query = 'SELECT * FROM users WHERE username = ?'",
      "remediated_code": "cursor.execute('SELECT * FROM users WHERE username = ?', (username,))",
      "estimated_minutes": 15
    }}
  ]
}}

Code to analyze:
{code_chunk}
"""


IAC_SECURITY_PROMPT = """
You are a cloud security engineer performing DEEP infrastructure analysis.
Analyze EVERY resource in this IaC configuration. Be THOROUGH and STRICT.

CRITICAL CHECKS (scan entire config):
1. S3 BUCKET EXPOSURE:
   - acl = "public-read" or "public-read-write"
   - Block public access = false
   - Any bucket without proper ACL restrictions
   - aws_s3_bucket_public_access_block not present
   - Policy grants s3:* to Principal: "*"

2. SECURITY GROUP EXPOSURE:
   - from_port = 0, to_port = 65535 with 0.0.0.0/0
   - Any wide-open ingress rule
   - No egress restrictions
   - SSH (22), RDP (3389), DB ports open to 0.0.0.0/0
   - HTTP (80) or HTTPS (443) open when shouldn't be

3. DATABASE SECURITY:
   - publicly_accessible = true
   - Multi-AZ = false (no redundancy)
   - No encryption: storage_encrypted = false
   - backup_retention_days = 0
   - No SSL/TLS enforcement
   - Master username/password in code

4. ENCRYPTION:
   - ebs_encryption_enabled = false
   - kms_key_id not specified
   - No encryption at rest or in transit
   - Default encryption not enabled

5. LOGGING & MONITORING:
   - CloudTrail disabled
   - Access logging not enabled
   - No CloudWatch alarms
   - VPC Flow Logs not enabled

6. HARDCODED CREDENTIALS:
   - admin_password = "..."
   - api_key in code
   - AWS secret keys embedded

7. NETWORK ISSUES:
   - No VPC specified
   - No subnets isolated
   - Route table allows 0.0.0.0/0 to resources

File: {filename}
Branch: {branch_name}

Return ONLY valid JSON with ALL findings, even if multiple:
{{
  "vulnerabilities": [
    {{
      "type": "PUBLIC_S3_BUCKET",
      "severity": "CRITICAL",
      "file": "{filename}",
      "resource": "aws_s3_bucket.data",
      "explanation": "S3 bucket configured with acl='public-read'. All objects are world-readable. Data breach risk.",
      "vulnerable_code": "resource 'aws_s3_bucket' 'data' {{ acl = 'public-read' }}",
      "fix": "Set acl to 'private' and use bucket policies for specific access",
      "remediated_code": "resource 'aws_s3_bucket' 'data' {{ acl = 'private' }}\nresource 'aws_s3_bucket_public_access_block' 'data' {{ bucket = aws_s3_bucket.data.id; block_public_acls = true }}",
      "estimated_minutes": 20
    }}
  ]
}}

Config to analyze:
{code_chunk}
"""


IAM_PROMPT = """
You are an IAM security specialist performing DEEP permission analysis.
Analyze EVERY statement in this policy. Be THOROUGH and identify all risks.

CRITICAL CHECKS (scan all statements):
1. WILDCARD OVERREACH:
   - Action: "*" (allows all actions)
   - Resource: "*" (applies to all resources)
   - Principal: "*" (open to anyone)
   - "arn:aws:*:*:*:*" patterns
   - "s3:*" or "ec2:*" instead of specific actions

2. DANGEROUS ACTIONS:
   - iam:* (full IAM permissions - privilege escalation)
   - sts:AssumeRole (can assume other roles)
   - s3:DeleteObject, s3:DeleteBucket (data destruction)
   - ec2:TerminateInstances (infrastructure destruction)
   - rds:DeleteDBCluster (database destruction)
   - kms:ScheduleKeyDeletion (encryption key destruction)

3. MISSING CONDITIONS:
   - s3:GetObject on arn:aws:s3:::*/* without IP/source restrictions
   - No conditions on sensitive operations
   - No MFA requirement for sensitive actions
   - No time-based restrictions

4. OVERLY BROAD RESOURCES:
   - arn:aws:s3:::*/* (all bucket objects)
   - arn:aws:lambda:region:account:function:* (all functions)
   - arn:aws:rds:*:account:db:* (all databases)
   - arn:aws:ec2:*:account:* (all EC2 resources)

5. PRINCIPAL ISSUES:
   - Principal: "*" (service role open to world)
   - Principal: AWS "arn:aws:iam::*:root" (any AWS account)
   - No restrictions on cross-account access
   - Using NotPrincipal (deny-style, harder to audit)

6. SENSITIVE DATA ACCESS:
   - kms:Decrypt on all keys
   - secretsmanager:GetSecretValue unrestricted
   - dynamodb:Scan on tables with sensitive data
   - logs:GetLogEvents on all log groups

7. CREDENTIAL EXPOSURE:
   - iam:CreateAccessKey unrestricted (create extra credentials)
   - iam:PutUserPolicy (add permissions to self)
   - sts:GetCallerIdentity (enumerate targets)

File: {filename}
Branch: {branch_name}

Return ONLY valid JSON with ANY findings detected:
{{
  "vulnerabilities": [
    {{
      "type": "WILDCARD_IAM_ACTION",
      "severity": "CRITICAL",
      "file": "{filename}",
      "statement": 1,
      "explanation": "Policy allows iam:* (all IAM actions) unrestricted. Attacker can create users, steal keys, modify policies, grant themselves permissions.",
      "vulnerable_code": "{{ 'Effect': 'Allow', 'Action': 'iam:*', 'Resource': '*' }}",
      "fix": "Specify only needed actions. Never use wildcard for iam:* actions",
      "remediated_code": "{{ 'Effect': 'Allow', 'Action': ['iam:GetUser', 'iam:ListAccessKeys'], 'Resource': 'arn:aws:iam::ACCOUNT:user/SPECIFIC_USER' }}",
      "estimated_minutes": 45
    }}
  ]
}}

IAM policy to analyze:
{code_chunk}
"""


DEBT_PROMPT = """
You are a code quality engineer performing DEEP technical debt analysis.
Analyze EVERY function and class for quality issues. Be THOROUGH.

CRITICAL CHECKS:
1. FUNCTION COMPLEXITY:
   - Functions > 30 lines (should be < 20)
   - Nested depth > 3 levels
   - Cyclomatic complexity (too many branches)
   - Multiple responsibilities

2. CODE DUPLICATION:
   - Same code pattern repeated 2+ times
   - Copy-pasted logic blocks
   - Duplicate if/else logic
   - Similar database queries

3. ERROR HANDLING:
   - bare except: (catches all exceptions)
   - except Exception: (too broad)
   - Swallowed exceptions (except ... pass)
   - No logging of errors
   - No proper error propagation

4. HARDCODED VALUES:
   - Magic numbers (100, 255, 1000) not in constants
   - Hardcoded strings ("admin", "localhost", "localhost:5000")
   - Hardcoded file paths
   - Hardcoded credentials or URLs
   - API endpoints as strings

5. MISSING DOCUMENTATION:
   - No docstrings on functions
   - Missing type hints
   - No comments on complex logic
   - Unclear variable names (x, temp, data)

6. POOR PATTERNS:
   - Mutable default arguments: def func(items=[]):
   - Global variables
   - Tight coupling between classes
   - God objects doing too much
   - Inconsistent naming conventions

7. PERFORMANCE:
   - Nested loops without optimization
   - O(n²) algorithms that should be O(n) or O(n log n)
   - Database queries in loops
   - Loading entire files/datasets when not needed

File: {filename}
Branch: {branch_name}

Return ONLY valid JSON with all debt identified:
{{
  "vulnerabilities": [
    {{
      "type": "FUNCTION_TOO_COMPLEX",
      "severity": "MEDIUM",
      "file": "{filename}",
      "function": "process_user_data",
      "lines": "45-120",
      "explanation": "Function is 75 lines with 6 nested levels and handles validation, processing, logging, and response formatting. Hard to test and maintain.",
      "fix": "Extract into separate functions: validate_user(), process_data(), format_response(), log_action()",
      "remediated_code": "def validate_user(user): ...\ndef process_data(data): ...\ndef format_response(result): ...\ndef process_user_data(user): validate_user(user); return format_response(process_data(user))",
      "estimated_minutes": 60
    }}
  ]
}}

Code to analyze:
{code_chunk}
"""


DEPENDENCY_PROMPT = """
You are a dependency security analyst performing DEEP package vulnerability analysis.
Analyze EVERY dependency for security risks and versioning issues.

CRITICAL CHECKS:
1. KNOWN VULNERABILITIES:
   - Check if version has published CVEs
   - Common vulnerable package versions:
     - requests < 2.25.1 (certificate validation)
     - urllib3 < 1.26 (SSL verification)
     - jinja2 < 2.11.3 (SSTI)
     - flask < 1.1.2 (Werkzeug issues)
     - django < 3.0 (various)
     - pillow < 8.0 (buffer overflow)
     - yaml dumps (untrusted data)

2. OUTDATED PACKAGES:
   - Major versions behind latest (e.g., 1.x when 5.x available)
   - "Severely outdated" = over 2+ major versions behind
   - Packages with 1 year+ no updates
   - Deprecated packages still in use

3. UNPINNED VERSIONS:
   - requests (no version, always latest)
   - django>=2.0 (could jump to breaking version)
   - numpy==* (wildcard matching anything)
   - No version pins at all

4. SUSPICIOUS PACKAGES:
   - Typosquatting (installed instead of django: djamgo)
   - Packages with 0 downloads
   - Packages from unknown authors
   - Recently created packages with popular names

5. DEVELOPMENT DEPENDENCIES:
   - pytest, pytest-cov in requirements.txt (should be requirements-dev.txt)
   - Black, flake8, pylint in production
   - Mock libraries in production

6. RISKY PACKAGES:
   - eval/exec libraries in dependencies
   - pickle-based serialization
   - Deserialization libraries without validation

File: {filename}
Branch: {branch_name}

Return ONLY valid JSON with ALL findings:
{{
  "findings": [
    {{
      "type": "VULNERABLE_PACKAGE",
      "severity": "HIGH",
      "file": "{filename}",
      "package": "flask==1.0.0",
      "current_version": "1.0.0",
      "safe_version": "2.3.0",
      "explanation": "Flask 1.0.0 is 5+ years old and has 12+ known security vulnerabilities including Werkzeug issues.",
      "fix": "Update to Flask 2.3.0: pip install --upgrade flask",
      "estimated_minutes": 5
    }},
    {{
      "type": "UNPINNED_VERSION",
      "severity": "MEDIUM",
      "file": "{filename}",
      "package": "requests",
      "explanation": "requests version not pinned. Could auto-upgrade to breaking version.",
      "fix": "Pin to specific version: requests==2.31.0",
      "estimated_minutes": 2
    }}
  ]
}}

Dependencies to analyze:
{code_chunk}
"""
```

---

## [7] backend/ai/synthesizer.py
**Size:** 7.2KB

```python
# =============================================================================
# synthesizer.py — Post-scan synthesis engine for GitHopper
# Owner: Ananya (AI / Bedrock Eng)
#
# What this does:
#   1. Deduplicates findings across chunks
#   2. Assigns confidence scores to each finding
#   3. Produces a prioritized Top 5 action list
#   4. Classifies the repo into an archetype
# =============================================================================

import json
import logging
import boto3

logger = logging.getLogger(__name__)

MODEL_ID = "anthropic.claude-sonnet-4-20250514"
REGION = "ap-south-2"  # Hyderabad
MAX_TOKENS = 2048

bedrock = boto3.client("bedrock-runtime", region_name=REGION)

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

DEDUP_AND_PRIORITIZE_PROMPT = """
You are a senior security engineer reviewing a list of findings from an automated scan.

Your job:
1. Remove duplicate findings (same issue in same file reported multiple times)
2. Assign a confidence score to each finding (HIGH / MEDIUM / LOW) based on how certain you are it's a real issue
3. Flag likely false positives — e.g. a "secret" in a test file is probably intentional
4. Return the top 5 most important findings to fix first, ranked by: severity first, then confidence, then estimated fix time

Return ONLY valid JSON, no preamble:
{{
  "top_5_actions": [
    {{
      "rank": 1,
      "type": "HARDCODED_SECRET",
      "severity": "CRITICAL",
      "file": "config/db.py",
      "explanation": "plain English explanation",
      "fix": "exact fix instruction",
      "remediated_code": "fixed code",
      "estimated_minutes": 10,
      "confidence": "HIGH",
      "false_positive_risk": "LOW",
      "business_impact": "what happens if not fixed"
    }}
  ],
  "total_findings": 12,
  "deduplicated_from": 18,
  "false_positives_removed": 3
}}

Findings to analyze:
{all_findings}
"""

ARCHETYPE_PROMPT = """
You are a codebase health analyst. Based on the scan results below, classify this repository into exactly one archetype.

Archetypes:
- STARTUP_DEBT_BOMB: moves fast, ignores debt, security is okay but code quality is poor
- LEGACY_ROTTING: high debt, outdated deps, low test coverage, architectural issues
- MISCONFIGURED_CLOUD: code is clean but infra/IaC/IAM is the problem
- SECURITY_BLIND_SPOT: hardcoded secrets pattern, good code quality otherwise
- ACTUALLY_HEALTHY: minimal issues, good practices overall

Also produce a risk radar with scores 0-100 for 5 dimensions.

Return ONLY valid JSON, no preamble:
{{
  "archetype": "STARTUP_DEBT_BOMB",
  "archetype_description": "2-3 sentence plain English description of what this means for this specific repo",
  "risk_radar": {{
    "security": 80,
    "debt": 40,
    "dependencies": 60,
    "iac": 20,
    "iam": 50
  }},
  "health_score": 64,
  "one_liner": "This repo ships fast but is one leaked key away from a breach."
}}

Scan results:
Security findings: {security_count} issues
Debt findings: {debt_count} issues
Finding types: {finding_types}
Severity breakdown: {severity_breakdown}
"""

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def invoke_bedrock(prompt: str) -> dict:
    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": MAX_TOKENS,
                "messages": [{"role": "user", "content": prompt}]
            })
        )
        raw = json.loads(response["body"].read())
        text = raw["content"][0]["text"].strip()

        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
            text = text.strip()

        return json.loads(text)

    except Exception as e:
        logger.error(f"Synthesizer Bedrock error: {e}")
        return {}


def get_severity_breakdown(findings: list) -> dict:
    breakdown = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in findings:
        sev = f.get("severity", "LOW")
        breakdown[sev] = breakdown.get(sev, 0) + 1
    return breakdown


def get_finding_types(findings: list) -> list:
    return list(set(f.get("type", "UNKNOWN") for f in findings))


# ---------------------------------------------------------------------------
# Main synthesis function — called after scan_all_chunks()
# ---------------------------------------------------------------------------

def synthesize(scan_results: dict) -> dict:
    """
    Takes raw scan output and produces enriched report.

    Input:
        {
            "security_findings": [...],
            "debt_findings": [...]
        }

    Output:
        {
            "top_5_actions": [...],
            "archetype": "STARTUP_DEBT_BOMB",
            "risk_radar": {...},
            "health_score": 64,
            "one_liner": "...",
            "total_security": 8,
            "total_debt": 4,
            "deduplicated_from": 18
        }
    """
    security = scan_results.get("security_findings", [])
    debt = scan_results.get("debt_findings", [])
    all_findings = security + debt

    if not all_findings:
        return {
            "top_5_actions": [],
            "archetype": "ACTUALLY_HEALTHY",
            "risk_radar": {
                "security": 10, "debt": 10,
                "dependencies": 10, "iac": 10, "iam": 10
            },
            "health_score": 95,
            "one_liner": "No significant issues found.",
            "total_security": 0,
            "total_debt": 0
        }

    # Step 1 — dedup + top 5
    dedup_result = invoke_bedrock(
        DEDUP_AND_PRIORITIZE_PROMPT.format(
            all_findings=json.dumps(all_findings, indent=2)
        )
    )

    # Step 2 — archetype + risk radar
    severity_breakdown = get_severity_breakdown(all_findings)
    finding_types = get_finding_types(all_findings)

    archetype_result = invoke_bedrock(
        ARCHETYPE_PROMPT.format(
            security_count=len(security),
            debt_count=len(debt),
            finding_types=", ".join(finding_types),
            severity_breakdown=json.dumps(severity_breakdown)
        )
    )

    return {
        "top_5_actions": dedup_result.get("top_5_actions", []),
        "total_findings": dedup_result.get("total_findings", len(all_findings)),
        "deduplicated_from": dedup_result.get("deduplicated_from", len(all_findings)),
        "false_positives_removed": dedup_result.get("false_positives_removed", 0),
        "archetype": archetype_result.get("archetype", "UNKNOWN"),
        "archetype_description": archetype_result.get("archetype_description", ""),
        "risk_radar": archetype_result.get("risk_radar", {}),
        "health_score": archetype_result.get("health_score", 50),
        "one_liner": archetype_result.get("one_liner", ""),
        "total_security": len(security),
        "total_debt": len(debt)
    }
```

---

## [8] backend/ananya_flagged_files.json
**Size:** 24.1KB

```json
{
  "flagged_files": [
    {
      "content": "Flask==2.3.3\nFlask-CORS==4.0.0\npython-dotenv==1.0.0\nrequests==2.31.0\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "txt",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 4,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 0,
        "total_lines": 4
      },
      "path": "backend/requirements.txt",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 69
    },
    {
      "content": "{\n    \"name\": \"githopperintro\",\n    \"private\": true,\n    \"version\": \"0.0.0\",\n    \"type\": \"module\",\n    \"scripts\": {\n        \"dev\": \"vite\",\n        \"build\": \"vite build\",\n        \"preview\": \"vite preview\"\n    },\n    \"dependencies\": {\n        \"firebase\": \"^12.11.0\",\n        \"gsap\": \"^3.14.2\",\n        \"lenis\": \"^1.3.21\",\n        \"motion\": \"^12.38.0\",\n        \"ogl\": \"^1.0.11\",\n        \"react\": \"^18.3.1\",\n        \"react-dom\": \"^18.3.1\",\n        \"react-router-dom\": \"^7.13.2\",\n        \"three\": \"^0.183.2\"\n    },\n    \"devDependencies\": {\n        \"@tailwindcss/postcss\": \"^4.2.2\",\n        \"@vitejs/plugin-react\": \"^4.4.1\",\n        \"autoprefixer\": \"^10.4.27\",\n        \"postcss\": \"^8.5.8\",\n        \"tailwindcss\": \"^4.2.2\",\n        \"vite\": \"^5.4.10\"\n    }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 30,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 2,
        "total_lines": 30
      },
      "path": "frontend/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 751
    },
    {
      "content": "# GitHopper Backend\n\nPython Flask backend server for GitHopper - connects to the frontend React application and provides API endpoints for repository scanning.\n\n## Overview\n\nThe backend provides:\n- REST API for repository scanning\n- Health check endpoint\n- CORS support for frontend communication\n- Serving the frontend static files\n- Repository analysis endpoints (placeholder for future implementation)\n\n## Project Structure\n\n```\nbackend/\n\u251c\u2500\u2500 app.py              # Main Flask application\n\u251c\u2500\u2500 requirements.txt    # Python dependencies\n\u251c\u2500\u2500 .env.example        # Environment configuration template\n\u2514\u2500\u2500 README.md           # This file\n```\n\n## Prerequisites\n\n- Python 3.8 or higher\n- pip (Python package manager)\n- Virtual environment (recommended)\n\n## Installation\n\n### 1. Create a Virtual Environment\n\n```bash\n# Windows\npython -m venv venv\nvenv\\Scripts\\activate\n\n# macOS/Linux\npython3 -m venv venv\nsource venv/bin/activate\n```\n\n### 2. Install Dependencies\n\n```bash\npip install -r requirements.txt\n```\n\n### 3. Configure Environment\n\n```bash\n# Copy the example environment file\ncp .env.example .env\n\n# Edit .env with your configuration\n```\n\n## Running the Backend\n\n### Development Server\n\n```bash\npython app.py\n```\n\nThe server will start at `http://localhost:5000`\n\n### With Flask CLI\n\n```bash\nflask run\n```\n\n## API Endpoints\n\n### Health Check\n- **GET** `/api/health`\n- **Description**: Check if backend is running\n- **Response**: \n  ```json\n  {\n    \"status\": \"healthy\",\n    \"message\": \"GitHopper backend is running\",\n    \"version\": \"1.0.0\"\n  }\n  ```\n\n### Scan Repository\n- **POST** `/api/scan`\n- **Description**: Initiate a repository scan\n- **Request Body**:\n  ```json\n  {\n    \"repo_url\": \"https://github.com/username/repo\"\n  }\n  ```\n- **Response** (202 Accepted):\n  ```json\n  {\n    \"status\": \"pending\",\n    \"repo_url\": \"https://github.com/username/repo\",\n    \"message\": \"Scan initiated for repository\",\n    \"scan_id\": \"scan_123456\"\n  }\n  ```\n\n### Get Scan Status\n- **GET** `/api/scan/status/<scan_id>`\n- **Description**: Get the status of an ongoing or completed scan\n- **Response**:\n  ```json\n  {\n    \"scan_id\": \"scan_123456\",\n    \"status\": \"completed\",\n    \"progress\": 100,\n    \"result\": {\n      \"security_issues\": 5,\n      \"technical_debt\": 3,\n      \"health_score\": 78\n    }\n  }\n  ```\n\n## Frontend Integration\n\nThe backend serves the frontend static files automatically. Once you build the frontend:\n\n```bash\ncd ../frontend\nnpm run build\n```\n\nThe built files will be served from `/` and the backend will handle routing.\n\n## CORS Configuration\n\nCORS is enabled to allow the frontend (running on separate port during development) to communicate with the backend. \n\n- Frontend: `http://localhost:5173` (Vite dev server)\n- Backend: `http://localhost:5000` (Flask server)\n\n## Development Workflow\n\n### Terminal 1 - Frontend Development\n```bash\ncd frontend\nnpm install\nnpm run dev\n```\nFrontend will be available at: `http://localhost:5173`\n\n### Terminal 2 - Backend Development\n```bash\ncd backend\n# Create and activate virtual environment\npython -m venv venv\nsource venv/bin/activate  # On Windows: venv\\Scripts\\activate\npip install -r requirements.txt\npython app.py\n```\nBackend will be available at: `http://localhost:5000`\n\n## Environment Variables\n\nSee `.env.example` for available configuration:\n\n| Variable | Description | Default |\n|----------|-------------|---------|\n| FLASK_ENV | Environment type | development |\n| FLASK_DEBUG | Enable debug mode | True |\n| FLASK_APP | Entry point file | app.py |\n| SECRET_KEY | Secret key for sessions | your-secret-key-here |\n\n## Future Implementation\n\nThis backend is prepared for:\n- Actual repository scanning logic\n- Database integration for storing scan results\n- Authentication and authorization\n- Advanced analysis features\n- Caching layer for performance\n- Logging and monitoring\n\n## Troubleshooting\n\n### Port Already in Use\n```bash\n# Change the port in app.py\napp.run(host='0.0.0.0', port=5001, debug=True)\n```\n\n### Module Not Found\n```bash\n# Ensure virtual environment is activated and dependencies installed\npip install -r requirements.txt\n```\n\n### CORS Issues\nEnsure `Flask-CORS` is installed and that routes use `@CORS(app)` or `@cross_origin()`\n\n## License\n\nMIT\n",
      "debt_category_hint": "code_quality",
      "debt_signal_count": 1,
      "debt_signals": [
        {
          "line_number": 20,
          "line_snippet": "\u251c\u2500\u2500 .env.example        # Environment configuration template",
          "pattern": "TEMP"
        }
      ],
      "language": "markdown",
      "metrics": {
        "blank_lines": 47,
        "code_lines": 123,
        "comment_lines": 34,
        "comment_ratio": 0.167,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 204
      },
      "path": "backend/README.md",
      "reasons_flagged": [
        "has_debt_signals"
      ],
      "size_bytes": 4241
    },
    {
      "content": "from flask import Flask, render_template, jsonify, request\nfrom flask_cors import CORS\nimport os\nfrom pathlib import Path\n\n# Fix path to import sibling modules easily\nimport sys\nsys.path.append(os.path.dirname(__file__))\n\nfrom github_client import fetch_repo, categorize_files\nfrom chunker import chunk_code\n\n# Initialize Flask app\napp = Flask(__name__, \n            static_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist'),\n            static_url_path='/',\n            template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend'))\n\n# Enable CORS for frontend communication\nCORS(app)\n\n# ==================== API ROUTES ====================\n\n@app.route('/api/health', methods=['GET'])\ndef health_check():\n    \"\"\"Health check endpoint\"\"\"\n    return jsonify({\n        'status': 'healthy',\n        'message': 'GitHopper backend is running',\n        'version': '1.0.0'\n    }), 200\n\n\n@app.route('/api/scan', methods=['POST'])\ndef scan_repo():\n    \"\"\"\n    Receive GitHub repository URL for scanning\n    Fetches the repo, categorizes, and chunks the code.\n    \"\"\"\n    try:\n        data = request.get_json()\n        repo_url = data.get('repo_url')\n        \n        if not repo_url:\n            return jsonify({'error': 'repo_url is required'}), 400\n            \n        # Optional: Auth token to bypass rate limits\n        github_token = os.environ.get('GITHUB_TOKEN')\n        \n        # 1. Fetch\n        print(f\"Fetching repo: {repo_url}\")\n        files = fetch_repo(repo_url, github_token=github_token)\n        \n        # 2. Categorize\n        config_files, dep_files, source_code = categorize_files(files)\n        \n        # 3. Chunk\n        all_chunks = chunk_code(files)\n        \n        return jsonify({\n            'status': 'success',\n            'repo_url': repo_url,\n            'message': 'Scan initiated for repository',\n            'data': {\n                'total_files_fetched': len(files),\n                'config_files': len(config_files),\n                'dependency_files': len(dep_files),\n                'source_files': len(source_code),\n                'total_chunks': len(all_chunks)\n            }\n        }), 200\n    \n    except Exception as e:\n        return jsonify({'error': str(e)}), 500\n\n\n@app.route('/api/scan/status/<scan_id>', methods=['GET'])\ndef get_scan_status(scan_id):\n    \"\"\"Get the status of a scan\"\"\"\n    return jsonify({\n        'scan_id': scan_id,\n        'status': 'completed',\n        'progress': 100,\n        'result': {\n            'security_issues': 5,\n            'technical_debt': 3,\n            'health_score': 78\n        }\n    }), 200\n\n\n@app.route('/', methods=['GET'])\ndef index():\n    \"\"\"Serve the main page\"\"\"\n    return render_template('index.html')\n\n\n@app.route('/<path:path>', methods=['GET'])\ndef serve_static(path):\n    \"\"\"Serve static files\"\"\"\n    file_path = os.path.join(app.static_folder, path)\n    if os.path.isfile(file_path):\n        return app.send_static_file(path)\n    return render_template('index.html')\n\n\n# ==================== ERROR HANDLERS ====================\n\n@app.errorhandler(404)\ndef not_found(error):\n    \"\"\"Handle 404 errors\"\"\"\n    return jsonify({'error': 'Not found'}), 404\n\n\n@app.errorhandler(500)\ndef server_error(error):\n    \"\"\"Handle 500 errors\"\"\"\n    return jsonify({'error': 'Internal server error'}), 500\n\n\n# ==================== DEVELOPMENT SERVER ====================\n\nif __name__ == '__main__':\n    # Development configuration\n    app.config['ENV'] = 'development'\n    app.config['DEBUG'] = True\n    \n    # Run the Flask development server\n    print(\"=\" * 60)\n    print(\"GitHopper Backend Server\")\n    print(\"=\" * 60)\n    print(\"Server running at: http://localhost:5000\")\n    print(\"API Documentation: http://localhost:5000/api/health\")\n    print(\"=\" * 60)\n    \n    app.run(host='0.0.0.0', port=5000, debug=True)\n",
      "debt_category_hint": "code_quality",
      "debt_signal_count": 13,
      "debt_signals": [
        {
          "line_number": 1,
          "line_snippet": "from flask import Flask, render_template, jsonify, request",
          "pattern": "TEMP"
        },
        {
          "line_number": 17,
          "line_snippet": "template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend'))",
          "pattern": "TEMP"
        },
        {
          "line_number": 48,
          "line_snippet": "github_token = os.environ.get('GITHUB_TOKEN')",
          "pattern": "token\\s*="
        },
        {
          "line_number": 51,
          "line_snippet": "print(f\"Fetching repo: {repo_url}\")",
          "pattern": "print\\("
        },
        {
          "line_number": 52,
          "line_snippet": "files = fetch_repo(repo_url, github_token=github_token)",
          "pattern": "token\\s*="
        },
        {
          "line_number": 95,
          "line_snippet": "return render_template('index.html')",
          "pattern": "TEMP"
        },
        {
          "line_number": 104,
          "line_snippet": "return render_template('index.html')",
          "pattern": "TEMP"
        },
        {
          "line_number": 129,
          "line_snippet": "print(\"=\" * 60)",
          "pattern": "print\\("
        },
        {
          "line_number": 130,
          "line_snippet": "print(\"GitHopper Backend Server\")",
          "pattern": "print\\("
        },
        {
          "line_number": 131,
          "line_snippet": "print(\"=\" * 60)",
          "pattern": "print\\("
        },
        {
          "line_number": 132,
          "line_snippet": "print(\"Server running at: http://localhost:5000\")",
          "pattern": "print\\("
        },
        {
          "line_number": 133,
          "line_snippet": "print(\"API Documentation: http://localhost:5000/api/health\")",
          "pattern": "print\\("
        },
        {
          "line_number": 134,
          "line_snippet": "print(\"=\" * 60)",
          "pattern": "print\\("
        }
      ],
      "language": "python",
      "metrics": {
        "blank_lines": 31,
        "code_lines": 93,
        "comment_lines": 12,
        "comment_ratio": 0.088,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 4,
        "total_lines": 136
      },
      "path": "backend/app.py",
      "reasons_flagged": [
        "has_debt_signals"
      ],
      "size_bytes": 3834
    },
    {
      "content": "def chunk_code(files, max_chars=3000):\n    \"\"\"\n    Chunks code files logic-safely so Bedrock token limits aren't hit.\n    \"\"\"\n    chunks = []\n    \n    for file in files:\n        content = file[\"content\"]\n        path = file[\"path\"]\n        lang = file[\"language\"]\n        \n        # Basic chunking: split by character limit.\n        # A more advanced chunker could split by functions/classes.\n        file_len = len(content)\n        \n        # If the file is very small, we keep it as one chunk entirely\n        if file_len <= max_chars:\n            chunks.append({\n                \"file\": path,\n                \"language\": lang,\n                \"code\": content,\n                \"chunk_index\": 0,\n                \"total_chunks\": 1\n            })\n            continue\n            \n        # If larger, we slice it\n        total_chunks = (file_len // max_chars) + (1 if file_len % max_chars > 0 else 0)\n        \n        for i in range(total_chunks):\n            start_idx = i * max_chars\n            end_idx = min(start_idx + max_chars, file_len)\n            chunk_text = content[start_idx:end_idx]\n            \n            chunks.append({\n                \"file\": path,\n                \"language\": lang,\n                \"code\": chunk_text,\n                \"chunk_index\": i,\n                \"total_chunks\": total_chunks\n            })\n            \n    return chunks\n\n# Test the pipeline if executed directly\nif __name__ == \"__main__\":\n    print(\"Testing Chunking Logic...\")\n    sample_files = [{\n        \"path\": \"test.txt\",\n        \"language\": \"txt\",\n        \"content\": \"A\" * 3500\n    }]\n    \n    chunks = chunk_code(sample_files, max_chars=1000)\n    print(f\"Created {len(chunks)} chunks.\")\n    if chunks:\n        print(f\"First chunk length: {len(chunks[0]['code'])}\")\n        print(f\"Last chunk length: {len(chunks[-1]['code'])}\")\n",
      "debt_category_hint": "code_quality",
      "debt_signal_count": 4,
      "debt_signals": [
        {
          "line_number": 47,
          "line_snippet": "print(\"Testing Chunking Logic...\")",
          "pattern": "print\\("
        },
        {
          "line_number": 55,
          "line_snippet": "print(f\"Created {len(chunks)} chunks.\")",
          "pattern": "print\\("
        },
        {
          "line_number": 57,
          "line_snippet": "print(f\"First chunk length: {len(chunks[0]['code'])}\")",
          "pattern": "print\\("
        },
        {
          "line_number": 58,
          "line_snippet": "print(f\"Last chunk length: {len(chunks[-1]['code'])}\")",
          "pattern": "print\\("
        }
      ],
      "language": "python",
      "metrics": {
        "blank_lines": 9,
        "code_lines": 44,
        "comment_lines": 5,
        "comment_ratio": 0.086,
        "long_function_count": 1,
        "long_functions_detected": [
          {
            "approximate_length_lines": 58,
            "approximate_start_line": 1,
            "first_line": "def chunk_code(files, max_chars=3000):"
          }
        ],
        "max_indentation_depth": 4,
        "total_lines": 58
      },
      "path": "backend/chunker.py",
      "reasons_flagged": [
        "has_debt_signals"
      ],
      "size_bytes": 1829
    },
    {
      "content": "import requests\nfrom urllib.parse import urlparse\n\n# Setup filtering constants\nALLOWED_EXTENSIONS = {\n    '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.rb', '.php', \n    '.c', '.cpp', '.h', '.cs', '.md', '.json', '.yml', '.yaml', '.html', '.css'\n}\n\nCRITICAL_FILES = {\n    'package.json', 'requirements.txt', '.env.example', 'pom.xml', \n    'go.mod', 'dockerfile', 'docker-compose.yml'\n}\n\nEXCLUDED_DIRS = {\n    'node_modules', 'venv', '.git', 'build', 'dist', 'out', 'bin', \n    'obj', 'images', 'assets', '.next', '__pycache__', 'coverage'\n}\n\nEXT_MAP = {\n    \"py\": \"python\",\n    \"js\": \"javascript\",\n    \"ts\": \"typescript\",\n    \"java\": \"java\",\n    \"go\": \"go\",\n    \"rb\": \"ruby\",\n    \"php\": \"php\",\n    \"c\": \"c\",\n    \"cpp\": \"cpp\",\n    \"cs\": \"csharp\",\n    \"md\": \"markdown\",\n    \"json\": \"json\",\n    \"yml\": \"yaml\",\n    \"yaml\": \"yaml\",\n    \"html\": \"html\",\n    \"css\": \"css\"\n}\n\ndef parse_repo_url(url):\n    \"\"\"Extract owner and repo from https://github.com/user/repo\"\"\"\n    url = url.strip()\n    if url.endswith('/'):\n        url = url[:-1]\n    if url.endswith('.git'):\n        url = url[:-4]\n        \n    if url.startswith('http'):\n        path = urlparse(url).path.strip('/')\n    else:\n        path = url.strip('/')\n    \n    parts = path.split('/')\n    if len(parts) >= 2:\n        return parts[-2], parts[-1]\n    raise ValueError(f\"Invalid GitHub URL: {url}\")\n\ndef should_keep_file(file_path):\n    \"\"\"Determine if a file should be included in the AI scan.\"\"\"\n    path_parts = file_path.split('/')\n    \n    # 1. Ignore excluded directories\n    if any(excluded in path_parts for excluded in EXCLUDED_DIRS):\n        return False\n        \n    filename = path_parts[-1].lower()\n    \n    # 2. Keep critical configuration and dependency files\n    if filename in CRITICAL_FILES:\n        return True\n        \n    # 3. Check allowed extensions\n    ext = '.' + filename.split('.')[-1] if '.' in filename else ''\n    if ext in ALLOWED_EXTENSIONS:\n        return True\n        \n    return False\n\ndef get_default_branch(owner, repo, headers):\n    \"\"\"Fetch the default branch of a GitHub repository.\"\"\"\n    url = f\"https://api.github.com/repos/{owner}/{repo}\"\n    response = requests.get(url, headers=headers, timeout=10)\n    if response.status_code == 403:\n        raise Exception(\"GitHub rate limit exceeded\")\n    if response.status_code == 200:\n        return response.json().get('default_branch', 'main')\n    return 'main' # Fallback\n\ndef fetch_repo(url, github_token=None, max_files=30):\n    \"\"\"\n    Fetch the useful files from a GitHub repository.\n    Uses GitHub Tree API directly then fetches Raw content to save API limit.\n    \"\"\"\n    owner, repo = parse_repo_url(url)\n    \n    headers = {'Accept': 'application/vnd.github.v3+json'}\n    if github_token:\n        headers['Authorization'] = f'token {github_token}'\n        \n    branch = get_default_branch(owner, repo, headers)\n    \n    # Get the recursive tree\n    tree_url = f\"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1\"\n    response = requests.get(tree_url, headers=headers, timeout=10)\n    \n    if response.status_code == 403:\n        raise Exception(\"GitHub rate limit exceeded\")\n    if response.status_code != 200:\n        raise Exception(f\"Failed to fetch repo tree (Status {response.status_code}): {response.text}\")\n        \n    tree = response.json().get('tree', [])\n    \n    # Filter tree\n    valid_files = [item for item in tree if item['type'] == 'blob' and should_keep_file(item['path'])]\n    \n    # Optional: Prioritize config files, then regular code. Cap at max_files to prevent massive payloads.\n    valid_files.sort(key=lambda x: 0 if x['path'].split('/')[-1].lower() in CRITICAL_FILES else 1)\n    valid_files = valid_files[:max_files]\n    \n    fetched_files = []\n    \n    for item in valid_files:\n        path = item['path']\n        raw_url = f\"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}\"\n        \n        # We download via Raw endpoint as it rarely ratelimits compared to the API\n        try:\n            file_resp = requests.get(raw_url, timeout=10)\n        except requests.exceptions.RequestException as e:\n            print(f\"Failed to fetch {path}: {e}\")\n            continue\n            \n        if file_resp.status_code == 403:\n            raise Exception(\"GitHub rate limit exceeded\")\n            \n        if file_resp.status_code == 200:\n            content = file_resp.text\n            \n            if not content.strip():\n                continue\n                \n            if len(content) > 10000:\n                continue\n            \n            # Simple language detection based on extension\n            raw_ext = path.split('.')[-1] if '.' in path else 'text'\n            language = EXT_MAP.get(raw_ext.lower(), raw_ext)\n            \n            print(f\"Fetched: {path}\")\n            \n            fetched_files.append({\n                \"path\": path,\n                \"language\": language,\n                \"content\": content\n            })\n            \n    return fetched_files\n\ndef categorize_files(files):\n    \"\"\"\n    Groups fetched files into config, dependencies, and code\n    to allow for optimized, domain-specific AI processing.\n    \"\"\"\n    config, deps, code = [], [], []\n\n    for f in files:\n        name = f[\"path\"].lower()\n        basename = name.split('/')[-1]\n        \n        if basename in [\"package.json\", \"requirements.txt\", \"dockerfile\", \"pom.xml\", \"go.mod\"]:\n            deps.append(f)\n        elif basename.endswith((\".yml\", \".yaml\", \".json\", \".env\", \".env.example\")):\n            config.append(f)\n        else:\n            code.append(f)\n\n    return config, deps, code\n",
      "debt_category_hint": "code_quality",
      "debt_signal_count": 3,
      "debt_signals": [
        {
          "line_number": 88,
          "line_snippet": "def fetch_repo(url, github_token=None, max_files=30):",
          "pattern": "token\\s*="
        },
        {
          "line_number": 129,
          "line_snippet": "print(f\"Failed to fetch {path}: {e}\")",
          "pattern": "print\\("
        },
        {
          "line_number": 148,
          "line_snippet": "print(f\"Fetched: {path}\")",
          "pattern": "print\\("
        }
      ],
      "language": "python",
      "metrics": {
        "blank_lines": 37,
        "code_lines": 130,
        "comment_lines": 9,
        "comment_ratio": 0.051,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 4,
        "total_lines": 176
      },
      "path": "backend/github_client.py",
      "reasons_flagged": [
        "has_debt_signals"
      ],
      "size_bytes": 5621
    }
  ],
  "flagged_files_count": 6,
  "message": "Extracted 6 flagged/dependency files",
  "repo_url": "ananyamehrotra/githoppermain.git",
  "status": "success",
  "total_files_scanned": 29
}

```

---

## [9] backend/app.py
**Size:** 21.2KB

```python
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
from pathlib import Path
import json
import hashlib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from pipeline import GitHopperPipeline
from mcp_server import ContinuousIntelligencePipeline, ContinuousWatchManager, MCPMemoryStore

# Initialize Flask app
app = Flask(__name__, 
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist'),
            static_url_path='/',
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'frontend'))

# Enable CORS for frontend communication
CORS(app)

mcp_store = MCPMemoryStore()
continuous_pipeline = ContinuousIntelligencePipeline(store=mcp_store)
watch_manager = ContinuousWatchManager(pipeline=continuous_pipeline)

# Add headers to allow Firebase auth popups
@app.after_request
def add_cors_headers(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
    response.headers['Cross-Origin-Embedder-Policy'] = 'credentialless'
    return response

# ==================== API ROUTES ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'GitHopper backend is running',
        'version': '1.0.0'
    }), 200


@app.route('/api/scan', methods=['POST'])
def scan_repo():
    """
    Receive GitHub repository URL for scanning
    Fetches the repo, categorizes, and chunks the code.
    Falls back to mock data if GitHub API rate limit is hit.
    """
    try:
        print("[SCAN] Starting scan request...")
        data = request.get_json()
        repo_url = data.get('repo_url')
        
        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400
        
        # Normalize URL - add https://github.com/ if missing
        if not repo_url.startswith('http'):
            repo_url = f"https://github.com/{repo_url}"
        
        print(f"[SCAN] Repository: {repo_url}")
        
        # Optional: Auth token to bypass rate limits
        github_token = os.environ.get('GITHUB_TOKEN')
        
        # 1. Fetch
        print(f"[SCAN] Step 1: Fetching repo...")
        try:
            files = fetch_repo(repo_url, github_token=github_token)
            print(f"[SCAN] Step 1 DONE: Fetched {len(files)} files")
        except Exception as fetch_error:
            print(f"[SCAN] GitHub API Error: {str(fetch_error)}")
            # Fallback: Return simple mock response with chunking info
            print(f"[SCAN] Using mock chunking (rate limit fallback)...")
            response_data = {
                'status': 'success',
                'repo_url': repo_url,
                'message': 'Scan initiated (mock mode - GitHub rate limited)',
                'data': {
                    'total_files_fetched': 5,
                    'config_files': 1,
                    'dependency_files': 1,
                    'source_files': 3,
                    'total_chunks': 8,
                    'files_by_category': {
                        'config': [{'path': 'config/database.py', 'language': 'python'}],
                        'dependencies': [{'path': 'requirements.txt', 'language': 'text'}],
                        'source_code': [
                            {'path': 'main.py', 'language': 'python'},
                            {'path': 'app.js', 'language': 'javascript'},
                            {'path': 'utils.py', 'language': 'python'}
                        ]
                    },
                    'analysis_summary': {
                        'total_debt_signals': 5,
                        'files_with_debt_signals': 2,
                        'cost_estimate': {
                            'notes': 'Mock data - GitHub API rate limited',
                            'chunks_to_analyze': 8,
                            'total_code_chars': 2400,
                            'approx_tokens': 600
                        }
                    }
                }
            }
            return jsonify(response_data), 200
        
        # 2. Categorize
        print(f"[SCAN] Step 2: Categorizing files...")
        config_files, dep_files, source_code = categorize_files(files)
        print(f"[SCAN] Step 2 DONE: {len(config_files)} config, {len(dep_files)} deps, {len(source_code)} source")
        
        # 3. Chunk
        print(f"[SCAN] Step 3: Chunking code...")
        all_chunks = chunk_code(files)
        print(f"[SCAN] Step 3 DONE: Created {len(all_chunks)} chunks")
        
        # Extract just paths and language for frontend display
        print(f"[SCAN] Step 4: Building response...")
        def extract_file_info(file_list):
            return [{'path': f['path'], 'language': f.get('language', 'text')} for f in file_list]
        
        # Calculate overall debt statistics
        total_debt_signals = sum(f.get('debt_signal_count', 0) for f in files)
        files_with_signals = sum(1 for f in files if f.get('debt_signal_count', 0) > 0)
        
        response_data = {
            'status': 'success',
            'repo_url': repo_url,
            'message': 'Scan initiated for repository',
            'data': {
                'total_files_fetched': len(files),
                'config_files': len(config_files),
                'dependency_files': len(dep_files),
                'source_files': len(source_code),
                'total_chunks': len(all_chunks),
                'files_by_category': {
                    'config': extract_file_info(config_files),
                    'dependencies': extract_file_info(dep_files),
                    'source_code': extract_file_info(source_code)
                },
                'analysis_summary': {
                    'total_debt_signals': total_debt_signals,
                    'files_with_debt_signals': files_with_signals,
                    'cost_estimate': {
                        'notes': 'Total tokens estimated for Bedrock analysis',
                        'chunks_to_analyze': len(all_chunks),
                        'total_code_chars': sum(c.get('char_count', 0) for c in all_chunks),
                        'approx_tokens': int(sum(c.get('char_count', 0) for c in all_chunks) / 4)
                    }
                },
                'detailed_files': [
                    {
                        'path': f['path'],
                        'language': f['language'],
                        'size_bytes': f.get('size_bytes', 0),
                        'debt_signals': f.get('debt_signals', []),
                        'debt_signal_count': f.get('debt_signal_count', 0),
                        'debt_category_hint': f.get('debt_category_hint', 'code_quality'),
                        'metrics': f.get('metrics', {})
                    }
                    for f in files
                ]
            }
        }
        print(f"[SCAN] Step 4 DONE: Response built")
        
        # Print data structure to terminal for analysis
        print("\n" + "="*80)
        print("SCAN ANALYSIS - DATA STRUCTURE")
        print("="*80)
        print(f"Repository: {repo_url}")
        print(f"Status: {response_data['status']}")
        print(f"\nSUMMARY:")
        print(f"  Total Files: {response_data['data']['total_files_fetched']}")
        print(f"  Config Files: {response_data['data']['config_files']}")
        print(f"  Dependency Files: {response_data['data']['dependency_files']}")
        print(f"  Source Code Files: {response_data['data']['source_files']}")
        print(f"  Code Chunks: {response_data['data']['total_chunks']}")
        print(f"\nFILE STRUCTURE BY CATEGORY:")
        
        # Print config files
        if response_data['data']['files_by_category']['config']:
            print(f"\nConfiguration Files ({len(response_data['data']['files_by_category']['config'])}):")
            for file in response_data['data']['files_by_category']['config']:
                print(f"   - {file['path']} ({file['language']})")
        else:
            print(f"\nConfiguration Files (0): None")
        
        # Print dependency files
        if response_data['data']['files_by_category']['dependencies']:
            print(f"\nDependency Files ({len(response_data['data']['files_by_category']['dependencies'])}):")
            for file in response_data['data']['files_by_category']['dependencies'][:10]:  # Show first 10
                print(f"   - {file['path']} ({file['language']})")
            if len(response_data['data']['files_by_category']['dependencies']) > 10:
                print(f"   ... and {len(response_data['data']['files_by_category']['dependencies']) - 10} more")
        else:
            print(f"\nDependency Files (0): None")
        
        # Print source code files
        if response_data['data']['files_by_category']['source_code']:
            print(f"\nSource Code Files ({len(response_data['data']['files_by_category']['source_code'])}):")
            for file in response_data['data']['files_by_category']['source_code'][:10]:  # Show first 10
                print(f"   - {file['path']} ({file['language']})")
            if len(response_data['data']['files_by_category']['source_code']) > 10:
                print(f"   ... and {len(response_data['data']['files_by_category']['source_code']) - 10} more")
        else:
            print(f"\nSource Code Files (0): None")
        
        print("\n" + "="*80)
        print("RAW JSON RESPONSE:")
        print("="*80)
        print(json.dumps(response_data, indent=2))
        print("="*80 + "\n")
        print(f"[SCAN] COMPLETE: Returning response")
        
        return jsonify(response_data), 200
    
    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in scan_repo: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/scan/flagged-content', methods=['POST'])
def get_flagged_content():
    """
    Extract flagged files (with debt signals) and dependency files
    Returns JSON with their full content for agent processing
    """
    try:
        print("[FLAGGED] Extracting flagged files content...")
        data = request.get_json()
        repo_url = data.get('repo_url')
        
        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400
        
        # Fetch repo
        github_token = os.environ.get('GITHUB_TOKEN')
        files = fetch_repo(repo_url, github_token=github_token)
        
        # Filter: files with debt signals OR dependency/testing category
        flagged_files = [
            {
                'path': f['path'],
                'language': f['language'],
                'content': f['content'],
                'size_bytes': f.get('size_bytes', 0),
                'debt_signals': f.get('debt_signals', []),
                'debt_signal_count': f.get('debt_signal_count', 0),
                'debt_category_hint': f.get('debt_category_hint', 'code_quality'),
                'metrics': f.get('metrics', {}),
                'reasons_flagged': [
                    'has_debt_signals' if f.get('debt_signal_count', 0) > 0 else None,
                    'dependency_file' if f.get('debt_category_hint', '') in ['dependencies', 'testing'] else None
                ]
            }
            for f in files
            if f.get('debt_signal_count', 0) > 0 or f.get('debt_category_hint', '') in ['dependencies', 'testing']
        ]
        
        # Clean up reasons list
        for file in flagged_files:
            file['reasons_flagged'] = [r for r in file['reasons_flagged'] if r is not None]
        
        response_data = {
            'status': 'success',
            'repo_url': repo_url,
            'message': f'Extracted {len(flagged_files)} flagged/dependency files',
            'total_files_scanned': len(files),
            'flagged_files_count': len(flagged_files),
            'flagged_files': flagged_files
        }
        
        print(f"[FLAGGED] DONE: {len(flagged_files)} files flagged out of {len(files)}")
        print(json.dumps({
            'status': response_data['status'],
            'repo_url': response_data['repo_url'],
            'message': response_data['message'],
            'total_files_scanned': response_data['total_files_scanned'],
            'flagged_files_count': response_data['flagged_files_count'],
            'files_summary': [
                {
                    'path': f['path'],
                    'debt_signals': f['debt_signal_count'],
                    'reasons': f['reasons_flagged']
                }
                for f in flagged_files
            ]
        }, indent=2))
        
        return jsonify(response_data), 200
    
    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in get_flagged_content: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/scan/status/<scan_id>', methods=['GET'])
def get_scan_status(scan_id):
    """Get the status of a scan"""
    return jsonify({
        'scan_id': scan_id,
        'status': 'completed',
        'progress': 100,
        'result': {
            'security_issues': 5,
            'technical_debt': 3,
            'health_score': 78
        }
    }), 200


@app.route('/api/analyze', methods=['POST'])
def analyze_repo():
    """
    Analyze code using the complete GitHopper pipeline:
    1. Fetch repository
    2. AI analysis with Bedrock
    3. Scoring and recommendations
    """
    try:
        print("[ANALYZE] Starting complete pipeline...")
        data = request.get_json()
        repo_url = data.get('repo_url')
        branch_name = data.get('branch_name', 'main')

        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400

        print(f"[ANALYZE] Repository: {repo_url}")
        print(f"[ANALYZE] Branch: {branch_name}")

        # Use the full pipeline
        pipeline = GitHopperPipeline()
        github_token = os.environ.get('GITHUB_TOKEN')
        result = pipeline.run_full_pipeline(repo_url, github_token, branch_name)

        if result.get('status') == 'success':
            # Save results
            repo_id = result['summary']['repo_id']
            results_dir = os.path.join(os.path.dirname(__file__), 'scan_results')
            os.makedirs(results_dir, exist_ok=True)

            results_file = os.path.join(results_dir, f'{repo_id}_pipeline.json')
            with open(results_file, 'w') as f:
                json.dump(result, f, indent=2)

            print(f"[ANALYZE] Pipeline complete: Health score {result['summary']['health_score']}")
        else:
            print(f"[ANALYZE] Pipeline failed: {result.get('error', 'Unknown error')}")

        return jsonify(result), 200

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in analyze_repo: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/analyze/continuous', methods=['POST'])
def analyze_repo_continuous():
    """
    Continuous intelligence extension:
    fetch -> diff -> MCP context injection -> optimized analysis -> scoring -> memory update
    """
    try:
        data = request.get_json() or {}
        repo_url = data.get('repo_url')
        branch_name = data.get('branch_name', 'main')
        generate_fixes = data.get('generate_fixes', True)

        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400

        github_token = os.environ.get('GITHUB_TOKEN')
        result = continuous_pipeline.run(
            repo_url=repo_url,
            github_token=github_token,
            branch_name=branch_name,
            generate_fixes=generate_fixes,
        )
        return jsonify(result), 200

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"\n[ERROR] Exception in analyze_repo_continuous: {error_msg}")
        print(f"[ERROR] Traceback:\n{tb}\n")
        return jsonify({'error': error_msg, 'type': type(e).__name__}), 500


@app.route('/api/continuous/start', methods=['POST'])
def start_continuous_watch():
    try:
        data = request.get_json() or {}
        repo_url = data.get('repo_url')
        branch_name = data.get('branch_name', 'main')
        interval_seconds = int(data.get('interval_seconds', 60))

        if not repo_url:
            return jsonify({'error': 'repo_url is required'}), 400

        github_token = os.environ.get('GITHUB_TOKEN')
        result = watch_manager.start(
            repo_url=repo_url,
            branch_name=branch_name,
            interval_seconds=interval_seconds,
            github_token=github_token,
        )
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/continuous/status/<watch_id>', methods=['GET'])
def get_continuous_watch_status(watch_id):
    result = watch_manager.status(watch_id)
    status_code = 404 if result.get('error') else 200
    return jsonify(result), status_code


@app.route('/api/continuous/stop/<watch_id>', methods=['POST'])
def stop_continuous_watch(watch_id):
    result = watch_manager.stop(watch_id)
    status_code = 404 if result.get('error') else 200
    return jsonify(result), status_code


@app.route('/api/mcp/context/<repo_id>', methods=['GET'])
def get_mcp_context(repo_id):
    try:
        return jsonify(mcp_store.get_context(repo_id)), 200
    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/mcp/unresolved/<repo_id>', methods=['GET'])
def get_mcp_unresolved(repo_id):
    try:
        return jsonify({
            'repo_id': repo_id,
            'unresolved_issues': mcp_store.get_unresolved_issues(repo_id)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/mcp/fix-status', methods=['POST'])
def update_mcp_fix_status():
    try:
        data = request.get_json() or {}
        required = ['repo_id', 'issue_fingerprint', 'status', 'validation_status']
        missing = [field for field in required if not data.get(field)]
        if missing:
            return jsonify({'error': f"Missing required fields: {', '.join(missing)}"}), 400

        result = mcp_store.update_fix_status(
            repo_id=data['repo_id'],
            issue_fingerprint=data['issue_fingerprint'],
            status=data['status'],
            validation_status=data['validation_status'],
            explanation=data.get('explanation', ''),
            diff_patch=data.get('diff_patch', ''),
            remediated_code=data.get('remediated_code', ''),
        )
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e), 'type': type(e).__name__}), 500


@app.route('/api/findings/<repo_id>', methods=['GET'])
def get_findings(repo_id):
    """
    Retrieve saved findings for a repo
    """
    try:
        results_file = os.path.join(os.path.dirname(__file__), 'scan_results', f'{repo_id}_findings.json')
        
        if not os.path.exists(results_file):
            return jsonify({'error': f'No findings for repo_id: {repo_id}'}), 404
        
        with open(results_file, 'r') as f:
            findings = json.load(f)
        
        return jsonify(findings), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/', methods=['GET'])
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    """Serve static files"""
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return app.send_static_file(path)
    return render_template('index.html')


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


# ==================== DEVELOPMENT SERVER ====================

if __name__ == '__main__':
    # Development configuration
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    
    # Run the Flask development server
    print("=" * 60)
    print("GitHopper Backend Server")
    print("=" * 60)
    print("Server running at: http://localhost:5000")
    print("API Documentation: http://localhost:5000/api/health")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=True)

```

---

## [10] backend/chunker.py
**Size:** 11.4KB

```python
import re

# Files that strongly indicate technical debt when present
DEBT_SIGNAL_PATTERNS = [
    r'TODO', r'FIXME', r'HACK', r'XXX', r'TEMP', r'DEPRECATED',
    r'console\.log', r'print\(', r'debugger', r'breakpoint',
    r'password\s*=', r'secret\s*=', r'api_key\s*=', r'token\s*=',
    r'hardcoded', r'workaround', r'quick.?fix', r'tech.?debt'
]

# Debt category hints per file/path pattern
DEBT_CATEGORY_HINTS = {
    'test': 'testing',
    'spec': 'testing',
    '__tests__': 'testing',
    'mock': 'testing',
    'package.json': 'dependencies',
    'requirements.txt': 'dependencies',
    'pom.xml': 'dependencies',
    'go.mod': 'dependencies',
    'dockerfile': 'architecture',
    'docker-compose': 'architecture',
    '.github/workflows': 'architecture',
    'config': 'architecture',
    'router': 'architecture',
    'route': 'architecture',
    'controller': 'architecture',
    'model': 'architecture',
    'service': 'architecture',
    'util': 'code_quality',
    'helper': 'code_quality',
    'common': 'code_quality',
    'shared': 'code_quality',
    'legacy': 'code_quality',
    'old': 'code_quality',
    'deprecated': 'code_quality',
}

EXT_MAP = {
    "py": "python", "js": "javascript", "ts": "typescript",
    "jsx": "javascript", "tsx": "typescript", "java": "java",
    "go": "go", "rb": "ruby", "php": "php", "c": "c",
    "cpp": "cpp", "cs": "csharp", "md": "markdown", "json": "json",
    "yml": "yaml", "yaml": "yaml", "html": "html", "css": "css"
}


def get_debt_category_hint(file_path):
    """Infer which debt category a file most likely relates to."""
    path_lower = file_path.lower()
    for pattern, category in DEBT_CATEGORY_HINTS.items():
        if pattern in path_lower:
            return category
    return 'code_quality'


def scan_debt_signals(content):
    """
    Scan raw file content for known debt signal patterns.
    Returns a list of {pattern, line_number, line_snippet} matches
    so analysis has exact line-level evidence.
    """
    signals = []
    lines = content.splitlines()
    for line_num, line in enumerate(lines, start=1):
        for pattern in DEBT_SIGNAL_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                signals.append({
                    "pattern": pattern,
                    "line_number": line_num,
                    "line_snippet": line.strip()[:120]
                })
                break
    return signals


def compute_file_metrics(content, language):
    """
    Lightweight static metrics computed for each file.
    These give Bedrock hard numbers to ground its analysis.
    """
    lines = content.splitlines()
    total_lines = len(lines)
    blank_lines = sum(1 for l in lines if not l.strip())
    comment_lines = 0
    long_functions = []
    max_indent = 0

    # Language-specific comment detection
    comment_prefixes = {
        'python': ('#',),
        'javascript': ('//', '/*', '*'),
        'typescript': ('//', '/*', '*'),
        'java': ('//', '/*', '*'),
        'go': ('//',),
        'ruby': ('#',),
        'php': ('//', '#', '/*'),
        'c': ('//', '/*', '*'),
        'cpp': ('//', '/*', '*'),
        'csharp': ('//',),
    }
    prefixes = comment_prefixes.get(language, ('//', '#'))

    # Detect comment lines
    for line in lines:
        stripped = line.strip()
        if any(stripped.startswith(p) for p in prefixes):
            comment_lines += 1

    # Detect deeply nested code (indentation proxy for complexity)
    for line in lines:
        if line.strip():
            indent = len(line) - len(line.lstrip())
            max_indent = max(max_indent, indent)

    # Detect suspiciously large functions/methods
    fn_patterns = [
        r'^\s*(def |async def |function |const .+ = .*(=>|\() |func |\w+ \w+\()',
    ]
    fn_start_lines = []
    for i, line in enumerate(lines):
        for pat in fn_patterns:
            if re.match(pat, line):
                fn_start_lines.append(i)

    for idx, start in enumerate(fn_start_lines):
        end = fn_start_lines[idx + 1] if idx + 1 < len(fn_start_lines) else total_lines
        fn_length = end - start
        if fn_length > 50:
            long_functions.append({
                "approximate_start_line": start + 1,
                "approximate_length_lines": fn_length,
                "first_line": lines[start].strip()[:100]
            })

    code_lines = total_lines - blank_lines - comment_lines
    comment_ratio = round(comment_lines / total_lines, 3) if total_lines else 0

    return {
        "total_lines": total_lines,
        "code_lines": code_lines,
        "blank_lines": blank_lines,
        "comment_lines": comment_lines,
        "comment_ratio": comment_ratio,
        "max_indentation_depth": max_indent // 4,
        "long_functions_detected": long_functions,
        "long_function_count": len(long_functions)
    }


# Patterns that mark the start of a logical block in various languages
LOGICAL_BOUNDARY_PATTERNS = [
    r'^\s*(def |async def )',
    r'^\s*(class )',
    r'^\s*(export (default |const |function |class ))',
    r'^\s*(function )',
    r'^\s*(const \w+ = \(|const \w+ = async)',
    r'^\s*(public |private |protected |static )',
    r'^\s*(func )',
    r'^\s*(def |end\b)',
    r'^##+ ',
]


def find_logical_boundaries(lines):
    """Return a sorted list of line indices that start a new logical block."""
    boundaries = [0]
    for i, line in enumerate(lines):
        for pat in LOGICAL_BOUNDARY_PATTERNS:
            if re.match(pat, line):
                if i not in boundaries:
                    boundaries.append(i)
                break
    return sorted(boundaries)


def _build_context_note(path, lang, chunk_idx, total_chunks,
                         start_line, end_line, signals, is_test, metrics):
    """
    Generate a plain-English note that gets prepended to the Bedrock prompt
    so the model has immediate context without parsing the JSON itself.
    """
    parts = [
        f"File: {path} ({lang})",
        f"Lines {start_line}–{end_line} (chunk {chunk_idx+1} of {total_chunks}).",
    ]
    if is_test:
        parts.append("This is a TEST file — focus on coverage gaps and mock quality.")
    if signals:
        signal_strs = [f"line {s['line_number']}: {s['line_snippet'][:60]}" for s in signals[:5]]
        parts.append(f"Debt signals in this chunk: {'; '.join(signal_strs)}")
    lf = metrics.get("long_function_count", 0)
    if lf:
        parts.append(f"Whole-file note: {lf} oversized function(s) detected.")
    indent = metrics.get("max_indentation_depth", 0)
    if indent >= 4:
        parts.append(f"Max nesting depth: {indent} levels (complexity risk).")
    return " | ".join(parts)


def chunk_code(files, max_chars=3000):
    """
    Smart chunker that splits at logical boundaries (function/class/section starts)
    rather than arbitrary character positions.

    Each chunk carries rich debt metadata so analysis knows exactly what it's
    looking at without needing to re-read the whole file.

    Output schema per chunk:
    {
        "chunk_id":          str
        "file":              str
        "language":          str
        "chunk_index":       int
        "total_chunks":      int
        "start_line":        int
        "end_line":          int
        "code":              str
        "char_count":        int
        "debt_category_hint":str
        "debt_signals":      list
        "file_metrics":      dict
        "is_entry_point":    bool
        "contains_tests":    bool
        "context_note":      str
    }
    """
    chunks = []

    for file in files:
        content = file["content"]
        path = file["path"]
        lang = file["language"]
        debt_hint = file.get("debt_category_hint", "code_quality")
        all_signals = file.get("debt_signals", [])
        metrics = file.get("metrics", {})
        is_test_file = any(t in path.lower() for t in ['test', 'spec', '__tests__', 'mock'])

        lines = content.splitlines(keepends=True)
        boundaries = find_logical_boundaries([l.rstrip('\n') for l in lines])

        # Build groups of lines between boundaries that fit within max_chars
        groups = []
        current_start = 0
        current_lines = []
        current_chars = 0

        i = 0
        while i < len(boundaries):
            boundary = boundaries[i]
            next_boundary = boundaries[i + 1] if i + 1 < len(boundaries) else len(lines)
            block = lines[boundary:next_boundary]
            block_chars = sum(len(l) for l in block)

            if current_chars + block_chars > max_chars and current_lines:
                groups.append((current_start, current_lines))
                current_start = boundary
                current_lines = block
                current_chars = block_chars
            else:
                if not current_lines:
                    current_start = boundary
                current_lines.extend(block)
                current_chars += block_chars
            i += 1

        if current_lines:
            groups.append((current_start, current_lines))

        total_chunks = len(groups)

        for chunk_idx, (start_line_0, chunk_lines) in enumerate(groups):
            code_text = ''.join(chunk_lines)
            start_line_1 = start_line_0 + 1
            end_line_1 = start_line_0 + len(chunk_lines)

            # Only include debt signals that fall within this chunk's line range
            chunk_signals = [
                s for s in all_signals
                if start_line_1 <= s["line_number"] <= end_line_1
            ]

            context_note = _build_context_note(
                path, lang, chunk_idx, total_chunks,
                start_line_1, end_line_1, chunk_signals, is_test_file, metrics
            )

            chunks.append({
                "chunk_id": f"{path}::chunk_{chunk_idx}",
                "file": path,
                "language": lang,
                "chunk_index": chunk_idx,
                "total_chunks": total_chunks,
                "start_line": start_line_1,
                "end_line": end_line_1,
                "code": code_text,
                "char_count": len(code_text),
                "debt_category_hint": debt_hint,
                "debt_signals": chunk_signals,
                "file_metrics": metrics,
                "is_entry_point": chunk_idx == 0,
                "contains_tests": is_test_file,
                "context_note": context_note
            })

    return chunks


if __name__ == "__main__":
    print("Testing Enhanced Chunking Logic...")
    sample_files = [{
        "path": "test.py",
        "language": "python",
        "content": "def hello():\n    pass\n" * 100,
        "debt_category_hint": "code_quality",
        "debt_signals": [],
        "metrics": {
            "total_lines": 200,
            "code_lines": 200,
            "blank_lines": 0,
            "comment_lines": 0,
            "comment_ratio": 0,
            "max_indentation_depth": 1,
            "long_functions_detected": [],
            "long_function_count": 0
        }
    }]
    
    chunks = chunk_code(sample_files, max_chars=1000)
    print(f"Created {len(chunks)} chunks.")
    if chunks:
        print(f"First chunk: {chunks[0]['chunk_id']}")
        print(f"Chunk count: {len(chunks)}")

```

---

## [11] backend/flagged_files.json
**Size:** 45.7KB

```json
{
  "flagged_files": [
    {
      "content": "{\n  \"name\": \"playground\",\n  \"version\": \"0.1.0\",\n  \"private\": true,\n  \"scripts\": {\n    \"dev\": \"cd ../.. && concurrently --kill-others -n compiler,runtime,playground \\\"yarn workspace babel-plugin-react-compiler run watch\\\" \\\"yarn workspace react-compiler-runtime run watch\\\" \\\"wait-on packages/babel-plugin-react-compiler/dist/index.js && cd apps/playground && NODE_ENV=development next dev\\\"\",\n    \"build:compiler\": \"cd ../.. && concurrently -n compiler,runtime \\\"yarn workspace babel-plugin-react-compiler run build --dts\\\" \\\"yarn workspace react-compiler-runtime run build\\\"\",\n    \"build\": \"yarn build:compiler && next build\",\n    \"postbuild\": \"node ./scripts/downloadFonts.js\",\n    \"preinstall\": \"cd ../.. && yarn install --frozen-lockfile\",\n    \"postinstall\": \"./scripts/link-compiler.sh\",\n    \"vercel-build\": \"yarn build\",\n    \"start\": \"next start\",\n    \"lint\": \"next lint\",\n    \"test\": \"playwright test --workers=4\"\n  },\n  \"dependencies\": {\n    \"@babel/core\": \"^7.18.9\",\n    \"@babel/generator\": \"^7.18.9\",\n    \"@babel/parser\": \"^7.18.9\",\n    \"@babel/plugin-syntax-typescript\": \"^7.18.9\",\n    \"@babel/plugin-transform-block-scoping\": \"^7.18.9\",\n    \"@babel/plugin-transform-modules-commonjs\": \"^7.18.9\",\n    \"@babel/preset-react\": \"^7.18.9\",\n    \"@babel/preset-typescript\": \"^7.26.0\",\n    \"@babel/traverse\": \"^7.18.9\",\n    \"@babel/types\": \"7.26.3\",\n    \"@heroicons/react\": \"^1.0.6\",\n    \"@monaco-editor/react\": \"^4.8.0-rc.2\",\n    \"@playwright/test\": \"^1.56.1\",\n    \"@use-gesture/react\": \"^10.2.22\",\n    \"hermes-eslint\": \"^0.25.0\",\n    \"hermes-parser\": \"^0.25.0\",\n    \"invariant\": \"^2.2.4\",\n    \"json5\": \"^2.2.3\",\n    \"lru-cache\": \"^11.2.2\",\n    \"lz-string\": \"^1.5.0\",\n    \"monaco-editor\": \"^0.52.0\",\n    \"next\": \"15.5.9\",\n    \"notistack\": \"^3.0.0-alpha.7\",\n    \"prettier\": \"^3.3.3\",\n    \"pretty-format\": \"^29.3.1\",\n    \"re-resizable\": \"^6.9.16\",\n    \"react\": \"19.2.3\",\n    \"react-dom\": \"19.2.3\"\n  },\n  \"devDependencies\": {\n    \"@types/node\": \"18.11.9\",\n    \"@types/react\": \"19.2\",\n    \"@types/react-dom\": \"19.2\",\n    \"autoprefixer\": \"^10.4.13\",\n    \"clsx\": \"^1.2.1\",\n    \"concurrently\": \"^7.4.0\",\n    \"eslint\": \"^8.28.0\",\n    \"eslint-config-next\": \"15.5.2\",\n    \"monaco-editor-webpack-plugin\": \"^7.1.0\",\n    \"postcss\": \"^8.4.31\",\n    \"tailwindcss\": \"^3.2.4\",\n    \"wait-on\": \"^7.2.0\"\n  },\n  \"resolutions\": {\n    \"@types/react\": \"19.2\",\n    \"@types/react-dom\": \"19.2\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 65,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 65
      },
      "path": "compiler/apps/playground/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 2376
    },
    {
      "content": "{\n  \"private\": true,\n  \"workspaces\": {\n    \"packages\": [\n      \"packages/*\"\n    ]\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\"\n  },\n  \"scripts\": {\n    \"copyright\": \"node scripts/copyright.js\",\n    \"hash\": \"scripts/hash.sh\",\n    \"start\": \"yarn workspace playground run start\",\n    \"next\": \"yarn workspace playground run dev\",\n    \"build\": \"yarn workspaces run build\",\n    \"dev\": \"cd apps/playground && yarn dev\",\n    \"test\": \"yarn workspaces run test\",\n    \"snap\": \"yarn workspace babel-plugin-react-compiler run snap\",\n    \"snap:build\": \"yarn workspace snap run build\",\n    \"npm:publish\": \"node scripts/release/publish\",\n    \"eslint-docs\": \"yarn workspace babel-plugin-react-compiler build && node scripts/build-eslint-docs.js\"\n  },\n  \"dependencies\": {\n    \"fs-extra\": \"^4.0.2\",\n    \"react-is\": \"0.0.0-experimental-4beb1fd8-20241118\"\n  },\n  \"devDependencies\": {\n    \"@babel/types\": \"^7.26.0\",\n    \"@tsconfig/strictest\": \"^2.0.5\",\n    \"concurrently\": \"^7.4.0\",\n    \"esbuild\": \"^0.25.0\",\n    \"folder-hash\": \"^4.0.4\",\n    \"npm-dts\": \"^1.3.13\",\n    \"object-assign\": \"^4.1.1\",\n    \"ora\": \"5.4.1\",\n    \"prettier\": \"^3.3.3\",\n    \"prettier-plugin-hermes-parser\": \"^0.26.0\",\n    \"prompt-promise\": \"^1.0.3\",\n    \"rimraf\": \"^6.0.1\",\n    \"to-fast-properties\": \"^2.0.0\",\n    \"tsup\": \"^8.4.0\",\n    \"typescript\": \"^5.4.3\",\n    \"wait-on\": \"^7.2.0\",\n    \"yargs\": \"^17.7.2\"\n  },\n  \"resolutions\": {\n    \"@babel/types\": \"7.26.3\"\n  },\n  \"packageManager\": \"yarn@1.22.22\"\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 52,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 52
      },
      "path": "compiler/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 1503
    },
    {
      "content": "{\n  \"name\": \"babel-plugin-react-compiler\",\n  \"version\": \"0.0.0-experimental-334f00b-20240725\",\n  \"description\": \"Babel plugin for React Compiler.\",\n  \"main\": \"dist/index.js\",\n  \"license\": \"MIT\",\n  \"files\": [\n    \"dist\",\n    \"!*.tsbuildinfo\"\n  ],\n  \"scripts\": {\n    \"build\": \"rimraf dist && tsup\",\n    \"test\": \"./scripts/link-react-compiler-runtime.sh && yarn snap:ci\",\n    \"jest\": \"yarn build && ts-node node_modules/.bin/jest\",\n    \"snap\": \"yarn workspace snap run snap\",\n    \"snap:build\": \"yarn workspace snap run build\",\n    \"snap:ci\": \"yarn snap:build && yarn snap\",\n    \"ts:analyze-trace\": \"scripts/ts-analyze-trace.sh\",\n    \"lint\": \"yarn eslint src\",\n    \"watch\": \"yarn build --dts --watch\"\n  },\n  \"dependencies\": {\n    \"@babel/types\": \"^7.26.0\"\n  },\n  \"devDependencies\": {\n    \"@babel/core\": \"^7.2.0\",\n    \"@babel/generator\": \"7.2.0\",\n    \"@babel/parser\": \"^7.2.0\",\n    \"@babel/plugin-syntax-typescript\": \"^7.18.6\",\n    \"@babel/plugin-transform-block-scoping\": \"^7.18.9\",\n    \"@babel/plugin-transform-modules-commonjs\": \"^7.18.6\",\n    \"@babel/preset-react\": \"^7.18.6\",\n    \"@babel/preset-typescript\": \"^7.18.6\",\n    \"@babel/traverse\": \"^7.2.0\",\n    \"@testing-library/react\": \"^13.4.0\",\n    \"@tsconfig/node18-strictest\": \"^1.0.0\",\n    \"@types/glob\": \"^8.1.0\",\n    \"@types/invariant\": \"^2.2.35\",\n    \"@types/jest\": \"^29.0.3\",\n    \"@types/node\": \"^18.7.18\",\n    \"@typescript-eslint/eslint-plugin\": \"^8.7.0\",\n    \"@typescript-eslint/parser\": \"^8.7.0\",\n    \"babel-jest\": \"^29.0.3\",\n    \"babel-plugin-fbt\": \"^1.0.0\",\n    \"babel-plugin-fbt-runtime\": \"^1.0.0\",\n    \"eslint\": \"^8.57.1\",\n    \"invariant\": \"^2.2.4\",\n    \"jest\": \"^29.0.3\",\n    \"jest-environment-jsdom\": \"^29.0.3\",\n    \"pretty-format\": \"^24\",\n    \"react\": \"0.0.0-experimental-4beb1fd8-20241118\",\n    \"react-dom\": \"0.0.0-experimental-4beb1fd8-20241118\",\n    \"ts-jest\": \"^29.1.1\",\n    \"ts-node\": \"^10.9.2\",\n    \"zod\": \"^3.25.0 || ^4.0.0\",\n    \"zod-validation-error\": \"^3.5.0 || ^4.0.0\"\n  },\n  \"resolutions\": {\n    \"./**/@babel/parser\": \"7.7.4\",\n    \"./**/@babel/plugin-syntax-flow\": \"7.7.4\",\n    \"./**/@babel/types\": \"7.7.4\",\n    \"@babel/core\": \"7.2.0\",\n    \"@babel/generator\": \"7.2.0\",\n    \"@babel/traverse\": \"7.7.4\"\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/babel-plugin-react-compiler\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 71,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 71
      },
      "path": "compiler/packages/babel-plugin-react-compiler/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 2346
    },
    {
      "content": "{\n  \"name\": \"eslint-plugin-react-compiler\",\n  \"version\": \"0.0.0-experimental-9ed098e-20240725\",\n  \"description\": \"ESLint plugin to display errors found by the React compiler.\",\n  \"main\": \"dist/index.js\",\n  \"scripts\": {\n    \"build\": \"rimraf dist && tsup\",\n    \"test\": \"jest\",\n    \"watch\": \"yarn build --watch\"\n  },\n  \"files\": [\n    \"dist\"\n  ],\n  \"dependencies\": {\n    \"@babel/core\": \"^7.24.4\",\n    \"@babel/parser\": \"^7.24.4\",\n    \"hermes-parser\": \"^0.25.1\",\n    \"zod\": \"^3.25.0 || ^4.0.0\",\n    \"zod-validation-error\": \"^3.5.0 || ^4.0.0\"\n  },\n  \"devDependencies\": {\n    \"@babel/preset-env\": \"^7.22.4\",\n    \"@babel/preset-typescript\": \"^7.18.6\",\n    \"@babel/types\": \"^7.26.0\",\n    \"@types/eslint\": \"^8.56.12\",\n    \"@types/jest\": \"^30.0.0\",\n    \"@types/node\": \"^20.2.5\",\n    \"babel-jest\": \"^29.0.3\",\n    \"eslint\": \"8.57.0\",\n    \"hermes-eslint\": \"^0.25.1\",\n    \"jest\": \"^29.5.0\",\n    \"regexp.escape\": \"^2.0.1\"\n  },\n  \"engines\": {\n    \"node\": \"^14.17.0 || ^16.0.0 || >= 18.0.0\"\n  },\n  \"peerDependencies\": {\n    \"eslint\": \">=7\"\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/eslint-plugin-react-compiler\"\n  },\n  \"license\": \"MIT\"\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 46,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 46
      },
      "path": "compiler/packages/eslint-plugin-react-compiler/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 1211
    },
    {
      "content": "{\n  \"name\": \"make-read-only-util\",\n  \"version\": \"0.0.1\",\n  \"license\": \"MIT\",\n  \"files\": [\n    \"src\"\n  ],\n  \"scripts\": {\n    \"build\": \"rimraf dist && tsup\",\n    \"test\": \"jest src\",\n    \"watch\": \"yarn build --watch\"\n  },\n  \"dependencies\": {\n    \"invariant\": \"^2.2.4\",\n    \"pretty-format\": \"^24\"\n  },\n  \"devDependencies\": {\n    \"@types/invariant\": \"^2.2.35\",\n    \"@types/jest\": \"^28.1.6\",\n    \"@types/node\": \"^20.2.5\",\n    \"jest\": \"^28.1.3\",\n    \"ts-jest\": \"^28.0.7\",\n    \"ts-node\": \"^10.9.2\"\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/make-read-only-util\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 30,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 30
      },
      "path": "compiler/packages/make-read-only-util/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 651
    },
    {
      "content": "{\n  \"name\": \"react-compiler-healthcheck\",\n  \"version\": \"0.0.0-experimental-ab3118d-20240725\",\n  \"description\": \"Health check script to test violations of the rules of react.\",\n  \"bin\": {\n    \"react-compiler-healthcheck\": \"dist/index.js\"\n  },\n  \"scripts\": {\n    \"build\": \"rimraf dist && tsup\",\n    \"test\": \"echo 'no tests'\",\n    \"watch\": \"yarn build --watch\"\n  },\n  \"dependencies\": {\n    \"@babel/core\": \"^7.24.4\",\n    \"@babel/parser\": \"^7.24.4\",\n    \"chalk\": \"4\",\n    \"fast-glob\": \"^3.3.2\",\n    \"ora\": \"5.4.1\",\n    \"yargs\": \"^17.7.2\",\n    \"zod\": \"^3.25.0 || ^4.0.0\",\n    \"zod-validation-error\": \"^3.5.0 || ^4.0.0\"\n  },\n  \"devDependencies\": {},\n  \"engines\": {\n    \"node\": \"^14.17.0 || ^16.0.0 || >= 18.0.0\"\n  },\n  \"license\": \"MIT\",\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/react-compiler-healthcheck\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 33,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 33
      },
      "path": "compiler/packages/react-compiler-healthcheck/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 893
    },
    {
      "content": "{\n  \"name\": \"react-compiler-runtime\",\n  \"version\": \"0.0.1\",\n  \"description\": \"Runtime for React Compiler\",\n  \"license\": \"MIT\",\n  \"main\": \"dist/index.js\",\n  \"typings\": \"dist/index.d.ts\",\n  \"files\": [\n    \"dist\",\n    \"src\"\n  ],\n  \"peerDependencies\": {\n    \"react\": \"^17.0.0 || ^18.0.0 || ^19.0.0 || ^0.0.0-experimental\"\n  },\n  \"scripts\": {\n    \"build\": \"rimraf dist && tsup\",\n    \"test\": \"echo 'no tests'\",\n    \"watch\": \"yarn build --watch\"\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/react-compiler-runtime\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 25,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 25
      },
      "path": "compiler/packages/react-compiler-runtime/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 603
    },
    {
      "content": "{\n  \"private\": \"true\",\n  \"name\": \"react-forgive-client\",\n  \"version\": \"0.0.0\",\n  \"description\": \"Experimental LSP client\",\n  \"license\": \"MIT\",\n  \"scripts\": {\n    \"build\": \"echo 'no build'\",\n    \"test\": \"echo 'no tests'\"\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/react-forgive\"\n  },\n  \"dependencies\": {\n    \"vscode-languageclient\": \"^9.0.1\"\n  },\n  \"devDependencies\": {\n    \"@types/vscode\": \"^1.95.0\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 22,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 22
      },
      "path": "compiler/packages/react-forgive/client/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 497
    },
    {
      "content": "{\n  \"name\": \"react-forgive\",\n  \"displayName\": \"React Analyzer\",\n  \"description\": \"React LSP\",\n  \"license\": \"MIT\",\n  \"version\": \"0.0.0\",\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/react-forgive\"\n  },\n  \"categories\": [\n    \"Programming Languages\"\n  ],\n  \"keywords\": [\n    \"react\",\n    \"react analyzer\",\n    \"react compiler\"\n  ],\n  \"publisher\": \"Meta\",\n  \"engines\": {\n    \"vscode\": \"^1.96.0\"\n  },\n  \"activationEvents\": [\n    \"onLanguage:javascriptreact\",\n    \"onLanguage:typescriptreact\"\n  ],\n  \"main\": \"./dist/extension.js\",\n  \"contributes\": {\n    \"commands\": [\n      {\n        \"command\": \"react-forgive.toggleAll\",\n        \"title\": \"React Analyzer: Toggle on/off\"\n      }\n    ]\n  },\n  \"scripts\": {\n    \"build\": \"yarn run compile\",\n    \"build:compiler\": \"yarn workspace babel-plugin-react-compiler build --dts\",\n    \"compile\": \"rimraf dist && concurrently -n server,client \\\"scripts/build.mjs -t server\\\" \\\"scripts/build.mjs -t client\\\"\",\n    \"dev\": \"yarn run package && yarn run install-ext\",\n    \"install-ext\": \"code --install-extension react-forgive-0.0.0.vsix\",\n    \"lint\": \"echo 'no tests'\",\n    \"package\": \"rm -f react-forgive-0.0.0.vsix && vsce package --yarn\",\n    \"postinstall\": \"cd client && yarn install && cd ../server && yarn install && cd ..\",\n    \"pretest\": \"yarn run build:compiler && yarn run compile && yarn run lint\",\n    \"test\": \"vscode-test\",\n    \"vscode:prepublish\": \"yarn run compile\",\n    \"watch\": \"scripts/build.mjs --watch\"\n  },\n  \"devDependencies\": {\n    \"@eslint/js\": \"^9.13.0\",\n    \"@types/mocha\": \"^10.0.10\",\n    \"@types/node\": \"^20\",\n    \"@types/vscode\": \"^1.96.0\",\n    \"@vscode/test-cli\": \"^0.0.10\",\n    \"@vscode/test-electron\": \"^2.4.1\",\n    \"eslint\": \"^9.13.0\",\n    \"mocha\": \"^11.0.1\",\n    \"typescript-eslint\": \"^8.16.0\",\n    \"yargs\": \"^17.7.2\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 63,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 2,
        "total_lines": 63
      },
      "path": "compiler/packages/react-forgive/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 1869
    },
    {
      "content": "{\n  \"private\": \"true\",\n  \"name\": \"react-forgive-server\",\n  \"version\": \"0.0.0\",\n  \"description\": \"Experimental LSP server\",\n  \"license\": \"MIT\",\n  \"scripts\": {\n    \"build\": \"rimraf dist && rollup --config --bundleConfigAsCjs\",\n    \"test\": \"echo 'no tests'\"\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/react-forgive\"\n  },\n  \"dependencies\": {\n    \"@babel/core\": \"^7.26.0\",\n    \"@babel/parser\": \"^7.26.0\",\n    \"@babel/plugin-syntax-typescript\": \"^7.25.9\",\n    \"@babel/types\": \"^7.26.0\",\n    \"prettier\": \"^3.3.3\",\n    \"vscode-languageserver\": \"^9.0.1\",\n    \"vscode-languageserver-textdocument\": \"^1.0.12\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 25,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 25
      },
      "path": "compiler/packages/react-forgive/server/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 695
    },
    {
      "content": "{\n  \"name\": \"react-mcp-server\",\n  \"version\": \"0.0.0\",\n  \"description\": \"React MCP Server (experimental)\",\n  \"bin\": {\n    \"react-mcp-server\": \"./dist/index.js\"\n  },\n  \"scripts\": {\n    \"build\": \"rimraf dist && tsup\",\n    \"test\": \"echo 'no tests'\",\n    \"dev\": \"concurrently --kill-others -n build,inspect \\\"yarn run watch\\\" \\\"wait-on dist/index.js && yarn run inspect\\\"\",\n    \"inspect\": \"npx @modelcontextprotocol/inspector node dist/index.js\",\n    \"watch\": \"yarn build --watch\"\n  },\n  \"dependencies\": {\n    \"@babel/core\": \"^7.26.0\",\n    \"@babel/parser\": \"^7.26\",\n    \"@babel/preset-env\": \"^7.26.9\",\n    \"@babel/preset-react\": \"^7.18.6\",\n    \"@babel/preset-typescript\": \"^7.27.1\",\n    \"@modelcontextprotocol/sdk\": \"^1.9.0\",\n    \"algoliasearch\": \"^5.23.3\",\n    \"cheerio\": \"^1.0.0\",\n    \"html-to-text\": \"^9.0.5\",\n    \"prettier\": \"^3.3.3\",\n    \"puppeteer\": \"^24.7.2\",\n    \"zod\": \"^3.25.0 || ^4.0.0\"\n  },\n  \"devDependencies\": {\n    \"@types/html-to-text\": \"^9.0.4\",\n    \"@types/jest\": \"^29.5.14\",\n    \"jest\": \"^29.7.0\",\n    \"ts-jest\": \"^29.3.2\"\n  },\n  \"license\": \"MIT\",\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/react-mcp-server\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 41,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 41
      },
      "path": "compiler/packages/react-mcp-server/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 1215
    },
    {
      "content": "{\n  \"name\": \"snap\",\n  \"version\": \"0.0.1\",\n  \"public\": false,\n  \"description\": \"Snapshot testing CLI tool\",\n  \"main\": \"dist/main.js\",\n  \"license\": \"MIT\",\n  \"files\": [\n    \"src\"\n  ],\n  \"scripts\": {\n    \"postinstall\": \"./scripts/link-react-compiler-runtime.sh && perl -p -i -e 's/react\\\\.element/react.transitional.element/' ../../node_modules/fbt/lib/FbtReactUtil.js && perl -p -i -e 's/didWarnAboutUsingAct = false;/didWarnAboutUsingAct = true;/' ../../node_modules/react-dom/cjs/react-dom-test-utils.development.js\",\n    \"build\": \"rimraf dist && concurrently -n snap,runtime \\\"tsc --build\\\" \\\"yarn --silent workspace react-compiler-runtime build\\\"\",\n    \"snap\": \"node dist/main.js\",\n    \"test\": \"echo 'no tests'\",\n    \"prettier\": \"prettier --write 'src/**/*.ts'\"\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\": \"git+https://github.com/facebook/react.git\",\n    \"directory\": \"compiler/packages/snap\"\n  },\n  \"dependencies\": {\n    \"@babel/code-frame\": \"^7.22.5\",\n    \"@babel/generator\": \"^7.19.1\",\n    \"@babel/plugin-syntax-jsx\": \"^7.18.6\",\n    \"@babel/preset-flow\": \"^7.7.4\",\n    \"@babel/preset-typescript\": \"^7.26.0\",\n    \"@parcel/watcher\": \"^2.1.0\",\n    \"@testing-library/react\": \"^13.4.0\",\n    \"babel-plugin-idx\": \"^3.0.3\",\n    \"babel-plugin-syntax-hermes-parser\": \"^0.25.1\",\n    \"chalk\": \"4\",\n    \"fbt\": \"^1.0.2\",\n    \"glob\": \"^10.3.10\",\n    \"hermes-parser\": \"^0.25.1\",\n    \"jsdom\": \"^22.1.0\",\n    \"react\": \"0.0.0-experimental-4beb1fd8-20241118\",\n    \"react-dom\": \"0.0.0-experimental-4beb1fd8-20241118\",\n    \"readline\": \"^1.3.0\",\n    \"yargs\": \"^17.7.1\",\n    \"zod\": \"^3.25.0 || ^4.0.0\",\n    \"zod-validation-error\": \"^3.5.0 || ^4.0.0\"\n  },\n  \"devDependencies\": {\n    \"@babel/core\": \"^7.19.1\",\n    \"@babel/parser\": \"^7.20.15\",\n    \"@babel/plugin-transform-modules-commonjs\": \"^7.18.6\",\n    \"@babel/preset-react\": \"^7.18.6\",\n    \"@babel/traverse\": \"^7.19.1\",\n    \"@types/babel__code-frame\": \"^7.0.6\",\n    \"@types/fbt\": \"^1.0.4\",\n    \"@types/glob\": \"^8.1.0\",\n    \"@types/node\": \"^18.7.18\",\n    \"@typescript-eslint/eslint-plugin\": \"^7.4.0\",\n    \"@typescript-eslint/parser\": \"^7.4.0\",\n    \"object-assign\": \"^4.1.1\"\n  },\n  \"resolutions\": {\n    \"./**/@babel/parser\": \"7.7.4\",\n    \"./**/@babel/types\": \"7.7.4\",\n    \"@babel/generator\": \"7.2.0\",\n    \"@babel/preset-flow\": \"7.22.5\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 65,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 65
      },
      "path": "compiler/packages/snap/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 2281
    },
    {
      "content": "{\n  \"devDependencies\": {\n    \"@babel/core\": \"^7.10.5\",\n    \"@babel/plugin-proposal-class-properties\": \"^7.10.4\",\n    \"@babel/preset-env\": \"^7.10.4\",\n    \"@babel/preset-react\": \"^7.10.4\",\n    \"babel-loader\": \"^8.1.0\",\n    \"react\": \"^19.0.0\",\n    \"react-art\": \"^19.0.0\",\n    \"react-dom\": \"^19.0.0\",\n    \"webpack\": \"^1.14.0\"\n  },\n  \"scripts\": {\n    \"prebuild\": \"cp -r ../../build/oss-experimental/* ./node_modules/\",\n    \"build\": \"webpack app.js bundle.js\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 17,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 17
      },
      "path": "fixtures/art/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 460
    },
    {
      "content": "{\n  \"name\": \"attribute-behavior\",\n  \"version\": \"0.1.0\",\n  \"private\": true,\n  \"dependencies\": {\n    \"file-saver\": \"^1.3.3\",\n    \"glamor\": \"^2.20.40\",\n    \"react\": \"^15.6.1\",\n    \"react-dom\": \"^15.6.1\",\n    \"react-scripts\": \"1.0.11\",\n    \"react-virtualized\": \"^9.9.0\"\n  },\n  \"resolutions\": {\n    \"fsevents\": \"1.2.13\"\n  },\n  \"scripts\": {\n    \"predev\":\n      \"cp ../../build/oss-experimental/react/umd/react.development.js public/ && cp ../../build/oss-experimental/react-dom/umd/react-dom.development.js public/ && cp ../../build/oss-experimental/react-dom/umd/react-dom-server.browser.development.js public/\",\n    \"dev\": \"react-scripts start\",\n    \"build\": \"react-scripts build\",\n    \"test\": \"react-scripts test --env=jsdom\",\n    \"eject\": \"react-scripts eject\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 24,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 24
      },
      "path": "fixtures/attribute-behavior/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 765
    },
    {
      "content": "{\n  \"name\": \"cpu-demo\",\n  \"version\": \"0.1.0\",\n  \"private\": true,\n  \"dependencies\": {\n    \"glamor\": \"^2.20.40\",\n    \"react\": \"0.0.0-experimental-269dd6ec5\",\n    \"react-dom\": \"0.0.0-experimental-269dd6ec5\",\n    \"react-markdown\": \"^3.2.0\",\n    \"react-scripts\": \"^1.1.4\",\n    \"victory\": \"^0.25.6\"\n  },\n  \"scripts\": {\n    \"copy-source\": \"cp -r ../../../build/oss-experimental/* ./node_modules/\",\n    \"dev\": \"react-scripts start\",\n    \"build\": \"react-scripts build\",\n    \"test\": \"react-scripts test --env=jsdom\",\n    \"eject\": \"react-scripts eject\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 20,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 20
      },
      "path": "fixtures/concurrent/time-slicing/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 548
    },
    {
      "content": "{\n  \"name\": \"react-fixtures\",\n  \"version\": \"0.1.0\",\n  \"private\": true,\n  \"devDependencies\": {\n    \"react-scripts\": \"^1.0.11\"\n  },\n  \"dependencies\": {\n    \"@babel/standalone\": \"^7.0.0\",\n    \"art\": \"^0.10.3\",\n    \"classnames\": \"^2.2.5\",\n    \"codemirror\": \"^5.40.0\",\n    \"core-js\": \"^2.4.1\",\n    \"jest-diff\": \"^29.4.1\",\n    \"prop-types\": \"^15.6.0\",\n    \"query-string\": \"^4.2.3\",\n    \"react\": \"^19.0.0\",\n    \"react-dom\": \"^19.0.0\",\n    \"semver\": \"^5.5.0\"\n  },\n  \"scripts\": {\n    \"dev\": \"react-scripts start\",\n    \"predev\": \"cp -a ../../build/oss-experimental/. node_modules\",\n    \"build\": \"react-scripts build && cp build/index.html build/200.html\",\n    \"test\": \"react-scripts test --env=jsdom\",\n    \"eject\": \"react-scripts eject\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 28,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 28
      },
      "path": "fixtures/dom/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 733
    },
    {
      "content": "{\n  \"private\": true,\n  \"name\": \"eslint-v10\",\n  \"dependencies\": {\n    \"eslint\": \"^10.0.0\",\n    \"eslint-plugin-react-hooks\": \"link:../../build/oss-stable/eslint-plugin-react-hooks\",\n    \"jiti\": \"^2.4.2\"\n  },\n  \"scripts\": {\n    \"build\": \"node build.mjs && yarn\",\n    \"lint\": \"tsc --noEmit && eslint index.js --report-unused-disable-directives\"\n  },\n  \"devDependencies\": {\n    \"typescript\": \"^5.4.3\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 16,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 16
      },
      "path": "fixtures/eslint-v10/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 402
    },
    {
      "content": "{\n  \"private\": true,\n  \"name\": \"eslint-v6\",\n  \"dependencies\": {\n    \"eslint\": \"^6\",\n    \"eslint-plugin-react-hooks\": \"link:../../build/oss-stable/eslint-plugin-react-hooks\"\n  },\n  \"scripts\": {\n    \"build\": \"node build.mjs && yarn\",\n    \"lint\": \"eslint index.js --report-unused-disable-directives\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 12,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 12
      },
      "path": "fixtures/eslint-v6/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 303
    },
    {
      "content": "{\n  \"private\": true,\n  \"name\": \"eslint-v7\",\n  \"dependencies\": {\n    \"eslint\": \"^7\",\n    \"eslint-plugin-react-hooks\": \"link:../../build/oss-stable/eslint-plugin-react-hooks\"\n  },\n  \"scripts\": {\n    \"build\": \"node build.mjs && yarn\",\n    \"lint\": \"eslint index.js --report-unused-disable-directives\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 12,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 12
      },
      "path": "fixtures/eslint-v7/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 303
    },
    {
      "content": "{\n  \"private\": true,\n  \"name\": \"eslint-v8\",\n  \"dependencies\": {\n    \"eslint\": \"^8\",\n    \"eslint-plugin-react-hooks\": \"link:../../build/oss-stable/eslint-plugin-react-hooks\"\n  },\n  \"scripts\": {\n    \"build\": \"node build.mjs && yarn\",\n    \"lint\": \"eslint index.js --report-unused-disable-directives\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 12,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 12
      },
      "path": "fixtures/eslint-v8/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 303
    },
    {
      "content": "{\n  \"private\": true,\n  \"name\": \"eslint-v9\",\n  \"dependencies\": {\n    \"eslint\": \"^9.33.0\",\n    \"eslint-plugin-react-hooks\": \"link:../../build/oss-stable/eslint-plugin-react-hooks\",\n    \"jiti\": \"^2.4.2\"\n  },\n  \"scripts\": {\n    \"build\": \"node build.mjs && yarn\",\n    \"lint\": \"tsc --noEmit && eslint index.js --report-unused-disable-directives\"\n  },\n  \"devDependencies\": {\n    \"typescript\": \"^5.4.3\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 16,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 16
      },
      "path": "fixtures/eslint-v9/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 401
    },
    {
      "content": "{\n  \"name\": \"expiration-2\",\n  \"version\": \"0.1.0\",\n  \"private\": true,\n  \"dependencies\": {\n    \"react\": \"^16.1.1\",\n    \"react-dom\": \"^16.1.1\",\n    \"react-scripts\": \"1.0.17\"\n  },\n  \"scripts\": {\n    \"predev\":\n      \"cp ../../build/oss-experimental/react/umd/react.development.js public/ && cp ../../build/oss-experimental/react-dom/umd/react-dom.development.js public/\",\n    \"dev\": \"react-scripts start\",\n    \"build\": \"react-scripts build\",\n    \"test\": \"react-scripts test --env=jsdom\",\n    \"eject\": \"react-scripts eject\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 18,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 18
      },
      "path": "fixtures/expiration/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 524
    },
    {
      "content": "{\n  \"name\": \"react-fiber-debugger\",\n  \"version\": \"0.0.1\",\n  \"private\": true,\n  \"devDependencies\": {\n    \"react-scripts\": \"0.9.5\"\n  },\n  \"dependencies\": {\n    \"dagre\": \"^0.7.4\",\n    \"pretty-format\": \"^4.2.1\",\n    \"react-draggable\": \"^2.2.6\",\n    \"react-motion\": \"^0.5.0\"\n  },\n  \"scripts\": {\n    \"dev\": \"react-scripts start\",\n    \"build\": \"react-scripts build\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 1,
      "debt_signals": [
        {
          "line_number": 2,
          "line_snippet": "\"name\": \"react-fiber-debugger\",",
          "pattern": "debugger"
        }
      ],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 18,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 18
      },
      "path": "fixtures/fiber-debugger/package.json",
      "reasons_flagged": [
        "has_debt_signals",
        "dependency_file"
      ],
      "size_bytes": 365
    },
    {
      "content": "{\n  \"name\": \"react-ssr\",\n  \"version\": \"0.1.0\",\n  \"private\": true,\n  \"engines\": {\n    \"node\": \">=14.9.0\"\n  },\n  \"license\": \"MIT\",\n  \"dependencies\": {\n    \"@babel/core\": \"7.14.3\",\n    \"@babel/register\": \"7.13.16\",\n    \"babel-loader\": \"8.1.0\",\n    \"babel-preset-react-app\": \"10.0.0\",\n    \"compression\": \"^1.7.4\",\n    \"concurrently\": \"^5.3.0\",\n    \"express\": \"^4.17.1\",\n    \"nodemon\": \"^2.0.6\",\n    \"react\": \"^19.0.0\",\n    \"react-dom\": \"^19.0.0\",\n    \"react-error-boundary\": \"^3.1.3\",\n    \"resolve\": \"1.12.0\",\n    \"rimraf\": \"^3.0.2\",\n    \"webpack\": \"4.44.2\",\n    \"webpack-cli\": \"^4.2.0\"\n  },\n  \"devDependencies\": {\n    \"cross-env\": \"^7.0.3\",\n    \"prettier\": \"1.19.1\"\n  },\n  \"scripts\": {\n    \"predev\": \"cp -r ../../build/oss-experimental/* ./node_modules/ && rm -rf node_modules/.cache;\",\n    \"prestart\": \"cp -r ../../build/oss-experimental/* ./node_modules/ && rm -rf node_modules/.cache;\",\n    \"dev\": \"concurrently \\\"npm run dev:server\\\" \\\"npm run dev:bundler\\\"\",\n    \"start\": \"concurrently \\\"npm run start:server\\\" \\\"npm run start:bundler\\\"\",\n    \"dev:server\": \"cross-env NODE_ENV=development nodemon -- --inspect server/server.js\",\n    \"start:server\": \"cross-env NODE_ENV=production nodemon -- server/server.js\",\n    \"dev:bundler\": \"cross-env NODE_ENV=development nodemon -- scripts/build.js\",\n    \"start:bundler\": \"cross-env NODE_ENV=production nodemon -- scripts/build.js\"\n  },\n  \"babel\": {\n    \"presets\": [\n      [\n        \"react-app\",\n        {\n          \"runtime\": \"automatic\"\n        }\n      ]\n    ]\n  },\n  \"nodemonConfig\": {\n    \"ignore\": [\n      \"build/*\"\n    ]\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 55,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 2,
        "total_lines": 55
      },
      "path": "fixtures/fizz/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 1575
    },
    {
      "content": "{\n  \"type\": \"module\"\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 3,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 0,
        "total_lines": 3
      },
      "path": "fixtures/flight-esm/loader/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 23
    },
    {
      "content": "{\n  \"name\": \"flight-esm\",\n  \"type\": \"module\",\n  \"version\": \"0.1.0\",\n  \"private\": true,\n  \"dependencies\": {\n    \"body-parser\": \"^1.20.1\",\n    \"browserslist\": \"^4.18.1\",\n    \"busboy\": \"^1.6.0\",\n    \"compression\": \"^1.7.4\",\n    \"concurrently\": \"^7.3.0\",\n    \"nodemon\": \"^2.0.19\",\n    \"prompts\": \"^2.4.2\",\n    \"react\": \"experimental\",\n    \"react-dom\": \"experimental\",\n    \"undici\": \"^5.20.0\",\n    \"webpack-sources\": \"^3.2.0\"\n  },\n  \"scripts\": {\n    \"predev\": \"cp -r ../../build/oss-experimental/* ./node_modules/ && rm -rf node_modules/.cache;\",\n    \"prestart\": \"cp -r ../../build/oss-experimental/* ./node_modules/ && rm -rf node_modules/.cache;\",\n    \"dev\": \"concurrently \\\"npm run dev:region\\\" \\\"npm run dev:global\\\"\",\n    \"dev:global\": \"NODE_ENV=development BUILD_PATH=dist node server/global\",\n    \"dev:region\": \"NODE_ENV=development BUILD_PATH=dist nodemon --watch src --watch dist -- --enable-source-maps --experimental-loader ./loader/region.js --conditions=react-server server/region\",\n    \"start\": \"concurrently \\\"npm run start:region\\\" \\\"npm run start:global\\\"\",\n    \"start:global\": \"NODE_ENV=production node server/global\",\n    \"start:region\": \"NODE_ENV=production node --experimental-loader ./loader/region.js --conditions=react-server server/region\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 29,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 1,
        "total_lines": 29
      },
      "path": "fixtures/flight-esm/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 1266
    },
    {
      "content": "{\n  \"type\": \"commonjs\"\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 3,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 0,
        "total_lines": 3
      },
      "path": "fixtures/flight-esm/server/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 25
    },
    {
      "content": "{\n  \"name\": \"flight-parcel\",\n  \"private\": true,\n  \"source\": \"src/server.tsx\",\n  \"server\": \"dist/server.js\",\n  \"targets\": {\n    \"server\": {\n      \"context\": \"react-server\",\n      \"includeNodeModules\": {\n        \"express\": false\n      }\n    }\n  },\n  \"scripts\": {\n    \"predev\": \"cp -r ../../build/oss-experimental/* ./node_modules/\",\n    \"prebuild\": \"cp -r ../../build/oss-experimental/* ./node_modules/\",\n    \"dev\": \"parcel\",\n    \"build\": \"parcel build\",\n    \"start\": \"node dist/server.js\"\n  },\n  \"dependencies\": {\n    \"@types/parcel-env\": \"^0.0.6\",\n    \"@types/express\": \"*\",\n    \"@types/node\": \"^22.10.1\",\n    \"@types/react\": \"^19\",\n    \"@types/react-dom\": \"^19\",\n    \"concurrently\": \"^7.3.0\",\n    \"express\": \"^4.18.2\",\n    \"parcel\": \"canary\",\n    \"process\": \"^0.11.10\",\n    \"react\": \"experimental\",\n    \"react-dom\": \"experimental\",\n    \"react-server-dom-parcel\": \"experimental\",\n    \"rsc-html-stream\": \"^0.0.4\"\n  }\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 36,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 2,
        "total_lines": 36
      },
      "path": "fixtures/flight-parcel/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 918
    },
    {
      "content": "{\n  \"type\": \"commonjs\"\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 3,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 0,
        "total_lines": 3
      },
      "path": "fixtures/flight/config/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 25
    },
    {
      "content": "{\n  \"type\": \"module\"\n}\n",
      "debt_category_hint": "dependencies",
      "debt_signal_count": 0,
      "debt_signals": [],
      "language": "json",
      "metrics": {
        "blank_lines": 0,
        "code_lines": 3,
        "comment_lines": 0,
        "comment_ratio": 0.0,
        "long_function_count": 0,
        "long_functions_detected": [],
        "max_indentation_depth": 0,
        "total_lines": 3
      },
      "path": "fixtures/flight/loader/package.json",
      "reasons_flagged": [
        "dependency_file"
      ],
      "size_bytes": 23
    }
  ],
  "flagged_files_count": 30,
  "message": "Extracted 30 flagged/dependency files",
  "repo_url": "facebook/react",
  "status": "success",
  "total_files_scanned": 30
}

```

---

## [12] backend/github_client.py
**Size:** 8.7KB

```python
import requests
from urllib.parse import urlparse
from chunker import scan_debt_signals, compute_file_metrics, get_debt_category_hint

# Setup filtering constants
ALLOWED_EXTENSIONS = {
    '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.rb', '.php', 
    '.c', '.cpp', '.h', '.cs', '.md', '.json', '.yml', '.yaml', '.html', '.css'
}

CRITICAL_FILES = {
    'package.json', 'requirements.txt', '.env.example', 'pom.xml', 
    'go.mod', 'dockerfile', 'docker-compose.yml'
}

EXCLUDED_DIRS = {
    'node_modules', 'venv', '.git', 'build', 'dist', 'out', 'bin', 
    'obj', 'images', 'assets', '.next', '__pycache__', 'coverage'
}

EXT_MAP = {
    "py": "python",
    "js": "javascript",
    "ts": "typescript",
    "java": "java",
    "go": "go",
    "rb": "ruby",
    "php": "php",
    "c": "c",
    "cpp": "cpp",
    "cs": "csharp",
    "md": "markdown",
    "json": "json",
    "yml": "yaml",
    "yaml": "yaml",
    "html": "html",
    "css": "css"
}

def parse_repo_url(url):
    """Extract owner and repo from https://github.com/user/repo"""
    url = url.strip()
    if url.endswith('/'):
        url = url[:-1]
    if url.endswith('.git'):
        url = url[:-4]
        
    if url.startswith('http'):
        path = urlparse(url).path.strip('/')
    else:
        path = url.strip('/')
    
    parts = path.split('/')
    if len(parts) >= 2:
        return parts[-2], parts[-1]
    raise ValueError(f"Invalid GitHub URL: {url}")

def should_keep_file(file_path):
    """Determine if a file should be included in the AI scan."""
    path_parts = file_path.split('/')
    
    # 1. Ignore excluded directories
    if any(excluded in path_parts for excluded in EXCLUDED_DIRS):
        return False
        
    filename = path_parts[-1].lower()
    
    # 2. Keep critical configuration and dependency files
    if filename in CRITICAL_FILES:
        return True
        
    # 3. Check allowed extensions
    ext = '.' + filename.split('.')[-1] if '.' in filename else ''
    if ext in ALLOWED_EXTENSIONS:
        return True
        
    return False

def get_default_branch(owner, repo, headers):
    """Fetch the default branch of a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 403:
        raise Exception("GitHub rate limit exceeded")
    if response.status_code == 200:
        return response.json().get('default_branch', 'main')
    return 'main' # Fallback


def get_latest_commit_sha(url, github_token=None, branch_name=None):
    """
    Fetch the latest commit SHA for a repository branch.
    Used by watch mode so scans trigger on actual repo changes, not polling alone.
    """
    owner, repo = parse_repo_url(url)

    headers = {'Accept': 'application/vnd.github.v3+json'}
    if github_token:
        headers['Authorization'] = f'token {github_token}'

    branch = branch_name or get_default_branch(owner, repo, headers)
    commit_url = f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}"

    try:
        response = requests.get(commit_url, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        raise Exception(f"GitHub commit request timed out for {owner}/{repo}@{branch}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"GitHub API error fetching commit SHA: {str(e)}")

    if response.status_code == 403:
        raise Exception("GitHub rate limit exceeded")
    if response.status_code != 200:
        raise Exception(f"Failed to fetch latest commit (Status {response.status_code}): {response.text[:200]}")

    data = response.json()
    return {
        "branch_name": branch,
        "commit_sha": data.get("sha"),
        "commit_url": data.get("html_url"),
    }

def fetch_repo(url, github_token=None, max_files=30):
    """
    Fetch the useful files from a GitHub repository.
    Uses GitHub Tree API directly then fetches Raw content to save API limit.
    """
    owner, repo = parse_repo_url(url)
    
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if github_token:
        headers['Authorization'] = f'token {github_token}'
        
    branch = get_default_branch(owner, repo, headers)
    
    # Get the recursive tree
    print(f"[DEBUG] Fetching tree for {owner}/{repo} branch {branch}...")
    tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    try:
        response = requests.get(tree_url, headers=headers, timeout=20)
    except requests.exceptions.Timeout:
        raise Exception(f"GitHub API tree request timed out for {owner}/{repo}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"GitHub API error fetching tree: {str(e)}")
    
    print(f"[DEBUG] Tree response status: {response.status_code}")
    
    if response.status_code == 403:
        raise Exception("GitHub rate limit exceeded")
    if response.status_code != 200:
        raise Exception(f"Failed to fetch repo tree (Status {response.status_code}): {response.text[:200]}")
    
    print(f"[DEBUG] Processing tree response...")    
    tree = response.json().get('tree', [])
    
    # Check if response was truncated (large repos)
    tree_data = response.json()
    if tree_data.get('truncated'):
        print(f"[WARN] Tree response was truncated. GitHub limits recursive tree to 100,000 items.")
        print(f"[WARN] Will use available {len(tree)} items")
    
    print(f"[DEBUG] Found {len(tree)} items in tree")
    
    # Filter tree
    valid_files = [item for item in tree if item['type'] == 'blob' and should_keep_file(item['path'])]
    
    # Optional: Prioritize config files, then regular code. Cap at max_files to prevent massive payloads.
    valid_files.sort(key=lambda x: 0 if x['path'].split('/')[-1].lower() in CRITICAL_FILES else 1)
    valid_files = valid_files[:max_files]
    
    fetched_files = []
    
    print(f"[DEBUG] Starting to fetch {len(valid_files)} files...")
    for idx, item in enumerate(valid_files):
        path = item['path']
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
        
        # We download via Raw endpoint as it rarely ratelimits compared to the API
        try:
            print(f"[DEBUG] Fetching file {idx+1}/{len(valid_files)}: {path}")
            file_resp = requests.get(raw_url, timeout=10)
        except requests.exceptions.Timeout:
            print(f"[WARN] File fetch timeout: {path}")
            continue
        except requests.exceptions.RequestException as e:
            print(f"[WARN] Failed to fetch {path}: {e}")
            continue
            
        if file_resp.status_code == 403:
            raise Exception("GitHub rate limit exceeded")
            
        if file_resp.status_code == 200:
            content = file_resp.text
            
            if not content.strip():
                print(f"[SKIP] Empty file: {path}")
                continue
                
            if len(content) > 10000:
                print(f"[SKIP] File too large ({len(content)} bytes): {path}")
                continue
            
            # Simple language detection based on extension
            raw_ext = path.split('.')[-1] if '.' in path else 'text'
            language = EXT_MAP.get(raw_ext.lower(), raw_ext)
            
            print(f"[OK] Fetched: {path} ({len(content)} bytes)")
            
            # Compute analysis metadata
            debt_signals = scan_debt_signals(content)
            metrics = compute_file_metrics(content, language)
            debt_hint = get_debt_category_hint(path)
            
            fetched_files.append({
                "path": path,
                "language": language,
                "content": content,
                "size_bytes": len(content.encode('utf-8')),
                "debt_category_hint": debt_hint,
                "debt_signals": debt_signals,
                "debt_signal_count": len(debt_signals),
                "metrics": metrics,
            })
            
    return fetched_files

def categorize_files(files):
    """
    Groups fetched files into config, dependencies, and code
    to allow for optimized, domain-specific AI processing.
    """
    config, deps, code = [], [], []

    for f in files:
        name = f["path"].lower()
        basename = name.split('/')[-1]
        
        if basename in ["package.json", "requirements.txt", "dockerfile", "pom.xml", "go.mod"]:
            deps.append(f)
        elif basename.endswith((".yml", ".yaml", ".json", ".env", ".env.example")):
            config.append(f)
        else:
            code.append(f)

    return config, deps, code

```

---

## [13] backend/lambdas/fetcher/handler.py
**Size:** 2.7KB

```python
import json
import os
import sys
import hashlib

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from github_client import fetch_repo, categorize_files
from chunker import chunk_code


def lambda_handler(event, context):
    """
    AWS Lambda handler for fetching and chunking GitHub repositories
    """
    try:
        print("[FETCHER] Starting fetch operation...")

        # Extract repo URL from event
        repo_url = event.get('repo_url')
        if not repo_url:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'repo_url is required'})
            }

        # Normalize URL
        if not repo_url.startswith('http'):
            repo_url = f"https://github.com/{repo_url}"

        print(f"[FETCHER] Repository: {repo_url}")

        # Generate repo ID
        repo_id = hashlib.md5(repo_url.encode()).hexdigest()[:8]

        # 1. Fetch repository
        print("[FETCHER] Step 1: Fetching repository...")
        github_token = os.environ.get('GITHUB_TOKEN')
        files = fetch_repo(repo_url, github_token=github_token)
        print(f"[FETCHER] Fetched {len(files)} files")

        # 2. Categorize files
        print("[FETCHER] Step 2: Categorizing files...")
        config_files, dep_files, source_code = categorize_files(files)
        print(f"[FETCHER] Categorized: {len(config_files)} config, {len(dep_files)} deps, {len(source_code)} source")

        # 3. Chunk code
        print("[FETCHER] Step 3: Chunking code...")
        chunks = chunk_code(files)
        print(f"[FETCHER] Created {len(chunks)} chunks")

        # Prepare response
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'repo_id': repo_id,
                'repo_url': repo_url,
                'total_files': len(files),
                'categories': {
                    'config': len(config_files),
                    'dependencies': len(dep_files),
                    'source_code': len(source_code)
                },
                'chunks': chunks,
                'files': files
            })
        }

        print(f"[FETCHER] Complete: {len(chunks)} chunks ready for analysis")
        return response

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"[FETCHER] ERROR: {error_msg}")
        print(f"[FETCHER] Traceback: {tb}")

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': error_msg,
                'type': type(e).__name__,
                'traceback': tb
            })
        }
```

---

## [14] backend/lambdas/processor/handler.py
**Size:** 0.0B

```python

```

---

## [15] backend/lambdas/scorer/handler.py
**Size:** 6.0KB

```python
import json
import os
import sys

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))


def calculate_health_score(security_findings, debt_findings):
    """
    Calculate overall health score based on findings
    """
    health_score = 100

    # Penalize for security issues
    for finding in security_findings:
        severity = finding.get('severity', 'LOW')
        if severity == 'CRITICAL':
            health_score -= 20
        elif severity == 'HIGH':
            health_score -= 10
        elif severity == 'MEDIUM':
            health_score -= 5
        elif severity == 'LOW':
            health_score -= 1

    # Penalize for debt issues (less severe)
    for finding in debt_findings:
        severity = finding.get('severity', 'LOW')
        if severity == 'CRITICAL':
            health_score -= 5
        elif severity == 'HIGH':
            health_score -= 3
        elif severity == 'MEDIUM':
            health_score -= 2
        elif severity == 'LOW':
            health_score -= 0.5

    return max(0, min(100, health_score))


def categorize_findings(findings):
    """
    Categorize findings by type and severity
    """
    categories = {
        'critical': [],
        'high': [],
        'medium': [],
        'low': []
    }

    for finding in findings:
        severity = finding.get('severity', 'LOW').lower()
        if severity in categories:
            categories[severity].append(finding)

    return categories


def lambda_handler(event, context):
    """
    AWS Lambda handler for scoring analysis results
    """
    try:
        print("[SCORER] Starting scoring operation...")

        # Extract analysis results from event
        body = event.get('body', '{}')
        if isinstance(body, str):
            data = json.loads(body)
        else:
            data = body

        repo_id = data.get('repo_id')
        repo_url = data.get('repo_url')
        security_findings = data.get('security_findings', [])
        debt_findings = data.get('debt_findings', [])
        chunks_scanned = data.get('chunks_scanned', 0)
        total_files = data.get('total_files', 0)

        if not repo_id or not repo_url:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'repo_id and repo_url are required'})
            }

        print(f"[SCORER] Scoring repo: {repo_url} ({repo_id})")

        # Calculate health score
        health_score = calculate_health_score(security_findings, debt_findings)

        # Categorize findings
        security_categories = categorize_findings(security_findings)
        debt_categories = categorize_findings(debt_findings)

        # Identify quick wins (estimated_minutes < 30)
        quick_wins = [
            f for f in security_findings
            if f.get('estimated_minutes', 60) < 30
        ]

        # Critical issues
        critical_issues = security_categories['critical']

        # Generate recommendations
        recommendations = []

        if len(critical_issues) > 0:
            recommendations.append({
                'priority': 'CRITICAL',
                'action': 'Address critical security issues immediately',
                'count': len(critical_issues)
            })

        if len(quick_wins) > 0:
            recommendations.append({
                'priority': 'HIGH',
                'action': 'Implement quick wins to improve score rapidly',
                'count': len(quick_wins)
            })

        if health_score < 70:
            recommendations.append({
                'priority': 'MEDIUM',
                'action': 'Comprehensive code review and refactoring needed',
                'score': health_score
            })

        # Prepare response
        result = {
            'repo_id': repo_id,
            'repo_url': repo_url,
            'health_score': health_score,
            'chunks_scanned': chunks_scanned,
            'total_files': total_files,
            'analysis': {
                'total_security_issues': len(security_findings),
                'total_debt_issues': len(debt_findings),
                'critical_issues': len(critical_issues),
                'quick_wins': len(quick_wins)
            },
            'findings': {
                'security_findings': security_findings,
                'debt_findings': debt_findings,
                'security_by_severity': {
                    'critical': len(security_categories['critical']),
                    'high': len(security_categories['high']),
                    'medium': len(security_categories['medium']),
                    'low': len(security_categories['low'])
                },
                'debt_by_severity': {
                    'critical': len(debt_categories['critical']),
                    'high': len(debt_categories['high']),
                    'medium': len(debt_categories['medium']),
                    'low': len(debt_categories['low'])
                },
                'quick_wins': quick_wins,
                'critical_issues': critical_issues
            },
            'recommendations': recommendations,
            'scoring_metadata': {
                'scoring_version': '1.0',
                'scoring_algorithm': 'weighted_penalty',
                'max_score': 100,
                'min_score': 0
            }
        }

        print(f"[SCORER] Complete: Health score {health_score}/100")

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    except Exception as e:
        import traceback
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"[SCORER] ERROR: {error_msg}")
        print(f"[SCORER] Traceback: {tb}")

        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': error_msg,
                'type': type(e).__name__,
                'traceback': tb
            })
        }
```

---

## [16] backend/mcp_runtime_server.py
**Size:** 4.2KB

```python
import logging
import os

from mcp.server.fastmcp import FastMCP

from mcp_server import ContinuousIntelligencePipeline, MCPMemoryStore
from mcp_server.continuous_pipeline import repo_id_from_url


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("reposcan-mcp")

mcp = FastMCP("RepoScan Continuous Intelligence", json_response=True)
store = MCPMemoryStore()
pipeline = ContinuousIntelligencePipeline(store=store)


def _normalize_repo_url(repo_url: str) -> str:
    repo_url = repo_url.strip()
    if not repo_url.startswith("http"):
        repo_url = f"https://github.com/{repo_url}"
    return repo_url


@mcp.tool()
def continuous_scan(repo_url: str, branch_name: str = "main", generate_fixes: bool = True):
    """
    Run RepoScan continuous intelligence analysis with MCP memory, incremental scanning,
    context injection, and optional auto-fix generation.
    """
    github_token = os.environ.get("GITHUB_TOKEN")
    return pipeline.run(
        repo_url=_normalize_repo_url(repo_url),
        github_token=github_token,
        branch_name=branch_name,
        generate_fixes=generate_fixes,
    )


@mcp.tool()
def get_unresolved_issues(repo_id: str):
    """Return unresolved issues for a previously scanned repository."""
    return {
        "repo_id": repo_id,
        "unresolved_issues": store.get_unresolved_issues(repo_id),
    }


@mcp.tool()
def get_issue_delta(repo_id: str):
    """
    Return the latest issue delta for a repo:
    new issues, resolved issues, and persisting issues from the most recent sync.
    """
    return store.get_latest_issue_delta(repo_id)


@mcp.tool()
def sync_agent_change(
    repo_url: str,
    branch_name: str = "main",
    command_name: str = "agent_change",
    notes: str = "",
    generate_fixes: bool = True,
):
    """
    Call this after Antigravity/Claude makes a code change.
    It records the command event, runs a fresh sync, and returns the updated issue delta.
    """
    normalized_repo_url = _normalize_repo_url(repo_url)
    repo_id = repo_id_from_url(normalized_repo_url)
    command_event = store.record_command_event(
        repo_id=repo_id,
        command_name=command_name,
        notes=notes,
        metadata={"branch_name": branch_name},
    )
    github_token = os.environ.get("GITHUB_TOKEN")
    result = pipeline.run(
        repo_url=normalized_repo_url,
        github_token=github_token,
        branch_name=branch_name,
        generate_fixes=generate_fixes,
    )
    return {
        "command_event": command_event,
        "scan_result": result,
        "issue_delta": store.get_latest_issue_delta(repo_id),
        "context": store.get_context(repo_id),
    }


@mcp.tool()
def update_fix_status(
    repo_id: str,
    issue_fingerprint: str,
    status: str,
    validation_status: str,
    explanation: str = "",
    diff_patch: str = "",
    remediated_code: str = "",
):
    """Update auto-fix status for a stored issue."""
    return store.update_fix_status(
        repo_id=repo_id,
        issue_fingerprint=issue_fingerprint,
        status=status,
        validation_status=validation_status,
        explanation=explanation,
        diff_patch=diff_patch,
        remediated_code=remediated_code,
    )


@mcp.resource("repomemory://context/{repo_id}")
def repo_context(repo_id: str):
    """Read stored MCP context for a repository."""
    return str(store.get_context(repo_id))


@mcp.resource("repomemory://unresolved/{repo_id}")
def unresolved_resource(repo_id: str):
    """Read unresolved issues for a repository."""
    return str(store.get_unresolved_issues(repo_id))


@mcp.resource("repomemory://delta/{repo_id}")
def delta_resource(repo_id: str):
    """Read latest issue delta for a repository."""
    return str(store.get_latest_issue_delta(repo_id))


@mcp.resource("repomemory://commands/{repo_id}")
def commands_resource(repo_id: str):
    """Read recent agent/command events for a repository."""
    return str(store.list_recent_commands(repo_id, limit=20))


if __name__ == "__main__":
    transport = os.environ.get("MCP_TRANSPORT", "stdio").strip().lower()
    logger.info("Starting RepoScan MCP server with transport=%s", transport)
    if transport == "http":
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")

```

---

## [17] backend/mcp_server/__init__.py
**Size:** 250.0B

```python
from .storage import MCPMemoryStore
from .continuous_pipeline import ContinuousIntelligencePipeline
from .watcher import ContinuousWatchManager

__all__ = [
    "MCPMemoryStore",
    "ContinuousIntelligencePipeline",
    "ContinuousWatchManager",
]


```

---

## [18] backend/mcp_server/analyzer.py
**Size:** 4.2KB

```python
from typing import Any, Dict, List

from ai.bedrock_client import _debt_signal_to_vulnerability, classify_file, invoke_bedrock

from .prompting import build_contextual_prompt


def normalize_vulnerability(vulnerability: Dict[str, Any], chunk: Dict[str, Any]) -> Dict[str, Any]:
    return {
        **vulnerability,
        "file": chunk.get("file", "unknown"),
        "category": "security",
        "line_range": vulnerability.get("line_range") or f"{chunk.get('start_line', '?')}-{chunk.get('end_line', '?')}",
    }


def scan_chunk_with_context(chunk: Dict[str, Any], repo_context: Dict[str, Any], branch_name: str = "main") -> Dict[str, Any]:
    prompt = build_contextual_prompt(chunk, repo_context, branch_name)
    result = invoke_bedrock(prompt, chunk.get("file", "unknown"))
    vulnerabilities = [
        normalize_vulnerability(vulnerability, chunk)
        for vulnerability in result.get("vulnerabilities", [])
    ]

    if not vulnerabilities and chunk.get("debt_signals"):
        vulnerabilities = [
            normalize_vulnerability(_debt_signal_to_vulnerability(signal, chunk.get("file", "unknown")), chunk)
            for signal in chunk.get("debt_signals", [])
        ]

    return {
        "file": chunk.get("file", "unknown"),
        "file_type": classify_file(chunk.get("file", "unknown")),
        "vulnerabilities": vulnerabilities,
        "has_issues": bool(vulnerabilities),
        "vulnerability_count": len(vulnerabilities),
    }


def scan_all_chunks_with_context(chunks: List[Dict[str, Any]], repo_context: Dict[str, Any], branch_name: str = "main") -> Dict[str, Any]:
    all_vulnerabilities: List[Dict[str, Any]] = []
    vulnerable_files: List[Dict[str, Any]] = []

    for chunk in chunks:
        result = scan_chunk_with_context(chunk, repo_context, branch_name)
        if result["has_issues"]:
            vulnerable_files.append(
                {
                    "file": result["file"],
                    "type": result["file_type"],
                    "count": result["vulnerability_count"],
                }
            )
            all_vulnerabilities.extend(result["vulnerabilities"])

    return {
        "vulnerabilities": all_vulnerabilities,
        "vulnerable_files": vulnerable_files,
        "total_files_analyzed": len(chunks),
        "files_with_issues": len(vulnerable_files),
        "total_vulnerabilities": len(all_vulnerabilities),
        "context_applied": True,
    }


def build_debt_findings_from_files(files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    for file in files:
        for signal in file.get("debt_signals", []):
            findings.append(
                {
                    "type": "DEBT_SIGNAL",
                    "severity": "MEDIUM" if file.get("debt_signal_count", 0) > 2 else "LOW",
                    "file": file["path"],
                    "line_range": str(signal.get("line_number", "?")),
                    "summary": signal.get("line_snippet", "Technical debt signal"),
                    "estimated_minutes": 10,
                    "estimated_minutes_to_fix": 10,
                    "metadata": {
                        "pattern": signal.get("pattern"),
                        "line_snippet": signal.get("line_snippet"),
                        "category_hint": file.get("debt_category_hint", "code_quality"),
                    },
                }
            )

        for long_fn in file.get("metrics", {}).get("long_functions_detected", []):
            findings.append(
                {
                    "type": "LONG_FUNCTION",
                    "severity": "MEDIUM",
                    "file": file["path"],
                    "line_range": str(long_fn.get("approximate_start_line", "?")),
                    "summary": long_fn.get("first_line", "Large function detected"),
                    "estimated_minutes": 20,
                    "estimated_minutes_to_fix": 20,
                    "metadata": {
                        "approximate_length_lines": long_fn.get("approximate_length_lines", 0),
                        "category_hint": file.get("debt_category_hint", "code_quality"),
                    },
                }
            )

    return findings


```

---

## [19] backend/mcp_server/autofix.py
**Size:** 4.2KB

```python
import difflib
import re
from typing import Any, Dict, List

from .analyzer import scan_chunk_with_context


def _make_patch(file_path: str, original: str, updated: str) -> str:
    return "".join(
        difflib.unified_diff(
            original.splitlines(keepends=True),
            updated.splitlines(keepends=True),
            fromfile=file_path,
            tofile=f"{file_path}.fixed",
        )
    )


def _fix_hardcoded_secret(content: str) -> Dict[str, Any]:
    updated = re.sub(r'(["\'])([^"\']{4,})(["\'])', '"REDACTED_FROM_ENV"', content, count=1)
    return {
        "updated": updated,
        "explanation": "Replaced a likely hardcoded secret with an environment-managed placeholder.",
    }


def _fix_unsafe_eval(content: str) -> Dict[str, Any]:
    updated = content.replace("eval(", "ast.literal_eval(")
    if updated != content and "import ast" not in updated:
        updated = "import ast\n" + updated
    return {
        "updated": updated,
        "explanation": "Replaced eval() with ast.literal_eval() for safer parsing.",
    }


def _fix_dependency_line(content: str, issue: Dict[str, Any]) -> Dict[str, Any]:
    recommended = issue.get("recommended_version") or issue.get("metadata", {}).get("recommended_version")
    package = issue.get("package") or issue.get("metadata", {}).get("package")
    if not package or not recommended:
        return {"updated": content, "explanation": "No concrete package/version data available for auto-upgrade."}
    updated = re.sub(
        rf"^{re.escape(package)}.*$",
        f"{package}=={recommended}",
        content,
        flags=re.MULTILINE,
    )
    return {
        "updated": updated,
        "explanation": f"Updated dependency suggestion for {package} to {recommended}.",
    }


def generate_fix(issue: Dict[str, Any], file_content: str) -> Dict[str, Any]:
    issue_type = (issue.get("issue_type") or issue.get("type") or "").upper()

    fixer_result = {"updated": file_content, "explanation": "No safe deterministic fix available yet."}
    if "SECRET" in issue_type:
        fixer_result = _fix_hardcoded_secret(file_content)
    elif "EVAL" in issue_type:
        fixer_result = _fix_unsafe_eval(file_content)
    elif issue_type in {"OUTDATED", "VULNERABLE", "UNPINNED"}:
        fixer_result = _fix_dependency_line(file_content, issue)

    updated = fixer_result["updated"]
    patch = _make_patch(issue["file_path"], file_content, updated)

    return {
        "issue": issue["summary"],
        "remediated_code": updated,
        "diff": patch,
        "explanation": fixer_result["explanation"],
    }


def validate_fix(
    issue: Dict[str, Any],
    fixed_code: str,
    repo_context: Dict[str, Any],
    language: str = "text",
) -> Dict[str, Any]:
    validation_chunk = {
        "file": issue["file_path"],
        "language": language,
        "code": fixed_code,
        "debt_signals": [],
        "context_note": "Validation pass on remediated code.",
        "start_line": 1,
        "end_line": max(1, len(fixed_code.splitlines())),
    }
    result = scan_chunk_with_context(validation_chunk, repo_context)
    remaining = [
        vuln for vuln in result.get("vulnerabilities", [])
        if (vuln.get("type") or "").upper() == issue["issue_type"].upper()
    ]

    status = "FAILED" if remaining else "VALIDATED"
    return {
        "status": status,
        "remaining_issues": remaining,
    }


def generate_and_validate_fixes(
    issues: List[Dict[str, Any]],
    file_map: Dict[str, Dict[str, Any]],
    repo_context: Dict[str, Any],
) -> List[Dict[str, Any]]:
    fixes = []
    for issue in issues:
        file_info = file_map.get(issue["file_path"])
        if not file_info:
            continue
        proposal = generate_fix(issue, file_info.get("content", ""))
        validation = validate_fix(
            issue,
            proposal["remediated_code"],
            repo_context,
            language=file_info.get("language", "text"),
        )
        fixes.append(
            {
                **proposal,
                "file_path": issue["file_path"],
                "fingerprint": issue["fingerprint"],
                "validation_status": validation["status"],
                "remaining_issues": validation["remaining_issues"],
            }
        )
    return fixes


```

---

## [20] backend/mcp_server/context.py
**Size:** 2.4KB

```python
from typing import Any, Dict, List


def build_repo_context(repo_context: Dict[str, Any], file_path: str) -> Dict[str, Any]:
    file_history = repo_context.get("file_history", {}).get(file_path, {})
    unresolved = file_history.get("unresolved", [])
    resolved = file_history.get("resolved", [])
    latest_scan = repo_context.get("latest_scan") or {}
    history = repo_context.get("history", [])

    trend = None
    if len(history) >= 2:
        current = history[0].get("scoring", {}).get("health_score")
        previous = history[1].get("scoring", {}).get("health_score")
        if current is not None and previous is not None:
            trend = {
                "current_health_score": current,
                "previous_health_score": previous,
                "delta": current - previous,
            }

    return {
        "latest_scan_id": latest_scan.get("scan_id"),
        "history_depth": len(history),
        "unresolved_for_file": unresolved,
        "resolved_for_file": resolved[:5],
        "trend": trend,
    }


def render_context_block(file_path: str, repo_context: Dict[str, Any]) -> str:
    file_ctx = build_repo_context(repo_context, file_path)
    unresolved = file_ctx["unresolved_for_file"]
    resolved = file_ctx["resolved_for_file"]
    trend = file_ctx["trend"]

    lines: List[str] = [
        "MCP CONTEXT",
        f"File under analysis: {file_path}",
        f"History depth: {file_ctx['history_depth']} prior scan(s)",
    ]

    if unresolved:
        lines.append("Previously unresolved issues for this file:")
        for issue in unresolved[:5]:
            lines.append(
                f"- {issue['issue_type']} ({issue['severity']}): {issue['summary']}"
            )
    else:
        lines.append("Previously unresolved issues for this file: none")

    if resolved:
        lines.append("Recently resolved issues for this file:")
        for issue in resolved[:3]:
            lines.append(
                f"- {issue['issue_type']} ({issue['severity']}): {issue['summary']}"
            )

    if trend:
        lines.append(
            "Repo score trend: "
            f"{trend['previous_health_score']} -> {trend['current_health_score']} "
            f"(delta {trend['delta']:+})"
        )

    lines.append("Use this history to avoid duplicate noise and focus on regressions, unresolved risks, and meaningful changes.")
    return "\n".join(lines)


```

---

## [21] backend/mcp_server/continuous_pipeline.py
**Size:** 9.8KB

```python
import hashlib
import json
from typing import Any, Dict, List

from chunker import chunk_code
from github_client import fetch_repo
from lambdas.scorer.handler import lambda_handler as scorer_lambda_handler

from .analyzer import build_debt_findings_from_files, scan_all_chunks_with_context
from .autofix import generate_and_validate_fixes
from .diffing import build_file_metadata, compute_incremental_changes
from .storage import MCPMemoryStore


def repo_id_from_url(repo_url: str) -> str:
    return hashlib.md5(repo_url.encode()).hexdigest()[:8]


def _severity_rank(severity: str) -> int:
    order = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}
    return order.get((severity or "LOW").upper(), 1)


def _issue_fingerprint(issue: Dict[str, Any]) -> str:
    raw = "|".join(
        [
            issue.get("file", issue.get("file_path", "unknown")),
            issue.get("type", "UNKNOWN"),
            str(issue.get("line_range", "?")),
            issue.get("explanation", issue.get("summary", ""))[:120],
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]


def _normalize_security_findings(vulnerabilities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    findings = []
    for vulnerability in vulnerabilities:
        findings.append(
            {
                **vulnerability,
                "file": vulnerability.get("file", "unknown"),
                "severity": vulnerability.get("severity", "LOW"),
                "estimated_minutes": vulnerability.get("estimated_minutes_to_fix", 15),
            }
        )
    return findings


def _issues_from_findings(security_findings: List[Dict[str, Any]], debt_findings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    issues: List[Dict[str, Any]] = []
    for finding in security_findings:
        issues.append(
            {
                "fingerprint": _issue_fingerprint(finding),
                "file_path": finding.get("file", "unknown"),
                "category": "security",
                "issue_type": finding.get("type", "UNKNOWN"),
                "severity": finding.get("severity", "LOW"),
                "status": "OPEN",
                "summary": finding.get("explanation", finding.get("type", "Security issue")),
                "metadata": {
                    "line_range": finding.get("line_range"),
                    "business_impact": finding.get("business_impact"),
                    "remediation": finding.get("remediation"),
                },
            }
        )
    for finding in debt_findings:
        issues.append(
            {
                "fingerprint": _issue_fingerprint(finding),
                "file_path": finding.get("file", "unknown"),
                "category": "debt",
                "issue_type": finding.get("type", "DEBT_SIGNAL"),
                "severity": finding.get("severity", "LOW"),
                "status": "OPEN",
                "summary": finding.get("summary", "Technical debt finding"),
                "metadata": finding.get("metadata", {}),
            }
        )
    issues.sort(key=lambda item: _severity_rank(item["severity"]), reverse=True)
    return issues


class ContinuousIntelligencePipeline:
    """
    Extension pipeline that wraps the existing fetch/chunk/score flow with:
    - memory
    - incremental scanning
    - context-aware analysis
    - auto-fix generation
    """

    def __init__(self, store: MCPMemoryStore = None):
        self.store = store or MCPMemoryStore()

    def run(
        self,
        repo_url: str,
        github_token: str = None,
        branch_name: str = "main",
        generate_fixes: bool = True,
    ) -> Dict[str, Any]:
        repo_id = repo_id_from_url(repo_url)
        files = fetch_repo(repo_url, github_token=github_token)
        file_map = {file["path"]: file for file in files}
        current_metadata = build_file_metadata(files)
        previous_snapshot = self.store.get_latest_snapshot(repo_id)
        previous_metadata = previous_snapshot["files"] if previous_snapshot else []
        changes = compute_incremental_changes(current_metadata, previous_metadata)
        unresolved = self.store.get_unresolved_issues(repo_id)
        unresolved_paths = {issue["file_path"] for issue in unresolved}

        if previous_snapshot is None:
            scan_mode = "full"
            selected_paths = [file["path"] for file in files]
        else:
            scan_mode = "incremental"
            selected_paths = sorted(
                set(changes["new_files"] + changes["modified_files"]) | unresolved_paths
            )

        selected_files = [file_map[path] for path in selected_paths if path in file_map]
        chunks = chunk_code(selected_files) if selected_files else []
        repo_context = self.store.get_context(repo_id)
        analysis = scan_all_chunks_with_context(chunks, repo_context, branch_name) if chunks else {
            "vulnerabilities": [],
            "vulnerable_files": [],
            "total_files_analyzed": 0,
            "files_with_issues": 0,
            "total_vulnerabilities": 0,
            "context_applied": True,
        }

        security_findings = _normalize_security_findings(analysis.get("vulnerabilities", []))
        debt_findings = build_debt_findings_from_files(selected_files)

        scorer_event = {
            "body": {
                "repo_id": repo_id,
                "repo_url": repo_url,
                "security_findings": security_findings,
                "debt_findings": debt_findings,
                "chunks_scanned": len(chunks),
                "total_files": len(files),
            }
        }
        score_response = scorer_lambda_handler(scorer_event, None)
        score_body = json.loads(score_response["body"])

        issues = _issues_from_findings(security_findings, debt_findings)
        stored = self.store.store_scan_results(
            repo_id=repo_id,
            repo_url=repo_url,
            branch_name=branch_name,
            scan_mode=scan_mode,
            issues=issues,
            summary={
                "total_files": len(files),
                "files_scanned": len(selected_files),
                "total_chunks": len(chunks),
                "analysis_summary": {
                    "security_findings": len(security_findings),
                    "debt_findings": len(debt_findings),
                },
            },
            scoring=score_body,
            change_summary=changes,
        )
        snapshot_info = self.store.store_snapshot(repo_id, branch_name, current_metadata)

        latest_context = self.store.get_context(repo_id)
        fixes = generate_and_validate_fixes(issues[:10], file_map, latest_context) if generate_fixes else []
        for fix in fixes:
            self.store.update_fix_status(
                repo_id=repo_id,
                issue_fingerprint=fix["fingerprint"],
                status="GENERATED",
                validation_status=fix["validation_status"],
                explanation=fix["explanation"],
                diff_patch=fix["diff"],
                remediated_code=fix["remediated_code"],
            )

        previous_scan = latest_context.get("history", [None, None])
        previous_score = None
        if len(previous_scan) > 1 and previous_scan[1]:
            previous_score = previous_scan[1].get("scoring", {}).get("health_score")
        current_score = score_body.get("health_score")

        return {
            "status": "success",
            "pipeline": "continuous_intelligence_extension",
            "repo_id": repo_id,
            "repo_url": repo_url,
            "branch_name": branch_name,
            "scan_mode": scan_mode,
            "data": {
                "total_files_fetched": len(files),
                "files_scanned": len(selected_files),
                "total_chunks": len(chunks),
                "changed_files": {
                    "new_files": changes["new_files"],
                    "modified_files": changes["modified_files"],
                    "deleted_files": changes["deleted_files"],
                    "unchanged_files_count": len(changes["unchanged_files"]),
                },
                "vulnerable_files": analysis.get("vulnerable_files", []),
                "security_findings": security_findings,
                "debt_findings": debt_findings,
                "autofix_suggestions": fixes,
            },
            "summary": {
                "repo_id": repo_id,
                "health_score": score_body.get("health_score"),
                "total_security_issues": score_body.get("analysis", {}).get("total_security_issues", 0),
                "total_debt_issues": score_body.get("analysis", {}).get("total_debt_issues", 0),
                "critical_issues": score_body.get("analysis", {}).get("critical_issues", 0),
                "quick_wins": score_body.get("analysis", {}).get("quick_wins", 0),
            },
            "continuous_intelligence": {
                "scan_id": stored["scan_id"],
                "snapshot_id": snapshot_info["snapshot_id"],
                "scan_mode": scan_mode,
                "history_depth": len(latest_context.get("history", [])),
                "files_considered": len(files),
                "files_scanned": len(selected_files),
                "new_issues": stored["new_issues"],
                "resolved_issues": stored["resolved_issues"],
                "persisting_issues": stored["persisting_issues"],
                "estimated_fix_minutes": sum(
                    item.get("estimated_minutes_to_fix", item.get("estimated_minutes", 0))
                    for item in security_findings + debt_findings
                ),
                "trend": {
                    "previous_health_score": previous_score,
                    "current_health_score": current_score,
                    "delta": (current_score - previous_score) if previous_score is not None and current_score is not None else None,
                },
            },
        }


```

---

## [22] backend/mcp_server/diffing.py
**Size:** 1.8KB

```python
import hashlib
from typing import Any, Dict, List


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_file_metadata(files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    metadata = []
    for file in files:
        content = file.get("content", "")
        metadata.append(
            {
                "path": file["path"],
                "language": file.get("language", "text"),
                "size_bytes": file.get("size_bytes", len(content.encode("utf-8"))),
                "content_hash": sha256_text(content),
                "debt_signal_count": file.get("debt_signal_count", 0),
                "debt_category_hint": file.get("debt_category_hint", "code_quality"),
            }
        )
    return metadata


def compute_incremental_changes(
    current_metadata: List[Dict[str, Any]],
    previous_metadata: List[Dict[str, Any]],
) -> Dict[str, List[str]]:
    current_map = {item["path"]: item for item in current_metadata}
    previous_map = {item["path"]: item for item in previous_metadata}

    new_files = sorted([path for path in current_map if path not in previous_map])
    deleted_files = sorted([path for path in previous_map if path not in current_map])
    modified_files = sorted(
        [
            path for path, item in current_map.items()
            if path in previous_map and item["content_hash"] != previous_map[path]["content_hash"]
        ]
    )
    unchanged_files = sorted(
        [
            path for path, item in current_map.items()
            if path in previous_map and item["content_hash"] == previous_map[path]["content_hash"]
        ]
    )

    return {
        "new_files": new_files,
        "modified_files": modified_files,
        "deleted_files": deleted_files,
        "unchanged_files": unchanged_files,
    }


```

---

## [23] backend/mcp_server/prompting.py
**Size:** 1.2KB

```python
from typing import Dict

from ai.bedrock_client import classify_file, generate_security_prompt

from .context import render_context_block


def select_prompt_profile(chunk: Dict, file_path: str) -> str:
    filename = file_path or chunk.get("file", "unknown")
    file_type = classify_file(filename)
    if file_type == "deps":
        return "dependency_vulnerability"
    if file_type in {"iam", "iac"}:
        return "config_security"
    return "application_security_and_debt"


def build_contextual_prompt(chunk: Dict, repo_context: Dict, branch_name: str) -> str:
    file_path = chunk.get("file", "unknown")
    file_type = classify_file(file_path)
    base_prompt = generate_security_prompt(file_path, chunk.get("code", ""), file_type, branch_name)
    context_block = render_context_block(file_path, repo_context)
    chunk_note = chunk.get("context_note", "")
    profile = select_prompt_profile(chunk, file_path)

    return (
        f"You are operating in optimized profile: {profile}.\n"
        "Return strict JSON only. Do not include markdown fences.\n\n"
        f"{context_block}\n\n"
        f"CHUNK CONTEXT\n{chunk_note}\n\n"
        f"{base_prompt}"
    )


```

---

## [24] backend/mcp_server/storage.py
**Size:** 22.0KB

```python
import json
import os
import sqlite3
import threading
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional


def utc_now() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


class MCPMemoryStore:
    """
    Lightweight persistent memory layer for continuous scans.
    Stores only metadata, summaries, and issue history.
    """

    def __init__(self, db_path: Optional[str] = None):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        data_dir = os.path.join(base_dir, "mcp_data")
        os.makedirs(data_dir, exist_ok=True)
        self.db_path = db_path or os.path.join(data_dir, "mcp_memory.db")
        self._lock = threading.Lock()
        self._init_db()

    def _connect(self):
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._lock:
            conn = self._connect()
            try:
                conn.executescript(
                    """
                    CREATE TABLE IF NOT EXISTS scans (
                        scan_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        repo_url TEXT NOT NULL,
                        branch_name TEXT NOT NULL,
                        scan_mode TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        summary_json TEXT NOT NULL,
                        scoring_json TEXT NOT NULL,
                        change_summary_json TEXT NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS snapshots (
                        snapshot_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        branch_name TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        file_count INTEGER NOT NULL,
                        files_json TEXT NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS issues (
                        issue_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        scan_id TEXT NOT NULL,
                        fingerprint TEXT NOT NULL,
                        file_path TEXT NOT NULL,
                        category TEXT NOT NULL,
                        issue_type TEXT NOT NULL,
                        severity TEXT NOT NULL,
                        status TEXT NOT NULL,
                        summary TEXT NOT NULL,
                        first_seen_at TEXT NOT NULL,
                        last_seen_at TEXT NOT NULL,
                        metadata_json TEXT NOT NULL
                    );

                    CREATE UNIQUE INDEX IF NOT EXISTS idx_issues_repo_fingerprint
                    ON issues(repo_id, fingerprint);

                    CREATE TABLE IF NOT EXISTS fixes (
                        fix_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        issue_fingerprint TEXT NOT NULL,
                        status TEXT NOT NULL,
                        validation_status TEXT NOT NULL,
                        explanation TEXT NOT NULL,
                        diff_patch TEXT NOT NULL,
                        remediated_code TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS scan_deltas (
                        delta_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        scan_id TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        new_issues_json TEXT NOT NULL,
                        resolved_issues_json TEXT NOT NULL,
                        persisting_issues_json TEXT NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS command_events (
                        event_id TEXT PRIMARY KEY,
                        repo_id TEXT NOT NULL,
                        command_name TEXT NOT NULL,
                        notes TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        metadata_json TEXT NOT NULL
                    );
                    """
                )
                conn.commit()
            finally:
                conn.close()

    def get_latest_snapshot(self, repo_id: str) -> Optional[Dict[str, Any]]:
        conn = self._connect()
        try:
            row = conn.execute(
                """
                SELECT snapshot_id, repo_id, branch_name, created_at, file_count, files_json
                FROM snapshots
                WHERE repo_id = ?
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (repo_id,),
            ).fetchone()
            if not row:
                return None
            return {
                "snapshot_id": row["snapshot_id"],
                "repo_id": row["repo_id"],
                "branch_name": row["branch_name"],
                "created_at": row["created_at"],
                "file_count": row["file_count"],
                "files": json.loads(row["files_json"]),
            }
        finally:
            conn.close()

    def store_snapshot(self, repo_id: str, branch_name: str, files_metadata: List[Dict[str, Any]]) -> Dict[str, Any]:
        snapshot_id = str(uuid.uuid4())
        created_at = utc_now()
        payload = json.dumps(files_metadata)
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    INSERT INTO snapshots (snapshot_id, repo_id, branch_name, created_at, file_count, files_json)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (snapshot_id, repo_id, branch_name, created_at, len(files_metadata), payload),
                )
                conn.commit()
            finally:
                conn.close()
        return {
            "snapshot_id": snapshot_id,
            "repo_id": repo_id,
            "branch_name": branch_name,
            "created_at": created_at,
            "file_count": len(files_metadata),
        }

    def get_unresolved_issues(self, repo_id: str) -> List[Dict[str, Any]]:
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM issues
                WHERE repo_id = ? AND status != 'RESOLVED'
                ORDER BY severity DESC, last_seen_at DESC
                """,
                (repo_id,),
            ).fetchall()
            return [self._row_to_issue(row) for row in rows]
        finally:
            conn.close()

    def get_recent_resolved_issues(self, repo_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM issues
                WHERE repo_id = ? AND status = 'RESOLVED'
                ORDER BY last_seen_at DESC
                LIMIT ?
                """,
                (repo_id, limit),
            ).fetchall()
            return [self._row_to_issue(row) for row in rows]
        finally:
            conn.close()

    def get_context(self, repo_id: str) -> Dict[str, Any]:
        latest_scan = self.get_latest_scan(repo_id)
        unresolved = self.get_unresolved_issues(repo_id)
        recent_resolved = self.get_recent_resolved_issues(repo_id)
        history = self.list_scans(repo_id, limit=10)
        latest_delta = self.get_latest_issue_delta(repo_id)
        recent_commands = self.list_recent_commands(repo_id, limit=10)

        file_history: Dict[str, Dict[str, Any]] = {}
        for issue in unresolved + recent_resolved:
            entry = file_history.setdefault(
                issue["file_path"],
                {"unresolved": [], "resolved": [], "last_seen_at": issue["last_seen_at"]},
            )
            bucket = "resolved" if issue["status"] == "RESOLVED" else "unresolved"
            entry[bucket].append(
                {
                    "issue_type": issue["issue_type"],
                    "severity": issue["severity"],
                    "summary": issue["summary"],
                    "fingerprint": issue["fingerprint"],
                }
            )

        return {
            "repo_id": repo_id,
            "latest_scan": latest_scan,
            "unresolved_issues": unresolved,
            "recent_resolved_issues": recent_resolved,
            "history": history,
            "latest_delta": latest_delta,
            "recent_commands": recent_commands,
            "file_history": file_history,
        }

    def get_latest_scan(self, repo_id: str) -> Optional[Dict[str, Any]]:
        scans = self.list_scans(repo_id, limit=1)
        return scans[0] if scans else None

    def list_scans(self, repo_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM scans
                WHERE repo_id = ?
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (repo_id, limit),
            ).fetchall()
            return [
                {
                    "scan_id": row["scan_id"],
                    "repo_id": row["repo_id"],
                    "repo_url": row["repo_url"],
                    "branch_name": row["branch_name"],
                    "scan_mode": row["scan_mode"],
                    "created_at": row["created_at"],
                    "summary": json.loads(row["summary_json"]),
                    "scoring": json.loads(row["scoring_json"]),
                    "change_summary": json.loads(row["change_summary_json"]),
                }
                for row in rows
            ]
        finally:
            conn.close()

    def store_scan_results(
        self,
        repo_id: str,
        repo_url: str,
        branch_name: str,
        scan_mode: str,
        issues: List[Dict[str, Any]],
        summary: Dict[str, Any],
        scoring: Dict[str, Any],
        change_summary: Dict[str, Any],
    ) -> Dict[str, Any]:
        scan_id = str(uuid.uuid4())
        created_at = utc_now()
        current_fingerprints = {issue["fingerprint"] for issue in issues}

        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    INSERT INTO scans (scan_id, repo_id, repo_url, branch_name, scan_mode, created_at,
                                       summary_json, scoring_json, change_summary_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        scan_id,
                        repo_id,
                        repo_url,
                        branch_name,
                        scan_mode,
                        created_at,
                        json.dumps(summary),
                        json.dumps(scoring),
                        json.dumps(change_summary),
                    ),
                )

                existing_rows = conn.execute(
                    "SELECT * FROM issues WHERE repo_id = ?",
                    (repo_id,),
                ).fetchall()

                existing = {row["fingerprint"]: row for row in existing_rows}
                new_count = 0
                persisting_count = 0
                resolved_count = 0
                new_issue_items: List[Dict[str, Any]] = []
                persisting_issue_items: List[Dict[str, Any]] = []
                resolved_issue_items: List[Dict[str, Any]] = []

                for issue in issues:
                    row = existing.get(issue["fingerprint"])
                    metadata_json = json.dumps(issue.get("metadata", {}))
                    if row:
                        persisting_count += 1
                        persisting_issue_items.append(self._issue_delta_item(issue))
                        conn.execute(
                            """
                            UPDATE issues
                            SET scan_id = ?, severity = ?, status = ?, summary = ?, last_seen_at = ?, metadata_json = ?
                            WHERE repo_id = ? AND fingerprint = ?
                            """,
                            (
                                scan_id,
                                issue["severity"],
                                issue["status"],
                                issue["summary"],
                                created_at,
                                metadata_json,
                                repo_id,
                                issue["fingerprint"],
                            ),
                        )
                    else:
                        new_count += 1
                        new_issue_items.append(self._issue_delta_item(issue))
                        conn.execute(
                            """
                            INSERT INTO issues (issue_id, repo_id, scan_id, fingerprint, file_path, category,
                                                issue_type, severity, status, summary, first_seen_at, last_seen_at, metadata_json)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                str(uuid.uuid4()),
                                repo_id,
                                scan_id,
                                issue["fingerprint"],
                                issue["file_path"],
                                issue["category"],
                                issue["issue_type"],
                                issue["severity"],
                                issue["status"],
                                issue["summary"],
                                created_at,
                                created_at,
                                metadata_json,
                            ),
                        )

                unresolved_existing = [
                    row for row in existing_rows
                    if row["status"] != "RESOLVED" and row["fingerprint"] not in current_fingerprints
                ]
                for row in unresolved_existing:
                    resolved_count += 1
                    resolved_issue_items.append(
                        {
                            "fingerprint": row["fingerprint"],
                            "file_path": row["file_path"],
                            "issue_type": row["issue_type"],
                            "severity": row["severity"],
                            "summary": row["summary"],
                        }
                    )
                    conn.execute(
                        """
                        UPDATE issues
                        SET status = 'RESOLVED', last_seen_at = ?
                        WHERE repo_id = ? AND fingerprint = ?
                        """,
                        (created_at, repo_id, row["fingerprint"]),
                    )

                conn.execute(
                    """
                    INSERT INTO scan_deltas (delta_id, repo_id, scan_id, created_at, new_issues_json, resolved_issues_json, persisting_issues_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        str(uuid.uuid4()),
                        repo_id,
                        scan_id,
                        created_at,
                        json.dumps(new_issue_items),
                        json.dumps(resolved_issue_items),
                        json.dumps(persisting_issue_items),
                    ),
                )

                conn.commit()
            finally:
                conn.close()

        return {
            "scan_id": scan_id,
            "created_at": created_at,
            "new_issues": new_count,
            "resolved_issues": resolved_count,
            "persisting_issues": persisting_count,
        }

    def get_latest_issue_delta(self, repo_id: str) -> Dict[str, Any]:
        conn = self._connect()
        try:
            row = conn.execute(
                """
                SELECT * FROM scan_deltas
                WHERE repo_id = ?
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (repo_id,),
            ).fetchone()
            if not row:
                return {
                    "repo_id": repo_id,
                    "new_issues": [],
                    "resolved_issues": [],
                    "persisting_issues": [],
                }
            return {
                "repo_id": repo_id,
                "scan_id": row["scan_id"],
                "created_at": row["created_at"],
                "new_issues": json.loads(row["new_issues_json"]),
                "resolved_issues": json.loads(row["resolved_issues_json"]),
                "persisting_issues": json.loads(row["persisting_issues_json"]),
            }
        finally:
            conn.close()

    def record_command_event(
        self,
        repo_id: str,
        command_name: str,
        notes: str = "",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        event_id = str(uuid.uuid4())
        created_at = utc_now()
        payload = json.dumps(metadata or {})
        with self._lock:
            conn = self._connect()
            try:
                conn.execute(
                    """
                    INSERT INTO command_events (event_id, repo_id, command_name, notes, created_at, metadata_json)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (event_id, repo_id, command_name, notes, created_at, payload),
                )
                conn.commit()
            finally:
                conn.close()
        return {
            "event_id": event_id,
            "repo_id": repo_id,
            "command_name": command_name,
            "notes": notes,
            "created_at": created_at,
            "metadata": metadata or {},
        }

    def list_recent_commands(self, repo_id: str, limit: int = 20) -> List[Dict[str, Any]]:
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM command_events
                WHERE repo_id = ?
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (repo_id, limit),
            ).fetchall()
            return [
                {
                    "event_id": row["event_id"],
                    "repo_id": row["repo_id"],
                    "command_name": row["command_name"],
                    "notes": row["notes"],
                    "created_at": row["created_at"],
                    "metadata": json.loads(row["metadata_json"]),
                }
                for row in rows
            ]
        finally:
            conn.close()

    def update_fix_status(
        self,
        repo_id: str,
        issue_fingerprint: str,
        status: str,
        validation_status: str,
        explanation: str = "",
        diff_patch: str = "",
        remediated_code: str = "",
    ) -> Dict[str, Any]:
        now = utc_now()
        with self._lock:
            conn = self._connect()
            try:
                row = conn.execute(
                    """
                    SELECT fix_id FROM fixes
                    WHERE repo_id = ? AND issue_fingerprint = ?
                    """,
                    (repo_id, issue_fingerprint),
                ).fetchone()
                if row:
                    fix_id = row["fix_id"]
                    conn.execute(
                        """
                        UPDATE fixes
                        SET status = ?, validation_status = ?, explanation = ?, diff_patch = ?,
                            remediated_code = ?, updated_at = ?
                        WHERE fix_id = ?
                        """,
                        (status, validation_status, explanation, diff_patch, remediated_code, now, fix_id),
                    )
                else:
                    fix_id = str(uuid.uuid4())
                    conn.execute(
                        """
                        INSERT INTO fixes (fix_id, repo_id, issue_fingerprint, status, validation_status,
                                           explanation, diff_patch, remediated_code, created_at, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            fix_id,
                            repo_id,
                            issue_fingerprint,
                            status,
                            validation_status,
                            explanation,
                            diff_patch,
                            remediated_code,
                            now,
                            now,
                        ),
                    )
                conn.commit()
            finally:
                conn.close()

        return {
            "fix_id": fix_id,
            "repo_id": repo_id,
            "issue_fingerprint": issue_fingerprint,
            "status": status,
            "validation_status": validation_status,
            "updated_at": now,
        }

    def _row_to_issue(self, row: sqlite3.Row) -> Dict[str, Any]:
        return {
            "issue_id": row["issue_id"],
            "repo_id": row["repo_id"],
            "scan_id": row["scan_id"],
            "fingerprint": row["fingerprint"],
            "file_path": row["file_path"],
            "category": row["category"],
            "issue_type": row["issue_type"],
            "severity": row["severity"],
            "status": row["status"],
            "summary": row["summary"],
            "first_seen_at": row["first_seen_at"],
            "last_seen_at": row["last_seen_at"],
            "metadata": json.loads(row["metadata_json"]),
        }

    def _issue_delta_item(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "fingerprint": issue["fingerprint"],
            "file_path": issue["file_path"],
            "issue_type": issue["issue_type"],
            "severity": issue["severity"],
            "summary": issue["summary"],
        }

```

---

## [25] backend/mcp_server/watcher.py
**Size:** 4.1KB

```python
import threading
import uuid
from typing import Any, Dict

from github_client import get_latest_commit_sha

from .continuous_pipeline import ContinuousIntelligencePipeline


class ContinuousWatchManager:
    def __init__(self, pipeline: ContinuousIntelligencePipeline = None):
        self.pipeline = pipeline or ContinuousIntelligencePipeline()
        self._watches: Dict[str, Dict[str, Any]] = {}
        self._lock = threading.Lock()

    def start(self, repo_url: str, branch_name: str = "main", interval_seconds: int = 60, github_token: str = None) -> Dict[str, Any]:
        watch_id = str(uuid.uuid4())
        state = {
            "watch_id": watch_id,
            "repo_url": repo_url,
            "branch_name": branch_name,
            "interval_seconds": max(15, interval_seconds),
            "github_token": github_token,
            "status": "running",
            "poll_count": 0,
            "run_count": 0,
            "change_detected_count": 0,
            "last_result": None,
            "last_error": None,
            "last_seen_commit": None,
            "last_scanned_commit": None,
            "stop_event": threading.Event(),
        }

        def _runner():
            while not state["stop_event"].is_set():
                try:
                    state["poll_count"] += 1
                    commit_info = get_latest_commit_sha(
                        repo_url,
                        github_token=github_token,
                        branch_name=branch_name,
                    )
                    latest_commit = commit_info.get("commit_sha")
                    resolved_branch = commit_info.get("branch_name", branch_name)
                    state["branch_name"] = resolved_branch
                    state["last_seen_commit"] = latest_commit

                    if state["last_scanned_commit"] != latest_commit:
                        result = self.pipeline.run(
                            repo_url=repo_url,
                            github_token=github_token,
                            branch_name=resolved_branch,
                            generate_fixes=True,
                        )
                        state["last_result"] = result
                        state["run_count"] += 1
                        state["change_detected_count"] += 1
                        state["last_scanned_commit"] = latest_commit
                    else:
                        state["status"] = "idle"
                    state["last_error"] = None
                except Exception as exc:
                    state["last_error"] = str(exc)
                    state["status"] = "error"
                else:
                    if not state["stop_event"].is_set():
                        state["status"] = "running"
                state["stop_event"].wait(state["interval_seconds"])

            state["status"] = "stopped"

        thread = threading.Thread(target=_runner, daemon=True)
        state["thread"] = thread

        with self._lock:
            self._watches[watch_id] = state
        thread.start()

        return {
            "watch_id": watch_id,
            "status": "running",
            "interval_seconds": state["interval_seconds"],
        }

    def status(self, watch_id: str) -> Dict[str, Any]:
        with self._lock:
            state = self._watches.get(watch_id)
        if not state:
            return {"error": "watch_not_found"}
        return {
            "watch_id": watch_id,
            "status": state["status"],
            "poll_count": state["poll_count"],
            "run_count": state["run_count"],
            "change_detected_count": state["change_detected_count"],
            "last_error": state["last_error"],
            "last_seen_commit": state["last_seen_commit"],
            "last_scanned_commit": state["last_scanned_commit"],
            "last_result": state["last_result"],
        }

    def stop(self, watch_id: str) -> Dict[str, Any]:
        with self._lock:
            state = self._watches.get(watch_id)
        if not state:
            return {"error": "watch_not_found"}
        state["stop_event"].set()
        return {
            "watch_id": watch_id,
            "status": "stopping",
        }

```

---

## [26] backend/package-lock.json
**Size:** 86.0B

```json
{
  "name": "backend",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {}
}

```

---

## [27] backend/pipeline.py
**Size:** 17.9KB

```python
import json
import os
import sys
import hashlib
import boto3
from datetime import datetime

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from github_client import fetch_repo, categorize_files
from chunker import chunk_code
from ai.bedrock_client import scan_chunk, scan_all_chunks


class GitHopperPipeline:
    """
    Complete GitHopper analysis pipeline:
    1. Fetch → 2. Analyze → 3. Score
    """

    def __init__(self):
        self.lambda_client = None
        self.use_lambda = os.environ.get('USE_LAMBDA', 'false').lower() == 'true'
        self.mock_mode = os.environ.get('MOCK_MODE', 'false').lower() == 'true'

        if self.use_lambda:
            self.lambda_client = boto3.client('lambda', region_name='us-east-1')

    def run_full_pipeline(self, repo_url, github_token=None, branch_name="main"):
        """
        Execute the complete pipeline: Fetch → Analyze → Score
        """
        print("🚀 Starting GitHopper Full Pipeline")
        print(f"📦 Repository: {repo_url}")
        print(f"📝 Branch: {branch_name}")
        print(f"🔧 Mode: {'Lambda' if self.use_lambda else 'Local'}")

        start_time = datetime.now()

        try:
            # Stage 1: Fetch
            print("\n" + "="*60)
            print("📥 STAGE 1: FETCHING REPOSITORY")
            print("="*60)

            fetch_result = self._stage_fetch(repo_url, github_token)
            if fetch_result.get('error'):
                return fetch_result

            # Stage 2: Analyze
            print("\n" + "="*60)
            print("🤖 STAGE 2: AI ANALYSIS WITH BEDROCK")
            print("="*60)

            analysis_result = self._stage_analyze(fetch_result, branch_name)
            if analysis_result.get('error'):
                return analysis_result

            # Stage 3: Score
            print("\n" + "="*60)
            print("📊 STAGE 3: SCORING & RECOMMENDATIONS")
            print("="*60)

            score_result = self._stage_score(analysis_result)
            if score_result.get('error'):
                return score_result

            # Final result
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            final_result = {
                'status': 'success',
                'pipeline': 'complete',
                'execution_time_seconds': duration,
                'stages': {
                    'fetch': fetch_result,
                    'analyze': analysis_result,
                    'score': score_result
                },
                # Add convenience data at top level for frontend
                'data': {
                    'total_files_fetched': fetch_result.get('total_files', 0),
                    'config_files': fetch_result.get('categories', {}).get('config', 0),
                    'dependency_files': fetch_result.get('categories', {}).get('dependencies', 0),
                    'source_files': fetch_result.get('categories', {}).get('source_code', 0),
                    'total_chunks': len(fetch_result.get('chunks', [])),
                    'files_by_category': {
                        'config': [f for f in fetch_result.get('files', []) if 'config' in f.get('path', '').lower()],
                        'dependencies': [f for f in fetch_result.get('files', []) if any(x in f.get('path', '').lower() for x in ['requirements', 'package.json', 'package-lock'])],
                        'source_code': [f for f in fetch_result.get('files', []) if 'config' not in f.get('path', '').lower() and not any(x in f.get('path', '').lower() for x in ['requirements', 'package.json', 'package-lock'])]
                    },
                    'detailed_files': fetch_result.get('files', []),
                    'analysis_summary': {
                        'total_debt_signals': sum(f.get('debt_signal_count', 0) for f in fetch_result.get('files', [])),
                        'files_with_debt_signals': sum(1 for f in fetch_result.get('files', []) if f.get('debt_signal_count', 0) > 0),
                        'cost_estimate': {
                            'chunks_to_analyze': len(fetch_result.get('chunks', [])),
                            'total_code_chars': sum(c.get('char_count', 0) for c in fetch_result.get('chunks', [])),
                            'approx_tokens': int(sum(c.get('char_count', 0) for c in fetch_result.get('chunks', [])) / 4)
                        }
                    }
                },
                'summary': {
                    'repo_url': repo_url,
                    'repo_id': fetch_result.get('repo_id'),
                    'health_score': score_result.get('health_score'),
                    'total_security_issues': score_result['analysis']['total_security_issues'],
                    'total_debt_issues': score_result['analysis']['total_debt_issues'],
                    'critical_issues': score_result['analysis']['critical_issues'],
                    'quick_wins': score_result['analysis']['quick_wins']
                }
            }

            print("\n" + "="*60)
            print("✅ PIPELINE COMPLETE")
            print("="*60)
            print(f"🏆 Health Score: {final_result['summary']['health_score']}/100")
            print(f"🔍 Security Issues: {final_result['summary']['total_security_issues']}")
            print(f"💸 Technical Debt: {final_result['summary']['total_debt_issues']}")
            print(f"⚡ Quick Wins: {final_result['summary']['quick_wins']}")
            print(f"⏱️  Execution Time: {duration:.1f} seconds")

            return final_result

        except Exception as e:
            import traceback
            error_msg = str(e)
            tb = traceback.format_exc()

            print(f"\n❌ PIPELINE ERROR: {error_msg}")

            return {
                'status': 'error',
                'error': error_msg,
                'traceback': tb,
                'stage': 'unknown'
            }

    def _stage_fetch(self, repo_url, github_token=None):
        """Stage 1: Fetch repository data"""
        try:
            if self.mock_mode:
                print(f"[FETCH] MOCK_MODE=true — using mock data")
                return self._mock_fetch(repo_url)

            if self.use_lambda:
                # Call fetcher lambda
                payload = {'repo_url': repo_url}
                if github_token:
                    payload['github_token'] = github_token

                response = self.lambda_client.invoke(
                    FunctionName='githopper-fetcher',
                    InvocationType='RequestResponse',
                    Payload=json.dumps(payload)
                )
                result = json.loads(response['Payload'].read())
                fetch_data = json.loads(result['body'])
                return fetch_data

            else:
                # Local execution: call github_client + chunker directly (no lambda indirection)
                print(f"[FETCH] Local mode — calling github_client directly for {repo_url}")
                files = fetch_repo(repo_url, github_token=github_token)
                print(f"[FETCH] Fetched {len(files)} files from GitHub")

                chunks = chunk_code(files)
                print(f"[FETCH] Created {len(chunks)} chunks")

                repo_id = hashlib.md5(repo_url.encode()).hexdigest()[:8]

                return {
                    'repo_id': repo_id,
                    'repo_url': repo_url,
                    'total_files': len(files),
                    'categories': {
                        'config': sum(1 for f in files if f.get('debt_category_hint') == 'architecture'),
                        'dependencies': sum(1 for f in files if f.get('debt_category_hint') == 'dependencies'),
                        'source_code': sum(1 for f in files if f.get('debt_category_hint') not in ('architecture', 'dependencies'))
                    },
                    'chunks': chunks,
                    'files': files
                }

        except Exception as e:
            print(f"[FETCH] ❌ Exception during fetch: {type(e).__name__}: {str(e)}")
            import traceback
            traceback.print_exc()
            print(f"[FETCH] ⚠️  Falling back to mock mode (set MOCK_MODE=true to suppress this)")
            return self._mock_fetch(repo_url)

    def _mock_fetch(self, repo_url):
        """Mock fetch for testing without GitHub API"""
        import hashlib
        repo_id = hashlib.md5(repo_url.encode()).hexdigest()[:8]
        
        # Mock files with test data
        mock_files = [
            {
                'path': 'config/db.py',
                'language': 'python',
                'content': 'import os\nAWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"\nDB_PASSWORD = "admin123"',
                'size_bytes': 250,
                'debt_signals': ['hardcoded_secrets'],
                'debt_signal_count': 1,
                'debt_category_hint': 'architecture',
                'metrics': {'total_lines': 50, 'code_lines': 40, 'blank_lines': 5, 'comment_lines': 5, 'comment_ratio': 0.1, 'max_indentation_depth': 2, 'long_function_count': 0}
            },
            {
                'path': 'requirements.txt',
                'language': 'text',
                'content': 'flask==0.12.0\nrequests==2.18.0\ndjango==2.0.0',
                'size_bytes': 50,
                'debt_signals': ['outdated_dependencies'],
                'debt_signal_count': 1,
                'debt_category_hint': 'dependencies',
                'metrics': {'total_lines': 3, 'code_lines': 3, 'blank_lines': 0, 'comment_lines': 0, 'comment_ratio': 0.0, 'max_indentation_depth': 0, 'long_function_count': 0}
            },
            {
                'path': 'src/app.py',
                'language': 'python',
                'content': '''def process_data(user_input):
    query = "SELECT * FROM users WHERE id = " + user_input
    return eval(user_input)

def long_function():
    # This function is over 50 lines
    x = 1
    y = 2
    z = x + y
    a = z * 2
    b = a + x
    return b''',
                'size_bytes': 350,
                'debt_signals': ['sql_injection', 'eval'],
                'debt_signal_count': 2,
                'debt_category_hint': 'code_quality',
                'metrics': {'total_lines': 120, 'code_lines': 95, 'blank_lines': 15, 'comment_lines': 10, 'comment_ratio': 0.08, 'max_indentation_depth': 3, 'long_function_count': 1}
            },
            {
                'path': 'src/utils.js',
                'language': 'javascript',
                'content': 'const SECRET_TOKEN = "sk-abc123xyz";\nfunction validateUser(id) { return id > 0; }',
                'size_bytes': 120,
                'debt_signals': ['hardcoded_secrets'],
                'debt_signal_count': 1,
                'debt_category_hint': 'code_quality',
                'metrics': {'total_lines': 40, 'code_lines': 30, 'blank_lines': 5, 'comment_lines': 5, 'comment_ratio': 0.125, 'max_indentation_depth': 2, 'long_function_count': 0}
            },
            {
                'path': 'tests/test_app.py',
                'language': 'python',
                'content': 'import unittest\nclass TestApp(unittest.TestCase):\n    def test_process(self):\n        assert process_data("test") is not None',
                'size_bytes': 200,
                'debt_signals': [],
                'debt_signal_count': 0,
                'debt_category_hint': 'testing',
                'metrics': {'total_lines': 60, 'code_lines': 50, 'blank_lines': 5, 'comment_lines': 5, 'comment_ratio': 0.083, 'max_indentation_depth': 2, 'long_function_count': 0}
            }
        ]
        
        # Mock chunks with correct format (file, code - not filename, content)
        mock_chunks = [
            {
                'file': 'config/db.py',
                'code': 'AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"',
                'language': 'python',
                'char_count': 45
            },
            {
                'file': 'src/app.py', 
                'code': 'query = "SELECT * FROM users WHERE id = " + user_input',
                'language': 'python',
                'char_count': 55
            },
            {
                'file': 'src/utils.js',
                'code': 'const SECRET_TOKEN = "sk-abc123xyz";',
                'language': 'javascript',
                'char_count': 38
            }
        ]
        
        return {
            'repo_id': repo_id,
            'repo_url': repo_url,
            'total_files': len(mock_files),
            'categories': {'config': 1, 'dependencies': 1, 'source_code': 3},
            'chunks': mock_chunks,
            'files': mock_files
        }

    def _stage_analyze(self, fetch_result, branch_name="main"):
        """Stage 2: Analyze with Bedrock - Dynamic prompts per repo"""
        try:
            chunks = fetch_result.get('chunks', [])
            files = fetch_result.get('files', [])

            if self.use_lambda:
                # Call bedrock analyzer lambda
                payload = {
                    'repo_id': fetch_result['repo_id'],
                    'repo_url': fetch_result['repo_url'],
                    'chunks': chunks,
                    'branch_name': branch_name,
                    'total_files': len(files)
                }

                response = self.lambda_client.invoke(
                    FunctionName='githopper-analyzer',
                    InvocationType='RequestResponse',
                    Payload=json.dumps(payload)
                )

                result = json.loads(response['Payload'].read())
                analysis_result = json.loads(result['body'])

            else:
                # Local execution with dynamic Bedrock analysis
                analysis_result = scan_all_chunks(chunks, branch_name)

            analysis_data = {
                'repo_id': fetch_result['repo_id'],
                'repo_url': fetch_result['repo_url'],
                'branch_name': branch_name,
                'vulnerabilities': analysis_result.get('vulnerabilities', []),
                'vulnerable_files': analysis_result.get('vulnerable_files', []),
                'total_files_analyzed': analysis_result.get('total_files_analyzed', len(chunks)),
                'files_with_issues': analysis_result.get('files_with_issues', 0),
                'total_vulnerabilities': analysis_result.get('total_vulnerabilities', 0),
                'cost_tracker': analysis_result.get('cost_tracker', {}),
                'billing': analysis_result.get('billing', {}),
                'chunks_scanned': len(chunks),
                'total_files': len(files)
            }

            return analysis_data

        except Exception as e:
            return {'error': f'Analysis stage failed: {str(e)}'}

    def _stage_score(self, analysis_result):
        """Stage 3: Score the results"""
        try:
            if self.use_lambda:
                # Call scorer lambda
                payload = analysis_result

                response = self.lambda_client.invoke(
                    FunctionName='githopper-scorer',
                    InvocationType='RequestResponse',
                    Payload=json.dumps(payload)
                )

                result = json.loads(response['Payload'].read())
                score_data = json.loads(result['body'])

            else:
                # Local execution
                from lambdas.scorer.handler import lambda_handler
                event = {'body': analysis_result}

                result = lambda_handler(event, None)
                score_data = json.loads(result['body'])

            if result.get('statusCode') != 200:
                return {'error': score_data.get('error', 'Scoring failed')}

            return score_data

        except Exception as e:
            return {'error': f'Scoring stage failed: {str(e)}'}


# CLI interface for testing
if __name__ == '__main__':
    import argparse
    from dotenv import load_dotenv

    # Load .env so GITHUB_TOKEN is available
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

    parser = argparse.ArgumentParser(description='GitHopper Full Pipeline')
    parser.add_argument('repo_url', help='GitHub repository URL')
    parser.add_argument('--token', help='GitHub token (optional, falls back to GITHUB_TOKEN env var)')
    parser.add_argument('--use-lambda', action='store_true', help='Use Lambda functions')
    parser.add_argument('--mock', action='store_true', help='Use mock data for testing')
    parser.add_argument('--branch', default='main', help='Branch to analyze (default: main)')

    args = parser.parse_args()

    if args.use_lambda:
        os.environ['USE_LAMBDA'] = 'true'

    if args.mock:
        os.environ['MOCK_MODE'] = 'true'

    # Use --token first, then fall back to env var
    github_token = args.token or os.environ.get('GITHUB_TOKEN')
    if github_token:
        print(f"[CLI] Using GitHub token: {github_token[:8]}...{github_token[-4:]}")
    else:
        print("[CLI] ⚠️  No GitHub token found — may hit rate limits on public repos")

    pipeline = GitHopperPipeline()
    result = pipeline.run_full_pipeline(args.repo_url, github_token, args.branch)

    print("\n" + "="*60)
    print("FINAL RESULT SUMMARY")
    print("="*60)
    summary = result.get('summary', {})
    print(f"Status:           {result.get('status')}")
    print(f"Health Score:     {summary.get('health_score')}")
    print(f"Security Issues:  {summary.get('total_security_issues')}")
    print(f"Debt Issues:      {summary.get('total_debt_issues')}")
    print(f"Critical Issues:  {summary.get('critical_issues')}")
    print(f"Quick Wins:       {summary.get('quick_wins')}")
    if result.get('status') == 'error':
        print(f"\n❌ Error: {result.get('error')}")
    print("="*60)
```

---

## [28] backend/requirements-mcp.txt
**Size:** 17.0B

```text
mcp[cli]>=1.2.0


```

---

## [29] backend/requirements.txt
**Size:** 88.0B

```text
Flask==2.3.3
Flask-CORS==4.0.0
python-dotenv==1.0.0
requests==2.31.0
boto3==1.34.0

```

---

## [30] backend/tests/local_test.py
**Size:** 6.7KB

```python
# =============================================================================
# test_bedrock.py — Local test for Ananya's Bedrock engine
# Run: python test_bedrock.py
# Needs: AWS credentials configured (aws configure) + boto3 installed
# =============================================================================

import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../ai"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../"))
from bedrock_client import scan_chunk, scan_all_chunks
from utils.file_classifier import classify_file

# ---------------------------------------------------------------------------
# Test chunks — planted vulnerabilities across all 4 types
# ---------------------------------------------------------------------------

APP_CODE_CHUNK = {
    "filename": "config/db.py",
    "content": """
import requests
import os

# Database config
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "admin123"
API_TOKEN = "sk-proj-abc123xyz"

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def process_data(data):
    result = eval(data)
    return result

def fetch_internal():
    url = "http://internal-api/data?user=" + input("enter user: ")
    return requests.get(url)
"""
}

IAC_CHUNK = {
    "filename": "infrastructure/main.tf",
    "content": """
resource "aws_s3_bucket" "data_bucket" {
  bucket = "my-company-data"
  acl    = "public-read"
}

resource "aws_security_group" "web_sg" {
  name = "web-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "main" {
  engine            = "mysql"
  instance_class    = "db.t3.micro"
  storage_encrypted = false
  publicly_accessible = true
  password          = "hardcoded_password_123"
}
"""
}

IAM_CHUNK = {
    "filename": "iam/admin_policy.json",
    "content": """{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreatePolicy",
        "iam:AttachUserPolicy",
        "iam:PassRole"
      ],
      "Resource": "*"
    }
  ]
}"""
}

DEPS_CHUNK = {
    "filename": "requirements.txt",
    "content": """
flask==0.12.0
requests==2.18.0
django==2.0.0
pillow==5.0.0
pyyaml==3.12
cryptography==2.1.0
sqlalchemy==1.2.0
"""
}

DEBT_CHUNK = {
    "filename": "utils/processor.py",
    "content": """
def process_everything(data, user, config, db, cache, logger, flags, retries, timeout, mode):
    try:
        if mode == 1:
            result = []
            for i in range(len(data)):
                if data[i] > 0:
                    result.append(data[i] * 2)
                elif data[i] < 0:
                    result.append(data[i] * -1)
                else:
                    result.append(0)
            for i in range(len(result)):
                if result[i] > 100:
                    result[i] = 100
                elif result[i] < 0:
                    result[i] = 0
            db.save(result)
            cache.set("result", result)
            logger.log(result)
            user.notify(result)
            config.update({"last_run": "now"})
            return result
        elif mode == 2:
            result = []
            for i in range(len(data)):
                if data[i] > 0:
                    result.append(data[i] * 2)
                elif data[i] < 0:
                    result.append(data[i] * -1)
                else:
                    result.append(0)
            for i in range(len(result)):
                if result[i] > 100:
                    result[i] = 100
                elif result[i] < 0:
                    result[i] = 0
            db.save(result)
            return result
    except:
        pass
"""
}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_classify():
    print("\n=== classify_file() ===")
    cases = [
        ("config/db.py", "app"),
        ("infrastructure/main.tf", "iac"),
        ("iam/admin_policy.json", "iam"),
        ("requirements.txt", "deps"),
        ("package.json", "deps"),
        ("cloudformation/template.yaml", "iac"),
    ]
    all_pass = True
    for filepath, expected in cases:
        got = classify_file(filepath)
        status = "✓" if got == expected else "✗"
        if got != expected:
            all_pass = False
        print(f"  {status} {filepath} → {got} (expected {expected})")
    return all_pass


def test_single_chunk(chunk, label):
    print(f"\n=== scan_chunk: {label} ===")
    result = scan_chunk(chunk)
    sec = result.get("security_findings", [])
    debt = result.get("debt_findings", [])
    print(f"  Security findings: {len(sec)}")
    for f in sec:
        print(f"    [{f.get('severity')}] {f.get('type')} — {f.get('explanation', '')[:80]}")
    print(f"  Debt findings: {len(debt)}")
    for f in debt:
        print(f"    [{f.get('severity')}] {f.get('type')} — {f.get('explanation', '')[:80]}")
    return result


def test_full_scan():
    print("\n=== scan_all_chunks: full repo simulation ===")
    all_chunks = [APP_CODE_CHUNK, IAC_CHUNK, IAM_CHUNK, DEPS_CHUNK, DEBT_CHUNK]
    result = scan_all_chunks(all_chunks)
    print(f"  Total security findings: {len(result['security_findings'])}")
    print(f"  Total debt findings:     {len(result['debt_findings'])}")
    print("\n  Full output JSON:")
    print(json.dumps(result, indent=2))
    return result


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("GitHopper — Bedrock Engine Test")
    print("=" * 50)

    # 1. classify_file (no AWS needed)
    classify_ok = test_classify()

    # 2. single chunk tests (needs AWS)
    print("\nRunning single chunk tests (needs AWS credentials)...")
    test_single_chunk(APP_CODE_CHUNK, "App code with secrets + injection")
    test_single_chunk(IAC_CHUNK, "Terraform with open S3 + SG")
    test_single_chunk(IAM_CHUNK, "IAM policy with wildcard")
    test_single_chunk(DEPS_CHUNK, "requirements.txt with old packages")

    # 3. full scan simulation
    test_full_scan()

    print("\n✓ All tests done.")
```

---

## [31] backend/tests/test_chunks/requirements.txt
**Size:** 0.0B

```text

```

---

## [32] backend/tests/test_chunks/sample_app.py
**Size:** 0.0B

```python

```

---

## [33] backend/tests/test_chunks/sample_iam.json
**Size:** 0.0B

```json

```

---

## [34] backend/utils/chunker.py
**Size:** 0.0B

```python

```

---

## [35] backend/utils/file_classifier.py
**Size:** 826.0B

```python
def classify_file(filepath):
    """
    Classify a file based on its path and extension.
    Returns one of: 'app', 'iac', 'iam', 'deps', or 'unknown'
    """
    filepath_lower = filepath.lower()
    
    # Application code (Python files)
    if filepath.endswith('.py'):
        return 'app'
    
    # Infrastructure as Code
    if filepath.endswith('.tf') or filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return 'iac'
    
    # IAM policies (JSON files in iam directory)
    if 'iam' in filepath_lower and filepath.endswith('.json'):
        return 'iam'
    
    # Dependencies (requirements.txt, package.json, etc.)
    if filepath.endswith('.txt') or (filepath.endswith('.json') and 'package' in filepath_lower):
        return 'deps'
    
    # Default
    return 'unknown'
```

---

## [36] backend/utils/github_client.py
**Size:** 0.0B

```python

```

---

## [37] codebase_dumper.py
**Size:** 5.8KB

```python
#!/usr/bin/env python3
"""
GitHopper Codebase Dumper
Consolidates entire codebase into a single file for easy reference
Run this script to update CODEBASE_DUMP.md with all current code
"""

import os
import json
from pathlib import Path
from datetime import datetime
import mimetypes

# Configuration
REPO_ROOT = Path(__file__).parent
OUTPUT_FILE = REPO_ROOT / "CODEBASE_DUMP.md"

# Directories to exclude
EXCLUDE_DIRS = {
    '.git',
    'node_modules',
    '__pycache__',
    '.pytest_cache',
    'venv',
    'env',
    '.env',
    'dist',
    'build',
    '.venv',
    '.next',
    '.cache',
    'mcp_data',  # Skip data files
    'scan_results',  # Skip result files
    'public',  # Skip static assets
}

# File extensions to include
INCLUDE_EXTENSIONS = {
    # Python
    '.py',
    # JavaScript/TypeScript
    '.js', '.jsx', '.ts', '.tsx', '.mjs',
    # Web
    '.html', '.css', '.scss', '.less',
    # Configuration
    '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf',
    # Documentation
    '.md', '.txt', '.rst',
    # Environment
    '.env', '.env.example',
    # Other
    '.dockerfile', '.sql', '.sh', '.bash',
}

# Files to explicitly exclude
EXCLUDE_FILES = {
    '.DS_Store',
    'Thumbs.db',
    '.gitignore',
    '.gitkeep',
}

def should_include_file(file_path, file_name):
    """Determine if a file should be included in the dump"""
    # Skip excluded files
    if file_name in EXCLUDE_FILES:
        return False
    
    # Check file extension
    ext = Path(file_name).suffix.lower()
    if ext not in INCLUDE_EXTENSIONS:
        return False
    
    # Skip certain patterns
    if '.min.' in file_name:  # minified files
        return False
    
    return True

def should_include_dir(dir_name):
    """Determine if a directory should be explored"""
    return dir_name not in EXCLUDE_DIRS

def get_file_size(file_path):
    """Get file size in readable format"""
    size = file_path.stat().st_size
    for unit in ['B', 'KB', 'MB']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}GB"

def collect_files():
    """Collect all files to include in the dump"""
    files = []
    
    for root, dirs, filenames in os.walk(REPO_ROOT):
        # Filter directories
        dirs[:] = [d for d in dirs if should_include_dir(d)]
        
        rel_root = Path(root).relative_to(REPO_ROOT)
        
        for filename in filenames:
            if should_include_file(root, filename):
                file_path = Path(root) / filename
                rel_path = file_path.relative_to(REPO_ROOT)
                
                files.append({
                    'path': rel_path,
                    'full_path': file_path,
                    'size': get_file_size(file_path),
                    'ext': Path(filename).suffix.lower(),
                })
    
    return sorted(files, key=lambda x: str(x['path']))

def get_language_from_ext(ext):
    """Get markdown language identifier from file extension"""
    language_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'jsx',
        '.ts': 'typescript',
        '.tsx': 'tsx',
        '.html': 'html',
        '.css': 'css',
        '.scss': 'scss',
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.toml': 'toml',
        '.sh': 'bash',
        '.dockerfile': 'dockerfile',
        '.md': 'markdown',
        '.sql': 'sql',
    }
    return language_map.get(ext, 'text')

def read_file_safe(file_path):
    """Safely read file content"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        return f"[Error reading file: {str(e)}]"

def generate_table_of_contents(files):
    """Generate a table of contents"""
    toc = "## 📑 Table of Contents\n\n"
    
    current_dir = None
    for file_info in files:
        dir_name = file_info['path'].parent
        if dir_name != current_dir:
            current_dir = dir_name
            toc += f"- **{dir_name}/**\n"
        
        file_name = file_info['path'].name
        toc += f"  - {file_name}\n"
    
    return toc

def generate_dump():
    """Generate the codebase dump file"""
    print(f"🔍 Scanning codebase at: {REPO_ROOT}")
    
    files = collect_files()
    print(f"📦 Found {len(files)} files to include")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Start building the dump
    dump_content = f"""# 📚 GitHopper Complete Codebase Dump

**Generated:** {timestamp}
**Repository:** {REPO_ROOT.name}
**Total Files:** {len(files)}

---

"""
    
    # Add table of contents
    dump_content += generate_table_of_contents(files)
    
    dump_content += """
---

# 📂 File Contents

"""
    
    # Add all files
    for i, file_info in enumerate(files, 1):
        path_str = str(file_info['path']).replace('\\', '/')
        language = get_language_from_ext(file_info['ext'])
        
        dump_content += f"""## [{i}] {path_str}
**Size:** {file_info['size']}

```{language}
"""
        
        content = read_file_safe(file_info['full_path'])
        dump_content += content
        
        dump_content += f"""
```

---

"""
    
    # Write output file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(dump_content)
    
    print(f"✅ Dump saved to: {OUTPUT_FILE}")
    print(f"📊 Total size: {get_file_size(OUTPUT_FILE)}")
    print(f"⏱️  Timestamp: {timestamp}")

if __name__ == '__main__':
    try:
        generate_dump()
        print("\n✨ Codebase dump completed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)

```

---

## [38] frontend/README.md
**Size:** 10.2KB

```markdown
# 🎨 GitHopper Frontend

Modern, responsive React frontend for GitHopper - providing beautiful dashboards and intuitive interfaces for repository analysis and insights.

## Overview

The frontend is built with React 18 and Vite, featuring:
- Real-time dashboard with animations
- Repository analysis visualizations
- Health score displays
- Technical debt reports
- Branch comparison tools
- Theme support (light/dark mode)
- Responsive design for all devices

## Tech Stack

- **React 18** - UI library
- **Vite 5.4** - Build tool and dev server (ultra-fast)
- **Tailwind CSS 4.2** - Utility-first CSS framework
- **React Router 7.13** - Client-side routing
- **Three.js 0.183** - 3D graphics and visualizations
- **GSAP 3.14** - Professional animation library
- **Lenis 1.3** - Smooth scrolling
- **Motion 12.38** - Animation framework
- **Firebase 12.11** - Authentication and data services

## 📋 Prerequisites

- Node.js 16 or higher
- npm or yarn package manager
- Git

## 🚀 Quick Start

### 1. Install Dependencies

```bash
npm install
# or
yarn install
```

### 2. Start Development Server

```bash
npm run dev
# or
yarn dev
```

The application will open at `http://localhost:5173`

### 3. Build for Production

```bash
npm run build
# or
yarn build
```

Creates an optimized production build in the `dist/` directory.

### 4. Preview Production Build

```bash
npm run preview
# or
yarn preview
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/              # Reusable React components
│   │   ├── AppLayout.jsx       # Main app layout wrapper
│   │   ├── Plasma.jsx          # 3D animated plasma background
│   │   ├── Plasma.css          # Plasma styling
│   │   ├── PlasmaBackground.jsx # Background wrapper
│   │   ├── ThemeToggle.jsx     # Light/dark mode toggle
│   │   ├── UserProfile.jsx     # User profile component
│   │   ├── ShinyText.jsx       # Animated text effect
│   │   └── [css files]         # Component-specific styling
│   │
│   ├── context/                 # React Context for state management
│   │   ├── ThemeContext.jsx    # Theme (light/dark) state
│   │   └── UserContext.jsx     # User authentication state
│   │
│   ├── pages/                   # Page components (top-level routes)
│   │   ├── HomePage.jsx        # Landing page
│   │   ├── DashboardPage.jsx   # Main dashboard
│   │   ├── AnalyseBranchesPage.jsx    # Branch analysis
│   │   ├── HealthScorePage.jsx        # Health metrics
│   │   ├── DebtReportPage.jsx         # Technical debt
│   │   ├── AuthPages.jsx              # Authentication
│   │   └── [css files]                # Page-specific styling
│   │
│   ├── services/                # API service layer
│   │   ├── api.js             # API client utilities
│   │   └── [service files]    # Domain-specific services
│   │
│   ├── main-home.jsx          # Application entry point
│   ├── styles.css             # Global styles
│   └── App.jsx                # Root component
│
├── public/                     # Static assets
│   └── assets/                # Images, icons, etc.
│
├── package.json               # Node dependencies and scripts
├── vite.config.js            # Vite configuration
├── tailwind.config.js        # Tailwind CSS configuration
├── postcss.config.js         # PostCSS (Tailwind) config
├── jsconfig.json             # JavaScript path aliases
├── components.json           # Component library config
└── README.md                 # This file
```

## 🎨 Components

### AppLayout
Main layout wrapper that provides consistent structure across all pages.

**Usage:**
```jsx
<AppLayout>
  <YourPageContent />
</AppLayout>
```

### Plasma
3D animated plasma background using Three.js. Provides a modern visual effect.

**Props:**
- `intensity` - Animation intensity (0-1)
- `speed` - Animation speed (0-2)

**Usage:**
```jsx
<Plasma intensity={0.8} speed={1} />
```

### ThemeToggle
Button to switch between light and dark themes.

**Usage:**
```jsx
<ThemeToggle />
```

### UserProfile
Displays user information and account options.

**Usage:**
```jsx
<UserProfile user={userData} />
```

## 🎯 Pages

### HomePage
Landing page with introduction and key features.

**Route:** `/`

### DashboardPage
Main dashboard showing repository overview and key metrics.

**Route:** `/dashboard`

### AnalyseBranchesPage
Compare and analyze multiple branches side-by-side.

**Route:** `/analyze-branches`

### HealthScorePage
Display code health metrics and trends.

**Route:** `/health-score`

### DebtReportPage
Technical debt analysis and recommendations.

**Route:** `/debt-report`

### AuthPages
Login, signup, and password reset pages.

**Routes:** `/login`, `/signup`, `/reset-password`

## 🌈 Theming

The application supports light and dark themes through React Context.

**Access theme in components:**
```jsx
import { useTheme } from './context/ThemeContext';

function MyComponent() {
  const { isDark, toggleTheme } = useTheme();
  
  return (
    <div className={isDark ? 'bg-gray-900' : 'bg-white'}>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
  );
}
```

## 🔧 Configuration

### Vite Configuration
Edit `vite.config.js` for:
- Dev server settings
- Build optimization
- Plugin configuration

### Tailwind Configuration
Edit `tailwind.config.js` for:
- Custom colors and themes
- Typography settings
- Animation/transition configs

### Environment Variables

Create a `.env` file in the frontend directory:

```env
VITE_API_BASE_URL=http://localhost:5000
VITE_FIREBASE_API_KEY=your_firebase_key
VITE_FIREBASE_AUTH_DOMAIN=your_domain
VITE_FIREBASE_PROJECT_ID=your_project_id
```

**Note:** Vite requires variables to start with `VITE_` to expose them to the client.

## 🚀 Development Workflow

### Running with Hot Module Replacement (HMR)
```bash
npm run dev
```
Changes automatically reload in the browser.

### Building a Preview
```bash
npm run build && npm run preview
```
Test the exact production build locally.

### Debugging
1. Open browser DevTools (F12)
2. Check the React tab (requires React DevTools extension)
3. Use console for logging and testing

## 📱 Responsive Design

The design uses Tailwind CSS breakpoints:
- `sm` - 640px
- `md` - 768px
- `lg` - 1024px
- `xl` - 1280px
- `2xl` - 1536px

**Example:**
```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
  {/* Content */}
</div>
```

## 🎬 Animations

### GSAP Animations
For complex timeline animations:

```jsx
import { useEffect } from 'react';
import gsap from 'gsap';

export function AnimatedComponent() {
  useEffect(() => {
    gsap.to('.element', { duration: 1, opacity: 1 });
  }, []);
  
  return <div className="element opacity-0">Content</div>;
}
```

### Motion Animations
For simpler animations:

```jsx
import { motion } from 'motion/react';

export function MotionComponent() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      Content
    </motion.div>
  );
}
```

## 🔗 API Integration

### API Service Pattern

```jsx
// services/repoService.js
export async function fetchRepository(repoId) {
  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/api/repos/${repoId}`
  );
  return response.json();
}

// Usage in component
import { fetchRepository } from './services/repoService';

export function RepoDetails({ repoId }) {
  const [repo, setRepo] = useState(null);
  
  useEffect(() => {
    fetchRepository(repoId).then(setRepo);
  }, [repoId]);
  
  return <div>{repo?.name}</div>;
}
```

## 🧪 Testing

### Recommended Testing Libraries
```bash
npm install --save-dev vitest @testing-library/react @testing-library/dom
```

**Example test:**
```jsx
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import MyComponent from './MyComponent';

describe('MyComponent', () => {
  it('renders correctly', () => {
    render(<MyComponent />);
    expect(screen.getByText('Expected Text')).toBeInTheDocument();
  });
});
```

## 📦 Deployment

### Building for Production
```bash
npm run build
```

### Deployment Platforms

**Vercel (Recommended for Vite):**
```bash
npm install -g vercel
vercel
```

**Netlify:**
```bash
npm run build
# Deploy the dist/ folder
```

**GitHub Pages:**
```bash
# Update vite.config.js base path
npm run build
# Push dist/ folder
```

**Docker:**
```dockerfile
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:18
WORKDIR /app
RUN npm install -g serve
COPY --from=build /app/dist ./dist
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in vite.config.js or use:
npm run dev -- --port 3000
```

### Dependencies Not Installing
```bash
rm -rf node_modules package-lock.json
npm install
```

### Build Fails
```bash
# Clear cache and rebuild
rm -rf dist
npm run build
```

### Hot Module Replacement (HMR) Not Working
Check `vite.config.js` HMR configuration and browser console for errors.

## 🔗 Useful Resources

- [React Documentation](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [React Router](https://reactrouter.com)
- [Three.js Documentation](https://threejs.org)
- [GSAP Documentation](https://gsap.com)

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/amazing-feature`
2. Make your changes
3. Commit: `git commit -m 'Add amazing feature'`
4. Push: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

Built with ❤️ for GitHopper
```

---

## [39] frontend/components.json
**Size:** 473.0B

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": false,
  "tsx": false,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/styles.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "iconLibrary": "radix",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  },
  "registries": {
    "@react-bits": "https://reactbits.dev/r/{name}.json"
  }
}

```

---

## [40] frontend/index.html
**Size:** 445.0B

```html
<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/x-icon" href="/assets/githopper.ico">
    <link rel="apple-touch-icon" href="/assets/githopper.png">
    <title>GitHopper</title>
</head>

<body>
    <div id="root"></div>
    <script type="module" src="/src/main-home.jsx"></script>
</body>

</html>
```

---

## [41] frontend/jsconfig.json
**Size:** 155.0B

```json
{
    "compilerOptions": {
        "baseUrl": ".",
        "paths": {
            "@/*": [
                "src/*"
            ]
        }
    }
}
```

---

## [42] frontend/package-lock.json
**Size:** 148.6KB

```json
{
    "name": "githopperintro",
    "version": "0.0.0",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "githopperintro",
            "version": "0.0.0",
            "dependencies": {
                "firebase": "^12.11.0",
                "gsap": "^3.14.2",
                "lenis": "^1.3.21",
                "motion": "^12.38.0",
                "ogl": "^1.0.11",
                "react": "^18.3.1",
                "react-dom": "^18.3.1",
                "react-router-dom": "^7.13.2",
                "three": "^0.183.2"
            },
            "devDependencies": {
                "@tailwindcss/postcss": "^4.2.2",
                "@vitejs/plugin-react": "^4.4.1",
                "autoprefixer": "^10.4.27",
                "postcss": "^8.5.8",
                "tailwindcss": "^4.2.2",
                "vite": "^5.4.10"
            }
        },
        "node_modules/@alloc/quick-lru": {
            "version": "5.2.0",
            "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
            "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=10"
            },
            "funding": {
                "url": "https://github.com/sponsors/sindresorhus"
            }
        },
        "node_modules/@babel/code-frame": {
            "version": "7.29.0",
            "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.0.tgz",
            "integrity": "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/helper-validator-identifier": "^7.28.5",
                "js-tokens": "^4.0.0",
                "picocolors": "^1.1.1"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/compat-data": {
            "version": "7.29.0",
            "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.0.tgz",
            "integrity": "sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/core": {
            "version": "7.29.0",
            "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.0.tgz",
            "integrity": "sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/code-frame": "^7.29.0",
                "@babel/generator": "^7.29.0",
                "@babel/helper-compilation-targets": "^7.28.6",
                "@babel/helper-module-transforms": "^7.28.6",
                "@babel/helpers": "^7.28.6",
                "@babel/parser": "^7.29.0",
                "@babel/template": "^7.28.6",
                "@babel/traverse": "^7.29.0",
                "@babel/types": "^7.29.0",
                "@jridgewell/remapping": "^2.3.5",
                "convert-source-map": "^2.0.0",
                "debug": "^4.1.0",
                "gensync": "^1.0.0-beta.2",
                "json5": "^2.2.3",
                "semver": "^6.3.1"
            },
            "engines": {
                "node": ">=6.9.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/babel"
            }
        },
        "node_modules/@babel/generator": {
            "version": "7.29.1",
            "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.1.tgz",
            "integrity": "sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/parser": "^7.29.0",
                "@babel/types": "^7.29.0",
                "@jridgewell/gen-mapping": "^0.3.12",
                "@jridgewell/trace-mapping": "^0.3.28",
                "jsesc": "^3.0.2"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/helper-compilation-targets": {
            "version": "7.28.6",
            "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.28.6.tgz",
            "integrity": "sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/compat-data": "^7.28.6",
                "@babel/helper-validator-option": "^7.27.1",
                "browserslist": "^4.24.0",
                "lru-cache": "^5.1.1",
                "semver": "^6.3.1"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/helper-globals": {
            "version": "7.28.0",
            "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
            "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/helper-module-imports": {
            "version": "7.28.6",
            "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.28.6.tgz",
            "integrity": "sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/traverse": "^7.28.6",
                "@babel/types": "^7.28.6"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/helper-module-transforms": {
            "version": "7.28.6",
            "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.6.tgz",
            "integrity": "sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/helper-module-imports": "^7.28.6",
                "@babel/helper-validator-identifier": "^7.28.5",
                "@babel/traverse": "^7.28.6"
            },
            "engines": {
                "node": ">=6.9.0"
            },
            "peerDependencies": {
                "@babel/core": "^7.0.0"
            }
        },
        "node_modules/@babel/helper-plugin-utils": {
            "version": "7.28.6",
            "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.28.6.tgz",
            "integrity": "sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/helper-string-parser": {
            "version": "7.27.1",
            "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
            "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/helper-validator-identifier": {
            "version": "7.28.5",
            "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
            "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/helper-validator-option": {
            "version": "7.27.1",
            "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.27.1.tgz",
            "integrity": "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/helpers": {
            "version": "7.29.2",
            "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.29.2.tgz",
            "integrity": "sha512-HoGuUs4sCZNezVEKdVcwqmZN8GoHirLUcLaYVNBK2J0DadGtdcqgr3BCbvH8+XUo4NGjNl3VOtSjEKNzqfFgKw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/template": "^7.28.6",
                "@babel/types": "^7.29.0"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/parser": {
            "version": "7.29.2",
            "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.2.tgz",
            "integrity": "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/types": "^7.29.0"
            },
            "bin": {
                "parser": "bin/babel-parser.js"
            },
            "engines": {
                "node": ">=6.0.0"
            }
        },
        "node_modules/@babel/plugin-transform-react-jsx-self": {
            "version": "7.27.1",
            "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.27.1.tgz",
            "integrity": "sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/helper-plugin-utils": "^7.27.1"
            },
            "engines": {
                "node": ">=6.9.0"
            },
            "peerDependencies": {
                "@babel/core": "^7.0.0-0"
            }
        },
        "node_modules/@babel/plugin-transform-react-jsx-source": {
            "version": "7.27.1",
            "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.27.1.tgz",
            "integrity": "sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/helper-plugin-utils": "^7.27.1"
            },
            "engines": {
                "node": ">=6.9.0"
            },
            "peerDependencies": {
                "@babel/core": "^7.0.0-0"
            }
        },
        "node_modules/@babel/template": {
            "version": "7.28.6",
            "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.28.6.tgz",
            "integrity": "sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/code-frame": "^7.28.6",
                "@babel/parser": "^7.28.6",
                "@babel/types": "^7.28.6"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/traverse": {
            "version": "7.29.0",
            "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.0.tgz",
            "integrity": "sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/code-frame": "^7.29.0",
                "@babel/generator": "^7.29.0",
                "@babel/helper-globals": "^7.28.0",
                "@babel/parser": "^7.29.0",
                "@babel/template": "^7.28.6",
                "@babel/types": "^7.29.0",
                "debug": "^4.3.1"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@babel/types": {
            "version": "7.29.0",
            "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.0.tgz",
            "integrity": "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/helper-string-parser": "^7.27.1",
                "@babel/helper-validator-identifier": "^7.28.5"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@esbuild/aix-ppc64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.21.5.tgz",
            "integrity": "sha512-1SDgH6ZSPTlggy1yI6+Dbkiz8xzpHJEVAlF/AM1tHPLsf5STom9rwtjE4hKAF20FfXXNTFqEYXyJNWh1GiZedQ==",
            "cpu": [
                "ppc64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "aix"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/android-arm": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.21.5.tgz",
            "integrity": "sha512-vCPvzSjpPHEi1siZdlvAlsPxXl7WbOVUBBAowWug4rJHb68Ox8KualB+1ocNvT5fjv6wpkX6o/iEpbDrf68zcg==",
            "cpu": [
                "arm"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/android-arm64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.21.5.tgz",
            "integrity": "sha512-c0uX9VAUBQ7dTDCjq+wdyGLowMdtR/GoC2U5IYk/7D1H1JYC0qseD7+11iMP2mRLN9RcCMRcjC4YMclCzGwS/A==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/android-x64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.21.5.tgz",
            "integrity": "sha512-D7aPRUUNHRBwHxzxRvp856rjUHRFW1SdQATKXH2hqA0kAZb1hKmi02OpYRacl0TxIGz/ZmXWlbZgjwWYaCakTA==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/darwin-arm64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.21.5.tgz",
            "integrity": "sha512-DwqXqZyuk5AiWWf3UfLiRDJ5EDd49zg6O9wclZ7kUMv2WRFr4HKjXp/5t8JZ11QbQfUS6/cRCKGwYhtNAY88kQ==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/darwin-x64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.21.5.tgz",
            "integrity": "sha512-se/JjF8NlmKVG4kNIuyWMV/22ZaerB+qaSi5MdrXtd6R08kvs2qCN4C09miupktDitvh8jRFflwGFBQcxZRjbw==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/freebsd-arm64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.21.5.tgz",
            "integrity": "sha512-5JcRxxRDUJLX8JXp/wcBCy3pENnCgBR9bN6JsY4OmhfUtIHe3ZW0mawA7+RDAcMLrMIZaf03NlQiX9DGyB8h4g==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "freebsd"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/freebsd-x64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.21.5.tgz",
            "integrity": "sha512-J95kNBj1zkbMXtHVH29bBriQygMXqoVQOQYA+ISs0/2l3T9/kj42ow2mpqerRBxDJnmkUDCaQT/dfNXWX/ZZCQ==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "freebsd"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-arm": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.21.5.tgz",
            "integrity": "sha512-bPb5AHZtbeNGjCKVZ9UGqGwo8EUu4cLq68E95A53KlxAPRmUyYv2D6F0uUI65XisGOL1hBP5mTronbgo+0bFcA==",
            "cpu": [
                "arm"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-arm64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.21.5.tgz",
            "integrity": "sha512-ibKvmyYzKsBeX8d8I7MH/TMfWDXBF3db4qM6sy+7re0YXya+K1cem3on9XgdT2EQGMu4hQyZhan7TeQ8XkGp4Q==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-ia32": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.21.5.tgz",
            "integrity": "sha512-YvjXDqLRqPDl2dvRODYmmhz4rPeVKYvppfGYKSNGdyZkA01046pLWyRKKI3ax8fbJoK5QbxblURkwK/MWY18Tg==",
            "cpu": [
                "ia32"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-loong64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.21.5.tgz",
            "integrity": "sha512-uHf1BmMG8qEvzdrzAqg2SIG/02+4/DHB6a9Kbya0XDvwDEKCoC8ZRWI5JJvNdUjtciBGFQ5PuBlpEOXQj+JQSg==",
            "cpu": [
                "loong64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-mips64el": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.21.5.tgz",
            "integrity": "sha512-IajOmO+KJK23bj52dFSNCMsz1QP1DqM6cwLUv3W1QwyxkyIWecfafnI555fvSGqEKwjMXVLokcV5ygHW5b3Jbg==",
            "cpu": [
                "mips64el"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-ppc64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.21.5.tgz",
            "integrity": "sha512-1hHV/Z4OEfMwpLO8rp7CvlhBDnjsC3CttJXIhBi+5Aj5r+MBvy4egg7wCbe//hSsT+RvDAG7s81tAvpL2XAE4w==",
            "cpu": [
                "ppc64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-riscv64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.21.5.tgz",
            "integrity": "sha512-2HdXDMd9GMgTGrPWnJzP2ALSokE/0O5HhTUvWIbD3YdjME8JwvSCnNGBnTThKGEB91OZhzrJ4qIIxk/SBmyDDA==",
            "cpu": [
                "riscv64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-s390x": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.21.5.tgz",
            "integrity": "sha512-zus5sxzqBJD3eXxwvjN1yQkRepANgxE9lgOW2qLnmr8ikMTphkjgXu1HR01K4FJg8h1kEEDAqDcZQtbrRnB41A==",
            "cpu": [
                "s390x"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/linux-x64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.21.5.tgz",
            "integrity": "sha512-1rYdTpyv03iycF1+BhzrzQJCdOuAOtaqHTWJZCWvijKD2N5Xu0TtVC8/+1faWqcP9iBCWOmjmhoH94dH82BxPQ==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/netbsd-x64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.21.5.tgz",
            "integrity": "sha512-Woi2MXzXjMULccIwMnLciyZH4nCIMpWQAs049KEeMvOcNADVxo0UBIQPfSmxB3CWKedngg7sWZdLvLczpe0tLg==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "netbsd"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/openbsd-x64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.21.5.tgz",
            "integrity": "sha512-HLNNw99xsvx12lFBUwoT8EVCsSvRNDVxNpjZ7bPn947b8gJPzeHWyNVhFsaerc0n3TsbOINvRP2byTZ5LKezow==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "openbsd"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/sunos-x64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.21.5.tgz",
            "integrity": "sha512-6+gjmFpfy0BHU5Tpptkuh8+uw3mnrvgs+dSPQXQOv3ekbordwnzTVEb4qnIvQcYXq6gzkyTnoZ9dZG+D4garKg==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "sunos"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/win32-arm64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.21.5.tgz",
            "integrity": "sha512-Z0gOTd75VvXqyq7nsl93zwahcTROgqvuAcYDUr+vOv8uHhNSKROyU961kgtCD1e95IqPKSQKH7tBTslnS3tA8A==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/win32-ia32": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.21.5.tgz",
            "integrity": "sha512-SWXFF1CL2RVNMaVs+BBClwtfZSvDgtL//G/smwAc5oVK/UPu2Gu9tIaRgFmYFFKrmg3SyAjSrElf0TiJ1v8fYA==",
            "cpu": [
                "ia32"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@esbuild/win32-x64": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.21.5.tgz",
            "integrity": "sha512-tQd/1efJuzPC6rCFwEvLtci/xNFcTZknmXs98FYDfGE4wP9ClFV98nyKrzJKVPMhdDnjzLhdUyMX4PsQAPjwIw==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@firebase/ai": {
            "version": "2.10.0",
            "resolved": "https://registry.npmjs.org/@firebase/ai/-/ai-2.10.0.tgz",
            "integrity": "sha512-1lI6HomyoO/8RSJb6ItyHLpHnB2z27m5F4aX/Vpi1nhwWoxdNjkq+6UQOykHyCE0KairojOE5qQ20i1tnF0nNA==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/app-check-interop-types": "0.3.3",
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x",
                "@firebase/app-types": "0.x"
            }
        },
        "node_modules/@firebase/analytics": {
            "version": "0.10.21",
            "resolved": "https://registry.npmjs.org/@firebase/analytics/-/analytics-0.10.21.tgz",
            "integrity": "sha512-j2y2q65BlgLGB5Pwjhv/Jopw2X/TBTzvAtI5z/DSp56U4wBj7LfhBfzbdCtFPges+Wz0g55GdoawXibOH5jGng==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/installations": "0.6.21",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/analytics-compat": {
            "version": "0.2.27",
            "resolved": "https://registry.npmjs.org/@firebase/analytics-compat/-/analytics-compat-0.2.27.tgz",
            "integrity": "sha512-ZObpYpAxL6JfgH7GnvlDD0sbzGZ0o4nijV8skatV9ZX49hJtCYbFqaEcPYptT94rgX1KUoKEderC7/fa7hybtw==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/analytics": "0.10.21",
                "@firebase/analytics-types": "0.8.3",
                "@firebase/component": "0.7.2",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/analytics-types": {
            "version": "0.8.3",
            "resolved": "https://registry.npmjs.org/@firebase/analytics-types/-/analytics-types-0.8.3.tgz",
            "integrity": "sha512-VrIp/d8iq2g501qO46uGz3hjbDb8xzYMrbu8Tp0ovzIzrvJZ2fvmj649gTjge/b7cCCcjT0H37g1gVtlNhnkbg==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/app": {
            "version": "0.14.10",
            "resolved": "https://registry.npmjs.org/@firebase/app/-/app-0.14.10.tgz",
            "integrity": "sha512-PlPhdtjgWUra+LImQTnXOUqUa/jcufZhizdR93ZjlQSS3ahCtDTG6pJw7j0OwFal18DQjICXfeVNsUUrcNisfA==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "idb": "7.1.1",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            }
        },
        "node_modules/@firebase/app-check": {
            "version": "0.11.2",
            "resolved": "https://registry.npmjs.org/@firebase/app-check/-/app-check-0.11.2.tgz",
            "integrity": "sha512-jcXQVMHAQ5AEKzVD5C7s5fmAYeFOuN6lAJeNTgZK2B9aLnofWaJt8u1A8Idm8gpsBBYSaY3cVyeH5SWMOVPBLQ==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/app-check-compat": {
            "version": "0.4.2",
            "resolved": "https://registry.npmjs.org/@firebase/app-check-compat/-/app-check-compat-0.4.2.tgz",
            "integrity": "sha512-M91NhxqbSkI0ChkJWy69blC+rPr6HEgaeRllddSaU1pQ/7IiegeCQM9pPDIgvWnwnBSzKhUHpe6ro/jhJ+cvzw==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/app-check": "0.11.2",
                "@firebase/app-check-types": "0.5.3",
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/app-check-interop-types": {
            "version": "0.3.3",
            "resolved": "https://registry.npmjs.org/@firebase/app-check-interop-types/-/app-check-interop-types-0.3.3.tgz",
            "integrity": "sha512-gAlxfPLT2j8bTI/qfe3ahl2I2YcBQ8cFIBdhAQA4I2f3TndcO+22YizyGYuttLHPQEpWkhmpFW60VCFEPg4g5A==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/app-check-types": {
            "version": "0.5.3",
            "resolved": "https://registry.npmjs.org/@firebase/app-check-types/-/app-check-types-0.5.3.tgz",
            "integrity": "sha512-hyl5rKSj0QmwPdsAxrI5x1otDlByQ7bvNvVt8G/XPO2CSwE++rmSVf3VEhaeOR4J8ZFaF0Z0NDSmLejPweZ3ng==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/app-compat": {
            "version": "0.5.10",
            "resolved": "https://registry.npmjs.org/@firebase/app-compat/-/app-compat-0.5.10.tgz",
            "integrity": "sha512-tFmBuZL0/v1h6eyKRgWI58ucft6dEJmAi9nhPUXoAW4ZbPSTlnsh31AuEwUoRTz+wwRk9gmgss9GZV05ZM9Kug==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/app": "0.14.10",
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            }
        },
        "node_modules/@firebase/app-types": {
            "version": "0.9.3",
            "resolved": "https://registry.npmjs.org/@firebase/app-types/-/app-types-0.9.3.tgz",
            "integrity": "sha512-kRVpIl4vVGJ4baogMDINbyrIOtOxqhkZQg4jTq3l8Lw6WSk0xfpEYzezFu+Kl4ve4fbPl79dvwRtaFqAC/ucCw==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/auth-compat": {
            "version": "0.6.4",
            "resolved": "https://registry.npmjs.org/@firebase/auth-compat/-/auth-compat-0.6.4.tgz",
            "integrity": "sha512-2pj8m/hnqXvMLfC0Mk+fORVTM5DQPkS6l8JpMgtoAWGVgCmYnoWdFMaNWtKbmCxBEyvMA3FlnCJyzrUSMWTfuA==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/auth": "1.12.2",
                "@firebase/auth-types": "0.13.0",
                "@firebase/component": "0.7.2",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/auth-compat/node_modules/@firebase/auth": {
            "version": "1.12.2",
            "resolved": "https://registry.npmjs.org/@firebase/auth/-/auth-1.12.2.tgz",
            "integrity": "sha512-CZJL8V10Vzibs+pDTXdQF+hot1IigIoqF4a4lA/qr5Deo1srcefiyIfgg28B67Lk7IxZhwfJMuI+1bu2xBmV0A==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x",
                "@react-native-async-storage/async-storage": "^2.2.0"
            },
            "peerDependenciesMeta": {
                "@react-native-async-storage/async-storage": {
                    "optional": true
                }
            }
        },
        "node_modules/@firebase/auth-interop-types": {
            "version": "0.2.4",
            "resolved": "https://registry.npmjs.org/@firebase/auth-interop-types/-/auth-interop-types-0.2.4.tgz",
            "integrity": "sha512-JPgcXKCuO+CWqGDnigBtvo09HeBs5u/Ktc2GaFj2m01hLarbxthLNm7Fk8iOP1aqAtXV+fnnGj7U28xmk7IwVA==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/auth-types": {
            "version": "0.13.0",
            "resolved": "https://registry.npmjs.org/@firebase/auth-types/-/auth-types-0.13.0.tgz",
            "integrity": "sha512-S/PuIjni0AQRLF+l9ck0YpsMOdE8GO2KU6ubmBB7P+7TJUCQDa3R1dlgYm9UzGbbePMZsp0xzB93f2b/CgxMOg==",
            "license": "Apache-2.0",
            "peerDependencies": {
                "@firebase/app-types": "0.x",
                "@firebase/util": "1.x"
            }
        },
        "node_modules/@firebase/component": {
            "version": "0.7.2",
            "resolved": "https://registry.npmjs.org/@firebase/component/-/component-0.7.2.tgz",
            "integrity": "sha512-iyVDGc6Vjx7Rm0cAdccLH/NG6fADsgJak/XW9IA2lPf8AjIlsemOpFGKczYyPHxm4rnKdR8z6sK4+KEC7NwmEg==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            }
        },
        "node_modules/@firebase/data-connect": {
            "version": "0.5.0",
            "resolved": "https://registry.npmjs.org/@firebase/data-connect/-/data-connect-0.5.0.tgz",
            "integrity": "sha512-G3GYHpWNJJ95502RQLApzw0jaG3pScHl+J/2MdxIuB51xtHnkRL6KvIAP3fFF1drUewWJHOnDA1U+q4Evf3KSw==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/auth-interop-types": "0.2.4",
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/database": {
            "version": "1.1.2",
            "resolved": "https://registry.npmjs.org/@firebase/database/-/database-1.1.2.tgz",
            "integrity": "sha512-lP96CMjMPy/+d1d9qaaHjHHdzdwvEOuyyLq9ehX89e2XMKwS1jHNzYBO+42bdSumuj5ukPbmnFtViZu8YOMT+w==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/app-check-interop-types": "0.3.3",
                "@firebase/auth-interop-types": "0.2.4",
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "faye-websocket": "0.11.4",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            }
        },
        "node_modules/@firebase/database-compat": {
            "version": "2.1.2",
            "resolved": "https://registry.npmjs.org/@firebase/database-compat/-/database-compat-2.1.2.tgz",
            "integrity": "sha512-j4A6IhVZbgxAzT6gJJC2PfOxYCK9SrDrUO7nTM4EscTYtKkAkzsbKoCnDdjFapQfnsncvPWjqVTr/0PffUwg3g==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/database": "1.1.2",
                "@firebase/database-types": "1.0.18",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            }
        },
        "node_modules/@firebase/database-types": {
            "version": "1.0.18",
            "resolved": "https://registry.npmjs.org/@firebase/database-types/-/database-types-1.0.18.tgz",
            "integrity": "sha512-yOY8IC2go9lfbVDMiy2ATun4EB2AFwocPaQADwMN/RHRUAZSM4rlAV7PGbWPSG/YhkJ2A9xQAiAENgSua9G5Fg==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/app-types": "0.9.3",
                "@firebase/util": "1.15.0"
            }
        },
        "node_modules/@firebase/firestore": {
            "version": "4.13.0",
            "resolved": "https://registry.npmjs.org/@firebase/firestore/-/firestore-4.13.0.tgz",
            "integrity": "sha512-7i4cVNJXTMim7/P7UsNim0DwyLPk4QQ3y1oSNzv4l0ykJOKYCiFMOuEeUxUYvrReXDJxWHrT/4XMeVQm+13rRw==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "@firebase/webchannel-wrapper": "1.0.5",
                "@grpc/grpc-js": "~1.9.0",
                "@grpc/proto-loader": "^0.7.8",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/firestore-compat": {
            "version": "0.4.7",
            "resolved": "https://registry.npmjs.org/@firebase/firestore-compat/-/firestore-compat-0.4.7.tgz",
            "integrity": "sha512-Et4XxtGnjp0Q9tmaEMETnY5GHJ8gQ9+RN6sSTT4ETWKmym2d6gIjarw0rCQcx+7BrWVYLEIOAXSXysl0b3xnUA==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/firestore": "4.13.0",
                "@firebase/firestore-types": "3.0.3",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/firestore-types": {
            "version": "3.0.3",
            "resolved": "https://registry.npmjs.org/@firebase/firestore-types/-/firestore-types-3.0.3.tgz",
            "integrity": "sha512-hD2jGdiWRxB/eZWF89xcK9gF8wvENDJkzpVFb4aGkzfEaKxVRD1kjz1t1Wj8VZEp2LCB53Yx1zD8mrhQu87R6Q==",
            "license": "Apache-2.0",
            "peerDependencies": {
                "@firebase/app-types": "0.x",
                "@firebase/util": "1.x"
            }
        },
        "node_modules/@firebase/functions": {
            "version": "0.13.3",
            "resolved": "https://registry.npmjs.org/@firebase/functions/-/functions-0.13.3.tgz",
            "integrity": "sha512-csO7ckK3SSs+NUZW1nms9EK7ckHe/1QOjiP8uAkCYa7ND18s44vjE9g3KxEeIUpyEPqZaX1EhJuFyZjHigAcYw==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/app-check-interop-types": "0.3.3",
                "@firebase/auth-interop-types": "0.2.4",
                "@firebase/component": "0.7.2",
                "@firebase/messaging-interop-types": "0.2.3",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/functions-compat": {
            "version": "0.4.3",
            "resolved": "https://registry.npmjs.org/@firebase/functions-compat/-/functions-compat-0.4.3.tgz",
            "integrity": "sha512-BxkEwWgx1of0tKaao/r2VR6WBLk/RAiyztatiONPrPE8gkitFkOnOCxf8i9cUyA5hX5RGt5H30uNn25Q6QNEmQ==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/functions": "0.13.3",
                "@firebase/functions-types": "0.6.3",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/functions-types": {
            "version": "0.6.3",
            "resolved": "https://registry.npmjs.org/@firebase/functions-types/-/functions-types-0.6.3.tgz",
            "integrity": "sha512-EZoDKQLUHFKNx6VLipQwrSMh01A1SaL3Wg6Hpi//x6/fJ6Ee4hrAeswK99I5Ht8roiniKHw4iO0B1Oxj5I4plg==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/installations": {
            "version": "0.6.21",
            "resolved": "https://registry.npmjs.org/@firebase/installations/-/installations-0.6.21.tgz",
            "integrity": "sha512-xGFGTeICJZ5vhrmmDukeczIcFULFXybojML2+QSDFoKj5A7zbGN7KzFGSKNhDkIxpjzsYG9IleJyUebuAcmqWA==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/util": "1.15.0",
                "idb": "7.1.1",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/installations-compat": {
            "version": "0.2.21",
            "resolved": "https://registry.npmjs.org/@firebase/installations-compat/-/installations-compat-0.2.21.tgz",
            "integrity": "sha512-zahIUkaVKbR8zmTeBHkdfaVl6JGWlhVoSjF7CVH33nFqD3SlPEpEEegn2GNT5iAfsVdtlCyJJ9GW4YKjq+RJKQ==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/installations": "0.6.21",
                "@firebase/installations-types": "0.5.3",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/installations-types": {
            "version": "0.5.3",
            "resolved": "https://registry.npmjs.org/@firebase/installations-types/-/installations-types-0.5.3.tgz",
            "integrity": "sha512-2FJI7gkLqIE0iYsNQ1P751lO3hER+Umykel+TkLwHj6plzWVxqvfclPUZhcKFVQObqloEBTmpi2Ozn7EkCABAA==",
            "license": "Apache-2.0",
            "peerDependencies": {
                "@firebase/app-types": "0.x"
            }
        },
        "node_modules/@firebase/logger": {
            "version": "0.5.0",
            "resolved": "https://registry.npmjs.org/@firebase/logger/-/logger-0.5.0.tgz",
            "integrity": "sha512-cGskaAvkrnh42b3BA3doDWeBmuHFO/Mx5A83rbRDYakPjO9bJtRL3dX7javzc2Rr/JHZf4HlterTW2lUkfeN4g==",
            "license": "Apache-2.0",
            "dependencies": {
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            }
        },
        "node_modules/@firebase/messaging": {
            "version": "0.12.25",
            "resolved": "https://registry.npmjs.org/@firebase/messaging/-/messaging-0.12.25.tgz",
            "integrity": "sha512-7RhDwoDHlOK1/ou0/LeubxmjcngsTjDdrY/ssg2vwAVpUuVAhQzQvuCAOYxcX5wNC1zCgQ54AP1vdngBwbCmOQ==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/installations": "0.6.21",
                "@firebase/messaging-interop-types": "0.2.3",
                "@firebase/util": "1.15.0",
                "idb": "7.1.1",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/messaging-compat": {
            "version": "0.2.25",
            "resolved": "https://registry.npmjs.org/@firebase/messaging-compat/-/messaging-compat-0.2.25.tgz",
            "integrity": "sha512-eoOQqGLtRlseTdiemTN44LlHZpltK5gnhq8XVUuLgtIOG+odtDzrz2UoTpcJWSzaJQVxNLb/x9f39tHdDM4N4w==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/messaging": "0.12.25",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/messaging-interop-types": {
            "version": "0.2.3",
            "resolved": "https://registry.npmjs.org/@firebase/messaging-interop-types/-/messaging-interop-types-0.2.3.tgz",
            "integrity": "sha512-xfzFaJpzcmtDjycpDeCUj0Ge10ATFi/VHVIvEEjDNc3hodVBQADZ7BWQU7CuFpjSHE+eLuBI13z5F/9xOoGX8Q==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/performance": {
            "version": "0.7.11",
            "resolved": "https://registry.npmjs.org/@firebase/performance/-/performance-0.7.11.tgz",
            "integrity": "sha512-V3uAhrz7IYJuji+OgT3qYTGKxpek/TViXti9OSsUJ4AexZ3jQjYH5Yrn7JvBxk8MGiSLsC872hh+BxQiPZsm7g==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/installations": "0.6.21",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0",
                "web-vitals": "^4.2.4"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/performance-compat": {
            "version": "0.2.24",
            "resolved": "https://registry.npmjs.org/@firebase/performance-compat/-/performance-compat-0.2.24.tgz",
            "integrity": "sha512-YRlejH8wLt7ThWao+HXoKUHUrZKGYq+otxkPS+8nuE5PeN1cBXX7NAJl9ueuUkBwMIrnKdnDqL/voHXxDAAt3g==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/performance": "0.7.11",
                "@firebase/performance-types": "0.2.3",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/performance-types": {
            "version": "0.2.3",
            "resolved": "https://registry.npmjs.org/@firebase/performance-types/-/performance-types-0.2.3.tgz",
            "integrity": "sha512-IgkyTz6QZVPAq8GSkLYJvwSLr3LS9+V6vNPQr0x4YozZJiLF5jYixj0amDtATf1X0EtYHqoPO48a9ija8GocxQ==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/remote-config": {
            "version": "0.8.2",
            "resolved": "https://registry.npmjs.org/@firebase/remote-config/-/remote-config-0.8.2.tgz",
            "integrity": "sha512-5EXqOThV4upjK9D38d/qOSVwOqRhemlaOFk9vCkMNNALeIlwr+4pLjtLNo4qoY8etQmU/1q4aIATE9N8PFqg0g==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/installations": "0.6.21",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/remote-config-compat": {
            "version": "0.2.23",
            "resolved": "https://registry.npmjs.org/@firebase/remote-config-compat/-/remote-config-compat-0.2.23.tgz",
            "integrity": "sha512-4+KqRRHEUUmKT6tFmnpWATOsaFfmSuBs1jXH8JzVtMLEYqq/WS9IDM92OdefFDSrAA2xGd0WN004z8mKeIIscw==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/remote-config": "0.8.2",
                "@firebase/remote-config-types": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/remote-config-types": {
            "version": "0.5.0",
            "resolved": "https://registry.npmjs.org/@firebase/remote-config-types/-/remote-config-types-0.5.0.tgz",
            "integrity": "sha512-vI3bqLoF14L/GchtgayMiFpZJF+Ao3uR8WCde0XpYNkSokDpAKca2DxvcfeZv7lZUqkUwQPL2wD83d3vQ4vvrg==",
            "license": "Apache-2.0"
        },
        "node_modules/@firebase/storage": {
            "version": "0.14.2",
            "resolved": "https://registry.npmjs.org/@firebase/storage/-/storage-0.14.2.tgz",
            "integrity": "sha512-o/culaTeJ8GRpKXRJov21rux/n9dRaSOWLebyatFP2sqEdCxQPjVA1H9Z2fzYwQxMIU0JVmC7SPPmU11v7L6vQ==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x"
            }
        },
        "node_modules/@firebase/storage-compat": {
            "version": "0.4.2",
            "resolved": "https://registry.npmjs.org/@firebase/storage-compat/-/storage-compat-0.4.2.tgz",
            "integrity": "sha512-R+aB38wxCH5zjIO/xu9KznI7fgiPuZAG98uVm1NcidHyyupGgIDLKigGmRGBZMnxibe/m2oxNKoZpfEbUX2aQQ==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/storage": "0.14.2",
                "@firebase/storage-types": "0.8.3",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app-compat": "0.x"
            }
        },
        "node_modules/@firebase/storage-types": {
            "version": "0.8.3",
            "resolved": "https://registry.npmjs.org/@firebase/storage-types/-/storage-types-0.8.3.tgz",
            "integrity": "sha512-+Muk7g9uwngTpd8xn9OdF/D48uiQ7I1Fae7ULsWPuKoCH3HU7bfFPhxtJYzyhjdniowhuDpQcfPmuNRAqZEfvg==",
            "license": "Apache-2.0",
            "peerDependencies": {
                "@firebase/app-types": "0.x",
                "@firebase/util": "1.x"
            }
        },
        "node_modules/@firebase/util": {
            "version": "1.15.0",
            "resolved": "https://registry.npmjs.org/@firebase/util/-/util-1.15.0.tgz",
            "integrity": "sha512-AmWf3cHAOMbrCPG4xdPKQaj5iHnyYfyLKZxwz+Xf55bqKbpAmcYifB4jQinT2W9XhDRHISOoPyBOariJpCG6FA==",
            "hasInstallScript": true,
            "license": "Apache-2.0",
            "dependencies": {
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            }
        },
        "node_modules/@firebase/webchannel-wrapper": {
            "version": "1.0.5",
            "resolved": "https://registry.npmjs.org/@firebase/webchannel-wrapper/-/webchannel-wrapper-1.0.5.tgz",
            "integrity": "sha512-+uGNN7rkfn41HLO0vekTFhTxk61eKa8mTpRGLO0QSqlQdKvIoGAvLp3ppdVIWbTGYJWM6Kp0iN+PjMIOcnVqTw==",
            "license": "Apache-2.0"
        },
        "node_modules/@grpc/grpc-js": {
            "version": "1.9.15",
            "resolved": "https://registry.npmjs.org/@grpc/grpc-js/-/grpc-js-1.9.15.tgz",
            "integrity": "sha512-nqE7Hc0AzI+euzUwDAy0aY5hCp10r734gMGRdU+qOPX0XSceI2ULrcXB5U2xSc5VkWwalCj4M7GzCAygZl2KoQ==",
            "license": "Apache-2.0",
            "dependencies": {
                "@grpc/proto-loader": "^0.7.8",
                "@types/node": ">=12.12.47"
            },
            "engines": {
                "node": "^8.13.0 || >=10.10.0"
            }
        },
        "node_modules/@grpc/proto-loader": {
            "version": "0.7.15",
            "resolved": "https://registry.npmjs.org/@grpc/proto-loader/-/proto-loader-0.7.15.tgz",
            "integrity": "sha512-tMXdRCfYVixjuFK+Hk0Q1s38gV9zDiDJfWL3h1rv4Qc39oILCu1TRTDt7+fGUI8K4G1Fj125Hx/ru3azECWTyQ==",
            "license": "Apache-2.0",
            "dependencies": {
                "lodash.camelcase": "^4.3.0",
                "long": "^5.0.0",
                "protobufjs": "^7.2.5",
                "yargs": "^17.7.2"
            },
            "bin": {
                "proto-loader-gen-types": "build/bin/proto-loader-gen-types.js"
            },
            "engines": {
                "node": ">=6"
            }
        },
        "node_modules/@jridgewell/gen-mapping": {
            "version": "0.3.13",
            "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
            "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@jridgewell/sourcemap-codec": "^1.5.0",
                "@jridgewell/trace-mapping": "^0.3.24"
            }
        },
        "node_modules/@jridgewell/remapping": {
            "version": "2.3.5",
            "resolved": "https://registry.npmjs.org/@jridgewell/remapping/-/remapping-2.3.5.tgz",
            "integrity": "sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@jridgewell/gen-mapping": "^0.3.5",
                "@jridgewell/trace-mapping": "^0.3.24"
            }
        },
        "node_modules/@jridgewell/resolve-uri": {
            "version": "3.1.2",
            "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
            "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.0.0"
            }
        },
        "node_modules/@jridgewell/sourcemap-codec": {
            "version": "1.5.5",
            "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
            "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/@jridgewell/trace-mapping": {
            "version": "0.3.31",
            "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
            "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@jridgewell/resolve-uri": "^3.1.0",
                "@jridgewell/sourcemap-codec": "^1.4.14"
            }
        },
        "node_modules/@protobufjs/aspromise": {
            "version": "1.1.2",
            "resolved": "https://registry.npmjs.org/@protobufjs/aspromise/-/aspromise-1.1.2.tgz",
            "integrity": "sha512-j+gKExEuLmKwvz3OgROXtrJ2UG2x8Ch2YZUxahh+s1F2HZ+wAceUNLkvy6zKCPVRkU++ZWQrdxsUeQXmcg4uoQ==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@protobufjs/base64": {
            "version": "1.1.2",
            "resolved": "https://registry.npmjs.org/@protobufjs/base64/-/base64-1.1.2.tgz",
            "integrity": "sha512-AZkcAA5vnN/v4PDqKyMR5lx7hZttPDgClv83E//FMNhR2TMcLUhfRUBHCmSl0oi9zMgDDqRUJkSxO3wm85+XLg==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@protobufjs/codegen": {
            "version": "2.0.4",
            "resolved": "https://registry.npmjs.org/@protobufjs/codegen/-/codegen-2.0.4.tgz",
            "integrity": "sha512-YyFaikqM5sH0ziFZCN3xDC7zeGaB/d0IUb9CATugHWbd1FRFwWwt4ld4OYMPWu5a3Xe01mGAULCdqhMlPl29Jg==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@protobufjs/eventemitter": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/@protobufjs/eventemitter/-/eventemitter-1.1.0.tgz",
            "integrity": "sha512-j9ednRT81vYJ9OfVuXG6ERSTdEL1xVsNgqpkxMsbIabzSo3goCjDIveeGv5d03om39ML71RdmrGNjG5SReBP/Q==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@protobufjs/fetch": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/@protobufjs/fetch/-/fetch-1.1.0.tgz",
            "integrity": "sha512-lljVXpqXebpsijW71PZaCYeIcE5on1w5DlQy5WH6GLbFryLUrBD4932W/E2BSpfRJWseIL4v/KPgBFxDOIdKpQ==",
            "license": "BSD-3-Clause",
            "dependencies": {
                "@protobufjs/aspromise": "^1.1.1",
                "@protobufjs/inquire": "^1.1.0"
            }
        },
        "node_modules/@protobufjs/float": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/@protobufjs/float/-/float-1.0.2.tgz",
            "integrity": "sha512-Ddb+kVXlXst9d+R9PfTIxh1EdNkgoRe5tOX6t01f1lYWOvJnSPDBlG241QLzcyPdoNTsblLUdujGSE4RzrTZGQ==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@protobufjs/inquire": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/@protobufjs/inquire/-/inquire-1.1.0.tgz",
            "integrity": "sha512-kdSefcPdruJiFMVSbn801t4vFK7KB/5gd2fYvrxhuJYg8ILrmn9SKSX2tZdV6V+ksulWqS7aXjBcRXl3wHoD9Q==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@protobufjs/path": {
            "version": "1.1.2",
            "resolved": "https://registry.npmjs.org/@protobufjs/path/-/path-1.1.2.tgz",
            "integrity": "sha512-6JOcJ5Tm08dOHAbdR3GrvP+yUUfkjG5ePsHYczMFLq3ZmMkAD98cDgcT2iA1lJ9NVwFd4tH/iSSoe44YWkltEA==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@protobufjs/pool": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/@protobufjs/pool/-/pool-1.1.0.tgz",
            "integrity": "sha512-0kELaGSIDBKvcgS4zkjz1PeddatrjYcmMWOlAuAPwAeccUrPHdUqo/J6LiymHHEiJT5NrF1UVwxY14f+fy4WQw==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@protobufjs/utf8": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/@protobufjs/utf8/-/utf8-1.1.0.tgz",
            "integrity": "sha512-Vvn3zZrhQZkkBE8LSuW3em98c0FwgO4nxzv6OdSxPKJIEKY2bGbHn+mhGIPerzI4twdxaP8/0+06HBpwf345Lw==",
            "license": "BSD-3-Clause"
        },
        "node_modules/@rolldown/pluginutils": {
            "version": "1.0.0-beta.27",
            "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.0-beta.27.tgz",
            "integrity": "sha512-+d0F4MKMCbeVUJwG96uQ4SgAznZNSq93I3V+9NHA4OpvqG8mRCpGdKmK8l/dl02h2CCDHwW2FqilnTyDcAnqjA==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/@rollup/rollup-android-arm-eabi": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm-eabi/-/rollup-android-arm-eabi-4.60.0.tgz",
            "integrity": "sha512-WOhNW9K8bR3kf4zLxbfg6Pxu2ybOUbB2AjMDHSQx86LIF4rH4Ft7vmMwNt0loO0eonglSNy4cpD3MKXXKQu0/A==",
            "cpu": [
                "arm"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ]
        },
        "node_modules/@rollup/rollup-android-arm64": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm64/-/rollup-android-arm64-4.60.0.tgz",
            "integrity": "sha512-u6JHLll5QKRvjciE78bQXDmqRqNs5M/3GVqZeMwvmjaNODJih/WIrJlFVEihvV0MiYFmd+ZyPr9wxOVbPAG2Iw==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ]
        },
        "node_modules/@rollup/rollup-darwin-arm64": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-arm64/-/rollup-darwin-arm64-4.60.0.tgz",
            "integrity": "sha512-qEF7CsKKzSRc20Ciu2Zw1wRrBz4g56F7r/vRwY430UPp/nt1x21Q/fpJ9N5l47WWvJlkNCPJz3QRVw008fi7yA==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ]
        },
        "node_modules/@rollup/rollup-darwin-x64": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-x64/-/rollup-darwin-x64-4.60.0.tgz",
            "integrity": "sha512-WADYozJ4QCnXCH4wPB+3FuGmDPoFseVCUrANmA5LWwGmC6FL14BWC7pcq+FstOZv3baGX65tZ378uT6WG8ynTw==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ]
        },
        "node_modules/@rollup/rollup-freebsd-arm64": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-arm64/-/rollup-freebsd-arm64-4.60.0.tgz",
            "integrity": "sha512-6b8wGHJlDrGeSE3aH5mGNHBjA0TTkxdoNHik5EkvPHCt351XnigA4pS7Wsj/Eo9Y8RBU6f35cjN9SYmCFBtzxw==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "freebsd"
            ]
        },
        "node_modules/@rollup/rollup-freebsd-x64": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-freebsd-x64/-/rollup-freebsd-x64-4.60.0.tgz",
            "integrity": "sha512-h25Ga0t4jaylMB8M/JKAyrvvfxGRjnPQIR8lnCayyzEjEOx2EJIlIiMbhpWxDRKGKF8jbNH01NnN663dH638mA==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "freebsd"
            ]
        },
        "node_modules/@rollup/rollup-linux-arm-gnueabihf": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-gnueabihf/-/rollup-linux-arm-gnueabihf-4.60.0.tgz",
            "integrity": "sha512-RzeBwv0B3qtVBWtcuABtSuCzToo2IEAIQrcyB/b2zMvBWVbjo8bZDjACUpnaafaxhTw2W+imQbP2BD1usasK4g==",
            "cpu": [
                "arm"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-arm-musleabihf": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm-musleabihf/-/rollup-linux-arm-musleabihf-4.60.0.tgz",
            "integrity": "sha512-Sf7zusNI2CIU1HLzuu9Tc5YGAHEZs5Lu7N1ssJG4Tkw6e0MEsN7NdjUDDfGNHy2IU+ENyWT+L2obgWiguWibWQ==",
            "cpu": [
                "arm"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-arm64-gnu": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-gnu/-/rollup-linux-arm64-gnu-4.60.0.tgz",
            "integrity": "sha512-DX2x7CMcrJzsE91q7/O02IJQ5/aLkVtYFryqCjduJhUfGKG6yJV8hxaw8pZa93lLEpPTP/ohdN4wFz7yp/ry9A==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-arm64-musl": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-arm64-musl/-/rollup-linux-arm64-musl-4.60.0.tgz",
            "integrity": "sha512-09EL+yFVbJZlhcQfShpswwRZ0Rg+z/CsSELFCnPt3iK+iqwGsI4zht3secj5vLEs957QvFFXnzAT0FFPIxSrkQ==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-loong64-gnu": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-gnu/-/rollup-linux-loong64-gnu-4.60.0.tgz",
            "integrity": "sha512-i9IcCMPr3EXm8EQg5jnja0Zyc1iFxJjZWlb4wr7U2Wx/GrddOuEafxRdMPRYVaXjgbhvqalp6np07hN1w9kAKw==",
            "cpu": [
                "loong64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-loong64-musl": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-loong64-musl/-/rollup-linux-loong64-musl-4.60.0.tgz",
            "integrity": "sha512-DGzdJK9kyJ+B78MCkWeGnpXJ91tK/iKA6HwHxF4TAlPIY7GXEvMe8hBFRgdrR9Ly4qebR/7gfUs9y2IoaVEyog==",
            "cpu": [
                "loong64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-ppc64-gnu": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-gnu/-/rollup-linux-ppc64-gnu-4.60.0.tgz",
            "integrity": "sha512-RwpnLsqC8qbS8z1H1AxBA1H6qknR4YpPR9w2XX0vo2Sz10miu57PkNcnHVaZkbqyw/kUWfKMI73jhmfi9BRMUQ==",
            "cpu": [
                "ppc64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-ppc64-musl": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-ppc64-musl/-/rollup-linux-ppc64-musl-4.60.0.tgz",
            "integrity": "sha512-Z8pPf54Ly3aqtdWC3G4rFigZgNvd+qJlOE52fmko3KST9SoGfAdSRCwyoyG05q1HrrAblLbk1/PSIV+80/pxLg==",
            "cpu": [
                "ppc64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-riscv64-gnu": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-gnu/-/rollup-linux-riscv64-gnu-4.60.0.tgz",
            "integrity": "sha512-3a3qQustp3COCGvnP4SvrMHnPQ9d1vzCakQVRTliaz8cIp/wULGjiGpbcqrkv0WrHTEp8bQD/B3HBjzujVWLOA==",
            "cpu": [
                "riscv64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-riscv64-musl": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-riscv64-musl/-/rollup-linux-riscv64-musl-4.60.0.tgz",
            "integrity": "sha512-pjZDsVH/1VsghMJ2/kAaxt6dL0psT6ZexQVrijczOf+PeP2BUqTHYejk3l6TlPRydggINOeNRhvpLa0AYpCWSQ==",
            "cpu": [
                "riscv64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-s390x-gnu": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-s390x-gnu/-/rollup-linux-s390x-gnu-4.60.0.tgz",
            "integrity": "sha512-3ObQs0BhvPgiUVZrN7gqCSvmFuMWvWvsjG5ayJ3Lraqv+2KhOsp+pUbigqbeWqueGIsnn+09HBw27rJ+gYK4VQ==",
            "cpu": [
                "s390x"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-x64-gnu": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-gnu/-/rollup-linux-x64-gnu-4.60.0.tgz",
            "integrity": "sha512-EtylprDtQPdS5rXvAayrNDYoJhIz1/vzN2fEubo3yLE7tfAw+948dO0g4M0vkTVFhKojnF+n6C8bDNe+gDRdTg==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-linux-x64-musl": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-linux-x64-musl/-/rollup-linux-x64-musl-4.60.0.tgz",
            "integrity": "sha512-k09oiRCi/bHU9UVFqD17r3eJR9bn03TyKraCrlz5ULFJGdJGi7VOmm9jl44vOJvRJ6P7WuBi/s2A97LxxHGIdw==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ]
        },
        "node_modules/@rollup/rollup-openbsd-x64": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-openbsd-x64/-/rollup-openbsd-x64-4.60.0.tgz",
            "integrity": "sha512-1o/0/pIhozoSaDJoDcec+IVLbnRtQmHwPV730+AOD29lHEEo4F5BEUB24H0OBdhbBBDwIOSuf7vgg0Ywxdfiiw==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "openbsd"
            ]
        },
        "node_modules/@rollup/rollup-openharmony-arm64": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-openharmony-arm64/-/rollup-openharmony-arm64-4.60.0.tgz",
            "integrity": "sha512-pESDkos/PDzYwtyzB5p/UoNU/8fJo68vcXM9ZW2V0kjYayj1KaaUfi1NmTUTUpMn4UhU4gTuK8gIaFO4UGuMbA==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "openharmony"
            ]
        },
        "node_modules/@rollup/rollup-win32-arm64-msvc": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-arm64-msvc/-/rollup-win32-arm64-msvc-4.60.0.tgz",
            "integrity": "sha512-hj1wFStD7B1YBeYmvY+lWXZ7ey73YGPcViMShYikqKT1GtstIKQAtfUI6yrzPjAy/O7pO0VLXGmUVWXQMaYgTQ==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ]
        },
        "node_modules/@rollup/rollup-win32-ia32-msvc": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-ia32-msvc/-/rollup-win32-ia32-msvc-4.60.0.tgz",
            "integrity": "sha512-SyaIPFoxmUPlNDq5EHkTbiKzmSEmq/gOYFI/3HHJ8iS/v1mbugVa7dXUzcJGQfoytp9DJFLhHH4U3/eTy2Bq4w==",
            "cpu": [
                "ia32"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ]
        },
        "node_modules/@rollup/rollup-win32-x64-gnu": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-gnu/-/rollup-win32-x64-gnu-4.60.0.tgz",
            "integrity": "sha512-RdcryEfzZr+lAr5kRm2ucN9aVlCCa2QNq4hXelZxb8GG0NJSazq44Z3PCCc8wISRuCVnGs0lQJVX5Vp6fKA+IA==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ]
        },
        "node_modules/@rollup/rollup-win32-x64-msvc": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/@rollup/rollup-win32-x64-msvc/-/rollup-win32-x64-msvc-4.60.0.tgz",
            "integrity": "sha512-PrsWNQ8BuE00O3Xsx3ALh2Df8fAj9+cvvX9AIA6o4KpATR98c9mud4XtDWVvsEuyia5U4tVSTKygawyJkjm60w==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ]
        },
        "node_modules/@tailwindcss/node": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/node/-/node-4.2.2.tgz",
            "integrity": "sha512-pXS+wJ2gZpVXqFaUEjojq7jzMpTGf8rU6ipJz5ovJV6PUGmlJ+jvIwGrzdHdQ80Sg+wmQxUFuoW1UAAwHNEdFA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@jridgewell/remapping": "^2.3.5",
                "enhanced-resolve": "^5.19.0",
                "jiti": "^2.6.1",
                "lightningcss": "1.32.0",
                "magic-string": "^0.30.21",
                "source-map-js": "^1.2.1",
                "tailwindcss": "4.2.2"
            }
        },
        "node_modules/@tailwindcss/oxide": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide/-/oxide-4.2.2.tgz",
            "integrity": "sha512-qEUA07+E5kehxYp9BVMpq9E8vnJuBHfJEC0vPC5e7iL/hw7HR61aDKoVoKzrG+QKp56vhNZe4qwkRmMC0zDLvg==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">= 20"
            },
            "optionalDependencies": {
                "@tailwindcss/oxide-android-arm64": "4.2.2",
                "@tailwindcss/oxide-darwin-arm64": "4.2.2",
                "@tailwindcss/oxide-darwin-x64": "4.2.2",
                "@tailwindcss/oxide-freebsd-x64": "4.2.2",
                "@tailwindcss/oxide-linux-arm-gnueabihf": "4.2.2",
                "@tailwindcss/oxide-linux-arm64-gnu": "4.2.2",
                "@tailwindcss/oxide-linux-arm64-musl": "4.2.2",
                "@tailwindcss/oxide-linux-x64-gnu": "4.2.2",
                "@tailwindcss/oxide-linux-x64-musl": "4.2.2",
                "@tailwindcss/oxide-wasm32-wasi": "4.2.2",
                "@tailwindcss/oxide-win32-arm64-msvc": "4.2.2",
                "@tailwindcss/oxide-win32-x64-msvc": "4.2.2"
            }
        },
        "node_modules/@tailwindcss/oxide-android-arm64": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-android-arm64/-/oxide-android-arm64-4.2.2.tgz",
            "integrity": "sha512-dXGR1n+P3B6748jZO/SvHZq7qBOqqzQ+yFrXpoOWWALWndF9MoSKAT3Q0fYgAzYzGhxNYOoysRvYlpixRBBoDg==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "android"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-darwin-arm64": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-darwin-arm64/-/oxide-darwin-arm64-4.2.2.tgz",
            "integrity": "sha512-iq9Qjr6knfMpZHj55/37ouZeykwbDqF21gPFtfnhCCKGDcPI/21FKC9XdMO/XyBM7qKORx6UIhGgg6jLl7BZlg==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-darwin-x64": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-darwin-x64/-/oxide-darwin-x64-4.2.2.tgz",
            "integrity": "sha512-BlR+2c3nzc8f2G639LpL89YY4bdcIdUmiOOkv2GQv4/4M0vJlpXEa0JXNHhCHU7VWOKWT/CjqHdTP8aUuDJkuw==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-freebsd-x64": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-freebsd-x64/-/oxide-freebsd-x64-4.2.2.tgz",
            "integrity": "sha512-YUqUgrGMSu2CDO82hzlQ5qSb5xmx3RUrke/QgnoEx7KvmRJHQuZHZmZTLSuuHwFf0DJPybFMXMYf+WJdxHy/nQ==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "freebsd"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-linux-arm-gnueabihf": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm-gnueabihf/-/oxide-linux-arm-gnueabihf-4.2.2.tgz",
            "integrity": "sha512-FPdhvsW6g06T9BWT0qTwiVZYE2WIFo2dY5aCSpjG/S/u1tby+wXoslXS0kl3/KXnULlLr1E3NPRRw0g7t2kgaQ==",
            "cpu": [
                "arm"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-linux-arm64-gnu": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm64-gnu/-/oxide-linux-arm64-gnu-4.2.2.tgz",
            "integrity": "sha512-4og1V+ftEPXGttOO7eCmW7VICmzzJWgMx+QXAJRAhjrSjumCwWqMfkDrNu1LXEQzNAwz28NCUpucgQPrR4S2yw==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-linux-arm64-musl": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-arm64-musl/-/oxide-linux-arm64-musl-4.2.2.tgz",
            "integrity": "sha512-oCfG/mS+/+XRlwNjnsNLVwnMWYH7tn/kYPsNPh+JSOMlnt93mYNCKHYzylRhI51X+TbR+ufNhhKKzm6QkqX8ag==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-linux-x64-gnu": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-x64-gnu/-/oxide-linux-x64-gnu-4.2.2.tgz",
            "integrity": "sha512-rTAGAkDgqbXHNp/xW0iugLVmX62wOp2PoE39BTCGKjv3Iocf6AFbRP/wZT/kuCxC9QBh9Pu8XPkv/zCZB2mcMg==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-linux-x64-musl": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-linux-x64-musl/-/oxide-linux-x64-musl-4.2.2.tgz",
            "integrity": "sha512-XW3t3qwbIwiSyRCggeO2zxe3KWaEbM0/kW9e8+0XpBgyKU4ATYzcVSMKteZJ1iukJ3HgHBjbg9P5YPRCVUxlnQ==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-wasm32-wasi": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-wasm32-wasi/-/oxide-wasm32-wasi-4.2.2.tgz",
            "integrity": "sha512-eKSztKsmEsn1O5lJ4ZAfyn41NfG7vzCg496YiGtMDV86jz1q/irhms5O0VrY6ZwTUkFy/EKG3RfWgxSI3VbZ8Q==",
            "bundleDependencies": [
                "@napi-rs/wasm-runtime",
                "@emnapi/core",
                "@emnapi/runtime",
                "@tybys/wasm-util",
                "@emnapi/wasi-threads",
                "tslib"
            ],
            "cpu": [
                "wasm32"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "dependencies": {
                "@emnapi/core": "^1.8.1",
                "@emnapi/runtime": "^1.8.1",
                "@emnapi/wasi-threads": "^1.1.0",
                "@napi-rs/wasm-runtime": "^1.1.1",
                "@tybys/wasm-util": "^0.10.1",
                "tslib": "^2.8.1"
            },
            "engines": {
                "node": ">=14.0.0"
            }
        },
        "node_modules/@tailwindcss/oxide-win32-arm64-msvc": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-win32-arm64-msvc/-/oxide-win32-arm64-msvc-4.2.2.tgz",
            "integrity": "sha512-qPmaQM4iKu5mxpsrWZMOZRgZv1tOZpUm+zdhhQP0VhJfyGGO3aUKdbh3gDZc/dPLQwW4eSqWGrrcWNBZWUWaXQ==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/oxide-win32-x64-msvc": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/oxide-win32-x64-msvc/-/oxide-win32-x64-msvc-4.2.2.tgz",
            "integrity": "sha512-1T/37VvI7WyH66b+vqHj/cLwnCxt7Qt3WFu5Q8hk65aOvlwAhs7rAp1VkulBJw/N4tMirXjVnylTR72uI0HGcA==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">= 20"
            }
        },
        "node_modules/@tailwindcss/postcss": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/@tailwindcss/postcss/-/postcss-4.2.2.tgz",
            "integrity": "sha512-n4goKQbW8RVXIbNKRB/45LzyUqN451deQK0nzIeauVEqjlI49slUlgKYJM2QyUzap/PcpnS7kzSUmPb1sCRvYQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@alloc/quick-lru": "^5.2.0",
                "@tailwindcss/node": "4.2.2",
                "@tailwindcss/oxide": "4.2.2",
                "postcss": "^8.5.6",
                "tailwindcss": "4.2.2"
            }
        },
        "node_modules/@types/babel__core": {
            "version": "7.20.5",
            "resolved": "https://registry.npmjs.org/@types/babel__core/-/babel__core-7.20.5.tgz",
            "integrity": "sha512-qoQprZvz5wQFJwMDqeseRXWv3rqMvhgpbXFfVyWhbx9X47POIA6i/+dXefEmZKoAgOaTdaIgNSMqMIU61yRyzA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/parser": "^7.20.7",
                "@babel/types": "^7.20.7",
                "@types/babel__generator": "*",
                "@types/babel__template": "*",
                "@types/babel__traverse": "*"
            }
        },
        "node_modules/@types/babel__generator": {
            "version": "7.27.0",
            "resolved": "https://registry.npmjs.org/@types/babel__generator/-/babel__generator-7.27.0.tgz",
            "integrity": "sha512-ufFd2Xi92OAVPYsy+P4n7/U7e68fex0+Ee8gSG9KX7eo084CWiQ4sdxktvdl0bOPupXtVJPY19zk6EwWqUQ8lg==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/types": "^7.0.0"
            }
        },
        "node_modules/@types/babel__template": {
            "version": "7.4.4",
            "resolved": "https://registry.npmjs.org/@types/babel__template/-/babel__template-7.4.4.tgz",
            "integrity": "sha512-h/NUaSyG5EyxBIp8YRxo4RMe2/qQgvyowRwVMzhYhBCONbW8PUsg4lkFMrhgZhUe5z3L3MiLDuvyJ/CaPa2A8A==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/parser": "^7.1.0",
                "@babel/types": "^7.0.0"
            }
        },
        "node_modules/@types/babel__traverse": {
            "version": "7.28.0",
            "resolved": "https://registry.npmjs.org/@types/babel__traverse/-/babel__traverse-7.28.0.tgz",
            "integrity": "sha512-8PvcXf70gTDZBgt9ptxJ8elBeBjcLOAcOtoO/mPJjtji1+CdGbHgm77om1GrsPxsiE+uXIpNSK64UYaIwQXd4Q==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/types": "^7.28.2"
            }
        },
        "node_modules/@types/estree": {
            "version": "1.0.8",
            "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.8.tgz",
            "integrity": "sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/@types/node": {
            "version": "25.5.0",
            "resolved": "https://registry.npmjs.org/@types/node/-/node-25.5.0.tgz",
            "integrity": "sha512-jp2P3tQMSxWugkCUKLRPVUpGaL5MVFwF8RDuSRztfwgN1wmqJeMSbKlnEtQqU8UrhTmzEmZdu2I6v2dpp7XIxw==",
            "license": "MIT",
            "dependencies": {
                "undici-types": "~7.18.0"
            }
        },
        "node_modules/@vitejs/plugin-react": {
            "version": "4.7.0",
            "resolved": "https://registry.npmjs.org/@vitejs/plugin-react/-/plugin-react-4.7.0.tgz",
            "integrity": "sha512-gUu9hwfWvvEDBBmgtAowQCojwZmJ5mcLn3aufeCsitijs3+f2NsrPtlAWIR6OPiqljl96GVCUbLe0HyqIpVaoA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@babel/core": "^7.28.0",
                "@babel/plugin-transform-react-jsx-self": "^7.27.1",
                "@babel/plugin-transform-react-jsx-source": "^7.27.1",
                "@rolldown/pluginutils": "1.0.0-beta.27",
                "@types/babel__core": "^7.20.5",
                "react-refresh": "^0.17.0"
            },
            "engines": {
                "node": "^14.18.0 || >=16.0.0"
            },
            "peerDependencies": {
                "vite": "^4.2.0 || ^5.0.0 || ^6.0.0 || ^7.0.0"
            }
        },
        "node_modules/ansi-regex": {
            "version": "5.0.1",
            "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
            "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
            "license": "MIT",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/ansi-styles": {
            "version": "4.3.0",
            "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
            "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
            "license": "MIT",
            "dependencies": {
                "color-convert": "^2.0.1"
            },
            "engines": {
                "node": ">=8"
            },
            "funding": {
                "url": "https://github.com/chalk/ansi-styles?sponsor=1"
            }
        },
        "node_modules/autoprefixer": {
            "version": "10.4.27",
            "resolved": "https://registry.npmjs.org/autoprefixer/-/autoprefixer-10.4.27.tgz",
            "integrity": "sha512-NP9APE+tO+LuJGn7/9+cohklunJsXWiaWEfV3si4Gi/XHDwVNgkwr1J3RQYFIvPy76GmJ9/bW8vyoU1LcxwKHA==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/postcss/"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/autoprefixer"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "browserslist": "^4.28.1",
                "caniuse-lite": "^1.0.30001774",
                "fraction.js": "^5.3.4",
                "picocolors": "^1.1.1",
                "postcss-value-parser": "^4.2.0"
            },
            "bin": {
                "autoprefixer": "bin/autoprefixer"
            },
            "engines": {
                "node": "^10 || ^12 || >=14"
            },
            "peerDependencies": {
                "postcss": "^8.1.0"
            }
        },
        "node_modules/baseline-browser-mapping": {
            "version": "2.10.12",
            "resolved": "https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.10.12.tgz",
            "integrity": "sha512-qyq26DxfY4awP2gIRXhhLWfwzwI+N5Nxk6iQi8EFizIaWIjqicQTE4sLnZZVdeKPRcVNoJOkkpfzoIYuvCKaIQ==",
            "dev": true,
            "license": "Apache-2.0",
            "bin": {
                "baseline-browser-mapping": "dist/cli.cjs"
            },
            "engines": {
                "node": ">=6.0.0"
            }
        },
        "node_modules/browserslist": {
            "version": "4.28.1",
            "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.28.1.tgz",
            "integrity": "sha512-ZC5Bd0LgJXgwGqUknZY/vkUQ04r8NXnJZ3yYi4vDmSiZmC/pdSN0NbNRPxZpbtO4uAfDUAFffO8IZoM3Gj8IkA==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/browserslist"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/browserslist"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "baseline-browser-mapping": "^2.9.0",
                "caniuse-lite": "^1.0.30001759",
                "electron-to-chromium": "^1.5.263",
                "node-releases": "^2.0.27",
                "update-browserslist-db": "^1.2.0"
            },
            "bin": {
                "browserslist": "cli.js"
            },
            "engines": {
                "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
            }
        },
        "node_modules/caniuse-lite": {
            "version": "1.0.30001781",
            "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001781.tgz",
            "integrity": "sha512-RdwNCyMsNBftLjW6w01z8bKEvT6e/5tpPVEgtn22TiLGlstHOVecsX2KHFkD5e/vRnIE4EGzpuIODb3mtswtkw==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/browserslist"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "CC-BY-4.0"
        },
        "node_modules/cliui": {
            "version": "8.0.1",
            "resolved": "https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz",
            "integrity": "sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ==",
            "license": "ISC",
            "dependencies": {
                "string-width": "^4.2.0",
                "strip-ansi": "^6.0.1",
                "wrap-ansi": "^7.0.0"
            },
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/color-convert": {
            "version": "2.0.1",
            "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
            "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
            "license": "MIT",
            "dependencies": {
                "color-name": "~1.1.4"
            },
            "engines": {
                "node": ">=7.0.0"
            }
        },
        "node_modules/color-name": {
            "version": "1.1.4",
            "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
            "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
            "license": "MIT"
        },
        "node_modules/convert-source-map": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-2.0.0.tgz",
            "integrity": "sha512-Kvp459HrV2FEJ1CAsi1Ku+MY3kasH19TFykTz2xWmMeq6bk2NU3XXvfJ+Q61m0xktWwt+1HSYf3JZsTms3aRJg==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/cookie": {
            "version": "1.1.1",
            "resolved": "https://registry.npmjs.org/cookie/-/cookie-1.1.1.tgz",
            "integrity": "sha512-ei8Aos7ja0weRpFzJnEA9UHJ/7XQmqglbRwnf2ATjcB9Wq874VKH9kfjjirM6UhU2/E5fFYadylyhFldcqSidQ==",
            "license": "MIT",
            "engines": {
                "node": ">=18"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/express"
            }
        },
        "node_modules/debug": {
            "version": "4.4.3",
            "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
            "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ms": "^2.1.3"
            },
            "engines": {
                "node": ">=6.0"
            },
            "peerDependenciesMeta": {
                "supports-color": {
                    "optional": true
                }
            }
        },
        "node_modules/detect-libc": {
            "version": "2.1.2",
            "resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.2.tgz",
            "integrity": "sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==",
            "dev": true,
            "license": "Apache-2.0",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/electron-to-chromium": {
            "version": "1.5.328",
            "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.328.tgz",
            "integrity": "sha512-QNQ5l45DzYytThO21403XN3FvK0hOkWDG8viNf6jqS42msJ8I4tGDSpBCgvDRRPnkffafiwAym2X2eHeGD2V0w==",
            "dev": true,
            "license": "ISC"
        },
        "node_modules/emoji-regex": {
            "version": "8.0.0",
            "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
            "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
            "license": "MIT"
        },
        "node_modules/enhanced-resolve": {
            "version": "5.20.1",
            "resolved": "https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-5.20.1.tgz",
            "integrity": "sha512-Qohcme7V1inbAfvjItgw0EaxVX5q2rdVEZHRBrEQdRZTssLDGsL8Lwrznl8oQ/6kuTJONLaDcGjkNP247XEhcA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "graceful-fs": "^4.2.4",
                "tapable": "^2.3.0"
            },
            "engines": {
                "node": ">=10.13.0"
            }
        },
        "node_modules/esbuild": {
            "version": "0.21.5",
            "resolved": "https://registry.npmjs.org/esbuild/-/esbuild-0.21.5.tgz",
            "integrity": "sha512-mg3OPMV4hXywwpoDxu3Qda5xCKQi+vCTZq8S9J/EpkhB2HzKXq4SNFZE3+NK93JYxc8VMSep+lOUSC/RVKaBqw==",
            "dev": true,
            "hasInstallScript": true,
            "license": "MIT",
            "bin": {
                "esbuild": "bin/esbuild"
            },
            "engines": {
                "node": ">=12"
            },
            "optionalDependencies": {
                "@esbuild/aix-ppc64": "0.21.5",
                "@esbuild/android-arm": "0.21.5",
                "@esbuild/android-arm64": "0.21.5",
                "@esbuild/android-x64": "0.21.5",
                "@esbuild/darwin-arm64": "0.21.5",
                "@esbuild/darwin-x64": "0.21.5",
                "@esbuild/freebsd-arm64": "0.21.5",
                "@esbuild/freebsd-x64": "0.21.5",
                "@esbuild/linux-arm": "0.21.5",
                "@esbuild/linux-arm64": "0.21.5",
                "@esbuild/linux-ia32": "0.21.5",
                "@esbuild/linux-loong64": "0.21.5",
                "@esbuild/linux-mips64el": "0.21.5",
                "@esbuild/linux-ppc64": "0.21.5",
                "@esbuild/linux-riscv64": "0.21.5",
                "@esbuild/linux-s390x": "0.21.5",
                "@esbuild/linux-x64": "0.21.5",
                "@esbuild/netbsd-x64": "0.21.5",
                "@esbuild/openbsd-x64": "0.21.5",
                "@esbuild/sunos-x64": "0.21.5",
                "@esbuild/win32-arm64": "0.21.5",
                "@esbuild/win32-ia32": "0.21.5",
                "@esbuild/win32-x64": "0.21.5"
            }
        },
        "node_modules/escalade": {
            "version": "3.2.0",
            "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
            "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
            "license": "MIT",
            "engines": {
                "node": ">=6"
            }
        },
        "node_modules/faye-websocket": {
            "version": "0.11.4",
            "resolved": "https://registry.npmjs.org/faye-websocket/-/faye-websocket-0.11.4.tgz",
            "integrity": "sha512-CzbClwlXAuiRQAlUyfqPgvPoNKTckTPGfwZV4ZdAhVcP2lh9KUxJg2b5GkE7XbjKQ3YJnQ9z6D9ntLAlB+tP8g==",
            "license": "Apache-2.0",
            "dependencies": {
                "websocket-driver": ">=0.5.1"
            },
            "engines": {
                "node": ">=0.8.0"
            }
        },
        "node_modules/firebase": {
            "version": "12.11.0",
            "resolved": "https://registry.npmjs.org/firebase/-/firebase-12.11.0.tgz",
            "integrity": "sha512-W9f3Y+cgQYgF9gvCGxt0upec8zwAtiQVcHuU8MfzUIgVU/9fRQWtu48Geiv1lsigtBz9QHML++Km9xAKO5GB5Q==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/ai": "2.10.0",
                "@firebase/analytics": "0.10.21",
                "@firebase/analytics-compat": "0.2.27",
                "@firebase/app": "0.14.10",
                "@firebase/app-check": "0.11.2",
                "@firebase/app-check-compat": "0.4.2",
                "@firebase/app-compat": "0.5.10",
                "@firebase/app-types": "0.9.3",
                "@firebase/auth": "1.12.2",
                "@firebase/auth-compat": "0.6.4",
                "@firebase/data-connect": "0.5.0",
                "@firebase/database": "1.1.2",
                "@firebase/database-compat": "2.1.2",
                "@firebase/firestore": "4.13.0",
                "@firebase/firestore-compat": "0.4.7",
                "@firebase/functions": "0.13.3",
                "@firebase/functions-compat": "0.4.3",
                "@firebase/installations": "0.6.21",
                "@firebase/installations-compat": "0.2.21",
                "@firebase/messaging": "0.12.25",
                "@firebase/messaging-compat": "0.2.25",
                "@firebase/performance": "0.7.11",
                "@firebase/performance-compat": "0.2.24",
                "@firebase/remote-config": "0.8.2",
                "@firebase/remote-config-compat": "0.2.23",
                "@firebase/storage": "0.14.2",
                "@firebase/storage-compat": "0.4.2",
                "@firebase/util": "1.15.0"
            }
        },
        "node_modules/firebase/node_modules/@firebase/auth": {
            "version": "1.12.2",
            "resolved": "https://registry.npmjs.org/@firebase/auth/-/auth-1.12.2.tgz",
            "integrity": "sha512-CZJL8V10Vzibs+pDTXdQF+hot1IigIoqF4a4lA/qr5Deo1srcefiyIfgg28B67Lk7IxZhwfJMuI+1bu2xBmV0A==",
            "license": "Apache-2.0",
            "dependencies": {
                "@firebase/component": "0.7.2",
                "@firebase/logger": "0.5.0",
                "@firebase/util": "1.15.0",
                "tslib": "^2.1.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "@firebase/app": "0.x",
                "@react-native-async-storage/async-storage": "^2.2.0"
            },
            "peerDependenciesMeta": {
                "@react-native-async-storage/async-storage": {
                    "optional": true
                }
            }
        },
        "node_modules/fraction.js": {
            "version": "5.3.4",
            "resolved": "https://registry.npmjs.org/fraction.js/-/fraction.js-5.3.4.tgz",
            "integrity": "sha512-1X1NTtiJphryn/uLQz3whtY6jK3fTqoE3ohKs0tT+Ujr1W59oopxmoEh7Lu5p6vBaPbgoM0bzveAW4Qi5RyWDQ==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": "*"
            },
            "funding": {
                "type": "github",
                "url": "https://github.com/sponsors/rawify"
            }
        },
        "node_modules/framer-motion": {
            "version": "12.38.0",
            "resolved": "https://registry.npmjs.org/framer-motion/-/framer-motion-12.38.0.tgz",
            "integrity": "sha512-rFYkY/pigbcswl1XQSb7q424kSTQ8q6eAC+YUsSKooHQYuLdzdHjrt6uxUC+PRAO++q5IS7+TamgIw1AphxR+g==",
            "license": "MIT",
            "dependencies": {
                "motion-dom": "^12.38.0",
                "motion-utils": "^12.36.0",
                "tslib": "^2.4.0"
            },
            "peerDependencies": {
                "@emotion/is-prop-valid": "*",
                "react": "^18.0.0 || ^19.0.0",
                "react-dom": "^18.0.0 || ^19.0.0"
            },
            "peerDependenciesMeta": {
                "@emotion/is-prop-valid": {
                    "optional": true
                },
                "react": {
                    "optional": true
                },
                "react-dom": {
                    "optional": true
                }
            }
        },
        "node_modules/fsevents": {
            "version": "2.3.3",
            "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
            "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
            "dev": true,
            "hasInstallScript": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
            }
        },
        "node_modules/gensync": {
            "version": "1.0.0-beta.2",
            "resolved": "https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz",
            "integrity": "sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/get-caller-file": {
            "version": "2.0.5",
            "resolved": "https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz",
            "integrity": "sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==",
            "license": "ISC",
            "engines": {
                "node": "6.* || 8.* || >= 10.*"
            }
        },
        "node_modules/graceful-fs": {
            "version": "4.2.11",
            "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz",
            "integrity": "sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==",
            "dev": true,
            "license": "ISC"
        },
        "node_modules/gsap": {
            "version": "3.14.2",
            "resolved": "https://registry.npmjs.org/gsap/-/gsap-3.14.2.tgz",
            "integrity": "sha512-P8/mMxVLU7o4+55+1TCnQrPmgjPKnwkzkXOK1asnR9Jg2lna4tEY5qBJjMmAaOBDDZWtlRjBXjLa0w53G/uBLA==",
            "license": "Standard 'no charge' license: https://gsap.com/standard-license."
        },
        "node_modules/http-parser-js": {
            "version": "0.5.10",
            "resolved": "https://registry.npmjs.org/http-parser-js/-/http-parser-js-0.5.10.tgz",
            "integrity": "sha512-Pysuw9XpUq5dVc/2SMHpuTY01RFl8fttgcyunjL7eEMhGM3cI4eOmiCycJDVCo/7O7ClfQD3SaI6ftDzqOXYMA==",
            "license": "MIT"
        },
        "node_modules/idb": {
            "version": "7.1.1",
            "resolved": "https://registry.npmjs.org/idb/-/idb-7.1.1.tgz",
            "integrity": "sha512-gchesWBzyvGHRO9W8tzUWFDycow5gwjvFKfyV9FF32Y7F50yZMp7mP+T2mJIWFx49zicqyC4uefHM17o6xKIVQ==",
            "license": "ISC"
        },
        "node_modules/is-fullwidth-code-point": {
            "version": "3.0.0",
            "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
            "integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
            "license": "MIT",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/jiti": {
            "version": "2.6.1",
            "resolved": "https://registry.npmjs.org/jiti/-/jiti-2.6.1.tgz",
            "integrity": "sha512-ekilCSN1jwRvIbgeg/57YFh8qQDNbwDb9xT/qu2DAHbFFZUicIl4ygVaAvzveMhMVr3LnpSKTNnwt8PoOfmKhQ==",
            "dev": true,
            "license": "MIT",
            "bin": {
                "jiti": "lib/jiti-cli.mjs"
            }
        },
        "node_modules/js-tokens": {
            "version": "4.0.0",
            "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
            "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
            "license": "MIT"
        },
        "node_modules/jsesc": {
            "version": "3.1.0",
            "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz",
            "integrity": "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA==",
            "dev": true,
            "license": "MIT",
            "bin": {
                "jsesc": "bin/jsesc"
            },
            "engines": {
                "node": ">=6"
            }
        },
        "node_modules/json5": {
            "version": "2.2.3",
            "resolved": "https://registry.npmjs.org/json5/-/json5-2.2.3.tgz",
            "integrity": "sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg==",
            "dev": true,
            "license": "MIT",
            "bin": {
                "json5": "lib/cli.js"
            },
            "engines": {
                "node": ">=6"
            }
        },
        "node_modules/lenis": {
            "version": "1.3.21",
            "resolved": "https://registry.npmjs.org/lenis/-/lenis-1.3.21.tgz",
            "integrity": "sha512-RXWTYm7KQE4Kv8ezxL6wvK0Oiv7aRr6FDo+eNaaniTeu7pLdHokqMIJ5CXO4x5ezvd+9ONdpSFkprLpXsVWmEw==",
            "license": "MIT",
            "workspaces": [
                "packages/*",
                "playground",
                "playground/*"
            ],
            "funding": {
                "type": "github",
                "url": "https://github.com/sponsors/darkroomengineering"
            },
            "peerDependencies": {
                "@nuxt/kit": ">=3.0.0",
                "react": ">=17.0.0",
                "vue": ">=3.0.0"
            },
            "peerDependenciesMeta": {
                "@nuxt/kit": {
                    "optional": true
                },
                "react": {
                    "optional": true
                },
                "vue": {
                    "optional": true
                }
            }
        },
        "node_modules/lightningcss": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss/-/lightningcss-1.32.0.tgz",
            "integrity": "sha512-NXYBzinNrblfraPGyrbPoD19C1h9lfI/1mzgWYvXUTe414Gz/X1FD2XBZSZM7rRTrMA8JL3OtAaGifrIKhQ5yQ==",
            "dev": true,
            "license": "MPL-2.0",
            "dependencies": {
                "detect-libc": "^2.0.3"
            },
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            },
            "optionalDependencies": {
                "lightningcss-android-arm64": "1.32.0",
                "lightningcss-darwin-arm64": "1.32.0",
                "lightningcss-darwin-x64": "1.32.0",
                "lightningcss-freebsd-x64": "1.32.0",
                "lightningcss-linux-arm-gnueabihf": "1.32.0",
                "lightningcss-linux-arm64-gnu": "1.32.0",
                "lightningcss-linux-arm64-musl": "1.32.0",
                "lightningcss-linux-x64-gnu": "1.32.0",
                "lightningcss-linux-x64-musl": "1.32.0",
                "lightningcss-win32-arm64-msvc": "1.32.0",
                "lightningcss-win32-x64-msvc": "1.32.0"
            }
        },
        "node_modules/lightningcss-android-arm64": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-android-arm64/-/lightningcss-android-arm64-1.32.0.tgz",
            "integrity": "sha512-YK7/ClTt4kAK0vo6w3X+Pnm0D2cf2vPHbhOXdoNti1Ga0al1P4TBZhwjATvjNwLEBCnKvjJc2jQgHXH0NEwlAg==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "android"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-darwin-arm64": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-darwin-arm64/-/lightningcss-darwin-arm64-1.32.0.tgz",
            "integrity": "sha512-RzeG9Ju5bag2Bv1/lwlVJvBE3q6TtXskdZLLCyfg5pt+HLz9BqlICO7LZM7VHNTTn/5PRhHFBSjk5lc4cmscPQ==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-darwin-x64": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-darwin-x64/-/lightningcss-darwin-x64-1.32.0.tgz",
            "integrity": "sha512-U+QsBp2m/s2wqpUYT/6wnlagdZbtZdndSmut/NJqlCcMLTWp5muCrID+K5UJ6jqD2BFshejCYXniPDbNh73V8w==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-freebsd-x64": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-freebsd-x64/-/lightningcss-freebsd-x64-1.32.0.tgz",
            "integrity": "sha512-JCTigedEksZk3tHTTthnMdVfGf61Fky8Ji2E4YjUTEQX14xiy/lTzXnu1vwiZe3bYe0q+SpsSH/CTeDXK6WHig==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "freebsd"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-linux-arm-gnueabihf": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-linux-arm-gnueabihf/-/lightningcss-linux-arm-gnueabihf-1.32.0.tgz",
            "integrity": "sha512-x6rnnpRa2GL0zQOkt6rts3YDPzduLpWvwAF6EMhXFVZXD4tPrBkEFqzGowzCsIWsPjqSK+tyNEODUBXeeVHSkw==",
            "cpu": [
                "arm"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-linux-arm64-gnu": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-gnu/-/lightningcss-linux-arm64-gnu-1.32.0.tgz",
            "integrity": "sha512-0nnMyoyOLRJXfbMOilaSRcLH3Jw5z9HDNGfT/gwCPgaDjnx0i8w7vBzFLFR1f6CMLKF8gVbebmkUN3fa/kQJpQ==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-linux-arm64-musl": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-musl/-/lightningcss-linux-arm64-musl-1.32.0.tgz",
            "integrity": "sha512-UpQkoenr4UJEzgVIYpI80lDFvRmPVg6oqboNHfoH4CQIfNA+HOrZ7Mo7KZP02dC6LjghPQJeBsvXhJod/wnIBg==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-linux-x64-gnu": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-gnu/-/lightningcss-linux-x64-gnu-1.32.0.tgz",
            "integrity": "sha512-V7Qr52IhZmdKPVr+Vtw8o+WLsQJYCTd8loIfpDaMRWGUZfBOYEJeyJIkqGIDMZPwPx24pUMfwSxxI8phr/MbOA==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-linux-x64-musl": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-musl/-/lightningcss-linux-x64-musl-1.32.0.tgz",
            "integrity": "sha512-bYcLp+Vb0awsiXg/80uCRezCYHNg1/l3mt0gzHnWV9XP1W5sKa5/TCdGWaR/zBM2PeF/HbsQv/j2URNOiVuxWg==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-win32-arm64-msvc": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-win32-arm64-msvc/-/lightningcss-win32-arm64-msvc-1.32.0.tgz",
            "integrity": "sha512-8SbC8BR40pS6baCM8sbtYDSwEVQd4JlFTOlaD3gWGHfThTcABnNDBda6eTZeqbofalIJhFx0qKzgHJmcPTnGdw==",
            "cpu": [
                "arm64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lightningcss-win32-x64-msvc": {
            "version": "1.32.0",
            "resolved": "https://registry.npmjs.org/lightningcss-win32-x64-msvc/-/lightningcss-win32-x64-msvc-1.32.0.tgz",
            "integrity": "sha512-Amq9B/SoZYdDi1kFrojnoqPLxYhQ4Wo5XiL8EVJrVsB8ARoC1PWW6VGtT0WKCemjy8aC+louJnjS7U18x3b06Q==",
            "cpu": [
                "x64"
            ],
            "dev": true,
            "license": "MPL-2.0",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">= 12.0.0"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/parcel"
            }
        },
        "node_modules/lodash.camelcase": {
            "version": "4.3.0",
            "resolved": "https://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-4.3.0.tgz",
            "integrity": "sha512-TwuEnCnxbc3rAvhf/LbG7tJUDzhqXyFnv3dtzLOPgCG/hODL7WFnsbwktkD7yUV0RrreP/l1PALq/YSg6VvjlA==",
            "license": "MIT"
        },
        "node_modules/long": {
            "version": "5.3.2",
            "resolved": "https://registry.npmjs.org/long/-/long-5.3.2.tgz",
            "integrity": "sha512-mNAgZ1GmyNhD7AuqnTG3/VQ26o760+ZYBPKjPvugO8+nLbYfX6TVpJPseBvopbdY+qpZ/lKUnmEc1LeZYS3QAA==",
            "license": "Apache-2.0"
        },
        "node_modules/loose-envify": {
            "version": "1.4.0",
            "resolved": "https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz",
            "integrity": "sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==",
            "license": "MIT",
            "dependencies": {
                "js-tokens": "^3.0.0 || ^4.0.0"
            },
            "bin": {
                "loose-envify": "cli.js"
            }
        },
        "node_modules/lru-cache": {
            "version": "5.1.1",
            "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz",
            "integrity": "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "yallist": "^3.0.2"
            }
        },
        "node_modules/magic-string": {
            "version": "0.30.21",
            "resolved": "https://registry.npmjs.org/magic-string/-/magic-string-0.30.21.tgz",
            "integrity": "sha512-vd2F4YUyEXKGcLHoq+TEyCjxueSeHnFxyyjNp80yg0XV4vUhnDer/lvvlqM/arB5bXQN5K2/3oinyCRyx8T2CQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@jridgewell/sourcemap-codec": "^1.5.5"
            }
        },
        "node_modules/motion": {
            "version": "12.38.0",
            "resolved": "https://registry.npmjs.org/motion/-/motion-12.38.0.tgz",
            "integrity": "sha512-uYfXzeHlgThchzwz5Te47dlv5JOUC7OB4rjJ/7XTUgtBZD8CchMN8qEJ4ZVsUmTyYA44zjV0fBwsiktRuFnn+w==",
            "license": "MIT",
            "dependencies": {
                "framer-motion": "^12.38.0",
                "tslib": "^2.4.0"
            },
            "peerDependencies": {
                "@emotion/is-prop-valid": "*",
                "react": "^18.0.0 || ^19.0.0",
                "react-dom": "^18.0.0 || ^19.0.0"
            },
            "peerDependenciesMeta": {
                "@emotion/is-prop-valid": {
                    "optional": true
                },
                "react": {
                    "optional": true
                },
                "react-dom": {
                    "optional": true
                }
            }
        },
        "node_modules/motion-dom": {
            "version": "12.38.0",
            "resolved": "https://registry.npmjs.org/motion-dom/-/motion-dom-12.38.0.tgz",
            "integrity": "sha512-pdkHLD8QYRp8VfiNLb8xIBJis1byQ9gPT3Jnh2jqfFtAsWUA3dEepDlsWe/xMpO8McV+VdpKVcp+E+TGJEtOoA==",
            "license": "MIT",
            "dependencies": {
                "motion-utils": "^12.36.0"
            }
        },
        "node_modules/motion-utils": {
            "version": "12.36.0",
            "resolved": "https://registry.npmjs.org/motion-utils/-/motion-utils-12.36.0.tgz",
            "integrity": "sha512-eHWisygbiwVvf6PZ1vhaHCLamvkSbPIeAYxWUuL3a2PD/TROgE7FvfHWTIH4vMl798QLfMw15nRqIaRDXTlYRg==",
            "license": "MIT"
        },
        "node_modules/ms": {
            "version": "2.1.3",
            "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
            "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/nanoid": {
            "version": "3.3.11",
            "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.11.tgz",
            "integrity": "sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w==",
            "dev": true,
            "funding": [
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "bin": {
                "nanoid": "bin/nanoid.cjs"
            },
            "engines": {
                "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
            }
        },
        "node_modules/node-releases": {
            "version": "2.0.36",
            "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-2.0.36.tgz",
            "integrity": "sha512-TdC8FSgHz8Mwtw9g5L4gR/Sh9XhSP/0DEkQxfEFXOpiul5IiHgHan2VhYYb6agDSfp4KuvltmGApc8HMgUrIkA==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/ogl": {
            "version": "1.0.11",
            "resolved": "https://registry.npmjs.org/ogl/-/ogl-1.0.11.tgz",
            "integrity": "sha512-kUpC154AFfxi16pmZUK4jk3J+8zxwTWGPo03EoYA8QPbzikHoaC82n6pNTbd+oEaJonaE8aPWBlX7ad9zrqLsA==",
            "license": "Unlicense"
        },
        "node_modules/picocolors": {
            "version": "1.1.1",
            "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
            "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
            "dev": true,
            "license": "ISC"
        },
        "node_modules/postcss": {
            "version": "8.5.8",
            "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.8.tgz",
            "integrity": "sha512-OW/rX8O/jXnm82Ey1k44pObPtdblfiuWnrd8X7GJ7emImCOstunGbXUpp7HdBrFQX6rJzn3sPT397Wp5aCwCHg==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/postcss/"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/postcss"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "nanoid": "^3.3.11",
                "picocolors": "^1.1.1",
                "source-map-js": "^1.2.1"
            },
            "engines": {
                "node": "^10 || ^12 || >=14"
            }
        },
        "node_modules/postcss-value-parser": {
            "version": "4.2.0",
            "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz",
            "integrity": "sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/protobufjs": {
            "version": "7.5.4",
            "resolved": "https://registry.npmjs.org/protobufjs/-/protobufjs-7.5.4.tgz",
            "integrity": "sha512-CvexbZtbov6jW2eXAvLukXjXUW1TzFaivC46BpWc/3BpcCysb5Vffu+B3XHMm8lVEuy2Mm4XGex8hBSg1yapPg==",
            "hasInstallScript": true,
            "license": "BSD-3-Clause",
            "dependencies": {
                "@protobufjs/aspromise": "^1.1.2",
                "@protobufjs/base64": "^1.1.2",
                "@protobufjs/codegen": "^2.0.4",
                "@protobufjs/eventemitter": "^1.1.0",
                "@protobufjs/fetch": "^1.1.0",
                "@protobufjs/float": "^1.0.2",
                "@protobufjs/inquire": "^1.1.0",
                "@protobufjs/path": "^1.1.2",
                "@protobufjs/pool": "^1.1.0",
                "@protobufjs/utf8": "^1.1.0",
                "@types/node": ">=13.7.0",
                "long": "^5.0.0"
            },
            "engines": {
                "node": ">=12.0.0"
            }
        },
        "node_modules/react": {
            "version": "18.3.1",
            "resolved": "https://registry.npmjs.org/react/-/react-18.3.1.tgz",
            "integrity": "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ==",
            "license": "MIT",
            "dependencies": {
                "loose-envify": "^1.1.0"
            },
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/react-dom": {
            "version": "18.3.1",
            "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz",
            "integrity": "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw==",
            "license": "MIT",
            "dependencies": {
                "loose-envify": "^1.1.0",
                "scheduler": "^0.23.2"
            },
            "peerDependencies": {
                "react": "^18.3.1"
            }
        },
        "node_modules/react-refresh": {
            "version": "0.17.0",
            "resolved": "https://registry.npmjs.org/react-refresh/-/react-refresh-0.17.0.tgz",
            "integrity": "sha512-z6F7K9bV85EfseRCp2bzrpyQ0Gkw1uLoCel9XBVWPg/TjRj94SkJzUTGfOa4bs7iJvBWtQG0Wq7wnI0syw3EBQ==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/react-router": {
            "version": "7.13.2",
            "resolved": "https://registry.npmjs.org/react-router/-/react-router-7.13.2.tgz",
            "integrity": "sha512-tX1Aee+ArlKQP+NIUd7SE6Li+CiGKwQtbS+FfRxPX6Pe4vHOo6nr9d++u5cwg+Z8K/x8tP+7qLmujDtfrAoUJA==",
            "license": "MIT",
            "dependencies": {
                "cookie": "^1.0.1",
                "set-cookie-parser": "^2.6.0"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "react": ">=18",
                "react-dom": ">=18"
            },
            "peerDependenciesMeta": {
                "react-dom": {
                    "optional": true
                }
            }
        },
        "node_modules/react-router-dom": {
            "version": "7.13.2",
            "resolved": "https://registry.npmjs.org/react-router-dom/-/react-router-dom-7.13.2.tgz",
            "integrity": "sha512-aR7SUORwTqAW0JDeiWF07e9SBE9qGpByR9I8kJT5h/FrBKxPMS6TiC7rmVO+gC0q52Bx7JnjWe8Z1sR9faN4YA==",
            "license": "MIT",
            "dependencies": {
                "react-router": "7.13.2"
            },
            "engines": {
                "node": ">=20.0.0"
            },
            "peerDependencies": {
                "react": ">=18",
                "react-dom": ">=18"
            }
        },
        "node_modules/require-directory": {
            "version": "2.1.1",
            "resolved": "https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz",
            "integrity": "sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==",
            "license": "MIT",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/rollup": {
            "version": "4.60.0",
            "resolved": "https://registry.npmjs.org/rollup/-/rollup-4.60.0.tgz",
            "integrity": "sha512-yqjxruMGBQJ2gG4HtjZtAfXArHomazDHoFwFFmZZl0r7Pdo7qCIXKqKHZc8yeoMgzJJ+pO6pEEHa+V7uzWlrAQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@types/estree": "1.0.8"
            },
            "bin": {
                "rollup": "dist/bin/rollup"
            },
            "engines": {
                "node": ">=18.0.0",
                "npm": ">=8.0.0"
            },
            "optionalDependencies": {
                "@rollup/rollup-android-arm-eabi": "4.60.0",
                "@rollup/rollup-android-arm64": "4.60.0",
                "@rollup/rollup-darwin-arm64": "4.60.0",
                "@rollup/rollup-darwin-x64": "4.60.0",
                "@rollup/rollup-freebsd-arm64": "4.60.0",
                "@rollup/rollup-freebsd-x64": "4.60.0",
                "@rollup/rollup-linux-arm-gnueabihf": "4.60.0",
                "@rollup/rollup-linux-arm-musleabihf": "4.60.0",
                "@rollup/rollup-linux-arm64-gnu": "4.60.0",
                "@rollup/rollup-linux-arm64-musl": "4.60.0",
                "@rollup/rollup-linux-loong64-gnu": "4.60.0",
                "@rollup/rollup-linux-loong64-musl": "4.60.0",
                "@rollup/rollup-linux-ppc64-gnu": "4.60.0",
                "@rollup/rollup-linux-ppc64-musl": "4.60.0",
                "@rollup/rollup-linux-riscv64-gnu": "4.60.0",
                "@rollup/rollup-linux-riscv64-musl": "4.60.0",
                "@rollup/rollup-linux-s390x-gnu": "4.60.0",
                "@rollup/rollup-linux-x64-gnu": "4.60.0",
                "@rollup/rollup-linux-x64-musl": "4.60.0",
                "@rollup/rollup-openbsd-x64": "4.60.0",
                "@rollup/rollup-openharmony-arm64": "4.60.0",
                "@rollup/rollup-win32-arm64-msvc": "4.60.0",
                "@rollup/rollup-win32-ia32-msvc": "4.60.0",
                "@rollup/rollup-win32-x64-gnu": "4.60.0",
                "@rollup/rollup-win32-x64-msvc": "4.60.0",
                "fsevents": "~2.3.2"
            }
        },
        "node_modules/safe-buffer": {
            "version": "5.2.1",
            "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz",
            "integrity": "sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==",
            "funding": [
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/feross"
                },
                {
                    "type": "patreon",
                    "url": "https://www.patreon.com/feross"
                },
                {
                    "type": "consulting",
                    "url": "https://feross.org/support"
                }
            ],
            "license": "MIT"
        },
        "node_modules/scheduler": {
            "version": "0.23.2",
            "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.23.2.tgz",
            "integrity": "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ==",
            "license": "MIT",
            "dependencies": {
                "loose-envify": "^1.1.0"
            }
        },
        "node_modules/semver": {
            "version": "6.3.1",
            "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.1.tgz",
            "integrity": "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA==",
            "dev": true,
            "license": "ISC",
            "bin": {
                "semver": "bin/semver.js"
            }
        },
        "node_modules/set-cookie-parser": {
            "version": "2.7.2",
            "resolved": "https://registry.npmjs.org/set-cookie-parser/-/set-cookie-parser-2.7.2.tgz",
            "integrity": "sha512-oeM1lpU/UvhTxw+g3cIfxXHyJRc/uidd3yK1P242gzHds0udQBYzs3y8j4gCCW+ZJ7ad0yctld8RYO+bdurlvw==",
            "license": "MIT"
        },
        "node_modules/source-map-js": {
            "version": "1.2.1",
            "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
            "integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
            "dev": true,
            "license": "BSD-3-Clause",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/string-width": {
            "version": "4.2.3",
            "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
            "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
            "license": "MIT",
            "dependencies": {
                "emoji-regex": "^8.0.0",
                "is-fullwidth-code-point": "^3.0.0",
                "strip-ansi": "^6.0.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/strip-ansi": {
            "version": "6.0.1",
            "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
            "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
            "license": "MIT",
            "dependencies": {
                "ansi-regex": "^5.0.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/tailwindcss": {
            "version": "4.2.2",
            "resolved": "https://registry.npmjs.org/tailwindcss/-/tailwindcss-4.2.2.tgz",
            "integrity": "sha512-KWBIxs1Xb6NoLdMVqhbhgwZf2PGBpPEiwOqgI4pFIYbNTfBXiKYyWoTsXgBQ9WFg/OlhnvHaY+AEpW7wSmFo2Q==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/tapable": {
            "version": "2.3.2",
            "resolved": "https://registry.npmjs.org/tapable/-/tapable-2.3.2.tgz",
            "integrity": "sha512-1MOpMXuhGzGL5TTCZFItxCc0AARf1EZFQkGqMm7ERKj8+Hgr5oLvJOVFcC+lRmR8hCe2S3jC4T5D7Vg/d7/fhA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/webpack"
            }
        },
        "node_modules/three": {
            "version": "0.183.2",
            "resolved": "https://registry.npmjs.org/three/-/three-0.183.2.tgz",
            "integrity": "sha512-di3BsL2FEQ1PA7Hcvn4fyJOlxRRgFYBpMTcyOgkwJIaDOdJMebEFPA+t98EvjuljDx4hNulAGwF6KIjtwI5jgQ==",
            "license": "MIT"
        },
        "node_modules/tslib": {
            "version": "2.8.1",
            "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
            "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
            "license": "0BSD"
        },
        "node_modules/undici-types": {
            "version": "7.18.2",
            "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-7.18.2.tgz",
            "integrity": "sha512-AsuCzffGHJybSaRrmr5eHr81mwJU3kjw6M+uprWvCXiNeN9SOGwQ3Jn8jb8m3Z6izVgknn1R0FTCEAP2QrLY/w==",
            "license": "MIT"
        },
        "node_modules/update-browserslist-db": {
            "version": "1.2.3",
            "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.2.3.tgz",
            "integrity": "sha512-Js0m9cx+qOgDxo0eMiFGEueWztz+d4+M3rGlmKPT+T4IS/jP4ylw3Nwpu6cpTTP8R1MAC1kF4VbdLt3ARf209w==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/browserslist"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/browserslist"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "escalade": "^3.2.0",
                "picocolors": "^1.1.1"
            },
            "bin": {
                "update-browserslist-db": "cli.js"
            },
            "peerDependencies": {
                "browserslist": ">= 4.21.0"
            }
        },
        "node_modules/vite": {
            "version": "5.4.21",
            "resolved": "https://registry.npmjs.org/vite/-/vite-5.4.21.tgz",
            "integrity": "sha512-o5a9xKjbtuhY6Bi5S3+HvbRERmouabWbyUcpXXUA1u+GNUKoROi9byOJ8M0nHbHYHkYICiMlqxkg1KkYmm25Sw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "esbuild": "^0.21.3",
                "postcss": "^8.4.43",
                "rollup": "^4.20.0"
            },
            "bin": {
                "vite": "bin/vite.js"
            },
            "engines": {
                "node": "^18.0.0 || >=20.0.0"
            },
            "funding": {
                "url": "https://github.com/vitejs/vite?sponsor=1"
            },
            "optionalDependencies": {
                "fsevents": "~2.3.3"
            },
            "peerDependencies": {
                "@types/node": "^18.0.0 || >=20.0.0",
                "less": "*",
                "lightningcss": "^1.21.0",
                "sass": "*",
                "sass-embedded": "*",
                "stylus": "*",
                "sugarss": "*",
                "terser": "^5.4.0"
            },
            "peerDependenciesMeta": {
                "@types/node": {
                    "optional": true
                },
                "less": {
                    "optional": true
                },
                "lightningcss": {
                    "optional": true
                },
                "sass": {
                    "optional": true
                },
                "sass-embedded": {
                    "optional": true
                },
                "stylus": {
                    "optional": true
                },
                "sugarss": {
                    "optional": true
                },
                "terser": {
                    "optional": true
                }
            }
        },
        "node_modules/web-vitals": {
            "version": "4.2.4",
            "resolved": "https://registry.npmjs.org/web-vitals/-/web-vitals-4.2.4.tgz",
            "integrity": "sha512-r4DIlprAGwJ7YM11VZp4R884m0Vmgr6EAKe3P+kO0PPj3Unqyvv59rczf6UiGcb9Z8QxZVcqKNwv/g0WNdWwsw==",
            "license": "Apache-2.0"
        },
        "node_modules/websocket-driver": {
            "version": "0.7.4",
            "resolved": "https://registry.npmjs.org/websocket-driver/-/websocket-driver-0.7.4.tgz",
            "integrity": "sha512-b17KeDIQVjvb0ssuSDF2cYXSg2iztliJ4B9WdsuB6J952qCPKmnVq4DyW5motImXHDC1cBT/1UezrJVsKw5zjg==",
            "license": "Apache-2.0",
            "dependencies": {
                "http-parser-js": ">=0.5.1",
                "safe-buffer": ">=5.1.0",
                "websocket-extensions": ">=0.1.1"
            },
            "engines": {
                "node": ">=0.8.0"
            }
        },
        "node_modules/websocket-extensions": {
            "version": "0.1.4",
            "resolved": "https://registry.npmjs.org/websocket-extensions/-/websocket-extensions-0.1.4.tgz",
            "integrity": "sha512-OqedPIGOfsDlo31UNwYbCFMSaO9m9G/0faIHj5/dZFDMFqPTcx6UwqyOy3COEaEOg/9VsGIpdqn62W5KhoKSpg==",
            "license": "Apache-2.0",
            "engines": {
                "node": ">=0.8.0"
            }
        },
        "node_modules/wrap-ansi": {
            "version": "7.0.0",
            "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
            "integrity": "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==",
            "license": "MIT",
            "dependencies": {
                "ansi-styles": "^4.0.0",
                "string-width": "^4.1.0",
                "strip-ansi": "^6.0.0"
            },
            "engines": {
                "node": ">=10"
            },
            "funding": {
                "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
            }
        },
        "node_modules/y18n": {
            "version": "5.0.8",
            "resolved": "https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz",
            "integrity": "sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA==",
            "license": "ISC",
            "engines": {
                "node": ">=10"
            }
        },
        "node_modules/yallist": {
            "version": "3.1.1",
            "resolved": "https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz",
            "integrity": "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g==",
            "dev": true,
            "license": "ISC"
        },
        "node_modules/yargs": {
            "version": "17.7.2",
            "resolved": "https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz",
            "integrity": "sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w==",
            "license": "MIT",
            "dependencies": {
                "cliui": "^8.0.1",
                "escalade": "^3.1.1",
                "get-caller-file": "^2.0.5",
                "require-directory": "^2.1.1",
                "string-width": "^4.2.3",
                "y18n": "^5.0.5",
                "yargs-parser": "^21.1.1"
            },
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/yargs-parser": {
            "version": "21.1.1",
            "resolved": "https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz",
            "integrity": "sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw==",
            "license": "ISC",
            "engines": {
                "node": ">=12"
            }
        }
    }
}

```

---

## [43] frontend/package.json
**Size:** 781.0B

```json
{
    "name": "githopperintro",
    "private": true,
    "version": "0.0.0",
    "type": "module",
    "scripts": {
        "dev": "vite",
        "build": "vite build",
        "preview": "vite preview"
    },
    "dependencies": {
        "firebase": "^12.11.0",
        "gsap": "^3.14.2",
        "lenis": "^1.3.21",
        "motion": "^12.38.0",
        "ogl": "^1.0.11",
        "react": "^18.3.1",
        "react-dom": "^18.3.1",
        "react-router-dom": "^7.13.2",
        "three": "^0.183.2"
    },
    "devDependencies": {
        "@tailwindcss/postcss": "^4.2.2",
        "@vitejs/plugin-react": "^4.4.1",
        "autoprefixer": "^10.4.27",
        "postcss": "^8.5.8",
        "tailwindcss": "^4.2.2",
        "vite": "^5.4.10"
    }
}

```

---

## [44] frontend/postcss.config.js
**Size:** 108.0B

```javascript
export default {
    plugins: {
        "@tailwindcss/postcss": {},
        autoprefixer: {},
    },
};
```

---

## [45] frontend/src/components/AppLayout.jsx
**Size:** 147.0B

```jsx
import React from 'react';

export function AppLayout({ children }) {
    return (
        <>
            {children}
        </>
    );
}

```

---

## [46] frontend/src/components/Plasma.css
**Size:** 195.0B

```css
.plasma-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    background: rgba(255, 0, 0, 0.05);
    z-index: 10;
}
```

---

## [47] frontend/src/components/Plasma.jsx
**Size:** 7.0KB

```jsx
import { useEffect, useRef } from 'react';
import { Renderer, Program, Mesh, Triangle } from 'ogl';
import './Plasma.css';

const hexToRgb = hex => {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    if (!result) return [0.447, 0.918, 0.114]; // Default to green #72ea1e
    return [parseInt(result[1], 16) / 255, parseInt(result[2], 16) / 255, parseInt(result[3], 16) / 255];
};

const vertex = `#version 300 es
precision highp float;
in vec2 position;
in vec2 uv;
out vec2 vUv;
void main() {
  vUv = uv;
  gl_Position = vec4(position, 0.0, 1.0);
}
`;

const fragment = `#version 300 es
precision highp float;
uniform vec2 iResolution;
uniform float iTime;
uniform vec3 uCustomColor;
uniform float uUseCustomColor;
uniform float uSpeed;
uniform float uDirection;
uniform float uScale;
uniform float uOpacity;
uniform vec2 uMouse;
uniform float uMouseInteractive;
out vec4 fragColor;

void mainImage(out vec4 o, vec2 C) {
  vec2 center = iResolution.xy * 0.5;
  C = (C - center) / uScale + center;
  
  vec2 mouseOffset = (uMouse - center) * 0.0002;
  C += mouseOffset * length(C - center) * step(0.5, uMouseInteractive);
  
  float i, d, z, T = iTime * uSpeed * uDirection;
  vec3 O, p, S;

  for (vec2 r = iResolution.xy, Q; ++i < 60.; O += o.w/d*o.xyz) {
    p = z*normalize(vec3(C-.5*r,r.y)); 
    p.z -= 4.; 
    S = p;
    d = p.y-T;
    
    p.x += .4*(1.+p.y)*sin(d + p.x*0.1)*cos(.34*d + p.x*0.05); 
    Q = p.xz *= mat2(cos(p.y+vec4(0,11,33,0)-T)); 
    z+= d = abs(sqrt(length(Q*Q)) - .25*(5.+S.y))/3.+8e-4; 
    o = 1.+sin(S.y+p.z*.5+S.z-length(S-p)+vec4(2,1,0,8));
  }
  
  o.xyz = tanh(O/1e4);
}

bool finite1(float x){ return !(isnan(x) || isinf(x)); }
vec3 sanitize(vec3 c){
  return vec3(
    finite1(c.r) ? c.r : 0.0,
    finite1(c.g) ? c.g : 0.0,
    finite1(c.b) ? c.b : 0.0
  );
}

void main() {
  vec4 o = vec4(0.0);
  mainImage(o, gl_FragCoord.xy);
  vec3 rgb = sanitize(o.rgb);
  
  float intensity = (rgb.r + rgb.g + rgb.b) / 3.0;
  vec3 customColor = intensity * uCustomColor;
  vec3 finalColor = mix(rgb, customColor, step(0.5, uUseCustomColor));
  
  // Boost green channel specifically
  finalColor.g = clamp(finalColor.g * 3.0 + 0.5, 0.0, 1.0);
  
  float alpha = clamp((length(rgb) * 2.0 + 0.3) * uOpacity, 0.0, 1.0);
  fragColor = vec4(finalColor * 1.5, alpha);
}`;

export const Plasma = ({
    color = '#72ea1e',
    speed = 0.6,
    direction = 'forward',
    scale = 1.1,
    opacity = 0.8,
    mouseInteractive = true
}) => {
    const containerRef = useRef(null);
    const mousePos = useRef({ x: 0, y: 0 });

    useEffect(() => {
        if (!containerRef.current) return;
        const containerEl = containerRef.current;

        const useCustomColor = color ? 1.0 : 0.0;
        const customColorRgb = color ? hexToRgb(color) : [0.447, 0.918, 0.114];

        const directionMultiplier = direction === 'reverse' ? -1.0 : 1.0;

        const renderer = new Renderer({
            webgl: 2,
            alpha: true,
            antialias: false,
            dpr: Math.min(window.devicePixelRatio || 1, 2)
        });
        const gl = renderer.gl;
        const canvas = gl.canvas;
        canvas.style.display = 'block';
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.style.position = 'absolute';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.zIndex = '9999';
        containerRef.current.appendChild(canvas);

        const geometry = new Triangle(gl);

        const program = new Program(gl, {
            vertex: vertex,
            fragment: fragment,
            uniforms: {
                iTime: { value: 0 },
                iResolution: { value: new Float32Array([1, 1]) },
                uCustomColor: { value: new Float32Array(customColorRgb) },
                uUseCustomColor: { value: useCustomColor },
                uSpeed: { value: speed * 0.4 },
                uDirection: { value: directionMultiplier },
                uScale: { value: scale },
                uOpacity: { value: opacity },
                uMouse: { value: new Float32Array([0, 0]) },
                uMouseInteractive: { value: mouseInteractive ? 1.0 : 0.0 }
            }
        });

        const mesh = new Mesh(gl, { geometry, program });

        const handleMouseMove = e => {
            if (!mouseInteractive || !containerRef.current) return;
            const rect = containerRef.current.getBoundingClientRect();
            mousePos.current.x = e.clientX - rect.left;
            mousePos.current.y = e.clientY - rect.top;
            const mouseUniform = program.uniforms.uMouse.value;
            mouseUniform[0] = mousePos.current.x;
            mouseUniform[1] = mousePos.current.y;
        };

        if (mouseInteractive) {
            containerEl.addEventListener('mousemove', handleMouseMove);
        }

        const setSize = () => {
            if (!containerRef.current) return;
            const rect = containerRef.current.getBoundingClientRect();
            const width = Math.max(1, Math.floor(rect.width));
            const height = Math.max(1, Math.floor(rect.height));
            renderer.setSize(width, height);
            const res = program.uniforms.iResolution.value;
            res[0] = gl.drawingBufferWidth;
            res[1] = gl.drawingBufferHeight;
        };

        const ro = new ResizeObserver(setSize);
        ro.observe(containerEl);
        setSize();

        let raf = 0;
        const t0 = performance.now();
        const loop = t => {
            let timeValue = (t - t0) * 0.001;
            if (direction === 'pingpong') {
                const pingpongDuration = 10;
                const segmentTime = timeValue % pingpongDuration;
                const isForward = Math.floor(timeValue / pingpongDuration) % 2 === 0;
                const u = segmentTime / pingpongDuration;
                const smooth = u * u * (3 - 2 * u);
                const pingpongTime = isForward ? smooth * pingpongDuration : (1 - smooth) * pingpongDuration;
                program.uniforms.uDirection.value = 1.0;
                program.uniforms.iTime.value = pingpongTime;
            } else {
                program.uniforms.iTime.value = timeValue;
            }
            renderer.render({ scene: mesh });
            raf = requestAnimationFrame(loop);
        };
        raf = requestAnimationFrame(loop);

        return () => {
            cancelAnimationFrame(raf);
            ro.disconnect();
            if (mouseInteractive && containerEl) {
                containerEl.removeEventListener('mousemove', handleMouseMove);
            }
            try {
                containerEl?.removeChild(canvas);
            } catch {
                console.warn('Canvas already removed from container');
            }
        };
    }, [color, speed, direction, scale, opacity, mouseInteractive]);

    return <div ref={containerRef} className="plasma-container" />;
};

export default Plasma;

```

---

## [48] frontend/src/components/PlasmaBackground.css
**Size:** 227.0B

```css
#plasma,
.plasma-canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: block;
    z-index: 3;
    pointer-events: none;
    opacity: 1;
    mix-blend-mode: lighten;
}
```

---

## [49] frontend/src/components/PlasmaBackground.jsx
**Size:** 3.8KB

```jsx
import React, { useEffect, useRef } from 'react';
import './PlasmaBackground.css';

export function PlasmaBackground() {
    const canvasRef = useRef(null);
    const mouseRef = useRef({ x: 0, y: 0 });

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        let W, H, t = 0;

        const off = document.createElement('canvas');
        const octx = off.getContext('2d');
        const SCALE = 2;
        let oW, oH;

        function resize() {
            W = canvas.width = window.innerWidth;
            H = canvas.height = window.innerHeight;
            oW = Math.ceil(W / SCALE);
            oH = Math.ceil(H / SCALE);
            off.width = oW;
            off.height = oH;
        }

        function plasmaColor(v) {
            // Only green plasma - no rainbow colors
            const intensity = v;
            return [
                0,
                Math.floor(intensity * 255),
                0
            ];
        }

        function handleMouseMove(e) {
            mouseRef.current.x = e.clientX / W;
            mouseRef.current.y = e.clientY / H;
        }

        function render() {
            t += 0.025;
            const imageData = octx.createImageData(oW, oH);
            const data = imageData.data;

            const mx = mouseRef.current.x;
            const my = mouseRef.current.y;

            for (let y = 0; y < oH; y++) {
                for (let x = 0; x < oW; x++) {
                    const nx = x / oW;
                    const ny = y / oH;

                    // Multiple flowing layers for liquid effect
                    const v1 = Math.sin(nx * 10 + t * 0.5) * Math.cos(ny * 5 - t * 0.3);
                    const v2 = Math.sin(ny * 8 - t * 0.4) * Math.cos(nx * 6 + t * 0.2);
                    const v3 = Math.sin((nx + ny) * 7 + t * 0.6);

                    // Perlin-like turbulence
                    const v4 = Math.sin(Math.sqrt(
                        (nx - 0.5 + Math.sin(t * 0.3) * 0.3) ** 2 +
                        (ny - 0.5 + Math.cos(t * 0.25) * 0.3) ** 2
                    ) * 18 - t * 0.8);

                    // High frequency detail
                    const v5 = Math.sin(
                        nx * 15 * Math.cos(t * 0.4) +
                        ny * 12 * Math.sin(t * 0.35) +
                        t * 0.7
                    );

                    // Mouse reactivity
                    const dx = nx - mx;
                    const dy = ny - my;
                    const distToMouse = Math.sqrt(dx * dx + dy * dy);
                    const mouseInfluence = Math.sin(distToMouse * 8 - t * 1.5) * Math.exp(-distToMouse * 3);

                    // Combine all layers
                    const combined = (v1 + v2 + v3 + v4 + v5 + mouseInfluence * 2) / 6;
                    const norm = (combined + 1) / 2;
                    const [r, g, b] = plasmaColor(norm);

                    const i = (y * oW + x) * 4;
                    data[i] = r;
                    data[i + 1] = g;
                    data[i + 2] = b;
                    data[i + 3] = 255;
                }
            }

            octx.putImageData(imageData, 0, 0);
            ctx.clearRect(0, 0, W, H);
            ctx.imageSmoothingEnabled = true;
            ctx.drawImage(off, 0, 0, W, H);
            requestAnimationFrame(render);
        }

        window.addEventListener('resize', resize);
        window.addEventListener('mousemove', handleMouseMove);
        resize();
        render();

        return () => {
            window.removeEventListener('resize', resize);
            window.removeEventListener('mousemove', handleMouseMove);
        };
    }, []);

    return <canvas ref={canvasRef} id="plasma" className="plasma-canvas" />;
}

```

---

## [50] frontend/src/components/ShinyText.css
**Size:** 99.0B

```css
.shiny-text {
    display: inline-block;
    white-space: nowrap;
    letter-spacing: 0.06em;
}
```

---

## [51] frontend/src/components/ShinyText.jsx
**Size:** 3.7KB

```jsx
import { useState, useCallback, useEffect, useRef } from "react";
import {
    motion,
    useMotionValue,
    useAnimationFrame,
    useTransform,
} from "motion/react";
import "./ShinyText.css";

const ShinyText = ({
    text,
    disabled = false,
    speed = 2,
    className = "",
    color = "#b5b5b5",
    shineColor = "#ffffff",
    spread = 120,
    yoyo = false,
    pauseOnHover = false,
    direction = "left",
    delay = 0,
}) => {
    const [isPaused, setIsPaused] = useState(false);
    const progress = useMotionValue(0);
    const elapsedRef = useRef(0);
    const lastTimeRef = useRef(null);
    const directionRef = useRef(direction === "left" ? 1 : -1);

    const animationDuration = speed * 1000;
    const delayDuration = delay * 1000;

    useAnimationFrame((time) => {
        if (disabled || isPaused) {
            lastTimeRef.current = null;
            return;
        }

        if (lastTimeRef.current === null) {
            lastTimeRef.current = time;
            return;
        }

        const deltaTime = time - lastTimeRef.current;
        lastTimeRef.current = time;
        elapsedRef.current += deltaTime;

        if (yoyo) {
            const cycleDuration = animationDuration + delayDuration;
            const fullCycle = cycleDuration * 2;
            const cycleTime = elapsedRef.current % fullCycle;

            if (cycleTime < animationDuration) {
                const p = (cycleTime / animationDuration) * 100;
                progress.set(directionRef.current === 1 ? p : 100 - p);
            } else if (cycleTime < cycleDuration) {
                progress.set(directionRef.current === 1 ? 100 : 0);
            } else if (cycleTime < cycleDuration + animationDuration) {
                const reverseTime = cycleTime - cycleDuration;
                const p = 100 - (reverseTime / animationDuration) * 100;
                progress.set(directionRef.current === 1 ? p : 100 - p);
            } else {
                progress.set(directionRef.current === 1 ? 0 : 100);
            }
        } else {
            const cycleDuration = animationDuration + delayDuration;
            const cycleTime = elapsedRef.current % cycleDuration;

            if (cycleTime < animationDuration) {
                const p = (cycleTime / animationDuration) * 100;
                progress.set(directionRef.current === 1 ? p : 100 - p);
            } else {
                progress.set(directionRef.current === 1 ? 100 : 0);
            }
        }
    });

    useEffect(() => {
        directionRef.current = direction === "left" ? 1 : -1;
        elapsedRef.current = 0;
        progress.set(0);
    }, [direction, progress]);

    const backgroundPosition = useTransform(
        progress,
        (p) => `${150 - p * 2}% center`
    );

    const handleMouseEnter = useCallback(() => {
        if (pauseOnHover) setIsPaused(true);
    }, [pauseOnHover]);

    const handleMouseLeave = useCallback(() => {
        if (pauseOnHover) setIsPaused(false);
    }, [pauseOnHover]);

    const gradientStyle = {
        backgroundImage: `linear-gradient(${spread}deg, ${color} 0%, ${color} 35%, ${shineColor} 50%, ${color} 65%, ${color} 100%)`,
        backgroundSize: "200% auto",
        WebkitBackgroundClip: "text",
        backgroundClip: "text",
        WebkitTextFillColor: "transparent",
    };

    return (
        <motion.span
            className={`shiny-text ${className}`}
            style={{ ...gradientStyle, backgroundPosition }}
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
        >
            {text}
        </motion.span>
    );
};

export default ShinyText;
```

---

## [52] frontend/src/components/ThemeToggle.css
**Size:** 947.0B

```css
.theme-toggle {
    position: fixed;
    top: 20px;
    left: 24px;
    z-index: 50;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 1px solid var(--line);
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(8px);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--green);
    transition: all 0.3s ease;
    padding: 0;
}

.theme-toggle svg {
    width: 20px;
    height: 20px;
}

.theme-toggle:hover {
    background: rgba(0, 0, 0, 0.6);
    border-color: var(--green);
    transform: scale(1.1);
}

.theme-toggle:active {
    transform: scale(0.95);
}

/* Light mode styles */
[data-theme="light"] .theme-toggle {
    background: rgba(255, 255, 255, 0.4);
    border-color: var(--line);
}

[data-theme="light"] .theme-toggle:hover {
    background: rgba(255, 255, 255, 0.6);
    border-color: var(--green);
}
```

---

## [53] frontend/src/components/ThemeToggle.jsx
**Size:** 1.5KB

```jsx
import React from 'react';
import { useTheme } from '../context/ThemeContext';
import './ThemeToggle.css';

export function ThemeToggle() {
    const { isDark, toggleTheme } = useTheme();

    return (
        <button
            className="theme-toggle"
            onClick={toggleTheme}
            aria-label="Toggle theme"
            title={isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
        >
            {isDark ? (
                // Moon icon for dark mode (click to go light)
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
                </svg>
            ) : (
                // Sun icon for light mode (click to go dark)
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <circle cx="12" cy="12" r="5" />
                    <line x1="12" y1="1" x2="12" y2="3" />
                    <line x1="12" y1="21" x2="12" y2="23" />
                    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" />
                    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" />
                    <line x1="1" y1="12" x2="3" y2="12" />
                    <line x1="21" y1="12" x2="23" y2="12" />
                    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" />
                    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" />
                </svg>
            )}
        </button>
    );
}

```

---

## [54] frontend/src/components/UserProfile.css
**Size:** 2.5KB

```css
.user-profile {
    position: fixed;
    top: 20px;
    right: 24px;
    z-index: 11;
}

.profile-button {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid var(--green);
    background: transparent;
    color: var(--green);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: "Space Grotesk", sans-serif;
}

.profile-button:hover {
    background: var(--green);
    color: #000000;
    box-shadow: 0 8px 24px rgba(76, 172, 0, 0.3);
}

.profile-button:active {
    transform: scale(0.95);
}

.profile-dropdown {
    position: absolute;
    top: 56px;
    right: 0;
    background: rgba(0, 0, 0, 0.3);
    border: 2px solid var(--green);
    border-radius: 12px;
    min-width: 200px;
    box-shadow: 0 8px 32px rgba(76, 172, 0, 0.15);
    z-index: 12;
    overflow: hidden;
    animation: dropdownSlide 0.2s ease;
    backdrop-filter: blur(10px);
}

[data-theme="light"] .profile-dropdown {
    background: rgba(255, 255, 255, 0.4);
    box-shadow: 0 8px 32px rgba(76, 172, 0, 0.2);
}

@keyframes dropdownSlide {
    from {
        opacity: 0;
        transform: translateY(-8px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.dropdown-header {
    padding: 12px 16px;
    border-bottom: 1px solid rgba(76, 172, 0, 0.4);
}

.user-email {
    margin: 0;
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
    word-break: break-all;
    letter-spacing: 0;
    font-family: "Rajdhani", "Space Grotesk", sans-serif;
    font-style: normal;
}

.logout-button {
    width: 100%;
    padding: 12px 16px;
    border: none;
    background: transparent;
    color: #ff5555;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    transition: all 0.3s ease;
    font-family: "Rajdhani", "Space Grotesk", sans-serif;
    text-align: left;
    font-style: normal;
}

.logout-button:hover {
    background: rgba(76, 172, 0, 0.15);
    color: #ff5555;
    border-left: 3px solid var(--green);
    padding-left: 13px;
}

@media (max-width: 768px) {
    .user-profile {
        top: 16px;
        right: 16px;
    }

    .profile-button {
        width: 36px;
        height: 36px;
    }

    .profile-dropdown {
        min-width: 160px;
    }
}
```

---

## [55] frontend/src/components/UserProfile.jsx
**Size:** 2.3KB

```jsx
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

```

---

## [56] frontend/src/context/ThemeContext.jsx
**Size:** 1.6KB

```jsx
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

```

---

## [57] frontend/src/context/UserContext.jsx
**Size:** 1.1KB

```jsx
import React, { createContext, useContext, useEffect, useState } from 'react';
import { auth } from '../services/firebase';
import { onAuthStateChanged, signOut } from 'firebase/auth';

const UserContext = createContext();

export function UserProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
            setUser(currentUser);
            setLoading(false);
        });

        return () => unsubscribe();
    }, []);

    const logout = async () => {
        try {
            await signOut(auth);
            setUser(null);
        } catch (err) {
            console.error('Logout error:', err);
        }
    };

    return (
        <UserContext.Provider value={{ user, loading, logout }}>
            {children}
        </UserContext.Provider>
    );
}

export function useUser() {
    const context = useContext(UserContext);
    if (!context) {
        throw new Error('useUser must be used within UserProvider');
    }
    return context;
}

```

---

## [58] frontend/src/main-home.jsx
**Size:** 2.6KB

```jsx
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
                <Route
                    path="/security-audit"
                    element={
                        <ProtectedRoute>
                            <SecurityAuditPage />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/debt-report"
                    element={
                        <ProtectedRoute>
                            <DebtReportPage />
                        </ProtectedRoute>
                    }
                />
                <Route
                    path="/health-score"
                    element={
                        <ProtectedRoute>
                            <HealthScorePage />
                        </ProtectedRoute>
                    }
                />
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
```

---

## [59] frontend/src/pages/AnalyseBranchesPage.css
**Size:** 1.4KB

```css
.page-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    background-color: var(--bg);
    color: var(--text);
    transition: background-color 0.3s ease, color 0.3s ease;
}

.page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem;
    z-index: 50;
}

.page-content {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
}

.page-title {
    font-family: "Bebas Neue", sans-serif;
    font-size: 5rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    background: linear-gradient(90deg, #72ea1e, #a4ff00, #72ea1e);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    margin: 0;
    text-align: center;
}

@keyframes shimmer {
    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 200% center;
    }
}

/* Light mode adjustments */
html.light-mode .page-title {
    background: linear-gradient(90deg, #2d7a1a, #72ea1e, #2d7a1a);
    background-size: 200% auto;
}

@media (max-width: 768px) {
    .page-title {
        font-size: 2.5rem;
    }

    .page-header {
        padding: 1rem;
    }
}
```

---

## [60] frontend/src/pages/AnalyseBranchesPage.jsx
**Size:** 34.3KB

```jsx
import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import "./DashboardPage.css";
import "./AnalyseBranchesPage.css";

export function AnalyseBranchesPage() {
    const location = useLocation();
    const navigate = useNavigate();
    useTheme();
    const scanResult = location.state?.scanResult;
    const repoUrl = location.state?.repoUrl;
    const scanMode = location.state?.scanMode;
    const [expandedVulnerability, setExpandedVulnerability] = useState(null);

    if (!scanResult) {
        return (
            <>
                <Plasma color="#72ea1e" speed={0.6} direction="forward" scale={1.1} opacity={0.1} mouseInteractive={true} />
                <ThemeToggle />
                <UserProfile />
                <div className="page-shell" style={{ padding: "40px", textAlign: "center" }}>
                    <h2 style={{ color: "#72ea1e" }}>No scan results available</h2>
                    <p>Please go back to the dashboard and scan a repository first.</p>
                    <button onClick={() => navigate("/dashboard")} style={{
                        marginTop: "20px",
                        padding: "10px 20px",
                        background: "#72ea1e",
                        color: "#000",
                        border: "none",
                        borderRadius: "4px",
                        cursor: "pointer",
                        fontSize: "16px",
                        fontWeight: "bold"
                    }}>
                        Back to Dashboard
                    </button>
                </div>
            </>
        );
    }

    const isContinuous = scanResult.pipeline === "continuous_intelligence_extension" || scanMode === "continuous";
    const analyze = scanResult.stages?.analyze || {};
    const continuous = scanResult.continuous_intelligence || {};
    const data = scanResult.data || {};
    const vulnerableFiles = isContinuous ? (data.vulnerable_files || []) : (analyze.vulnerable_files || []);
    const vulnerabilities = isContinuous ? (data.security_findings || []) : (analyze.vulnerabilities || []);
    const debtFindings = isContinuous ? (data.debt_findings || []) : [];
    const autofixSuggestions = isContinuous ? (data.autofix_suggestions || []) : [];
    const billing = analyze.billing || {};
    const filesSummary = {
        total: isContinuous ? (data.total_files_fetched || 0) : (analyze.total_files_analyzed || 0),
        withIssues: isContinuous ? vulnerableFiles.length : (analyze.files_with_issues || 0),
        totalVulnerabilities: isContinuous ? vulnerabilities.length : (analyze.total_vulnerabilities || 0)
    };

    return (
        <>
            <Plasma color="#72ea1e" speed={0.6} direction="forward" scale={1.1} opacity={0.1} mouseInteractive={true} />
            <ThemeToggle />
            <UserProfile />
            <div className="page-shell" style={{ padding: "40px" }}>
                <section className="scan-hero" aria-label="analyse branches section">
                    <div className="scan-content">
                        <h2 className="scan-title" style={{ marginBottom: "30px" }}>
                            <span className="scan-word">BEDROCK</span>
                            <span className="scan-ampersand">&</span>
                            <span className="secure-word">ANALYSIS</span>
                        </h2>

                        {/* Repository Info */}
                        <div style={{
                            background: "rgba(114, 234, 30, 0.1)",
                            border: "1px solid #72ea1e",
                            borderRadius: "8px",
                            padding: "20px",
                            marginBottom: "20px"
                        }}>
                            <p style={{ margin: "0 0 10px 0", color: "#a1d96a", fontSize: "12px" }}>Repository</p>
                            <p style={{ margin: "0 0 15px 0", color: "#d9ffb8", fontSize: "14px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                {repoUrl || scanResult.repo_url || analyze.repo_url}
                            </p>
                            <p style={{ margin: "0 0 10px 0", color: "#a1d96a", fontSize: "12px" }}>Branch</p>
                            <p style={{ margin: "0", color: "#d9ffb8", fontSize: "14px", fontFamily: "monospace" }}>
                                {scanResult.branch_name || analyze.branch_name || "main"}
                            </p>
                        </div>

                        {isContinuous && (
                            <div style={{
                                background: "rgba(76, 175, 80, 0.08)",
                                border: "1px solid #4caf50",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "20px"
                            }}>
                                <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Continuous Intelligence</h3>
                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: "14px" }}>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>SCAN MODE</p>
                                        <p style={{ margin: 0, color: "#d9ffb8", fontSize: "18px", fontWeight: "bold", textTransform: "uppercase" }}>{continuous.scan_mode || "full"}</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>NEW ISSUES</p>
                                        <p style={{ margin: 0, color: "#ff9999", fontSize: "18px", fontWeight: "bold" }}>{continuous.new_issues ?? 0}</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>RESOLVED</p>
                                        <p style={{ margin: 0, color: "#9ccc65", fontSize: "18px", fontWeight: "bold" }}>{continuous.resolved_issues ?? 0}</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>PERSISTING</p>
                                        <p style={{ margin: 0, color: "#ffb74d", fontSize: "18px", fontWeight: "bold" }}>{continuous.persisting_issues ?? 0}</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>FIX TIME</p>
                                        <p style={{ margin: 0, color: "#90caf9", fontSize: "18px", fontWeight: "bold" }}>{continuous.estimated_fix_minutes ?? 0}m</p>
                                    </div>
                                    <div style={{ background: "#000", border: "1px solid #4caf50", borderRadius: "6px", padding: "14px" }}>
                                        <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "11px" }}>SCORE DELTA</p>
                                        <p style={{ margin: 0, color: "#d9ffb8", fontSize: "18px", fontWeight: "bold" }}>
                                            {continuous.trend?.delta == null ? "N/A" : `${continuous.trend.delta > 0 ? "+" : ""}${continuous.trend.delta}`}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        )}

                        <div style={{ marginBottom: "30px", textAlign: "left" }}>
                            <button
                                onClick={() => navigate("/dashboard")}
                                style={{
                                    padding: "8px 20px",
                                    background: "transparent",
                                    color: "#72ea1e",
                                    border: "1px solid #72ea1e",
                                    borderRadius: "4px",
                                    cursor: "pointer",
                                    fontSize: "14px",
                                    fontWeight: "bold",
                                    transition: "all 0.2s ease-in-out"
                                }}
                                onMouseEnter={(e) => {
                                    e.target.style.background = "#72ea1e";
                                    e.target.style.color = "#000";
                                }}
                                onMouseLeave={(e) => {
                                    e.target.style.background = "transparent";
                                    e.target.style.color = "#72ea1e";
                                }}
                            >
                                ← Back to Dashboard
                            </button>
                        </div>

                        {/* Summary Cards */}
                        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "20px", marginBottom: "30px" }}>
                            <div style={{
                                background: "rgba(114, 234, 30, 0.1)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#72ea1e", marginTop: 0 }}>Total Files</h4>
                                <p style={{ fontSize: "32px", color: "#d9ffb8", margin: "10px 0" }}>{filesSummary.total}</p>
                            </div>
                            <div style={{
                                background: "rgba(255, 107, 107, 0.1)",
                                border: "1px solid #ff6b6b",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#ff6b6b", marginTop: 0 }}>Files with Issues</h4>
                                <p style={{ fontSize: "32px", color: "#ff9999", margin: "10px 0" }}>{filesSummary.withIssues}</p>
                            </div>
                            <div style={{
                                background: "rgba(255, 152, 0, 0.1)",
                                border: "1px solid #ff9800",
                                borderRadius: "8px",
                                padding: "20px",
                                textAlign: "center"
                            }}>
                                <h4 style={{ color: "#ff9800", marginTop: 0 }}>Vulnerabilities Found</h4>
                                <p style={{ fontSize: "32px", color: "#ffb74d", margin: "10px 0" }}>{filesSummary.totalVulnerabilities}</p>
                            </div>
                        </div>

                        {isContinuous && debtFindings.length > 0 && (
                            <div style={{
                                background: "rgba(114, 234, 30, 0.05)",
                                border: "1px solid #72ea1e",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#72ea1e", marginTop: 0 }}>Technical Debt Signals ({debtFindings.length})</h3>
                                <div style={{ display: "grid", gap: "12px" }}>
                                    {debtFindings.slice(0, 8).map((item, idx) => (
                                        <div key={idx} style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "14px" }}>
                                            <p style={{ margin: "0 0 4px 0", color: "#d9ffb8", fontFamily: "monospace", fontSize: "12px" }}>{item.file}</p>
                                            <p style={{ margin: "0 0 6px 0", color: "#a1d96a", fontSize: "12px" }}>{item.type}</p>
                                            <p style={{ margin: 0, color: "#d2ddb8", fontSize: "13px" }}>{item.summary}</p>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* Vulnerable Files List */}
                        {vulnerableFiles.length > 0 && (
                            <div style={{
                                background: "rgba(255, 107, 107, 0.05)",
                                border: "1px solid #ff6b6b",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#ff6b6b", marginTop: 0 }}>Vulnerable Files ({vulnerableFiles.length})</h3>
                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))", gap: "15px" }}>
                                    {vulnerableFiles.map((file, idx) => (
                                        <div key={idx} style={{
                                            background: "#000",
                                            border: "1px solid #ff9999",
                                            borderRadius: "4px",
                                            padding: "15px"
                                        }}>
                                            <p style={{ margin: "0 0 8px 0", color: "#ff6b6b", fontWeight: "bold", fontSize: "13px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                {file.file}
                                            </p>
                                            <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px" }}>
                                                Type: <span style={{ color: "#d9ffb8" }}>{file.type}</span>
                                            </p>
                                            <p style={{ margin: "0", color: "#ff9800", fontSize: "12px" }}>
                                                Vulnerabilities: <span style={{ color: "#ffb74d", fontWeight: "bold" }}>{file.count}</span>
                                            </p>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* Detailed Vulnerabilities - Bedrock Analysis */}
                        {vulnerabilities.length > 0 && (
                            <div style={{
                                background: "rgba(255, 152, 0, 0.05)",
                                border: "1px solid #ff9800",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#ff9800", marginTop: 0 }}>Detailed Analysis ({vulnerabilities.length})</h3>
                                <div style={{ maxHeight: "1000px", overflowY: "auto" }}>
                                    {vulnerabilities.map((vuln, idx) => (
                                        <div key={idx} style={{
                                            borderBottom: idx < vulnerabilities.length - 1 ? "1px solid #333" : "none",
                                            paddingBottom: "20px",
                                            marginBottom: "20px",
                                            cursor: "pointer"
                                        }} onClick={() => setExpandedVulnerability(expandedVulnerability === idx ? null : idx)}>
                                            {/* Header */}
                                            <div style={{
                                                display: "flex",
                                                justifyContent: "space-between",
                                                alignItems: "start",
                                                padding: "12px",
                                                background: "rgba(255, 152, 0, 0.1)",
                                                borderRadius: "4px",
                                                marginBottom: "10px"
                                            }}>
                                                <div style={{ flex: 1 }}>
                                                    <p style={{ margin: "0 0 5px 0", color: "#ff6b6b", fontWeight: "bold", fontSize: "14px" }}>
                                                        {expandedVulnerability === idx ? "[OPEN]" : "[+]"} {vuln.type || "Unknown"}
                                                    </p>
                                                    <p style={{ margin: "0", color: "#d9ffb8", fontSize: "12px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                        {vuln.file}
                                                    </p>
                                                </div>
                                                <div style={{
                                                    padding: "4px 8px",
                                                    borderRadius: "4px",
                                                    fontSize: "11px",
                                                    fontWeight: "bold",
                                                    background: vuln.severity === "CRITICAL" ? "#ff6b6b" : vuln.severity === "HIGH" ? "#ff9800" : vuln.severity === "MEDIUM" ? "#ffb74d" : "#4caf50",
                                                    color: "#000"
                                                }}>
                                                    {vuln.severity}
                                                </div>
                                            </div>

                                            {/* Expanded Details */}
                                            {expandedVulnerability === idx && (
                                                <div style={{ paddingLeft: "12px", color: "#d2ddb8" }}>
                                                    {/* Explanation */}
                                                    <div style={{ marginBottom: "15px" }}>
                                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px", fontWeight: "bold" }}>EXPLANATION</p>
                                                        <p style={{ margin: "0", color: "#d2ddb8", fontSize: "13px", lineHeight: "1.5" }}>
                                                            {vuln.explanation || "No explanation provided"}
                                                        </p>
                                                    </div>

                                                    {/* Business Impact */}
                                                    <div style={{ marginBottom: "15px",  padding: "10px", background: "rgba(255, 107, 107, 0.1)", borderLeft: "3px solid #ff6b6b", borderRadius: "4px" }}>
                                                        <p style={{ margin: "0 0 5px 0", color: "#ff6b6b", fontSize: "12px", fontWeight: "bold" }}>BUSINESS IMPACT</p>
                                                        <p style={{ margin: "0", color: "#ff9999", fontSize: "13px", lineHeight: "1.5" }}>
                                                            {vuln.business_impact || "Impact information not available"}
                                                        </p>
                                                    </div>

                                                    {/* Remediation */}
                                                    <div style={{ marginBottom: "15px" }}>
                                                        <p style={{ margin: "0 0 5px 0", color: "#4caf50", fontSize: "12px", fontWeight: "bold" }}>REMEDIATION</p>
                                                        <p style={{ margin: "0", color: "#9ccc65", fontSize: "13px", lineHeight: "1.5", fontFamily: "monospace", whiteSpace: "pre-wrap", wordBreak: "break-word" }}>
                                                            {vuln.remediation || "See explanation above"}
                                                        </p>
                                                    </div>

                                                    {/* Fix Time Estimate */}
                                                    {vuln.estimated_minutes_to_fix && (
                                                        <div>
                                                            <p style={{ margin: "0 0 5px 0", color: "#64b5f6", fontSize: "12px", fontWeight: "bold" }}>ESTIMATED FIX TIME</p>
                                                            <p style={{ margin: "0", color: "#90caf9", fontSize: "13px" }}>
                                                                ~{vuln.estimated_minutes_to_fix} minutes
                                                            </p>
                                                        </div>
                                                    )}
                                                </div>
                                            )}
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {isContinuous && autofixSuggestions.length > 0 && (
                            <div style={{
                                background: "rgba(100, 181, 246, 0.06)",
                                border: "1px solid #64b5f6",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#64b5f6", marginTop: 0 }}>AutoFix Suggestions ({autofixSuggestions.length})</h3>
                                <div style={{ display: "grid", gap: "16px" }}>
                                    {autofixSuggestions.slice(0, 6).map((fix, idx) => (
                                        <div key={idx} style={{ background: "#000", border: "1px solid #64b5f6", borderRadius: "6px", padding: "16px" }}>
                                            <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "start" }}>
                                                <div>
                                                    <p style={{ margin: "0 0 6px 0", color: "#d9ffb8", fontFamily: "monospace", fontSize: "12px" }}>{fix.file_path}</p>
                                                    <p style={{ margin: 0, color: "#d2ddb8", fontSize: "13px" }}>{fix.issue}</p>
                                                </div>
                                                <div style={{
                                                    padding: "4px 8px",
                                                    borderRadius: "999px",
                                                    background: fix.validation_status === "VALIDATED" ? "#4caf50" : "#ff9800",
                                                    color: "#000",
                                                    fontWeight: "bold",
                                                    fontSize: "11px"
                                                }}>
                                                    {fix.validation_status}
                                                </div>
                                            </div>
                                            <div style={{ marginTop: "12px" }}>
                                                <p style={{ margin: "0 0 6px 0", color: "#90caf9", fontSize: "12px", fontWeight: "bold" }}>EXPLANATION</p>
                                                <p style={{ margin: "0 0 10px 0", color: "#d2ddb8", fontSize: "13px" }}>{fix.explanation}</p>
                                                <p style={{ margin: "0 0 6px 0", color: "#90caf9", fontSize: "12px", fontWeight: "bold" }}>PATCH PREVIEW</p>
                                                <pre style={{
                                                    margin: 0,
                                                    whiteSpace: "pre-wrap",
                                                    wordBreak: "break-word",
                                                    fontSize: "11px",
                                                    color: "#b3e5fc",
                                                    background: "rgba(100, 181, 246, 0.08)",
                                                    padding: "10px",
                                                    borderRadius: "4px",
                                                    maxHeight: "180px",
                                                    overflow: "auto"
                                                }}>
                                                    {fix.diff || "No patch generated"}
                                                </pre>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* Billing & Cost Information */}
                        {billing && (
                            <div style={{
                                background: "rgba(76, 175, 80, 0.05)",
                                border: "1px solid #4caf50",
                                borderRadius: "8px",
                                padding: "20px",
                                marginBottom: "30px"
                            }}>
                                <h3 style={{ color: "#4caf50", marginTop: 0 }}>Analysis Cost & Billing</h3>
                                
                                {/* Cost Metrics */}
                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: "15px", marginBottom: "20px" }}>
                                    <div style={{ background: "#000", padding: "15px", borderRadius: "4px", border: "1px solid #4caf50" }}>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px" }}>API Calls Used</p>
                                        <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>
                                            {billing.calls_made || 0}
                                        </p>
                                    </div>
                                    <div style={{ background: "#000", padding: "15px", borderRadius: "4px", border: "1px solid #4caf50" }}>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px" }}>Estimated Cost</p>
                                        <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>
                                            ${(analyze.cost_tracker?.estimated_cost || 0).toFixed(4)}
                                        </p>
                                    </div>
                                    <div style={{ background: "#000", padding: "15px", borderRadius: "4px", border: "1px solid #4caf50" }}>
                                        <p style={{ margin: "0 0 5px 0", color: "#a1d96a", fontSize: "12px" }}>Free Calls Remaining</p>
                                        <p style={{ margin: "0", color: "#d2ddb8", fontSize: "18px", fontWeight: "bold" }}>
                                            {billing.free_calls_remaining >= 0 ? billing.free_calls_remaining : "N/A"}
                                        </p>
                                    </div>
                                </div>

                                {/* Billing Status */}
                                <div style={{
                                    background: billing.will_be_charged ? "rgba(255, 107, 107, 0.1)" : "rgba(76, 175, 80, 0.1)",
                                    border: `1px solid ${billing.will_be_charged ? "#ff6b6b" : "#4caf50"}`,
                                    borderRadius: "4px",
                                    padding: "15px",
                                    marginBottom: "20px"
                                }}>
                                    <p style={{
                                        margin: "0",
                                        color: billing.will_be_charged ? "#ff6b6b" : "#4caf50",
                                        fontSize: "13px",
                                        fontWeight: "bold"
                                    }}>
                                        Status: {billing.will_be_charged ? "WARNING - You will be charged for additional analyses" : "Within free tier"}
                                    </p>
                                </div>

                                {/* Alternative Services */}
                                {billing.alternatives && billing.alternatives.length > 0 && (
                                    <div>
                                        <p style={{ margin: "0 0 15px 0", color: "#a1d96a", fontSize: "12px", fontWeight: "bold" }}>Alternative Services Comparison</p>
                                        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "12px" }}>
                                            {billing.alternatives.map((alt, idx) => (
                                                <a key={idx} href={alt.url} target="_blank" rel="noopener noreferrer" style={{
                                                    background: "#000",
                                                    border: "1px solid #72ea1e",
                                                    borderRadius: "4px",
                                                    padding: "12px",
                                                    textDecoration: "none",
                                                    transition: "all 0.3s"
                                                }} onMouseEnter={(e) => e.target.style.background = "rgba(114, 234, 30, 0.1)"} onMouseLeave={(e) => e.target.style.background = "#000"}>
                                                    <p style={{ margin: "0 0 5px 0", color: "#72ea1e", fontWeight: "bold", fontSize: "13px" }}>
                                                        {alt.name}
                                                    </p>
                                                    <p style={{ margin: "0", color: "#a1d96a", fontSize: "12px" }}>
                                                        {alt.cost}
                                                    </p>
                                                </a>
                                            ))}
                                        </div>
                                    </div>
                                )}
                            </div>
                        )}

                        {/* No Vulnerabilities Message */}
                        {vulnerabilities.length === 0 && (
                            <div style={{
                                background: "rgba(76, 175, 80, 0.1)",
                                border: "1px solid #4caf50",
                                borderRadius: "8px",
                                padding: "30px",
                                textAlign: "center",
                                marginBottom: "30px"
                            }}>
                                <p style={{ margin: "0", color: "#4caf50", fontSize: "16px", fontWeight: "bold" }}>
                                    No vulnerabilities found in this repository
                                </p>
                                <p style={{ margin: "5px 0 0 0", color: "#9ccc65", fontSize: "14px" }}>
                                    Code appears to be secure in the analyzed branch
                                </p>
                            </div>
                        )}

                        {/* Back Button */}
                        <button
                            onClick={() => navigate("/dashboard")}
                            style={{
                                padding: "12px 30px",
                                background: "#72ea1e",
                                color: "#000",
                                border: "none",
                                borderRadius: "4px",
                                cursor: "pointer",
                                fontSize: "16px",
                                fontWeight: "bold"
                            }}
                        >
                            Back to Dashboard
                        </button>
                    </div>
                </section>
            </div>
        </>
    );
}

```

---

## [61] frontend/src/pages/AuthPages.css
**Size:** 4.3KB

```css
.auth-page {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--bg);
    color: var(--text);
    padding: 20px;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.auth-container {
    position: relative;
    z-index: 10;
    width: 100%;
    max-width: 420px;
}

.auth-box {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 40px 32px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

[data-theme="light"] .auth-box {
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.08);
}

.auth-title {
    margin: 0 0 32px;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 0.02em;
    color: var(--text);
    text-align: center;
    font-family: "Space Grotesk", sans-serif;
}

.auth-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.form-group label {
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text);
}

.form-group input {
    padding: 12px 16px;
    font-size: 16px;
    border: 1px solid var(--line);
    border-radius: 8px;
    background: transparent;
    color: var(--text);
    font-family: "Space Grotesk", sans-serif;
    transition: all 0.3s ease;
}

.form-group input::placeholder {
    color: var(--text-dim);
}

.form-group input:focus {
    outline: none;
    border-color: var(--green);
    box-shadow: 0 0 12px rgba(76, 172, 0, 0.3);
}

.auth-button {
    padding: 14px 20px;
    background: var(--green);
    color: #000000;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: "Space Grotesk", sans-serif;
}

.auth-button:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(76, 172, 0, 0.4);
}

.auth-button:active:not(:disabled) {
    transform: translateY(0);
}

.auth-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.auth-error {
    padding: 12px 16px;
    background: rgba(255, 85, 85, 0.1);
    border: 1px solid rgba(255, 85, 85, 0.3);
    border-radius: 8px;
    color: #ff5555;
    font-size: 14px;
    text-align: center;
}

.auth-switch {
    text-align: center;
    margin-top: 24px;
    font-size: 14px;
    color: var(--text-dim);
}

.auth-link {
    color: var(--green);
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
}

.auth-link:hover {
    text-decoration: underline;
    opacity: 0.8;
}

.auth-divider {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 28px 0 20px;
}

.auth-divider::before,
.auth-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--line);
}

.auth-divider span {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-dim);
}

.google-button {
    width: 100%;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    border: 1px solid var(--line);
    background: var(--panel);
    color: var(--text);
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: "Space Grotesk", sans-serif;
}

.google-button:hover:not(:disabled) {
    border-color: var(--green);
    box-shadow: 0 4px 16px rgba(76, 172, 0, 0.2);
    background: var(--panel);
}

.google-button:active:not(:disabled) {
    transform: translateY(0);
}

.google-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.google-button svg {
    width: 18px;
    height: 18px;
}

/* Responsive */
@media (max-width: 480px) {
    .auth-box {
        padding: 32px 24px;
    }

    .auth-title {
        font-size: 24px;
        margin-bottom: 24px;
    }

    .auth-button {
        padding: 12px 16px;
        font-size: 14px;
    }
}
```

---

## [62] frontend/src/pages/DashboardPage.css
**Size:** 6.6KB

```css
.scan-hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 4rem 2rem;
    position: relative;
    background: var(--bg);
    border-top: 1px solid var(--line);
}

.scan-content {
    max-width: 900px;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 3rem;
    align-items: center;
    text-align: center;
}

/* Animated Title */
.scan-title {
    font-family: "Bebas Neue", sans-serif;
    font-size: clamp(3rem, 10vw, 7rem);
    font-weight: 400;
    letter-spacing: 0.05em;
    margin: 0;
    line-height: 1.2;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
    align-items: center;
}

.scan-word,
.secure-word {
    display: inline-block;
    background: linear-gradient(90deg, #72ea1e, #a8ff47, #72ea1e);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
}

.scan-ampersand {
    color: var(--text-dim);
    font-size: 0.8em;
    margin: 0 0.25rem;
}

@keyframes shimmer {
    0% {
        background-position: 0% center;
    }

    50% {
        background-position: 100% center;
    }

    100% {
        background-position: 0% center;
    }
}

/* Input Group */
.scan-input-group {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.scan-label {
    font-family: "Rajdhani", monospace;
    font-size: 0.875rem;
    letter-spacing: 0.15em;
    color: var(--text-dim);
    text-transform: uppercase;
    font-weight: 600;
}

.input-wrapper {
    display: flex;
    align-items: center;
    gap: 0;
    border: 2px solid var(--line);
    border-radius: 4px;
    overflow: hidden;
    background: transparent;
    transition: border-color 0.3s ease;
}

.input-wrapper:focus-within {
    border-color: var(--green);
    box-shadow: 0 0 20px rgba(114, 234, 30, 0.3);
}

.input-prefix {
    padding: 1rem 1.5rem;
    color: var(--text-dim);
    font-family: "Rajdhani", monospace;
    font-size: 0.95rem;
    white-space: nowrap;
    border-right: 1px solid var(--line);
}

.repo-input {
    flex: 1;
    padding: 1rem 1.5rem;
    border: none;
    outline: none;
    background: transparent;
    color: var(--text);
    font-family: "Rajdhani", monospace;
    font-size: 0.95rem;
}

.repo-input::placeholder {
    color: var(--text-dim);
}

.analyse-button {
    padding: 1rem 2.5rem;
    background: var(--green);
    color: #000000;
    border: none;
    font-family: "Bebas Neue", sans-serif;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    cursor: pointer;
    transition: all 0.3s ease;
    white-space: nowrap;
}

.analyse-button:hover {
    background: #89ff35;
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(114, 234, 30, 0.6);
}

.analyse-button:active {
    transform: scale(0.98);
}

/* Features Grid */
.scan-features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    width: 100%;
    margin-top: 2rem;
}

.feature-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    padding: 1.25rem 1.5rem;
    border: 2px solid var(--line);
    background: transparent;
    color: var(--text);
    font-family: "Rajdhani", sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    cursor: pointer;
    border-radius: 4px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.feature-button::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: rgba(114, 234, 30, 0.1);
    transition: left 0.3s ease;
    z-index: -1;
}

.feature-button:hover {
    border-color: var(--green);
    color: var(--green);
    box-shadow: 0 0 15px rgba(114, 234, 30, 0.3);
}

.feature-button:hover::before {
    left: 0;
}

.feature-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    background: var(--green);
    border-radius: 50%;
    animation: pulse 2s ease-in-out infinite;
}

.feature-button:hover .feature-dot {
    animation: pulse 1s ease-in-out infinite;
}

@keyframes pulse {

    0%,
    100% {
        opacity: 1;
        transform: scale(1);
    }

    50% {
        opacity: 0.6;
        transform: scale(1.2);
    }
}

/* Tagline */
.scan-tagline {
    font-family: "Sora", sans-serif;
    font-size: 1.1rem;
    color: var(--text-dim);
    margin: 2rem 0 0 0;
    font-style: italic;
    letter-spacing: 0.02em;
}

.scan-tagline .highlight {
    color: var(--green);
    font-weight: 600;
}

/* Light Mode Adjustments */
html.light-mode .scan-hero {
    background: rgba(255, 255, 255, 0.3);
}

html.light-mode .scan-word,
html.light-mode .secure-word {
    background: linear-gradient(90deg, #2d7a1a, #72ea1e, #2d7a1a);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

html.light-mode .input-wrapper {
    background: rgba(255, 255, 255, 0.1);
}

html.light-mode .repo-input {
    background: transparent;
}

html.light-mode .feature-button:hover {
    background: rgba(75, 172, 0, 0.1);
}

html.light-mode .scan-hero {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.85), rgba(245, 255, 238, 0.85));
}

html.light-mode .scan-hero .plasma-container {
    opacity: 0.85 !important;
}

/* Responsive Design */
@media (max-width: 768px) {
    .scan-title {
        font-size: clamp(2rem, 7vw, 4rem);
        gap: 0.25rem;
    }

    .scan-ampersand {
        display: block;
        width: 100%;
    }

    .input-wrapper {
        flex-wrap: wrap;
    }

    .input-prefix {
        padding: 0.875rem 1rem;
        font-size: 0.85rem;
        border-right: none;
        border-bottom: 1px solid var(--line);
        width: 100%;
    }

    .repo-input {
        padding: 0.875rem 1rem;
        width: 100%;
    }

    .analyse-button {
        padding: 0.875rem 1.5rem;
        font-size: 0.9rem;
    }

    .scan-features {
        grid-template-columns: 1fr;
        gap: 1rem;
    }

    .feature-button {
        padding: 1rem;
        font-size: 0.85rem;
    }

    .scan-hero {
        min-height: auto;
        padding: 3rem 1.5rem;
    }

    .scan-content {
        gap: 2rem;
    }
}

/* Plasma Visibility */
.scan-hero {
    z-index: 1;
}
```

---

## [63] frontend/src/pages/DashboardPage.jsx
**Size:** 24.5KB

```jsx
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import ShinyText from "../components/ShinyText";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import "./HomePage.css";
import "./DashboardPage.css";

export function DashboardPage() {
    const { isDark } = useTheme();
    const navigate = useNavigate();
    const [repoUrl, setRepoUrl] = useState("");
    const [branchName, setBranchName] = useState("main");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const [continuousMode, setContinuousMode] = useState(true);
    const [watchId, setWatchId] = useState("");
    const [watchStatus, setWatchStatus] = useState(null);
    const [watchError, setWatchError] = useState("");

    useEffect(() => {
        if (!watchId) {
            return undefined;
        }

        const loadStatus = async () => {
            try {
                const response = await fetch(`http://localhost:5000/api/continuous/status/${watchId}`);
                const data = await response.json();
                if (!response.ok) {
                    throw new Error(data.error || "Failed to fetch watch status");
                }
                setWatchStatus(data);
                setWatchError("");
            } catch (err) {
                setWatchError(err.message || "Failed to fetch watch status");
            }
        };

        loadStatus();
        const intervalId = window.setInterval(loadStatus, 5000);
        return () => window.clearInterval(intervalId);
    }, [watchId]);

    const handleAnalyse = async () => {
        if (!repoUrl.trim()) {
            setError("Please enter a GitHub repository URL");
            return;
        }

        setLoading(true);
        setError("");

        try {
            const endpoint = continuousMode
                ? "http://localhost:5000/api/analyze/continuous"
                : "http://localhost:5000/api/analyze";

            const response = await fetch(endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    repo_url: repoUrl,
                    branch_name: branchName || "main",
                    generate_fixes: continuousMode
                })
            });

            if (!response.ok) {
                throw new Error(`Failed to scan repository: ${response.status}`);
            }

            const data = await response.json();
            console.log("📊 Analysis complete:", data);

            // Navigate to analysis page with results
            navigate("/analyse-branches", {
                state: {
                    scanResult: data,
                    repoUrl: repoUrl,
                    scanMode: continuousMode ? "continuous" : "classic"
                }
            });
        } catch (err) {
            setError(err.message || "Failed to scan repository");
            console.error("Scan error:", err);
        } finally {
            setLoading(false);
        }
    };

    const handleStartWatch = async () => {
        if (!repoUrl.trim()) {
            setError("Please enter a GitHub repository URL");
            return;
        }

        try {
            const response = await fetch("http://localhost:5000/api/continuous/start", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    repo_url: repoUrl,
                    branch_name: branchName || "main",
                    interval_seconds: 60
                })
            });

            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || "Failed to start watch mode");
            }

            setWatchId(data.watch_id);
            setWatchStatus({ ...data, run_count: 0, last_result: null });
            setWatchError("");
        } catch (err) {
            setWatchError(err.message || "Failed to start watch mode");
        }
    };

    const handleStopWatch = async () => {
        if (!watchId) {
            return;
        }

        try {
            const response = await fetch(`http://localhost:5000/api/continuous/stop/${watchId}`, {
                method: "POST"
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || "Failed to stop watch mode");
            }
            setWatchStatus((prev) => prev ? { ...prev, status: data.status } : data);
        } catch (err) {
            setWatchError(err.message || "Failed to stop watch mode");
        }
    };

    return (
        <>
            <Plasma
                color="#72ea1e"
                speed={0.6}
                direction="forward"
                scale={1.1}
                opacity={0.1}
                mouseInteractive={true}
            />
            <ThemeToggle />
            <UserProfile />
            <div className="page-shell">
                <main className="home-hero" aria-label="landing hero">
                    <video className="hero-video-bg" autoPlay muted loop playsInline preload="auto" aria-hidden="true">
                        <source src={isDark ? "/assets/githopper.mp4" : "/assets/githopperlight.mp4"} type="video/mp4" />
                    </video>
                    <div className="hero-video-overlay" aria-hidden="true" />

                    <div className="hero-content">
                        <h1 className="git-lockup">
                            <ShinyText
                                text="GIT"
                                className="git-bold"
                                speed={2.1}
                                delay={0}
                                color="#72ea1e"
                                shineColor="#d9ffb8"
                                spread={122}
                                direction="left"
                                yoyo={false}
                                pauseOnHover={false}
                                disabled={false}
                            />
                            <ShinyText
                                text="HOPPER"
                                className="hopper-thin"
                                speed={2.2}
                                delay={0.08}
                                color="#69d31d"
                                shineColor="#d9ffb8"
                                spread={118}
                                direction="left"
                                yoyo={false}
                                pauseOnHover={false}
                                disabled={false}
                            />
                        </h1>

                        <p className="hero-tagline">
                            <em>One URL . Every vulnerability. No jargon.</em>
                        </p>
                    </div>
                </main>

                <section className="scan-hero" aria-label="scan and secure section">
                    <div className="scan-content">
                        <h2 className="scan-title">
                            <span className="scan-word">SCAN</span>
                            <span className="scan-ampersand">&</span>
                            <span className="secure-word">SECURE</span>
                        </h2>

                        <div className="scan-input-group">
                            <label htmlFor="repo-input" className="scan-label">SCAN YOUR REPO</label>
                            <div style={{ marginBottom: "14px", display: "flex", gap: "10px", flexWrap: "wrap" }}>
                                <button
                                    type="button"
                                    onClick={() => setContinuousMode(true)}
                                    disabled={loading}
                                    style={{
                                        padding: "8px 14px",
                                        borderRadius: "999px",
                                        border: "1px solid #72ea1e",
                                        background: continuousMode ? "#72ea1e" : "transparent",
                                        color: continuousMode ? "#000" : "#72ea1e",
                                        fontSize: "12px",
                                        fontWeight: "700",
                                        cursor: "pointer"
                                    }}
                                >
                                    CONTINUOUS INTELLIGENCE
                                </button>
                                <button
                                    type="button"
                                    onClick={() => setContinuousMode(false)}
                                    disabled={loading}
                                    style={{
                                        padding: "8px 14px",
                                        borderRadius: "999px",
                                        border: "1px solid #72ea1e",
                                        background: !continuousMode ? "#72ea1e" : "transparent",
                                        color: !continuousMode ? "#000" : "#72ea1e",
                                        fontSize: "12px",
                                        fontWeight: "700",
                                        cursor: "pointer"
                                    }}
                                >
                                    CLASSIC PIPELINE
                                </button>
                            </div>
                            <div className="input-wrapper">
                                <span className="input-prefix">github.com /</span>
                                <input
                                    id="repo-input"
                                    type="text"
                                    placeholder="username / repository"
                                    value={repoUrl}
                                    onChange={(e) => setRepoUrl(e.target.value)}
                                    className="repo-input"
                                    disabled={loading}
                                />
                                <button
                                    className="analyse-button"
                                    onClick={handleAnalyse}
                                    disabled={loading}
                                >
                                    {loading ? "SCANNING..." : "ANALYSE"}
                                </button>
                            </div>
                            
                            <div style={{ marginTop: "12px", display: "flex", gap: "10px", alignItems: "center" }}>
                                <label htmlFor="branch-input" style={{ color: "#72ea1e", fontSize: "12px", fontWeight: "600" }}>BRANCH (optional):</label>
                                <input
                                    id="branch-input"
                                    type="text"
                                    placeholder="main"
                                    value={branchName}
                                    onChange={(e) => setBranchName(e.target.value)}
                                    style={{
                                        padding: "6px 10px",
                                        background: "rgba(114, 234, 30, 0.1)",
                                        border: "1px solid #72ea1e",
                                        borderRadius: "4px",
                                        color: "#d9ffb8",
                                        fontSize: "13px",
                                        fontFamily: "monospace",
                                        width: "150px",
                                        disabled: loading
                                    }}
                                    disabled={loading}
                                />
                            </div>
                            
                            {error && <div style={{ color: "#ff6b6b", marginTop: "10px", fontSize: "14px" }}>{error}</div>}
                            <div style={{ marginTop: "10px", color: "#a1d96a", fontSize: "12px", maxWidth: "720px" }}>
                                {continuousMode
                                    ? "Continuous mode adds MCP memory, incremental scanning, context injection, and auto-fix suggestions."
                                    : "Classic mode uses the original RepoScan pipeline without the MCP extension layer."}
                            </div>

                            {continuousMode && (
                                <div style={{
                                    marginTop: "18px",
                                    border: "1px solid rgba(114, 234, 30, 0.45)",
                                    borderRadius: "10px",
                                    padding: "16px",
                                    background: "rgba(114, 234, 30, 0.06)",
                                    maxWidth: "780px"
                                }}>
                                    <div style={{ display: "flex", justifyContent: "space-between", gap: "12px", alignItems: "center", flexWrap: "wrap" }}>
                                        <div>
                                            <div style={{ color: "#72ea1e", fontWeight: "700", fontSize: "13px" }}>WATCH MODE TESTER</div>
                                            <div style={{ color: "#a1d96a", fontSize: "12px", marginTop: "4px" }}>
                                                Start background incremental scans from the UI before wiring the plugin host.
                                            </div>
                                        </div>
                                        <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
                                            <button
                                                type="button"
                                                onClick={handleStartWatch}
                                                disabled={loading}
                                                style={{
                                                    padding: "8px 14px",
                                                    borderRadius: "999px",
                                                    border: "1px solid #72ea1e",
                                                    background: "#72ea1e",
                                                    color: "#000",
                                                    fontSize: "12px",
                                                    fontWeight: "700",
                                                    cursor: "pointer"
                                                }}
                                            >
                                                START WATCH
                                            </button>
                                            <button
                                                type="button"
                                                onClick={handleStopWatch}
                                                disabled={!watchId}
                                                style={{
                                                    padding: "8px 14px",
                                                    borderRadius: "999px",
                                                    border: "1px solid #ff9800",
                                                    background: "transparent",
                                                    color: !watchId ? "#777" : "#ff9800",
                                                    fontSize: "12px",
                                                    fontWeight: "700",
                                                    cursor: !watchId ? "not-allowed" : "pointer"
                                                }}
                                            >
                                                STOP WATCH
                                            </button>
                                        </div>
                                    </div>

                                    {(watchId || watchError) && (
                                            <div style={{ marginTop: "14px", display: "grid", gap: "10px" }}>
                                            {watchId && (
                                                <div style={{ color: "#d9ffb8", fontSize: "12px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                    watch_id: {watchId}
                                                </div>
                                            )}
                                            {watchStatus && (
                                                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(140px, 1fr))", gap: "10px" }}>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>STATUS</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700", textTransform: "uppercase" }}>
                                                            {watchStatus.status || "running"}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>POLL COUNT</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700" }}>
                                                            {watchStatus.poll_count ?? 0}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>SCAN COUNT</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700" }}>
                                                            {watchStatus.run_count ?? 0}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>CHANGES DETECTED</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700" }}>
                                                            {watchStatus.change_detected_count ?? 0}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>LAST HEALTH SCORE</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700" }}>
                                                            {watchStatus.last_result?.summary?.health_score ?? "N/A"}
                                                        </div>
                                                    </div>
                                                    <div style={{ background: "#000", border: "1px solid #72ea1e", borderRadius: "6px", padding: "12px" }}>
                                                        <div style={{ color: "#a1d96a", fontSize: "11px" }}>LAST MODE</div>
                                                        <div style={{ color: "#d9ffb8", fontSize: "16px", fontWeight: "700", textTransform: "uppercase" }}>
                                                            {watchStatus.last_result?.continuous_intelligence?.scan_mode ?? "N/A"}
                                                        </div>
                                                    </div>
                                                </div>
                                            )}
                                            {watchStatus?.last_seen_commit && (
                                                <div style={{ color: "#d9ffb8", fontSize: "12px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                    last_seen_commit: {watchStatus.last_seen_commit}
                                                </div>
                                            )}
                                            {watchStatus?.last_scanned_commit && (
                                                <div style={{ color: "#a1d96a", fontSize: "12px", fontFamily: "monospace", wordBreak: "break-all" }}>
                                                    last_scanned_commit: {watchStatus.last_scanned_commit}
                                                </div>
                                            )}
                                            <div style={{ color: "#a1d96a", fontSize: "12px" }}>
                                                Polling can continue in the background, but a new scan now only runs when the latest branch commit SHA changes.
                                            </div>
                                            {watchStatus?.last_error && (
                                                <div style={{ color: "#ff6b6b", fontSize: "12px" }}>
                                                    watch error: {watchStatus.last_error}
                                                </div>
                                            )}
                                            {watchError && (
                                                <div style={{ color: "#ff6b6b", fontSize: "12px" }}>
                                                    {watchError}
                                                </div>
                                            )}
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>

                        <div className="scan-features">
                            <button className="feature-button" onClick={() => navigate('/analyse-branches')}>
                                <span className="feature-dot"></span>
                                ANALYSE BRANCHES
                            </button>
                            <button className="feature-button" onClick={() => navigate('/security-audit')}>
                                <span className="feature-dot"></span>
                                SECURITY AUDIT
                            </button>
                            <button className="feature-button" onClick={() => navigate('/debt-report')}>
                                <span className="feature-dot"></span>
                                DEBT REPORT
                            </button>
                            <button className="feature-button" onClick={() => navigate('/health-score')}>
                                <span className="feature-dot"></span>
                                HEALTH SCORE
                            </button>
                        </div>

                        <p className="scan-tagline">
                            <em>One URL . Every vulnerability. <span className="highlight">No jargon.</span></em>
                        </p>
                    </div>
                </section>
            </div>
        </>
    );
}

```

---

## [64] frontend/src/pages/DebtReportPage.css
**Size:** 1.4KB

```css
.page-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    background-color: var(--bg);
    color: var(--text);
    transition: background-color 0.3s ease, color 0.3s ease;
}

.page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem;
    z-index: 50;
}

.page-content {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
}

.page-title {
    font-family: "Bebas Neue", sans-serif;
    font-size: 5rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    background: linear-gradient(90deg, #72ea1e, #a4ff00, #72ea1e);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    margin: 0;
    text-align: center;
}

@keyframes shimmer {
    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 200% center;
    }
}

/* Light mode adjustments */
html.light-mode .page-title {
    background: linear-gradient(90deg, #2d7a1a, #72ea1e, #2d7a1a);
    background-size: 200% auto;
}

@media (max-width: 768px) {
    .page-title {
        font-size: 2.5rem;
    }

    .page-header {
        padding: 1rem;
    }
}
```

---

## [65] frontend/src/pages/DebtReportPage.jsx
**Size:** 1.2KB

```jsx
import React from "react";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import "./DashboardPage.css";
import "./DebtReportPage.css";

export function DebtReportPage() {

    return (
        <>
            <Plasma
                color="#72ea1e"
                speed={0.6}
                direction="forward"
                scale={1.1}
                opacity={0.1}
                mouseInteractive={true}
            />
            <ThemeToggle />
            <UserProfile />
            <div className="page-shell">
                <section className="scan-hero" aria-label="debt report section">
                    <div className="scan-content">
                        <h2 className="scan-title">
                            <span className="scan-word">DEBT</span>
                            <span className="scan-ampersand">&</span>
                            <span className="secure-word">REPORT</span>
                        </h2>
                    </div>
                </section>
            </div>
        </>
    );
}

```

---

## [66] frontend/src/pages/HealthScorePage.css
**Size:** 1.4KB

```css
.page-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    background-color: var(--bg);
    color: var(--text);
    transition: background-color 0.3s ease, color 0.3s ease;
}

.page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem;
    z-index: 50;
}

.page-content {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
}

.page-title {
    font-family: "Bebas Neue", sans-serif;
    font-size: 5rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    background: linear-gradient(90deg, #72ea1e, #a4ff00, #72ea1e);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    margin: 0;
    text-align: center;
}

@keyframes shimmer {
    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 200% center;
    }
}

/* Light mode adjustments */
html.light-mode .page-title {
    background: linear-gradient(90deg, #2d7a1a, #72ea1e, #2d7a1a);
    background-size: 200% auto;
}

@media (max-width: 768px) {
    .page-title {
        font-size: 2.5rem;
    }

    .page-header {
        padding: 1rem;
    }
}
```

---

## [67] frontend/src/pages/HealthScorePage.jsx
**Size:** 1.2KB

```jsx
import React from "react";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import "./DashboardPage.css";
import "./HealthScorePage.css";

export function HealthScorePage() {

    return (
        <>
            <Plasma
                color="#72ea1e"
                speed={0.6}
                direction="forward"
                scale={1.1}
                opacity={0.1}
                mouseInteractive={true}
            />
            <ThemeToggle />
            <UserProfile />
            <div className="page-shell">
                <section className="scan-hero" aria-label="health score section">
                    <div className="scan-content">
                        <h2 className="scan-title">
                            <span className="scan-word">HEALTH</span>
                            <span className="scan-ampersand">&</span>
                            <span className="secure-word">SCORE</span>
                        </h2>
                    </div>
                </section>
            </div>
        </>
    );
}

```

---

## [68] frontend/src/pages/HomePage.css
**Size:** 4.4KB

```css
.auth-nav-button {
    position: fixed;
    top: 20px;
    right: 24px;
    z-index: 11;
    padding: 12px 20px;
    background: var(--green);
    color: #000000;
    border: none;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    cursor: pointer;
    font-family: "Space Grotesk", sans-serif;
    transition: all 0.3s ease;
    box-shadow: 0 8px 24px rgba(76, 172, 0, 0.2);
}

.auth-nav-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 32px rgba(76, 172, 0, 0.4);
}

.auth-nav-button:active {
    transform: translateY(0);
}

@media (max-width: 768px) {
    .auth-nav-button {
        padding: 10px 16px;
        font-size: 12px;
        right: 16px;
    }
}

/* Call-to-Action Button */
.cta-btn {
    margin-top: 32px;
    padding: 16px 40px;
    background: var(--green);
    color: #000000;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    cursor: pointer;
    font-family: "Space Grotesk", sans-serif;
    transition: all 0.3s ease;
    box-shadow: 0 8px 24px rgba(76, 172, 0, 0.3);
    position: relative;
    overflow: hidden;
}

.cta-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s ease;
}

.cta-btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 40px rgba(76, 172, 0, 0.5);
}

.cta-btn:hover::before {
    left: 100%;
}

.cta-btn:active {
    transform: translateY(-2px);
}

@media (max-width: 768px) {
    .cta-btn {
        padding: 14px 32px;
        font-size: 14px;
        margin-top: 24px;
    }
}

@media (max-width: 480px) {
    .cta-btn {
        padding: 12px 24px;
        font-size: 13px;
        margin-top: 20px;
    }
}

/* Video Background Styles */
.hero-video-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    display: block;
    z-index: 0;
}

.hero-video-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: none;
    z-index: 0;
}

/* Fullscreen Video Background */
.background-videos {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    overflow: hidden;
    background: #000000;
}

.background-video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translate(-50%, -50%);
    object-fit: cover;
    object-position: center;
    display: block;
}

/* Page Shell Container */
.page-shell {
    position: relative;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: flex-start;
}

/* Home Hero Section */
.home-hero {
    position: relative;
    width: 100%;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-content {
    text-align: center;
    max-width: 600px;
    width: 90%;
    padding: 20px;
}

.git-lockup {
    font-size: 4rem;
    font-weight: 700;
    margin: 0;
    line-height: 1.1;
    letter-spacing: -0.02em;
    font-family: "Space Grotesk", sans-serif;
    color: #72ea1e;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(114, 234, 30, 0.3);
}

.git-bold {
    display: block;
    font-weight: 900;
    color: #72ea1e;
}

.hopper-thin {
    display: block;
    font-weight: 400;
    color: #69d31d;
}

.hero-tagline {
    font-size: 1.2rem;
    margin: 24px 0 0 0;
    line-height: 1.6;
    letter-spacing: 0.04em;
    font-family: "Space Grotesk", sans-serif;
    color: #ffffff;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.7);
}

/* Responsive Design */
@media (max-width: 768px) {
    .git-lockup {
        font-size: 2.5rem;
    }

    .hero-tagline {
        font-size: 1rem;
    }
}

@media (max-width: 480px) {
    .git-lockup {
        font-size: 2rem;
    }

    .hero-tagline {
        font-size: 0.9rem;
    }

    .hero-content {
        padding: 10px;
    }
}
```

---

## [69] frontend/src/pages/HomePage.jsx
**Size:** 3.2KB

```jsx
import React from "react";
import { useNavigate } from "react-router-dom";
import ShinyText from "../components/ShinyText";
import { ThemeToggle } from "../components/ThemeToggle";
import { Plasma } from "../components/Plasma";
import { useTheme } from "../context/ThemeContext";
import "./HomePage.css";

export function HomePage() {
    const { isDark } = useTheme();
    const navigate = useNavigate();

    return (
        <>
            <Plasma
                color="#72ea1e"
                speed={0.6}
                direction="forward"
                scale={1.1}
                opacity={0.1}
                mouseInteractive={true}
            />
            <ThemeToggle />
            <div className="page-shell">
                <main className="home-hero" aria-label="landing hero">
                    <video className="hero-video-bg" autoPlay muted loop playsInline preload="auto" aria-hidden="true">
                        <source src={isDark ? "/assets/githopper.mp4" : "/assets/githopperlight.mp4"} type="video/mp4" />
                    </video>
                    <div className="hero-video-overlay" aria-hidden="true" />

                    <div className="hero-content">
                        <h1 className="git-lockup">
                            <ShinyText
                                text="GIT"
                                className="git-bold"
                                speed={2.1}
                                delay={0}
                                color="#72ea1e"
                                shineColor="#d9ffb8"
                                spread={122}
                                direction="left"
                                yoyo={false}
                                pauseOnHover={false}
                                disabled={false}
                            />
                            <ShinyText
                                text="HOPPER"
                                className="hopper-thin"
                                speed={2.2}
                                delay={0.08}
                                color="#69d31d"
                                shineColor="#d9ffb8"
                                spread={118}
                                direction="left"
                                yoyo={false}
                                pauseOnHover={false}
                                disabled={false}
                            />
                        </h1>

                        <p className="hero-tagline">
                            <em>One URL . Every vulnerability. No jargon.</em>
                        </p>

                        <button
                            className="cta-btn"
                            onClick={() => navigate('/dashboard')}
                        >
                            Get Started →
                        </button>
                    </div>

                    <button
                        className="auth-nav-button"
                        onClick={() => navigate('/login')}
                    >
                        LOGIN / SIGN UP
                    </button>
                </main>
            </div>
        </>
    );
}

```

---

## [70] frontend/src/pages/LoginPage.jsx
**Size:** 4.6KB

```jsx
import React, { useState } from 'react';
import { auth, googleProvider, signInWithPopup } from '../services/firebase';
import { signInWithEmailAndPassword } from 'firebase/auth';
import { useTheme } from '../context/ThemeContext';
import './AuthPages.css';
import { useNavigate } from 'react-router-dom';
import Plasma from '../components/Plasma';

export function LoginPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const { isDark } = useTheme();
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            await signInWithEmailAndPassword(auth, email, password);
            navigate('/dashboard');
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const handleGoogleLogin = async () => {
        setError('');
        setLoading(true);

        try {
            await signInWithPopup(auth, googleProvider);
            navigate('/dashboard');
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="auth-page">
            <Plasma color="#72ea1e" speed={0.6} direction="forward" scale={1.1} opacity={0.1} mouseInteractive={true} />
            <div className="auth-container">
                <div className="auth-box">
                    <h1 className="auth-title">Login to GitHopper</h1>

                    {error && <div className="auth-error">{error}</div>}

                    <form onSubmit={handleLogin} className="auth-form">
                        <div className="form-group">
                            <label htmlFor="email">Email Address</label>
                            <input
                                type="email"
                                id="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                placeholder="your@email.com"
                                required
                            />
                        </div>

                        <div className="form-group">
                            <label htmlFor="password">Password</label>
                            <input
                                type="password"
                                id="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                placeholder="Enter your password"
                                required
                            />
                        </div>

                        <button type="submit" className="auth-button" disabled={loading}>
                            {loading ? 'Logging in...' : 'Login'}
                        </button>
                    </form>

                    <p className="auth-switch">
                        New user? <a href="/signup" className="auth-link">Sign up here</a>
                    </p>

                    <div className="auth-divider">
                        <span>or</span>
                    </div>

                    <button type="button" className="google-button" onClick={handleGoogleLogin} disabled={loading}>
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
                        </svg>
                        {loading ? 'Signing in...' : 'Sign in with Google'}
                    </button>
                </div>
            </div>
        </div>
    );
}

```

---

## [71] frontend/src/pages/SecurityAuditPage.css
**Size:** 1.4KB

```css
.page-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    background-color: var(--bg);
    color: var(--text);
    transition: background-color 0.3s ease, color 0.3s ease;
}

.page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem;
    z-index: 50;
}

.page-content {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
}

.page-title {
    font-family: "Bebas Neue", sans-serif;
    font-size: 5rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    background: linear-gradient(90deg, #72ea1e, #a4ff00, #72ea1e);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    margin: 0;
    text-align: center;
}

@keyframes shimmer {
    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 200% center;
    }
}

/* Light mode adjustments */
html.light-mode .page-title {
    background: linear-gradient(90deg, #2d7a1a, #72ea1e, #2d7a1a);
    background-size: 200% auto;
}

@media (max-width: 768px) {
    .page-title {
        font-size: 2.5rem;
    }

    .page-header {
        padding: 1rem;
    }
}
```

---

## [72] frontend/src/pages/SecurityAuditPage.jsx
**Size:** 1.2KB

```jsx
import React from "react";
import { ThemeToggle } from "../components/ThemeToggle";
import { UserProfile } from "../components/UserProfile";
import { Plasma } from "../components/Plasma";
import "./DashboardPage.css";
import "./SecurityAuditPage.css";

export function SecurityAuditPage() {

    return (
        <>
            <Plasma
                color="#72ea1e"
                speed={0.6}
                direction="forward"
                scale={1.1}
                opacity={0.1}
                mouseInteractive={true}
            />
            <ThemeToggle />
            <UserProfile />
            <div className="page-shell">
                <section className="scan-hero" aria-label="security audit section">
                    <div className="scan-content">
                        <h2 className="scan-title">
                            <span className="scan-word">SECURITY</span>
                            <span className="scan-ampersand">&</span>
                            <span className="secure-word">AUDIT</span>
                        </h2>
                    </div>
                </section>
            </div>
        </>
    );
}

```

---

## [73] frontend/src/pages/SignUpPage.jsx
**Size:** 5.4KB

```jsx
import React, { useState } from 'react';
import { auth, googleProvider, signInWithPopup } from '../services/firebase';
import { createUserWithEmailAndPassword } from 'firebase/auth';
import { useTheme } from '../context/ThemeContext';
import './AuthPages.css';
import { useNavigate } from 'react-router-dom';
import Plasma from '../components/Plasma';

export function SignUpPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const { isDark } = useTheme();
    const navigate = useNavigate();

    const handleSignUp = async (e) => {
        e.preventDefault();
        setError('');

        if (password !== confirmPassword) {
            setError('Passwords do not match');
            return;
        }

        setLoading(true);

        try {
            await createUserWithEmailAndPassword(auth, email, password);
            navigate('/dashboard');
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const handleGoogleSignUp = async () => {
        setError('');
        setLoading(true);

        try {
            await signInWithPopup(auth, googleProvider);
            navigate('/dashboard');
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="auth-page">
            <Plasma color="#72ea1e" speed={0.6} direction="forward" scale={1.1} opacity={0.1} mouseInteractive={true} />
            <div className="auth-container">
                <div className="auth-box">
                    <h1 className="auth-title">Create GitHopper Account</h1>

                    {error && <div className="auth-error">{error}</div>}

                    <form onSubmit={handleSignUp} className="auth-form">
                        <div className="form-group">
                            <label htmlFor="email">Email Address</label>
                            <input
                                type="email"
                                id="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                placeholder="your@email.com"
                                required
                            />
                        </div>

                        <div className="form-group">
                            <label htmlFor="password">Password</label>
                            <input
                                type="password"
                                id="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                placeholder="Create a strong password"
                                required
                            />
                        </div>

                        <div className="form-group">
                            <label htmlFor="confirmPassword">Confirm Password</label>
                            <input
                                type="password"
                                id="confirmPassword"
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                                placeholder="Confirm your password"
                                required
                            />
                        </div>

                        <button type="submit" className="auth-button" disabled={loading}>
                            {loading ? 'Creating Account...' : 'Sign Up'}
                        </button>
                    </form>

                    <p className="auth-switch">
                        Already have an account? <a href="/login" className="auth-link">Login here</a>
                    </p>

                    <div className="auth-divider">
                        <span>or</span>
                    </div>

                    <button type="button" className="google-button" onClick={handleGoogleSignUp} disabled={loading}>
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
                            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
                            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
                            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
                        </svg>
                        {loading ? 'Signing up...' : 'Sign up with Google'}
                    </button>
                </div>
            </div>
        </div>
    );
}

```

---

## [74] frontend/src/services/firebase.js
**Size:** 823.0B

```javascript
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { getAnalytics } from "firebase/analytics";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBMxfOSo8jKEOOrD9GmTyAtjl5JPewEvMA",
    authDomain: "githopper.firebaseapp.com",
    projectId: "githopper",
    storageBucket: "githopper.firebasestorage.app",
    messagingSenderId: "364587244760",
    appId: "1:364587244760:web:bfb125235ebffdcbd88bad",
    measurementId: "G-64TYKKN7RH"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const analytics = getAnalytics(app);
const googleProvider = new GoogleAuthProvider();

export { app, auth, analytics, googleProvider, signInWithPopup };

```

---

## [75] frontend/src/styles.css
**Size:** 27.0KB

```css
@import url("https://fonts.googleapis.com/css2?family=Archivo+Black&family=Bebas+Neue&family=Oswald:wght@300;400;500&family=Rajdhani:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;700&family=Sora:wght@500;700&display=swap");

:root {
    --bg: #000000;
    --green: #4BAC00;
    --orange: #d07a1b;
    --text: #d2ddb8;
    --text-dim: #8f9a79;
    --panel: #000000;
    --line: #1a1a1a;
}

/* Light Mode Theme - Attribute Selector */
[data-theme="light"] {
    --bg: #ffffff;
    --green: #4BAC00;
    --orange: #d07a1b;
    --text: #000000;
    --text-dim: #333333;
    --panel: #ffffff;
    --line: #e0e0e0;
}

/* Light Mode Theme - Class Selector (higher specificity) */
html.light-mode {
    --bg: #ffffff;
    --green: #4BAC00;
    --orange: #d07a1b;
    --text: #000000;
    --text-dim: #333333;
    --panel: #ffffff;
    --line: #e0e0e0;
}

* {
    box-sizing: border-box;
}

html {
    background: var(--bg);
    color: var(--text);
}

html,
body,
#root {
    margin: 0;
    height: 100%;
    width: 100%;
}

body {
    background: var(--bg);
}

body {
    background: var(--bg);
    color: var(--text);
    font-family: "Space Grotesk", sans-serif;
    transition: background-color 0.3s ease, color 0.3s ease;
}

/* Background Videos - Responsive */
.background-videos {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    overflow: hidden;
    pointer-events: none;
}

.background-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    opacity: 0.8;
    transition: opacity 0.3s ease;
}

[data-theme="light"] .background-video,
html.light-mode .background-video {
    opacity: 0.7;
}

/* Mobile optimization for videos */
@media (max-width: 768px) {
    .background-video {
        opacity: 0.6;
    }

    [data-theme="light"] .background-video,
    html.light-mode .background-video {
        opacity: 0.55;
    }
}

/* Very small screens */
@media (max-width: 480px) {
    .background-video {
        opacity: 0.5;
    }

    [data-theme="light"] .background-video,
    html.light-mode .background-video {
        opacity: 0.45;
    }
}

a {
    color: inherit;
}

.page-shell {
    min-height: 100vh;
    background: var(--bg);
    position: relative;
    z-index: 2;
    pointer-events: auto;
}

.top-nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 24px;
    border-bottom: 1px solid var(--line);
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(8px);
    transition: background-color 0.3s ease, border-color 0.3s ease;
}

[data-theme="light"] .top-nav {
    background: rgba(255, 255, 255, 0.8);
    border-bottom-color: var(--line);
}

.brand-mark {
    font-family: "Sora", sans-serif;
    font-size: 0.96rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-decoration: none;
    color: var(--green);
}

.nav-button {
    text-decoration: none;
    text-transform: uppercase;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    padding: 0.58rem 0.9rem;
    border: 1px solid #3f522d;
    color: var(--orange);
    background: #040404;
    transition: all 0.3s ease;
}

[data-theme="light"] .nav-button {
    border-color: #e0e0e0;
    background: #ffffff;
    color: var(--orange);
}

.nav-button:hover {
    border-color: var(--orange);
}

.home-hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: stretch;
    padding: 92px 24px 24px;
    max-width: none;
    width: 100%;
    margin: 0 auto;
    position: relative;
    overflow: hidden;
    isolation: isolate;
}

.hero-video-bg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 0;
    opacity: 0.75;
}

[data-theme="light"] .hero-video-bg,
html.light-mode .hero-video-bg {
    opacity: 0.65;
}

.hero-video-overlay {
    position: absolute;
    inset: 0;
    z-index: 1;
    background: transparent !important;
    display: none !important;
    transition: background 0.3s ease;
}

/* Light mode - remove overlay completely */
[data-theme="light"] .hero-video-overlay,
html.light-mode .hero-video-overlay {
    background: transparent !important;
    display: none !important;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 980px;
    width: 100%;
    margin: 0 auto;
}

.git-lockup {
    margin: 0;
    line-height: 0.9;
    letter-spacing: 0.02em;
    text-align: left;
}

.git-bold,
.hopper-thin {
    display: block;
    text-transform: uppercase;
    color: var(--green);
}

.git-bold {
    font-family: "Archivo Black", sans-serif;
    font-size: clamp(3.2rem, 12vw, 9.4rem);
    font-weight: 400;
    letter-spacing: 0.02em;
}

.hopper-thin {
    font-family: "Oswald", sans-serif;
    margin-top: -0.1em;
    font-size: clamp(2.9rem, 11vw, 8.6rem);
    font-weight: 300;
    letter-spacing: 0.05em;
}

.hero-tagline {
    margin: 18px 0 0;
    color: #c8c8c8;
    font-size: clamp(1.18rem, 2.75vw, 1.72rem);
    text-align: left;
    text-shadow: 0 0 18px rgba(215, 215, 215, 0.24);
    transition: color 0.3s ease, text-shadow 0.3s ease;
}

/* Light mode - change tagline to black */
[data-theme="light"] .hero-tagline,
html.light-mode .hero-tagline {
    color: #000000;
    text-shadow: 0 0 18px rgba(0, 0, 0, 0.1);
}

.hero-tagline em {
    font-style: italic;
}

.home-scroll-slot {
    min-height: 100vh;
    position: relative;
    overflow: hidden;
    background: transparent;
}

.ghost-layer {
    position: absolute;
    inset: 0;
    z-index: 7;
    pointer-events: none;
}

.home-scroll-slot::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 26vh;
    z-index: 3;
    pointer-events: none;
    background: transparent;
    display: none;
}

.scroll-fx-wrap {
    position: absolute;
    inset: 0;
    opacity: 0;
    display: none;
    pointer-events: none;
}

.scroll-fx-wrap::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 1;
    background: transparent;
    pointer-events: none;
}

.scroll-edge {
    position: absolute;
    z-index: 2;
    pointer-events: none;
    filter: blur(40px);
    opacity: 0.42;
}

.edge-green {
    width: 40vw;
    height: 32vh;
    left: -6vw;
    bottom: 4vh;
    background: radial-gradient(circle at center,
            rgba(124, 255, 31, 0.55),
            rgba(124, 255, 31, 0));
}

.edge-orange {
    width: 34vw;
    height: 26vh;
    right: -4vw;
    top: 10vh;
    background: radial-gradient(circle at center,
            rgba(208, 122, 27, 0.42),
            rgba(208, 122, 27, 0));
}

.content-layer {
    position: relative;
    z-index: 6;
    max-width: 1080px;
    margin: 0 auto;
    padding: 10.5rem 1.6rem 7.5rem;
    display: grid;
    gap: 4rem;
    font-family: "Rajdhani", "Space Grotesk", sans-serif;
}

.flow-block {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    animation: fadeRise 1.2s cubic-bezier(0.18, 0.7, 0.2, 1) both;
}

.scan-intro,
.problem-solution-section,
.features-flow,
.how-flow,
.target-wrap,
.rotating-feature,
.closing-note {
    padding: clamp(0.35rem, 1.3vw, 0.75rem) 0;
    background: transparent;
    border: 0;
    border-radius: 0;
    backdrop-filter: none;
    box-shadow: none;
    transition: transform 260ms ease;
}

.scan-intro:hover,
.problem-solution-section:hover,
.features-flow:hover,
.how-flow:hover,
.target-wrap:hover,
.rotating-feature:hover,
.closing-note:hover {
    transform: translateY(-3px);
}

.interactive-layer {
    will-change: transform;
}

.flow-block:nth-child(2) {
    animation-delay: 0.08s;
}

.flow-block:nth-child(3) {
    animation-delay: 0.14s;
}

.flow-block:nth-child(4) {
    animation-delay: 0.2s;
}

.flow-block:nth-child(5) {
    animation-delay: 0.25s;
}

@keyframes fadeRise {
    from {
        opacity: 0;
        transform: translateY(24px);
        filter: blur(2px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }
}

.scan-intro {
    color: #d7d7d7;
    max-width: 920px;
}

.scan-line-1 {
    margin: 0;
    font-family: "Bebas Neue", "Oswald", sans-serif;
    letter-spacing: 0.06em;
    font-size: clamp(1.65rem, 3.5vw, 2.7rem);
    line-height: 1.22;
}

.scan-line-2 {
    margin: 0.8rem 0 0;
    color: #c6c6c6;
    font-size: clamp(1.16rem, 2.2vw, 1.48rem);
    line-height: 1.62;
}

.section-kicker {
    margin: 0 0 1.1rem;
    font-family: "Bebas Neue", "Oswald", sans-serif;
    font-size: 0.82rem;
    text-transform: uppercase;
    letter-spacing: 0.24em;
    color: #9a9a9a;
}

.focus-container-custom {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 3rem;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
}

.divider-arrow-vertical {
    grid-column: 2;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    min-height: 300px;
}

.divider-arrow-vertical svg {
    width: 2px;
    height: 100%;
}

.focus-item {
    position: relative;
    will-change: filter, opacity;
    width: 100%;
}

.focus-item:nth-child(1) {
    grid-column: 1;
}

.focus-item:nth-child(3) {
    grid-column: 3;
}

.problem-solution-section {
    display: block;
}

.problem-solution-container {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 3rem;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

.problem-card-wrapper,
.solution-card-wrapper {
    perspective: 1000px;
}

.problem-card,
.solution-card {
    position: relative;
    padding: 2.5rem;
    border-radius: 12px;
    border: 1px solid transparent;
    background: linear-gradient(135deg, rgba(20, 20, 20, 0.8), rgba(15, 15, 15, 0.9));
    backdrop-filter: blur(10px);
    overflow: hidden;
    transition: all 320ms ease;
}

.problem-card::before,
.solution-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 12px;
    opacity: 0;
    transition: opacity 320ms ease;
    z-index: -1;
}

.problem-card::before {
    background: linear-gradient(135deg, rgba(255, 85, 85, 0.08), rgba(255, 153, 85, 0.05));
    border: 1px solid rgba(255, 85, 85, 0.15);
}

.solution-card::before {
    background: linear-gradient(135deg, rgba(124, 255, 31, 0.08), rgba(57, 255, 20, 0.05));
    border: 1px solid rgba(124, 255, 31, 0.15);
}

.problem-card-wrapper:hover .problem-card::before,
.solution-card-wrapper:hover .solution-card::before {
    opacity: 1;
}

.problem-kicker {
    color: #ff5555 !important;
}

.solution-kicker {
    color: #7cff1f !important;
}

.problem-title,
.solution-title {
    font-size: clamp(1.4rem, 3vw, 2rem);
    margin: 0 0 1.2rem;
    line-height: 1.4;
    font-weight: 600;
}

.problem-title {
    color: #ffaaaa;
}

.solution-title {
    color: #d4ff99;
}

.problem-sub {
    margin: 0.8rem 0;
    color: #c8c8c8;
    line-height: 1.6;
    font-size: 0.95rem;
}

.problem-insights,
.solution-benefits {
    margin-top: 1.8rem;
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
}

.insight-item {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    color: #d0d0d0;
    font-size: 0.94rem;
    line-height: 1.5;
}

.insight-dot {
    color: #ff5555;
    font-size: 1.2rem;
    flex-shrink: 0;
}

.solution-benefits {
    list-style: none;
    padding: 0;
}

.solution-benefits li {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 0.6rem 0;
    color: #d0d0d0;
    font-size: 0.94rem;
    line-height: 1.6;
}

.insight-item {
    color: #7cff1f;
    font-weight: 600;
}

.divider-arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    min-height: 300px;
    color: rgba(124, 255, 31, 0.3);
    animation: arrowBounce 2s ease-in-out infinite;
}

.divider-arrow svg {
    width: 40px;
    height: 200px;
}

@keyframes arrowBounce {

    0%,
    100% {
        transform: translateY(0);
        opacity: 0.5;
    }

    50% {
        transform: translateY(8px);
        opacity: 0.8;
    }
}

/* FEATURES GRID */
.features-header {
    margin-bottom: 3.5rem;
    text-align: center;
}

.features-title {
    margin: 0.8rem 0 0;
    font-size: clamp(1.8rem, 4vw, 2.6rem);
    color: #e0e0e0;
    font-weight: 600;
    line-height: 1.3;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    max-width: 1400px;
    margin: 0 auto;
}

.feature-card {
    position: relative;
    padding: 2.2rem 2rem;
    border-radius: 14px;
    border: 1px solid rgba(124, 255, 31, 0.12);
    background: linear-gradient(135deg, rgba(20, 30, 15, 0.6), rgba(12, 18, 8, 0.8));
    backdrop-filter: blur(12px);
    overflow: hidden;
    transition: all 280ms cubic-bezier(0.34, 1.56, 0.64, 1);
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 100%;
    background: radial-gradient(circle at 30% 30%, rgba(124, 255, 31, 0.06), transparent 50%);
    pointer-events: none;
    opacity: 0;
    transition: opacity 280ms ease;
}

.feature-card:hover::before {
    opacity: 1;
}

.feature-card:hover {
    border-color: rgba(124, 255, 31, 0.35);
    background: linear-gradient(135deg, rgba(30, 45, 20, 0.8), rgba(18, 26, 12, 0.95));
    box-shadow: 0 8px 32px rgba(124, 255, 31, 0.12), inset 0 1px 0 rgba(124, 255, 31, 0.1);
}

@keyframes badgePulse {

    0%,
    100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.15);
    }
}

.feature-card h3 {
    margin: 0 0 0.8rem;
    font-size: 1.3rem;
    color: #e8e8e8;
    font-weight: 600;
}

.feature-card p {
    margin: 0;
    color: #c0c0c0;
    font-size: 0.95rem;
    line-height: 1.6;
}

.feature-accent {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #7cff1f, transparent);
    opacity: 0;
    transition: opacity 280ms ease;
}

.feature-card:hover .feature-accent {
    opacity: 1;
}

@media (max-width: 900px) {
    .problem-solution-container {
        grid-template-columns: 1fr;
        gap: 2rem;
    }

    .divider-arrow {
        display: none;
    }

    .features-grid {
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 1.5rem;
    }
}

@media (max-width: 600px) {
    .problem-solution-container {
        gap: 1.5rem;
    }

    .problem-card,
    .solution-card {
        padding: 1.8rem 1.5rem;
    }

    .features-grid {
        grid-template-columns: 1fr;
        gap: 1.2rem;
    }

    .feature-card {
        padding: 1.8rem 1.5rem;
    }
}

.features-list {
    max-width: 920px;
    column-count: 2;
    column-gap: 2.6rem;
}

.features-list li {
    margin-bottom: 0.7rem;
    break-inside: avoid;
}

.features-flow,
.how-flow {
    max-width: 1040px;
}

/* HOW IT WORKS */
.how-header {
    margin-bottom: 3.5rem;
    text-align: center;
    overflow: hidden;
    position: relative;
    z-index: 1;
}

.how-header .step-num {
    display: none !important;
}

.how-steps-flow .step-num {
    display: none !important;
}

.how-steps-flow {
    position: relative;
    z-index: 2;
}

.how-title {
    margin: 0.8rem 0 0;
    font-size: clamp(1.8rem, 4vw, 2.6rem);
    color: #e0e0e0;
    font-weight: 600;
    line-height: 1.3;
}

.how-steps {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    align-items: center;
}

.how-step {
    position: relative;
    padding: 2.5rem 2rem;
    border-radius: 12px;
    border: 1px solid rgba(124, 255, 31, 0.15);
    background: linear-gradient(135deg, rgba(20, 30, 15, 0.5), rgba(12, 18, 8, 0.7));
    backdrop-filter: blur(10px);
    text-align: center;
    transition: all 280ms cubic-bezier(0.34, 1.56, 0.64, 1);
}

.how-step:hover {
    border-color: rgba(124, 255, 31, 0.35);
    background: linear-gradient(135deg, rgba(30, 45, 20, 0.7), rgba(18, 26, 12, 0.9));
    box-shadow: 0 8px 32px rgba(124, 255, 31, 0.12);
}

.step-num {
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7cff1f, #39FF14);
    color: #000;
    font-weight: 700;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 16px rgba(124, 255, 31, 0.28);
}

.step-num {
    margin: 1.2rem 0 0.8rem;
    font-size: 1.3rem;
    color: #e8e8e8;
    font-weight: 600;
}

.how-step p {
    margin: 0;
    color: #c0c0c0;
    font-size: 0.95rem;
    line-height: 1.6;
}

.step-connector {
    display: flex;
    align-items: center;
    justify-content: center;
    grid-column: span 1;
    height: 100%;
    min-height: 20px;
    opacity: 0.6;
    transition: opacity 280ms ease;
}

.step-connector:hover {
    opacity: 1;
}

.step-connector svg {
    width: 100%;
    height: 40px;
}

@media (max-width: 900px) {
    .how-steps {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }

    .step-connector {
        display: none;
    }
}

/* WHO BENEFITS */
.target-header {
    margin-bottom: 3.5rem;
    text-align: center;
}

.target-title {
    margin: 0.8rem 0 0;
    font-size: clamp(1.8rem, 4vw, 2.6rem);
    color: #e0e0e0;
    font-weight: 600;
    line-height: 1.3;
}

.target-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.target-user-card {
    position: relative;
    padding: 2.5rem 2rem;
    border-radius: 12px;
    border: 1px solid rgba(124, 255, 31, 0.12);
    background: linear-gradient(135deg, rgba(20, 30, 15, 0.6), rgba(12, 18, 8, 0.8));
    backdrop-filter: blur(12px);
    text-align: center;
    overflow: hidden;
    transition: all 320ms cubic-bezier(0.34, 1.56, 0.64, 1);
}

.target-user-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(124, 255, 31, 0.08), transparent 70%);
    opacity: 0;
    transition: opacity 320ms ease;
    z-index: 0;
}

.target-user-card:hover::before {
    opacity: 1;
}

.target-user-card:hover {
    border-color: rgba(124, 255, 31, 0.35);
    background: linear-gradient(135deg, rgba(30, 45, 20, 0.8), rgba(18, 26, 12, 0.95));
    box-shadow: 0 12px 48px rgba(124, 255, 31, 0.15);
}

.target-user-card h3 {
    position: relative;
    z-index: 1;
    margin: 0 0 0.8rem;
    font-size: 1.35rem;
    color: #e8e8e8;
    font-weight: 600;
}

.target-user-card p {
    position: relative;
    z-index: 1;
    margin: 0 0 1.5rem;
    color: #c0c0c0;
    font-size: 0.95rem;
    line-height: 1.6;
}

.user-badge {
    position: relative;
    z-index: 1;
    display: inline-block;
    padding: 0.6rem 1.2rem;
    border-radius: 20px;
    background: rgba(124, 255, 31, 0.12);
    border: 1px solid rgba(124, 255, 31, 0.25);
    color: #7cff1f;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    transition: all 280ms ease;
}

.target-user-card:hover .user-badge {
    background: rgba(124, 255, 31, 0.22);
    border-color: rgba(124, 255, 31, 0.4);
}

@media (max-width: 900px) {
    .target-grid {
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 1.5rem;
    }

    .target-user-card {
        padding: 2rem 1.5rem;
    }
}

.steps-track {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.85rem;
    align-items: center;
    max-width: 660px;
    margin: 0 auto;
}

.step-chip {
    border: 1px solid rgba(188, 188, 188, 0.2);
    background: linear-gradient(160deg, rgba(15, 15, 15, 0.62), rgba(8, 8, 8, 0.7));
    padding: 1.15rem 1.15rem;
    color: #d2d2d2;
    min-height: 98px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 1.03rem;
    transition: border-color 180ms ease, transform 180ms ease;
    border-radius: 14px;
}

.step-chip:hover {
    border-color: rgba(124, 255, 31, 0.32);
    transform: translateY(-2px);
}

.flow-arrow {
    color: rgba(212, 212, 212, 0.74);
    font-family: "Sora", sans-serif;
    font-size: 1.1rem;
    letter-spacing: 0.1em;
    justify-self: center;
    transform: rotate(90deg);
    animation: arrowPulse 2.6s ease-in-out infinite;
}

@keyframes arrowPulse {

    0%,
    100% {
        opacity: 0.35;
        transform: translateX(0);
    }

    50% {
        opacity: 0.9;
        transform: translateX(4px);
    }
}

.target-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.35rem;
}

.closing-note p {
    margin: 0;
    color: #c7c7c7;
    line-height: 1.75;
    font-size: 1.14rem;
}

.interactive-footnote {
    margin: 0.7rem 0 0;
    font-size: 0.66rem;
    line-height: 1.5;
    letter-spacing: 0.02em;
    color: rgba(200, 213, 180, 0.75);
}

.roadmap-wrap {
    max-width: 980px;
    margin: 0 auto;
    padding: 120px 22px 56px;
    text-align: center;
    font-family: "Rajdhani", "Space Grotesk", sans-serif;
}

.eyebrow {
    margin: 0;
    color: var(--orange);
    text-transform: uppercase;
    letter-spacing: 0.24em;
    font-size: 0.68rem;
}

.section-title {
    margin: 14px 0 8px;
    font-family: "Bebas Neue", "Oswald", sans-serif;
    letter-spacing: 0.06em;
    color: var(--green);
    font-size: clamp(1.9rem, 5vw, 3rem);
}

.roadmap-copy {
    margin: 0 auto;
    max-width: 580px;
    color: var(--text-dim);
    font-size: 1rem;
}

.roadmap-list {
    margin-top: 34px;
    display: grid;
    gap: 12px;
}

.roadmap-item {
    text-align: left;
    border: 1px solid var(--line);
    background: var(--panel);
    padding: 16px 16px;
    display: grid;
    grid-template-columns: 56px 1fr;
    grid-template-areas:
        "tag title"
        "tag desc";
    column-gap: 12px;
    align-items: center;
}

.roadmap-item span {
    grid-area: tag;
    color: var(--orange);
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    border: 1px solid #4f3a1f;
    padding: 4px 6px;
    text-align: center;
}

.roadmap-item h2 {
    grid-area: title;
    margin: 0;
    font-size: 1rem;
    color: var(--green);
    font-family: "Bebas Neue", "Oswald", sans-serif;
    letter-spacing: 0.06em;
    font-weight: 600;
}

.roadmap-item p {
    grid-area: desc;
    margin: 4px 0 0;
    color: var(--text-dim);
    font-size: 0.88rem;
    line-height: 1.45;
}

@media (max-width: 560px) {
    .top-nav {
        padding: 16px;
    }

    .brand-mark {
        font-size: 0.9rem;
    }

    .nav-button {
        font-size: 0.62rem;
        padding: 0.52rem 0.75rem;
    }

    .home-hero,
    .roadmap-wrap {
        padding: 108px 16px 44px;
    }

    .content-layer {
        padding: 7.4rem 0.95rem 4.8rem;
        gap: 3.2rem;
    }

    .content-layer::before {
        left: 0.45rem;
        top: 7.9rem;
        bottom: 5.2rem;
    }

    .scan-line-1 {
        font-size: 1.52rem;
    }

    .scan-line-2 {
        font-size: 1.06rem;
    }

    .problem-float,
    .solution-float {
        font-size: 1.28rem;
    }

    .features-list {
        column-count: 1;
    }

    .steps-track {
        gap: 0.75rem;
    }

    .flow-arrow {
        justify-self: center;
        transform: rotate(90deg);
        font-size: 0.9rem;
    }

    .target-grid {
        grid-template-columns: 1fr;
    }

    .roadmap-item {
        grid-template-columns: 1fr;
        grid-template-areas:
            "tag"
            "title"
            "desc";
        row-gap: 8px;
    }

    .roadmap-item span {
        width: fit-content;
    }
}

.rotating-feature {
    max-width: 920px;
}

.rotating-header-wrapper {
    display: flex;
    align-items: baseline;
    gap: 0.8rem;
    flex-wrap: wrap;
}

.rotating-label {
    margin: 0;
    font-family: "Sora", sans-serif;
    font-size: clamp(1.3rem, 2.4vw, 1.8rem);
    color: #d7d7d7;
    font-weight: 500;
}

.rotating-text-main {
    font-family: "Sora", sans-serif;
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    font-weight: 600;
    color: var(--green);
    letter-spacing: 0.02em;
    display: inline-flex;
    align-items: baseline;
    margin: 0;
}

/* ---- NEW INTERACTIVE SECTIONS ---- */
.stats-section {
    margin: 4rem 0;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 2rem;
    padding: 2rem 0;
}

.stat-card {
    padding: 1.5rem;
    background: rgba(17, 17, 17, 0.6);
    border: 1px solid var(--line);
    border-radius: 8px;
    text-align: center;
    transition: all 0.3s ease;
}

.stat-card:hover {
    border-color: var(--green);
    box-shadow: 0 0 20px rgba(60, 255, 20, 0.1);
    transform: translateY(-4px);
}

.stat-card p {
    margin-top: 0.8rem;
    color: var(--text-dim);
    font-size: 0.9rem;
}

.features-cards-section {
    margin: 4rem 0;
}

.feature-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    padding: 2rem 0;
}

.cta-section {
    margin: 4rem 0;
}

.cta-content {
    padding: 3rem 2rem;
    background: linear-gradient(135deg, rgba(17, 17, 17, 0.8) 0%, rgba(30, 30, 30, 0.6) 100%);
    border: 1px solid var(--line);
    border-radius: 12px;
    text-align: center;
}

.cta-content h2 {
    font-family: "Sora", sans-serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    line-height: 1.3;
    margin: 0 0 1.5rem;
    color: #d7d7d7;
    font-weight: 600;
}

.cta-buttons {
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 2rem;
}

/* ======== PLASMA CANVAS OPACITY IN LIGHT MODE ======== */
#plasma,
.plasma-canvas {
    transition: opacity 0.3s ease;
}

[data-theme="light"] #plasma,
[data-theme="light"] .plasma-canvas,
[data-theme="light"] .plasma-container,
html.light-mode #plasma,
html.light-mode .plasma-canvas,
html.light-mode .plasma-container {
    opacity: 0.3 !important;
}
```

---

## [76] frontend/tailwind.config.js
**Size:** 206.0B

```javascript
/** @type {import('tailwindcss').Config} */
export default {
    content: ["./index.html", "./roadmap.html", "./src/**/*.{js,jsx,ts,tsx}"],
    theme: {
        extend: {},
    },
    plugins: [],
};
```

---

## [77] frontend/vite.config.js
**Size:** 410.0B

```javascript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "node:path";

export default defineConfig({
    plugins: [react()],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "./src"),
        },
    },
    build: {
        rollupOptions: {
            input: {
                main: "index.html"
            }
        }
    }
});
```

---

## [78] mcp/ANTIGRAVITY_WORKFLOW.md
**Size:** 5.0KB

```markdown
# Antigravity MCP Workflow for RepoScan Continuous Intelligence

## Goal

Make Antigravity keep MCP memory in sync whenever the main Claude agent changes code, fixes issues, or introduces new ones.

## Required MCP Server

Register the RepoScan MCP server using either:

- [antigravity.mcp.template.json](c:/Users/Mukul%20Prasad/Desktop/PROJECTS/New%20folder/an/githoppermain/plugins/antigravity-reposcan-mcp/antigravity.mcp.template.json#L1)
- or the plugin-managed server entry in [plugins/antigravity-reposcan-mcp/.mcp.json](c:/Users/Mukul%20Prasad/Desktop/PROJECTS/New%20folder/an/githoppermain/plugins/antigravity-reposcan-mcp/.mcp.json#L1)

## Core MCP Calls

### Tools

- `continuous_scan(repo_url, branch_name, generate_fixes)`
- `sync_agent_change(repo_url, branch_name, command_name, notes, generate_fixes)`
- `get_issue_delta(repo_id)`
- `get_unresolved_issues(repo_id)`

### Resources

- `repomemory://context/{repo_id}`
- `repomemory://delta/{repo_id}`
- `repomemory://commands/{repo_id}`
- `repomemory://unresolved/{repo_id}`

## Recommended Antigravity Lifecycle

### 1. Session start

When Antigravity opens a repo or starts a task:

1. call `continuous_scan`
2. store returned `repo_id`
3. load:
   - `repomemory://context/{repo_id}`
   - `repomemory://delta/{repo_id}`
   - `repomemory://unresolved/{repo_id}`

Purpose:

- seed Claude with prior unresolved issues
- seed Claude with recent fixes and trend context

### 2. After Claude edits code

Whenever the main Claude agent:

- edits files
- applies a patch
- resolves a bug
- changes dependencies
- modifies configuration

Antigravity should immediately call:

```json
{
  "tool": "sync_agent_change",
  "arguments": {
    "repo_url": "https://github.com/owner/repo",
    "branch_name": "main",
    "command_name": "apply_patch",
    "notes": "Claude updated auth middleware and removed unsafe eval usage.",
    "generate_fixes": true
  }
}
```

Then reload:

- `repomemory://context/{repo_id}`
- `repomemory://delta/{repo_id}`
- `repomemory://commands/{repo_id}`

Purpose:

- MCP reflects new issues introduced by the latest change
- MCP reflects solved issues from the latest change
- Claude gets refreshed repo memory after its own actions

### 3. Before Claude plans next action

Antigravity should inject the refreshed MCP context into Claude’s next reasoning cycle:

- unresolved issues
- latest issue delta
- recent command events
- per-file history from `context`

That makes the system self-updating instead of static.

## Practical Host Rules

Antigravity should call `sync_agent_change` when:

- a write/edit tool succeeds
- a commit is created
- a dependency file changes
- a config/security-sensitive file changes
- Claude explicitly says an issue was fixed

Antigravity should not call it when:

- Claude only reads files
- Claude only chats/explains
- no code or repo state changed

## Minimal Orchestration Template

Use this host-side sequence:

```text
On repo open:
  1. MCP tool: continuous_scan
  2. MCP resource: repomemory://context/{repo_id}
  3. MCP resource: repomemory://delta/{repo_id}

On successful Claude write/edit:
  1. MCP tool: sync_agent_change
  2. MCP resource: repomemory://context/{repo_id}
  3. MCP resource: repomemory://delta/{repo_id}
  4. MCP resource: repomemory://commands/{repo_id}

On follow-up reasoning:
  Include latest delta + unresolved issue context in Claude prompt.
```

## Antigravity Config Shape

If Antigravity supports an MCP server registry config, use something like:

```json
{
  "mcpServers": {
    "reposcan-continuous-intelligence": {
      "command": "python",
      "args": [
        "c:/Users/Mukul Prasad/Desktop/PROJECTS/New folder/an/githoppermain/backend/mcp_runtime_server.py"
      ],
      "cwd": "c:/Users/Mukul Prasad/Desktop/PROJECTS/New folder/an/githoppermain/backend",
      "env": {
        "MCP_TRANSPORT": "stdio",
        "GITHUB_TOKEN": "REPLACE_WITH_YOUR_TOKEN"
      }
    }
  }
}
```

## Suggested Event Mapping

Map Antigravity events to MCP calls like this:

- `session_started` -> `continuous_scan`
- `file_write_completed` -> `sync_agent_change`
- `patch_applied` -> `sync_agent_change`
- `commit_created` -> `sync_agent_change`
- `task_completed` -> reload `repomemory://delta/{repo_id}`

## What Antigravity Should Show in UI

After every sync cycle, display:

- new issues
- resolved issues
- persisting issues
- last synced command
- latest health score
- latest scanned commit

## Recommended Prompt Injection Block

Antigravity can prepend something like this to Claude after every sync:

```text
Repo memory refreshed.
Latest delta:
- New issues: 2
- Resolved issues: 1
- Persisting issues: 3

Recent command:
- apply_patch: Claude updated auth middleware

Use this updated repo memory before making the next code change.
```

## Final Recommendation

For your setup:

1. Keep UI testing through Flask
2. Keep plugin registration for Antigravity
3. Make Antigravity call `sync_agent_change` after every successful write action
4. Reload `context`, `delta`, and `commands` resources right after that

That gives you the “live MCP intelligence layer” behavior you were asking for.


```

---

## [79] mcp/MCP_CONTINUOUS_INTELLIGENCE_PLAN.md
**Size:** 16.4KB

```markdown
# MCP Continuous Intelligence Layer for RepoScan AI

## Goal

Transform the current one-time RepoScan flow into a non-breaking extension layer that adds:

- Persistent memory
- Incremental scanning
- Context-aware Bedrock prompting
- Auto-fix generation
- Fix validation
- Continuous watch mode
- Better reporting for trends and quick wins

Tagline:

> From static analysis to continuous intelligent code improvement with memory and optimization.

## What I Added in This Repo

This implementation starts the extension as a plug-in style backend layer under `backend/mcp_server/`.

It does not replace the existing pipeline.
It adds a new parallel path and integration endpoints:

- New MCP memory store
- Incremental diff tracker
- Context injection wrapper for LLM analysis
- Prompt optimization layer
- Auto-fix generation and validation
- Watch mode manager
- New Flask APIs for continuous analysis

## Existing System Mapping

Current:

`fetch -> chunk -> Bedrock -> scoring -> UI`

Extended:

`fetch -> diff check -> MCP context injection -> optimized analysis -> scoring -> MCP memory update -> UI`

The original `/api/analyze` route remains available.
The extension uses new routes so existing behavior stays intact.

## New Files and Responsibilities

- `backend/mcp_server/storage.py`
  Lightweight SQLite memory store for scans, snapshots, issues, and fixes.
- `backend/mcp_server/diffing.py`
  Hash-based incremental scan logic.
- `backend/mcp_server/context.py`
  Builds history-aware context for the next analysis.
- `backend/mcp_server/prompting.py`
  Prompt profile routing and context injection helpers.
- `backend/mcp_server/analyzer.py`
  Wrapper over Bedrock/static analysis with strict JSON prompts and MCP context.
- `backend/mcp_server/autofix.py`
  Auto-fix proposal generation plus validation loop.
- `backend/mcp_server/watcher.py`
  Continuous scan manager using background polling.
- `backend/mcp_server/continuous_pipeline.py`
  Non-breaking orchestrator for continuous intelligence mode.

## Step-by-Step Architecture

### Step 1. Fetch Repo Metadata and Files

Uses the current GitHub fetch layer.

Inputs:

- `repo_url`
- `branch_name`
- optional `github_token`

No change needed from you yet.

Local in this repo now:

- Flask route receives the request.
- Python backend uses the existing fetch logic directly inside the app process.
- Files are pulled into local runtime memory for the duration of the scan.
- If a token is used, it is passed from local environment variables or request configuration.
- This is the fastest way to demo because there is no extra infrastructure between request and scan.

Future in AWS:

- API Gateway or an ALB can receive the request instead of a local Flask-only entrypoint.
- A Lambda function, ECS task, or containerized backend service can perform the GitHub fetch.
- GitHub credentials should move into AWS Secrets Manager instead of staying only in local `.env` style config.
- Large repo fetches can be queued through SQS so user requests do not wait on long scans synchronously.
- For webhook-driven scanning later, GitHub events can trigger EventBridge or an API endpoint instead of manual local polling.

### Step 2. Build Snapshot Metadata

For every fetched file we store metadata only:

- file path
- language
- size
- content hash
- debt signal count
- last seen time

We do not store the full repo code in MCP memory.

Local in this repo now:

- Snapshot metadata is created in Python in the same backend process that fetched the repo.
- Metadata is written into local SQLite through `backend/mcp_server/storage.py`.
- The database file lives on the local machine or local server disk.
- Hashing and signal counting happen inline during the scan request or watch cycle.
- This keeps setup simple and avoids cloud dependencies for the hackathon version.

Future in AWS:

- The same metadata model can be stored in DynamoDB for shared, durable scan history.
- If report exports are needed, summaries can also be written to S3.
- Compute for hashing and metadata extraction can still run in Lambda, ECS, or EC2 workers.
- DynamoDB partitioning can be based on `repo_id`, branch, and snapshot timestamp for efficient history lookup.
- Encryption at rest and IAM-based access control become standard instead of relying on local machine security.

### Step 3. Compute Incremental Changes

The diff tracker compares the latest snapshot against the previous snapshot and marks:

- `new_files`
- `modified_files`
- `deleted_files`
- `unchanged_files`

Scan scope becomes:

- new files
- modified files
- files with unresolved issues from prior scans

This is where token and cost reduction happens.

Local in this repo now:

- `backend/mcp_server/diffing.py` compares the new local snapshot with the previous snapshot from SQLite.
- The comparison happens inside one Python process, so there is no network hop between memory and storage.
- The backend decides immediately which files need re-analysis before sending anything to Bedrock.
- This reduces tokens even in local mode because unchanged files are skipped.
- Watch mode can re-use the same logic repeatedly on the same machine.

Future in AWS:

- The diff operation can run in stateless workers that pull prior snapshot metadata from DynamoDB.
- Incremental scan jobs can be triggered by SQS messages, EventBridge schedules, or GitHub webhooks.
- For bigger repos, diffing can be split into background jobs instead of blocking the API request.
- The result of the diff step can be stored as a scan manifest in DynamoDB or S3 so downstream workers know exactly what to analyze.
- This makes horizontal scaling easier because workers do not depend on one local SQLite file.

### Step 4. Inject Historical Context

Before Bedrock is called, the wrapper adds:

- unresolved prior issues for the file
- recent resolved issues for the file
- repo trend summary
- chunk-local debt signals
- prompt profile based on file type

Example:

```text
Previously detected in auth.py:
- 2 issues total
- 1 resolved
- 1 unresolved: HARDCODED_SECRET
Analyze the current chunk with this history in mind.
```

Local in this repo now:

- `backend/mcp_server/context.py` reads prior issue history from local SQLite.
- Context is assembled in memory right before the prompt is sent.
- The current Flask app remains the orchestrator, so prompt enrichment is just a backend wrapper around the existing analysis flow.
- There is no separate cache layer yet; history lookup is local and lightweight.
- This is enough to prove memory-aware analysis without adding cloud architecture.

Future in AWS:

- Context retrieval can read from DynamoDB and optionally cache hot repo summaries in ElastiCache if needed later.
- Prompt assembly can run in Lambda/ECS workers close to the Bedrock calling layer.
- If multiple services need the same context, a dedicated context service or MCP API layer can expose normalized history lookups.
- Large trend summaries can be precomputed and stored instead of built every time on demand.
- IAM, audit logging, and centralized observability become easier once context generation is moved into AWS-managed infrastructure.

### Step 5. Dynamic Prompt Optimization

Prompt profile is selected by file kind:

- config and infra files -> configuration/security profile
- dependency manifests -> dependency vulnerability profile
- application source -> code logic + security profile

Output is forced into strict JSON-compatible structure.

Local in this repo now:

- `backend/mcp_server/prompting.py` can keep prompt templates and routing rules in local Python code.
- The local backend decides which profile to apply before each Bedrock request.
- Template edits are simple code changes in the repo, which is ideal while prompt strategy is still changing fast.
- Strict JSON output handling is validated in the backend before results continue to scoring.
- This keeps prompt experimentation easy during development.

Future in AWS:

- Prompt profiles can remain in code or move to a managed config source such as AppConfig, S3, or DynamoDB.
- Different environments can use different prompt versions without changing application code on every tweak.
- A/B testing of prompt variants becomes easier when workers read versioned config from AWS-managed storage.
- Centralized prompt config also helps if multiple scan workers or services need consistent behavior.
- Bedrock remains the model endpoint, but the prompt-governance layer becomes easier to manage at scale.

### Step 6. Score Without Breaking Existing Contracts

The extension prepares scoring input compatible with the existing scorer:

- `security_findings`
- `debt_findings`
- `repo_id`
- `repo_url`

It then returns the original-style score block plus a new `continuous_intelligence` section.

Local in this repo now:

- The current backend can call the existing scorer directly after the MCP-enhanced analysis step.
- Response shaping happens inside the same Flask request lifecycle.
- Frontend compatibility is protected because the original response fields remain unchanged.
- The added `continuous_intelligence` block is generated locally and returned immediately.
- This is the safest integration path because it does not force frontend rewrites.

Future in AWS:

- The scoring service can stay embedded in one backend or be separated into its own Lambda/service if traffic grows.
- API Gateway can expose the same contract externally while internal workers generate the payload.
- Shared schemas can be versioned so old clients keep working while new clients consume extra fields.
- If analytics grow, score history can also be pushed into S3, DynamoDB, or an analytics store for trend dashboards.
- The contract remains the same, but transport and persistence become cloud-managed.

### Step 7. Auto-Fix and Validation Loop

For issues found in the latest scan:

1. Generate fix proposal
2. Build remediated code and diff patch
3. Re-analyze remediated code
4. Mark fix status:
   - `VALIDATED`
   - `PARTIAL`
   - `FAILED`

The current implementation includes heuristic fixes for:

- hardcoded secrets
- unsafe `eval`
- some dependency upgrade cases

And leaves room for Bedrock-powered fix generation when AWS credentials are active.

Local in this repo now:

- `backend/mcp_server/autofix.py` can generate heuristic patches directly in the backend process.
- Validation can re-run analysis locally against the remediated content before marking status.
- Patch preview can stay in memory or be stored in SQLite with fix status metadata.
- This is good for demoing safe suggestion loops without needing GitHub write access yet.
- If Bedrock credentials are already configured locally, the same flow can later switch from heuristics to LLM-assisted fixes.

Future in AWS:

- Fix generation can run as queued jobs using SQS plus Lambda/ECS workers, especially for expensive model calls.
- Validation can be expanded into isolated workers or CodeBuild jobs that run tests, linters, and policy checks.
- Generated patches can be stored in S3, DynamoDB, or a fix-history table for auditing.
- Secrets Manager should hold GitHub tokens if the system later opens PRs automatically.
- This step benefits a lot from AWS because fix generation and validation are the most bursty and compute-heavy parts of the pipeline.

### Step 8. Continuous Watch Mode

Background polling loop:

1. Fetch latest repo state
2. Run incremental scan
3. Update memory
4. Expose status to UI

This is demo-friendly and hackathon-safe.

Local in this repo now:

- `backend/mcp_server/watcher.py` can run a background polling thread inside the Flask backend process.
- Watch state can be tracked in local memory and/or SQLite.
- The UI can query the backend directly for status using the new watch endpoints.
- This is simple to build and works well while one demo server is running.
- The tradeoff is that watch jobs disappear if the local process restarts.

Future in AWS:

- EventBridge Scheduler can trigger periodic scans without depending on one always-on local process.
- SQS can buffer watch jobs so scans are resilient and retryable.
- Lambda, ECS, or Step Functions can execute each scheduled scan independently.
- CloudWatch Logs and metrics can track failures, durations, and scan frequency centrally.
- This is the right long-term model if multiple repos, users, or organizations need reliable continuous monitoring.

## New APIs

Implemented or scaffolded:

- `POST /api/analyze/continuous`
- `POST /api/continuous/start`
- `GET /api/continuous/status/<watch_id>`
- `POST /api/continuous/stop/<watch_id>`
- `GET /api/mcp/context/<repo_id>`
- `GET /api/mcp/unresolved/<repo_id>`
- `POST /api/mcp/fix-status`

Core MCP storage methods:

- `store_scan_results()`
- `get_context()`
- `get_unresolved_issues()`
- `update_fix_status()`

## Response Additions

The extension returns a new block like:

```json
{
  "continuous_intelligence": {
    "scan_mode": "full_or_incremental",
    "files_considered": 12,
    "files_scanned": 4,
    "new_issues": 3,
    "resolved_issues": 1,
    "persisting_issues": 2,
    "estimated_fix_minutes": 55,
    "history_depth": 4,
    "trend": {
      "previous_health_score": 71,
      "current_health_score": 78,
      "delta": 7
    }
  }
}
```

This is safe for the frontend because it is additive.

## What I Still Need From You

These are not blockers for the starter implementation, but they will improve the final hackathon version:

### Needed Soon

- A decision on whether MCP memory should stay local SQLite for demo, or move to managed AWS storage.
- Confirmation on whether watch mode can be simple polling, or if you want webhook/event-driven behavior.
- Confirmation on whether fix patches should be preview-only, or later pushed into GitHub PRs.

### Needed For Production-Like Version

- AWS account access details for the final deployment target
- Bedrock model preference:
  - Claude on Bedrock only
  - Claude + Gemini abstraction
  - fully provider-agnostic model gateway
- Whether you want issue/fix history stored per branch or only per repo
- Whether GitHub App auth is available for richer repo polling and PR automation

### Needed If You Want PR Automation Next

- GitHub token or GitHub App credentials
- repo write permissions
- preferred branch naming convention for generated fix branches

## AWS / Tech Stack by Phase

### Phase 1. Hackathon-Minimum

Already sufficient:

- Flask
- Python stdlib `sqlite3`
- existing Bedrock integration
- background polling thread in backend process

Optional AWS:

- none required

### Phase 2. Better Demo Stability

Recommended:

- Amazon EventBridge Scheduler for periodic scans
- DynamoDB instead of SQLite for shared history
- S3 for scan summaries and exported reports
- CloudWatch Logs for watch-mode observability

### Phase 3. Production Upgrade

Recommended:

- API Gateway + Lambda for MCP API layer
- DynamoDB for scan memory
- SQS for queued scan jobs
- EventBridge for continuous scheduling
- Secrets Manager for tokens
- Step Functions for multi-stage scan/fix/validate orchestration

### Phase 4. Auto-Fix PR Workflow

Recommended:

- GitHub App
- SQS or Step Functions for queued fix runs
- Lambda workers for patch generation
- optional CodeBuild for validation/test execution

## Suggested Delivery Plan

### Milestone 1

- MCP storage
- incremental scans
- context injection
- continuous analysis endpoint

### Milestone 2

- watch mode
- auto-fix generation
- validation loop
- enhanced reporting payload

### Milestone 3

- frontend dashboard widgets for:
  - new vs resolved
  - trend chart
  - quick wins
  - total fix time

### Milestone 4

- GitHub PR automation
- managed AWS persistence
- event-driven scanning

## Risks and How This Starter Handles Them

### Risk: MCP failure breaks scanning

Mitigation:

- extension catches MCP errors
- scan can still continue with best-effort analysis

### Risk: Full repo re-scan cost

Mitigation:

- hash-based changed file detection
- unresolved issue carry-forward only

### Risk: Storing sensitive code

Mitigation:

- snapshot store keeps metadata, hashes, summaries
- full code stays transient in request-time memory only

### Risk: Auto-fix is unreliable

Mitigation:

- validation loop
- explicit status: `VALIDATED`, `PARTIAL`, `FAILED`

## Recommended Next Input From You

Reply with any of these if you want me to take the next step:

1. "Keep it hackathon-local" -> I will keep SQLite + polling and extend the UI next.
2. "Make it AWS-ready" -> I will add deployment-oriented config and managed-service adapters.
3. "Add GitHub PR autofix" -> I will scaffold PR branch/patch flow next.
4. "Build the UI cards now" -> I will connect frontend pages to the new continuous endpoints.

```

---

## [80] mcp/MCP_SERVER_TEST_AND_INTEGRATION.md
**Size:** 5.4KB

```markdown
# RepoScan MCP Server: Test First, Then Integrate into Antigravity

## Important Clarification

There are now two layers in this repo:

1. The internal continuous intelligence backend extension under `backend/mcp_server/`
2. A formal MCP protocol wrapper at `backend/mcp_runtime_server.py`

The wrapper exposes the extension through real MCP tools and resources so you can load it in an MCP host.

## Files You Need

- `backend/mcp_runtime_server.py`
- `backend/requirements-mcp.txt`

## What This MCP Server Exposes

### Tools

- `continuous_scan(repo_url, branch_name="main", generate_fixes=True)`
- `sync_agent_change(repo_url, branch_name="main", command_name="agent_change", notes="", generate_fixes=True)`
- `get_unresolved_issues(repo_id)`
- `get_issue_delta(repo_id)`
- `update_fix_status(...)`

### Resources

- `repomemory://context/{repo_id}`
- `repomemory://unresolved/{repo_id}`
- `repomemory://delta/{repo_id}`
- `repomemory://commands/{repo_id}`

## Step 1. Install MCP SDK

From the repo root:

```powershell
cd backend
python -m pip install -r requirements-mcp.txt
```

Official references:

- MCP Python SDK quick example: https://py.sdk.modelcontextprotocol.io/
- MCP server quickstart: https://modelcontextprotocol.io/quickstart/server
- MCP transports: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports

## Step 2. Test It Locally in STDIO Mode

STDIO is the most common way hosts launch an MCP server.

Run:

```powershell
cd backend
$env:GITHUB_TOKEN="your_token_here"
python mcp_runtime_server.py
```

Important:

- Do not add `print()` statements to stdout in a stdio MCP server.
- This server uses logging instead.

## Step 3. Test It with MCP Inspector

The official docs show using the Inspector to connect to MCP servers.

One common approach is:

```powershell
npx -y @modelcontextprotocol/inspector
```

Then configure the server command roughly as:

- Command: `python`
- Args: `mcp_runtime_server.py`
- Working directory: your `backend` folder

After connecting, call:

- `continuous_scan`
- `get_unresolved_issues`

## Step 4. Optional HTTP Test Mode

If you want browser-style inspection instead of stdio:

```powershell
cd backend
$env:MCP_TRANSPORT="http"
$env:GITHUB_TOKEN="your_token_here"
python mcp_runtime_server.py
```

Per the Python SDK quick example, `streamable-http` typically serves on `http://localhost:8000/mcp`.

If your SDK version behaves differently, check the latest Python SDK docs above.

## Step 5. What a Successful Test Looks Like

You should be able to:

1. Load the MCP server
2. See the tools and resources
3. Run `continuous_scan` on a GitHub repo
4. Get a response containing:
   - scan summary
   - continuous intelligence fields
   - incremental scan info
   - autofix suggestions

## Step 6. Integrate into Antigravity After Testing

There are two good integration patterns.

### Option A. Antigravity loads this as an external MCP server

Use this if Antigravity already supports MCP server registration.

Register a server entry that launches:

```powershell
python c:\Users\Mukul Prasad\Desktop\PROJECTS\New folder\an\githoppermain\backend\mcp_runtime_server.py
```

Working directory:

```powershell
c:\Users\Mukul Prasad\Desktop\PROJECTS\New folder\an\githoppermain\backend
```

Required env vars:

- `GITHUB_TOKEN`
- optional `MCP_TRANSPORT=stdio`

Then Antigravity can call MCP tools like:

- `continuous_scan`
- `get_unresolved_issues`

This is the cleanest “true MCP” integration.

Recommended Antigravity flow:

1. Claude changes code
2. Antigravity calls `sync_agent_change`
3. Antigravity reloads:
   - `repomemory://context/{repo_id}`
   - `repomemory://delta/{repo_id}`
   - `repomemory://commands/{repo_id}`

That makes MCP state reflect newly solved and newly arising issues after each command cycle.

### Option B. Antigravity keeps calling Flask, and Flask calls the MCP layer internally

Use this if Antigravity is already tightly coupled to your current API.

In that case:

- keep using `/api/analyze/continuous`
- keep the formal MCP server for testing and future host integrations
- let Antigravity talk to Flask for now

This is the fastest hackathon path.

## Recommended Path for You

For fastest success:

1. Test `backend/mcp_runtime_server.py` in Inspector first
2. Keep Antigravity connected to Flask for the demo
3. After demo validation, register the MCP server directly in Antigravity

## Full Antigravity Integration Plan

### Phase 1

- Run Flask app as main product backend
- Run MCP server separately for host-level validation

### Phase 2

- Register MCP server in Antigravity config
- Let Antigravity use MCP tools for memory-aware scans

### Phase 3

- Move watch mode and autofix invocation to Antigravity workflows
- Optionally replace direct Flask orchestration with MCP-first orchestration

## What I Need From You Before Full Antigravity Wiring

- How Antigravity loads MCP servers:
  - JSON config
  - desktop app settings
  - command registration
  - plugin manifest
- Whether Antigravity expects:
  - stdio MCP
  - streamable HTTP MCP
- Whether Antigravity should call the MCP server directly or via the Flask API first

## Honest Note

The MCP wrapper is now scaffolded correctly for the official Python SDK approach, but I have not installed the `mcp` package inside this repo here.

So:

- the code is ready
- the local test/install step still needs to be run on your machine

Once you tell me how Antigravity registers MCP servers, I can wire the final config exactly.

```

---

## [81] plugins/antigravity-reposcan-mcp/.app.json
**Size:** 17.0B

```json
{
  "apps": []
}

```

---

## [82] plugins/antigravity-reposcan-mcp/.codex-plugin/plugin.json
**Size:** 1.6KB

```json
{
  "name": "antigravity-reposcan-mcp",
  "version": "1.0.0",
  "description": "RepoScan continuous intelligence plugin for Antigravity with MCP-backed memory, incremental scans, and autofix signals.",
  "author": {
    "name": "GitHopper Team",
    "email": "team@example.com",
    "url": "https://github.com/example/githopper"
  },
  "homepage": "https://github.com/example/githopper",
  "repository": "https://github.com/example/githopper",
  "license": "MIT",
  "keywords": [
    "mcp",
    "security"
  ],
  "skills": "./skills/",
  "hooks": "./hooks.json",
  "mcpServers": "./.mcp.json",
  "apps": "./.app.json",
  "interface": {
    "displayName": "Antigravity RepoScan MCP",
    "shortDescription": "Continuous repo scanning with memory and autofix suggestions.",
    "longDescription": "Adds MCP-powered continuous intelligence to RepoScan with history-aware analysis, incremental scans, unresolved issue memory, and patch suggestions.",
    "developerName": "GitHopper Team",
    "category": "Developer Tools",
    "capabilities": [
      "Interactive",
      "Write"
    ],
    "websiteURL": "https://github.com/example/githopper",
    "privacyPolicyURL": "https://github.com/example/githopper",
    "termsOfServiceURL": "https://github.com/example/githopper",
    "defaultPrompt": [
      "Run a continuous scan on this GitHub repository.",
      "Show unresolved security issues from memory.",
      "Suggest validated autofix patches for critical findings."
    ],
    "brandColor": "#72EA1E",
    "composerIcon": "../../frontend/public/assets/githopper.ico",
    "logo": "../../frontend/public/assets/githopper.ico",
    "screenshots": []
  }
}

```

---

## [83] plugins/antigravity-reposcan-mcp/.mcp.json
**Size:** 294.0B

```json
{
  "mcpServers": {
    "reposcan-continuous-intelligence": {
      "command": "python",
      "args": [
        "../../backend/mcp_runtime_server.py"
      ],
      "cwd": "../../backend",
      "env": {
        "MCP_TRANSPORT": "stdio",
        "GITHUB_TOKEN": "[SET_ME]"
      }
    }
  }
}

```

---

## [84] plugins/antigravity-reposcan-mcp/README.md
**Size:** 1.4KB

```markdown
# Antigravity RepoScan MCP Plugin

This plugin registers the RepoScan continuous intelligence MCP server for local Antigravity/Codex-style plugin loading.

## Local MCP server target

- Server entry: `reposcan-continuous-intelligence`
- Command target: `../../backend/mcp_runtime_server.py`

## Before use

1. Install MCP runtime dependency:

```powershell
cd backend
python -m pip install -r requirements-mcp.txt
```

2. Set `GITHUB_TOKEN`

3. Make sure Antigravity/plugin host launches the server from stdio mode

## Test paths

- Direct MCP test: `backend/mcp_runtime_server.py`
- UI test path: existing Flask app + `/api/analyze/continuous`

## Main exposed MCP tool

- `continuous_scan`
- `sync_agent_change`
- `get_issue_delta`

## Main MCP resources

- `repomemory://context/{repo_id}`
- `repomemory://unresolved/{repo_id}`
- `repomemory://delta/{repo_id}`
- `repomemory://commands/{repo_id}`

## Antigravity Sync Model

When the main Claude/Antigravity agent edits code, call:

- `sync_agent_change(repo_url, branch_name, command_name, notes)`

Recommended usage:

1. Claude makes a code change
2. Antigravity calls `sync_agent_change`
3. MCP re-runs incremental analysis
4. Antigravity reads:
   - `repomemory://context/{repo_id}`
   - `repomemory://delta/{repo_id}`
   - `repomemory://commands/{repo_id}`

This lets the MCP layer reflect:

- newly introduced issues
- resolved issues
- persisting issues
- latest agent commands that caused the sync

```

---

## [85] plugins/antigravity-reposcan-mcp/antigravity.mcp.template.json
**Size:** 432.0B

```json
{
  "mcpServers": {
    "reposcan-continuous-intelligence": {
      "command": "python",
      "args": [
        "c:/Users/Mukul Prasad/Desktop/PROJECTS/New folder/an/githoppermain/backend/mcp_runtime_server.py"
      ],
      "cwd": "c:/Users/Mukul Prasad/Desktop/PROJECTS/New folder/an/githoppermain/backend",
      "env": {
        "MCP_TRANSPORT": "stdio",
        "GITHUB_TOKEN": "REPLACE_WITH_YOUR_TOKEN"
      }
    }
  }
}


```

---

## [86] plugins/antigravity-reposcan-mcp/antigravity.sync.template.json
**Size:** 1.5KB

```json
{
  "workflow": {
    "on_session_started": [
      {
        "type": "mcp_tool",
        "server": "reposcan-continuous-intelligence",
        "tool": "continuous_scan",
        "arguments": {
          "repo_url": "{{repo_url}}",
          "branch_name": "{{branch_name}}",
          "generate_fixes": true
        }
      },
      {
        "type": "mcp_resource",
        "server": "reposcan-continuous-intelligence",
        "uri": "repomemory://context/{{repo_id}}"
      },
      {
        "type": "mcp_resource",
        "server": "reposcan-continuous-intelligence",
        "uri": "repomemory://delta/{{repo_id}}"
      }
    ],
    "on_successful_write": [
      {
        "type": "mcp_tool",
        "server": "reposcan-continuous-intelligence",
        "tool": "sync_agent_change",
        "arguments": {
          "repo_url": "{{repo_url}}",
          "branch_name": "{{branch_name}}",
          "command_name": "{{command_name}}",
          "notes": "{{command_summary}}",
          "generate_fixes": true
        }
      },
      {
        "type": "mcp_resource",
        "server": "reposcan-continuous-intelligence",
        "uri": "repomemory://context/{{repo_id}}"
      },
      {
        "type": "mcp_resource",
        "server": "reposcan-continuous-intelligence",
        "uri": "repomemory://delta/{{repo_id}}"
      },
      {
        "type": "mcp_resource",
        "server": "reposcan-continuous-intelligence",
        "uri": "repomemory://commands/{{repo_id}}"
      }
    ]
  }
}


```

---

## [87] plugins/antigravity-reposcan-mcp/hooks.json
**Size:** 19.0B

```json
{
  "hooks": []
}


```

---

## [88] plugins/antigravity-reposcan-mcp/skills/README.md
**Size:** 148.0B

```markdown
# Plugin Skills

This plugin does not add custom Codex skills yet.

The folder is present so the plugin manifest can reference `./skills/` safely.


```

---

## [89] update_codebase_dump.sh
**Size:** 1.2KB

```bash
#!/bin/bash
# GitHopper Codebase Dumper - Unix/Linux/macOS Script
# Run this file to automatically update CODEBASE_DUMP.md

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║   GitHopper Codebase Dumper                                ║"
echo "║   Consolidating entire codebase...                        ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

# Run the dumper script
echo "🔄 Running codebase dumper..."
echo ""
python3 codebase_dumper.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Dumper failed!"
    exit 1
fi

echo ""
echo "✅ Codebase dump completed!"
echo "📄 Output file: CODEBASE_DUMP.md"
echo ""
echo "You can now view the complete codebase in CODEBASE_DUMP.md"
echo ""

```

---

