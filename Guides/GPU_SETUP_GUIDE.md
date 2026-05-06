# GPU Setup Guide - NVIDIA CUDA for PyTorch

## Problem
GPU not detected even though you have an NVIDIA RTX GPU installed.

## Root Cause
PyTorch was likely installed **without CUDA support** (CPU-only version), or NVIDIA drivers are not properly installed.

## ✅ Quick Fix (Recommended - 5 minutes)

### Step 1: Check Your Setup
Run the diagnostic script:
```bash
Double-click: check_gpu.bat
```

This will show:
- GPU detected or not
- PyTorch CUDA status
- What needs to be fixed

### Step 2: Reinstall PyTorch with CUDA Support

**Open Command Prompt and run:**

```bash
pip uninstall torch torchvision torchaudio -y
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**This will:**
- Remove old PyTorch
- Install CUDA 11.8 version
- Takes 5-10 minutes

### Step 3: Verify GPU Works

```bash
Double-click: check_gpu.bat
```

**You should see:**
```
CUDA Available: True
GPU Name: NVIDIA GeForce RTX 4090 (or your GPU)
GPU Count: 1
```

### Step 4: Run the Masker

```bash
Double-click: run_gui.bat
```

**Header should now show:**
```
✓ GPU: NVIDIA GeForce RTX 4090
```

---

## 🔍 Detailed Troubleshooting

### Issue 1: "CUDA Available: False"

**Cause:** PyTorch CPU-only version installed

**Fix:**
```bash
pip uninstall torch -y
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

**Verify:**
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

### Issue 2: "CUDA Version: None" or "cuda/11.8" doesn't match driver

**Cause:** NVIDIA drivers outdated or mismatched CUDA version

**Fix 1 - Update Drivers:**
1. Go to: https://www.nvidia.com/Download/driverDetails.aspx
2. Select your GPU model
3. Download and install latest driver
4. **Restart your computer**
5. Run check_gpu.bat

**Fix 2 - Try Different CUDA Version:**
```bash
# Try CUDA 12.1 (newer)
pip install torch --index-url https://download.pytorch.org/whl/cu121

# Or CUDA 11.7 (older)
pip install torch --index-url https://download.pytorch.org/whl/cu117
```

### Issue 3: nvidia-smi not found

**Cause:** NVIDIA drivers not installed

**Fix:**
1. Download driver: https://www.nvidia.com/Download/driverDetails.aspx
   - Select your GPU (RTX series)
   - Select your Windows version (10 or 11)
   - Download installer
2. Run installer
3. **Restart computer** (important!)
4. Run check_gpu.bat

---

## 📊 CUDA Version Compatibility

**PyTorch versions available:**
```
cu118 - CUDA 11.8 (RECOMMENDED for most RTX cards)
cu121 - CUDA 12.1 (for newer drivers)
cu117 - CUDA 11.7 (compatibility)
cpu   - CPU only (no GPU)
```

**Which to use:**
- RTX 20/30/40 series → **cu118**
- Very old RTX (10/16 series) → **cu117**
- Newest drivers (2024+) → **cu121**

---

## 🚀 GPU Speed Impact

Once GPU is working:

**Processing 8K equirectangular images:**

| Setup | Speed | Speedup |
|-------|-------|---------|
| CPU Only | 30-60s per image | Baseline |
| GPU (Half Res) | 2-3s per image | **10-20x faster** |
| GPU (Quarter Res) | 0.5-1s per image | **30-60x faster** |

**1000 8K images:**
- CPU: 8-15 hours
- GPU (Half Res): 30-50 minutes
- GPU (Quarter Res): 8-15 minutes

---

## ✅ Verification Checklist

After making changes, run this command:

```bash
python -c "import torch; print('✓ GPU READY' if torch.cuda.is_available() else '✗ GPU NOT READY')"
```

Should print: `✓ GPU READY`

---

## 💡 Pro Tips

### Tip 1: Check GPU Memory
```bash
python -c "import torch; print(f'GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB')"
```

### Tip 2: Monitor GPU Usage During Processing
Open new Command Prompt and run:
```bash
nvidia-smi -l 1
```

This shows real-time GPU usage while processing.

### Tip 3: Clear CUDA Cache (if running out of memory)
```bash
python -c "import torch; torch.cuda.empty_cache()"
```

---

## 🆘 Still Not Working?

1. **Restart your computer** (sometimes CUDA needs reboot)
2. **Check driver version matches PyTorch**
   ```bash
   nvidia-smi  # Check Driver Version
   ```
3. **Try fresh PyTorch install**
   ```bash
   pip uninstall torch -y
   pip install torch --index-url https://download.pytorch.org/whl/cu118
   ```
4. **Check Windows Event Viewer** for driver errors
5. **Update Windows** (sometimes fixes driver issues)

---

## 📚 Additional Resources

- **NVIDIA Drivers:** https://www.nvidia.com/Download/driverDetails.aspx
- **CUDA Toolkit:** https://developer.nvidia.com/cuda-downloads
- **cuDNN:** https://developer.nvidia.com/cudnn
- **PyTorch Install:** https://pytorch.org/get-started/locally/

---

## 🎯 Next Steps

1. Run `check_gpu.bat`
2. Follow the suggested fix
3. Restart computer
4. Run `check_gpu.bat` again to verify
5. Run masking GUI - GPU should work!

**Good luck! GPU will give you 10-30x speedup! 🚀**
