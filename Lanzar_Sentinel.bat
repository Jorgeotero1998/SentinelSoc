@echo off
title SENTINEL SOC BY JORGE OTERO
color 0A
echo [*] Sentinel SOC: Verificando entorno...
pip install watchdog python-dotenv --quiet
cls
python src/monitor.py
pause
