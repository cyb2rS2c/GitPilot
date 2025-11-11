@echo off
REM launches the ps1 script with an interactive console window
powershell -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "%~dp0gitpilot.ps1"

pause
