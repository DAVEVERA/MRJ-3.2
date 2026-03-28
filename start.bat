@echo off
cd /d "%~dp0"
title MRJ3.0 — Mr. Jealousy

REM ── Kill any existing Python server ─────────────────────────
echo Checking for running Python processes...
taskkill /f /im python.exe >nul 2>&1
if errorlevel 1 (
    echo No existing Python process found.
) else (
    echo Stopped previous Python process.
    timeout /t 1 /nobreak >nul
)

REM ── Load environment variables from .env ─────────────────────
echo Loading environment from .env...
for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    if not "%%A"=="" if not "%%A:~0,1%%"=="#" set "%%A=%%B"
)

REM ── Install dependencies if needed ──────────────────────────
echo Installing / verifying dependencies...
pip install -r requirements.txt --quiet --no-warn-script-location
if errorlevel 1 (
    echo WARNING: pip install reported issues. Attempting to continue...
)

REM ── Start Flask server ───────────────────────────────────────
echo.
echo ============================================================
echo   MRJ3.0 is starting on http://localhost:5000
echo   Open your browser and navigate to http://localhost:5000
echo   Press Ctrl+C to stop the server.
echo ============================================================
echo.
python app.py

pause
