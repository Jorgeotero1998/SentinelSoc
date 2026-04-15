@echo off
cd /d "%~dp0"
title SENTINEL SOC ELITE BY JORGE OTERO
echo [*] Iniciando sistema desde %cd%...
python src/monitor.py
pause
