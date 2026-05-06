@echo off
REM GPU Diagnostics Script - Check CUDA and PyTorch Setup

echo.
echo ========================================
echo GPU DIAGNOSTICS
echo ========================================
echo.

REM Check Python
echo [1/4] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found
    goto end
)

echo.
echo [2/4] Checking NVIDIA GPU drivers...
echo.
nvidia-smi
if errorlevel 1 (
    echo WARNING: nvidia-smi not found
    echo Run: https://www.nvidia.com/Download/driverDetails.aspx
    echo.
)

echo.
echo [3/4] Checking PyTorch CUDA support...
python -c "import torch; print(f'PyTorch Version: {torch.__version__}'); print(f'CUDA Available: {torch.cuda.is_available()}'); print(f'CUDA Version: {torch.version.cuda}'); print(f'GPU Count: {torch.cuda.device_count()}'); print(f'GPU Name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"

if errorlevel 1 (
    echo ERROR: PyTorch check failed
)

echo.
echo [4/4] Result:
echo.
python -c "import torch; cuda_available = torch.cuda.is_available(); print('✓ GPU READY' if cuda_available else '✗ GPU NOT DETECTED - See fixes below')"

echo.
echo ========================================
echo FIXES (if GPU not detected):
echo ========================================
echo.
echo Method 1: Install CUDA-enabled PyTorch (RECOMMENDED)
echo.
echo pip uninstall torch torchvision torchaudio -y
echo pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
echo.
echo Method 2: Update NVIDIA Drivers
echo.
echo 1. Download latest driver from: https://www.nvidia.com/Download/driverDetails.aspx
echo 2. Install driver
echo 3. Restart computer
echo 4. Run this script again
echo.
echo Method 3: Check CUDA Installation
echo.
echo 1. Download CUDA Toolkit: https://developer.nvidia.com/cuda-downloads
echo 2. Download cuDNN: https://developer.nvidia.com/cudnn
echo 3. Install both
echo 4. Restart computer
echo.
echo ========================================
echo.

:end
pause
