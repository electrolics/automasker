@echo off
REM YOLO Equirectangular Image Masking Pipeline - Windows Quick Start
REM This script sets up the environment and runs the masking pipeline

echo.
echo ========================================
echo YOLO Equirectangular Image Masker
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

echo [1/3] Checking dependencies...
pip show ultralytics >nul 2>&1
if errorlevel 1 (
    echo [2/3] Installing required packages from requirements.txt...
    pip install -r ..\App\requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo [2/3] Dependencies already installed
)

echo.
echo [3/3] Starting YOLO Masking Pipeline...
echo.
echo Note: Edit App\yolo_equirectangular_masker.py to set:
echo   INPUT_DIR = your input folder path
echo   OUTPUT_DIR = your output folder path
echo.
echo Processing will begin shortly...
echo.

python ..\App\yolo_equirectangular_masker.py

if errorlevel 1 (
    echo.
    echo ERROR: Processing failed. Check the error messages above.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Processing Complete!
echo ========================================
echo.
echo Check your output folder for results.
echo.
pause
