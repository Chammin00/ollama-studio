@echo off
echo ==============================================================
echo   Register Daily Ollama Skills Sync with Windows Task Scheduler
echo ==============================================================
echo.
echo Setting up daily task to run at 4:00 AM...
schtasks /create /tn "OllamaDailySkillsSync" /tr "python \"G:\My Drive\Antigravity\Projects\ollama\sync_skills_to_ollama.py\"" /sc daily /st 04:00 /f
if %ERRORLEVEL% equ 0 (
    echo [SUCCESS] Windows Task 'OllamaDailySkillsSync' registered successfully!
) else (
    echo [NOTE] If this requires administrative elevation, run Command Prompt as Administrator.
)
echo.
pause
