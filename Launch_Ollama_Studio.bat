@echo off
title Ollama 1-Click Studio Launcher
cd /d "G:\My Drive\Antigravity\Projects\ollama"

echo ===================================================
echo        OLLAMA 1-CLICK STUDIO (ANTIGRAVITY)
echo ===================================================
echo.
echo Initializing Ollama AI Studio Web Interface...
echo URL: http://localhost:8111
echo.

python serve_and_launch.py
pause
