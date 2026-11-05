@echo off
cd /d "%~dp0"
echo Running GF180MCU Op-Amp Interactive Simulation...
"C:\FOSSEE\eSim\tools\ngspice\bin\ngspice.exe" GF180_OpAmp_interactive.cir
pause
