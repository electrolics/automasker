@echo off
REM Automatic GPU Setup - Install CUDA-enabled PyTorch

echo.
echo ========================================
echo PYTORCH GPU FIX - CUDA 11.8
echo ========================================
echo.
echo This will:
echo 1. Uninstall old PyTorch
echo 2. Install CUDA 11.8 version
echo 3. Verify GPU detection
echo.
echo This may take 5-10 minutes...
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not installed
    pause
    exit /b 1
)

echo [1/3] Removing old PyTorch...
pip uninstall torch torchvision torchaudio -y

echo.
echo [2/3] Installing PyTorch with CUDA 11.8...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

if errorlevel 1 (
    echo ERROR: Installation failed
    pause
    exit /b 1
)

echo.
echo [3/3] Verifying GPU...
python -c "import torch; cuda = torch.cuda.is_available(); gpu_name = torch.cuda.get_device_name(0) if cuda else 'None'; print(f'GPU Available: {cuda}'); print(f'GPU Name: {gpu_name}')"

echo.
echo ========================================
echo INSTALLATION COMPLETE
echo ========================================
echo.
echo Next steps:
echo 1. Close this window
echo 2. Run the masking GUI: run_gui.bat
echo 3. GPU should now be detected
echo.
pause
