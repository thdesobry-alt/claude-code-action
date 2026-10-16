@echo off
rem Lance le serveur Cannelures Laminoir puis ouvre le navigateur.
cd /d "%~dp0"
start "" http://localhost:8080
python serveur.py
if errorlevel 1 py serveur.py
pause
