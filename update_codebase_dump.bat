@echo off
REM GitHopper Codebase Dumper - Windows Batch Script
REM Run this file to automatically update CODEBASE_DUMP.md

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║   GitHopper Codebase Dumper                                ║
echo ║   Consolidating entire codebase...                        ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Run the dumper script
echo 🔄 Running codebase dumper...
echo.
python codebase_dumper.py

if errorlevel 1 (
    echo.
    echo ❌ Dumper failed!
    pause
    exit /b 1
)

echo.
echo ✅ Codebase dump completed!
echo 📄 Output file: CODEBASE_DUMP.md
echo.
echo You can now view the complete codebase in CODEBASE_DUMP.md
echo.
pause
