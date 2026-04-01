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
