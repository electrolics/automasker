@echo off
REM PyTorch GPU Setup - Official PyTorch Method

echo.
echo ========================================
echo PYTORCH OFFICIAL GPU SETUP
echo ========================================
echo.

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Detected Python: %PYTHON_VERSION%
echo.

REM Extract minor version
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
)

echo Checking compatibility...
echo.

REM Check version compatibility
if %MAJOR% NEQ 3 (
    echo ERROR: Python 3.x required
    echo Current: %PYTHON_VERSION%
    pause
    exit /b 1
)

if %MINOR% GTR 13 (
    echo WARNING: Python %MAJOR%.%MINOR% is not officially supported by PyTorch yet
    echo PyTorch supports: Python 3.9, 3.10, 3.11, 3.12, 3.13
    echo.
    echo You MUST downgrade to Python 3.12 or 3.13
    echo.
    echo Download Python 3.12: https://www.python.org/downloads/release/python-3124/
    echo.
    pause
    exit /b 1
)

if %MINOR% EQU 13 (
    echo Python 3.13 detected - Using CUDA 12.1
    set CUDA_VERSION=cu121
) else (
    echo Python 3.12 or earlier detected - Using CUDA 11.8
    set CUDA_VERSION=cu118
)

echo.
echo ========================================
echo INSTALLING PYTORCH
echo ========================================
echo.

REM Remove old installation
echo [1/3] Cleaning up old PyTorch...
pip uninstall torch torchvision torchaudio -y 2>nul

echo.
echo [2/3] Installing PyTorch with GPU support...
echo Command: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/%CUDA_VERSION%
echo.

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/%CUDA_VERSION%

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed
    echo.
    echo Possible causes:
    echo - Internet connection issue
    echo - Python version incompatible
    echo - Try running: pip install --upgrade pip
    echo.
    pause
    exit /b 1
)

echo.
echo [3/3] Verifying installation...
echo.

python -c "import torch; cuda_available = torch.cuda.is_available(); gpu_name = torch.cuda.get_device_name(0) if cuda_available else 'N/A'; print(f'CUDA Available: {cuda_available}'); print(f'GPU: {gpu_name}'); print(f'PyTorch: {torch.__version__}')"

if errorlevel 1 (
    echo ERROR: Verification failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo INSTALLATION SUCCESSFUL
echo ========================================
echo.
echo NEXT STEPS:
echo 1. RESTART YOUR COMPUTER (critical!)
echo 2. After restart, run: run_gui.bat
echo 3. GUI header should show your GPU name
echo 4. Processing will be 10-30x faster!
echo.
pause
