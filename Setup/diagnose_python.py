#!/usr/bin/env python3
"""
Diagnose Python and PyTorch compatibility issues
"""

import sys
import subprocess

print("\n" + "="*50)
print("PYTHON & PYTORCH COMPATIBILITY CHECK")
print("="*50 + "\n")

# Check Python version
major, minor, micro = sys.version_info[:3]
python_version = f"{major}.{minor}.{micro}"

print(f"🐍 Python Version: {python_version}")
print(f"   Location: {sys.executable}")

# Check compatibility
print(f"\n📊 Compatibility Status:")

if major == 3:
    if minor <= 12:
        print(f"   ✓ Python {major}.{minor} IS compatible with PyTorch CUDA")
        print(f"   → Use CUDA 11.8 or 12.1")
    elif minor == 13:
        print(f"   ⚠ Python 3.13 has LIMITED PyTorch CUDA support")
        print(f"   → Use CUDA 12.1 (not 11.8)")
    elif minor >= 14:
        print(f"   ✗ Python 3.{minor} NOT YET SUPPORTED by PyTorch")
        print(f"   → CUDA wheels not available")
        print(f"\n   FIX REQUIRED:")
        print(f"   Download Python 3.12: https://www.python.org/downloads/release/python-3124/")
        print(f"   Uninstall Python 3.{minor}")
        print(f"   Install Python 3.12")
        print(f"   Run: pip install torch --index-url https://download.pytorch.org/whl/cu121")
else:
    print(f"   ✗ Unsupported Python version: {major}.{minor}")

# Check PyTorch
print(f"\n📦 PyTorch Installation:")
try:
    import torch
    print(f"   ✓ PyTorch installed: {torch.__version__}")
    print(f"   ✓ CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"   ✓ GPU: {torch.cuda.get_device_name(0)}")
    else:
        print(f"   ✗ CUDA not available (likely CPU-only version)")
except ImportError:
    print(f"   ✗ PyTorch not installed")

print("\n" + "="*50)
print("RECOMMENDATIONS")
print("="*50 + "\n")

if major == 3 and minor >= 14:
    print("Your Python version is too new for PyTorch CUDA.")
    print("\nOPTION 1: Downgrade Python to 3.12 (RECOMMENDED)")
    print("  1. Download: https://www.python.org/downloads/release/python-3124/")
    print("  2. Uninstall current Python")
    print("  3. Install Python 3.12")
    print("  4. Run: fix_gpu.bat")
    print("\nOPTION 2: Use CPU (Not recommended - will be very slow)")
    print("  Already have CPU-only PyTorch installed")

elif major == 3 and minor == 13:
    print("Python 3.13 - Use CUDA 12.1+")
    print("\nRun: fix_gpu_advanced.bat")

elif major == 3 and minor <= 12:
    print("Python version is compatible!")
    print("\nRun: fix_gpu.bat")
else:
    print("Unsupported configuration - contact support")

print("\n" + "="*50 + "\n")
