@echo off
title GF180MCU Op-Amp Interactive Ngspice Simulation
echo ============================================================
echo   GF180MCU Open-Source PDK - Two-Stage Miller Op-Amp
echo   Interactive Ngspice Simulation
echo ============================================================
echo.
echo Launching Ngspice GUI with interactive plot window...
echo.

cd /d "%~dp0"
"C:\FOSSEE\eSim\tools\ngspice\bin\ngspice.exe" run_interactive.cir

echo.
echo Simulation finished.
pause
