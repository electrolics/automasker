#!/usr/bin/env python3
"""
Verify CUDA and GPU installation
Based on official PyTorch documentation
"""

import torch

print("\n" + "="*60)
print("PYTORCH & CUDA VERIFICATION")
print("="*60 + "\n")

# Test 1: Check PyTorch
print("✓ Test 1: PyTorch Installation")
print(f"  PyTorch Version: {torch.__version__}")

# Test 2: Check CUDA
print("\n✓ Test 2: CUDA Availability")
cuda_available = torch.cuda.is_available()
print(f"  CUDA Available: {cuda_available}")

if not cuda_available:
    print("\n  ⚠ CUDA not available")
    print("  This usually means:")
    print("  1. CUDA version of PyTorch not installed")
    print("  2. NVIDIA drivers not installed")
    print("  3. GPU not detected")
    print("\n  Fix: Run FIX_GPU_OFFICIAL.bat again and restart computer")
else:
    print(f"  CUDA Version: {torch.version.cuda}")

# Test 3: Check GPU
print("\n✓ Test 3: GPU Detection")
gpu_count = torch.cuda.device_count()
print(f"  GPU Count: {gpu_count}")

if gpu_count > 0:
    for i in range(gpu_count):
        gpu_name = torch.cuda.get_device_name(i)
        print(f"  GPU {i}: {gpu_name}")
else:
    print("  ⚠ No GPU detected")

# Test 4: Create tensor on GPU
if cuda_available:
    print("\n✓ Test 4: GPU Tensor Creation")
    try:
        x = torch.rand(5, 3).cuda()
        print(f"  ✓ Successfully created tensor on GPU")
        print(f"  Tensor shape: {x.shape}")
        print(f"  Tensor device: {x.device}")
    except Exception as e:
        print(f"  ✗ Error creating tensor: {e}")
else:
    print("\n✓ Test 4: GPU Tensor Creation")
    print("  Skipped (CUDA not available)")

# Test 5: Summary
print("\n" + "="*60)
print("SUMMARY")
print("="*60)

if cuda_available and gpu_count > 0:
    print("✅ GPU IS READY!")
    print("\n   You can now run the masking GUI:")
    print("   > run_gui.bat")
    print("\n   Processing will be 10-30x faster!")
else:
    print("❌ GPU NOT READY")
    print("\n   Follow these steps:")
    print("   1. Run: FIX_GPU_OFFICIAL.bat")
    print("   2. Restart your computer")
    print("   3. Run this verification again")
    print("   4. If still not working, check:")
    print("      - NVIDIA drivers installed: nvidia-smi")
    print("      - Correct CUDA version for your drivers")

print("\n" + "="*60 + "\n")
