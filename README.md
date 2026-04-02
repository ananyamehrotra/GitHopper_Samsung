# 🦗 GitHopper

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
