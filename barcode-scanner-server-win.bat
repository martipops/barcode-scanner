@echo off

cd /D "%~dp0"

venv\Scripts\activate.bat & @echo off & python barcode-scanner-gui.py

pause
