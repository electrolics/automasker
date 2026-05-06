@echo off
REM Advanced GPU Setup - Try Multiple CUDA Versions

echo.
echo ========================================
echo PYTORCH GPU FIX - ADVANCED
echo ========================================
echo.
echo Checking Python version...
echo.
python --version

echo.
echo [1/4] Removing old PyTorch...
pip uninstall torch torchvision torchaudio -y

echo.
echo [2/4] Trying CUDA 12.1 (newer, broader Python support)...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

if errorlevel 1 (
    echo.
    echo CUDA 12.1 failed, trying CUDA 12.4...
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
)

if errorlevel 1 (
    echo.
    echo All CUDA versions failed. This may be due to Python version.
    echo.
    echo Your Python version:
    python --version
    echo.
    echo PyTorch supports Python 3.8-3.12
    echo If you have Python 3.13+, you may need to downgrade to Python 3.12
    echo.
    echo Visit: https://www.python.org/downloads/
    echo Download Python 3.12.x
    echo Then uninstall current Python and install 3.12
    echo.
    pause
    exit /b 1
)

echo.
echo [3/4] Updating pip...
python -m pip install --upgrade pip

echo.
echo [4/4] Verifying GPU...
python -c "import torch; cuda = torch.cuda.is_available(); gpu_name = torch.cuda.get_device_name(0) if cuda else 'None'; print(f'GPU Available: {cuda}'); print(f'GPU Name: {gpu_name}'); print(f'PyTorch Version: {torch.__version__}')"

echo.
echo ========================================
echo INSTALLATION COMPLETE
echo ========================================
echo.
echo Next steps:
echo 1. Close this window
echo 2. RESTART YOUR COMPUTER (important!)
echo 3. Run: check_gpu.bat
echo 4. Run: run_gui.bat
echo.
pause
