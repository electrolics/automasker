# 🚀 Quick GPU Fix

Your GPU isn't being detected. Here's how to fix it in **2 minutes**:

## Option A: Automatic Fix (Easiest) ⭐

1. **Double-click**: `fix_gpu.bat`
2. **Wait** for installation (5-10 minutes)
3. **Restart** your computer
4. **Run GUI**: `run_gui.bat`
5. **Check header** - should show ✓ GPU: Your GPU Name

---

## Option B: Manual Fix (If Automatic Doesn't Work)

### Step 1: Open Command Prompt
- Press `Win + R`
- Type: `cmd`
- Press Enter

### Step 2: Run This Command
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Step 3: Wait for Install
Takes 5-10 minutes

### Step 4: Restart Computer
⚠️ **Important!** CUDA drivers need reboot

### Step 5: Verify GPU
Run diagnostic:
```bash
Double-click: check_gpu.bat
```

Should show:
```
✓ CUDA Available: True
✓ GPU Name: NVIDIA GeForce RTX...
```

### Step 6: Run Masker
```bash
Double-click: run_gui.bat
```

---

## Option C: Full CUDA Setup (If Still Not Working)

### Prerequisites Needed:
1. **NVIDIA Drivers** (latest)
   - Download: https://www.nvidia.com/Download/driverDetails.aspx
   - Install & restart

2. **CUDA Toolkit 11.8**
   - Download: https://developer.nvidia.com/cuda-11-8-0-download-archive
   - Install & restart

3. **Then Run:**
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cu118
   ```

---

## 🎯 Expected Result

After GPU is detected:

**Processing 8K Equirectangular Images:**
- CPU only: 30-60 seconds per image
- GPU (full res): 3-5 seconds per image
- GPU (half res): 1-2 seconds per image

**That's 10-30x FASTER!**

---

## ❓ What If It Still Doesn't Work?

1. **Verify NVIDIA drivers installed:**
   ```bash
   nvidia-smi
   ```
   If command not found → Install drivers from https://www.nvidia.com

2. **Check driver version matches PyTorch:**
   - Run `nvidia-smi`
   - Note the "CUDA Version" shown
   - If version is 12.x, try: `cu121` instead of `cu118`

3. **Try Different CUDA Version:**
   ```bash
   # For newer drivers (2024+)
   pip install torch --index-url https://download.pytorch.org/whl/cu121
   
   # For older drivers
   pip install torch --index-url https://download.pytorch.org/whl/cu117
   ```

4. **Restart Computer** (sometimes helps)

5. **Read Full Guide:** `GPU_SETUP_GUIDE.md`

---

## ✅ Checklist

- [ ] Ran `fix_gpu.bat` OR manual pip install
- [ ] Installation completed without errors
- [ ] Restarted computer
- [ ] Ran `check_gpu.bat` and saw "CUDA Available: True"
- [ ] GPU shows in masking GUI header
- [ ] Running masking - much faster now!

---

## 🎓 Why This Happens

PyTorch has two versions:
- **CPU version** - Uses your processor (slow)
- **CUDA version** - Uses your GPU (fast)

By default, pip might install the CPU version. We need to explicitly tell pip to install the GPU version:

```bash
--index-url https://download.pytorch.org/whl/cu118
```

This tells pip: "Get CUDA 11.8 version from this repository"

---

**Start with Option A (fix_gpu.bat) - it's easiest!** 🚀
