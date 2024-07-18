@echo off

cd /D "%~dp0"

python3 -m venv ./venv
powershell.exe -ExecutionPolicy Bypass -File "venv/bin/Activate.ps1"

pip install -r requirements.txt