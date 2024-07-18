cd /D "%~dp0"
powershell.exe -ExecutionPolicy Bypass -File "venv/bin/Activate.ps1"

python3 barcode-scanner-server.py