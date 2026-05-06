@echo off
REM Build Executable for YOLO Masker GUI
REM This script uses PyInstaller to create a standalone .exe file

echo.
echo ========================================
echo YOLO Masker GUI - Executable Builder
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

echo [1/4] Checking dependencies...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [2/4] Installing PyInstaller and dependencies...
    pip install -r ..\App\requirements_gui.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo [2/4] Dependencies already installed
)

echo.
echo [3/4] Building executable (this may take 2-5 minutes)...
echo Please wait while PyInstaller packages everything...
echo.

REM Change to parent directory for build
cd ..

REM Build executable
pyinstaller --onefile --windowed --name "YOLO_Masker" --add-data "App:App" --distpath "Build/dist" --workpath "Build/build" --specpath "Build" App/yolo_masker_gui.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to build executable
    echo Check the error messages above
    cd Launchers
    pause
    exit /b 1
)

cd Launchers

echo.
echo [4/4] Build complete!
echo.
echo ========================================
echo Executable Created Successfully!
echo ========================================
echo.
echo Location: ..\Build\dist\YOLO_Masker.exe
echo.
echo You can now run the application by:
echo 1. Double-clicking ..\Build\dist\YOLO_Masker.exe
echo 2. Or from command line: ..\Build\dist\YOLO_Masker.exe
echo.
echo Note: First run will download the YOLO model (~800MB)
echo.
pause
