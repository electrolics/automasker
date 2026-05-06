@echo off
REM Quick launcher for YOLO Masker GUI

echo.
echo ========================================
echo YOLO Masker GUI - Quick Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/2] Checking dependencies...
pip show ultralytics >nul 2>&1
if errorlevel 1 (
    echo [2/2] Installing required packages...
    pip install -r ..\App\requirements_gui.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo [2/2] Dependencies ready
)

echo.
echo Starting YOLO Masker GUI...
echo.

python ..\App\yolo_masker_gui.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start application
    pause
    exit /b 1
)
