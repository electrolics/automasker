# PyTorch Official GPU Setup Fix

## Problem
Python 3.14 is **NOT YET SUPPORTED** by PyTorch (as of 2024)

**PyTorch officially supports: Python 3.9, 3.10, 3.11, 3.12, 3.13**

## Solution

### Option 1: Downgrade Python to 3.12 (RECOMMENDED) ⭐

**Why:** Most stable, all CUDA versions work

#### Step 1: Download Python 3.12
Go to: https://www.python.org/downloads/
- Look for **Python 3.12.x** (latest 3.12)
- Select "Windows installer (64-bit)"
- Download it

#### Step 2: Uninstall Python 3.14
- Open Settings (Win + I)
- Apps → Installed apps
- Search "Python 3.14"
- Click → Uninstall

#### Step 3: Install Python 3.12
- Run Python 3.12 installer
- **IMPORTANT:** Check ✅ "Add Python to PATH"
- Click "Install Now"
- Wait to complete

#### Step 4: Restart Command Prompt
- Close all Command Prompt windows
- Open new Command Prompt
- Verify: `python --version` should show 3.12.x

#### Step 5: Install PyTorch with GPU
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### Step 6: Restart Computer
⚠️ **CRITICAL** - CUDA drivers need reboot

#### Step 7: Verify GPU
```bash
python -c "import torch; print(f'GPU: {torch.cuda.is_available()}')"
```

Should print: `GPU: True`

---

### Option 2: Use Python 3.13 (If you don't want 3.12)

#### Step 1: Download Python 3.13
Go to: https://www.python.org/downloads/
- Look for **Python 3.13.x**
- Download Windows installer (64-bit)

#### Step 2: Uninstall Python 3.14
- Same as Option 1 Step 2

#### Step 3: Install Python 3.13
- Run installer
- Check ✅ "Add Python to PATH"
- Install

#### Step 4: Restart Command Prompt & Install PyTorch
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**Note:** Python 3.13 requires CUDA 12.1+

#### Step 5-7: Same as Option 1

---

## Official PyTorch Commands by Python Version

### For Python 3.12 (CUDA 11.8)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### For Python 3.13 (CUDA 12.1)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### For Python 3.11 or earlier (CUDA 11.8)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## What NOT to Do
❌ Try to force Python 3.14 with PyTorch - wheels don't exist yet
❌ Use generic `pip install torch` - gets CPU version
❌ Use old PyTorch versions - won't work with newer Python

---

## After Installation

1. **Restart Computer** (important!)
2. Run masking GUI:
   ```bash
   run_gui.bat
   ```
3. Header should show:
   ```
   ✓ GPU: NVIDIA GeForce RTX...
   ```
4. Processing should be 10-30x faster!

---

## Verification

Test GPU works:
```bash
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

Should show: `True NVIDIA GeForce RTX...`

---

## Sources
- Official PyTorch: https://pytorch.org/get-started/locally/
- Python Downloads: https://www.python.org/downloads/
- CUDA Support: https://pytorch.org/get-started/locally/#windows-anaconda

---

## Recommended Action

1. **Download Python 3.12** from python.org
2. **Uninstall Python 3.14**
3. **Install Python 3.12** (check Add to PATH!)
4. **Restart computer**
5. **Run:** `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`
6. **Restart computer again**
7. **Run:** `run_gui.bat`
8. **Enjoy 30x speedup!** 🚀
