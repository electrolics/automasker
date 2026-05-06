@echo off
REM PyTorch Official Installation - Python 3.14 Support
REM Based on https://pytorch.org/get-started/locally/

echo.
echo ========================================
echo PYTORCH OFFICIAL INSTALLATION
echo Python 3.10-3.14 Supported
echo ========================================
echo.

python --version

echo.
echo This will install PyTorch with CUDA support
echo using the official PyTorch repository.
echo.

echo [1/3] Uninstalling old PyTorch...
pip uninstall torch torchvision torchaudio -y 2>nul

echo.
echo [2/3] Installing PyTorch with CUDA 12.4 (latest)...
echo.
echo Running: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
echo.

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

if errorlevel 1 (
    echo.
    echo cu124 failed, trying cu121...
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

    if errorlevel 1 (
        echo.
        echo cu121 failed, trying cu118...
        pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    )
)

echo.
echo [3/3] Verifying Installation...
echo.

python << PYTHON_END
import torch

print("=" * 50)
print("PYTORCH VERIFICATION")
print("=" * 50)
print(f"PyTorch Version: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Version: {torch.version.cuda}")
    print("")
    print("✓ GPU READY!")
    print("✓ Restart computer and run: run_gui.bat")
else:
    print(f"✗ CUDA not available")
    print("✗ This might be normal - see below")

print("=" * 50)
PYTHON_END

echo.
echo ========================================
echo NEXT STEPS:
echo ========================================
echo.
echo 1. Close this window
echo 2. RESTART YOUR COMPUTER (important!)
echo 3. Open Command Prompt again
echo 4. Run: run_gui.bat
echo 5. GPU should now be detected
echo.
pause
