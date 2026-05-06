# Launchers - Quick Start Scripts

All scripts in this folder are ready to run from here. Just double-click!

## 🚀 Main Launcher (Use This!)

### run_gui.bat
**The easiest way to start masking**

```bash
Double-click: run_gui.bat
```

**What it does:**
1. Checks Python installation
2. Installs/checks dependencies
3. Launches GUI application
4. You can select folders and start masking!

**Features:**
- Visual folder selection
- Real-time progress
- Settings adjustment
- GPU detection
- Easy to use

---

## 💻 Alternative Launcher

### run_masker.bat
**Command-line version for batch processing**

```bash
Double-click: run_masker.bat
```

**What it does:**
1. Checks Python installation
2. Installs/checks dependencies
3. Runs CLI masking pipeline

**Note:** Edit `../App/yolo_equirectangular_masker.py` first to set:
```python
INPUT_DIR = r"C:\path\to\your\images"
OUTPUT_DIR = r"C:\path\to\output"
```

---

## 🔨 Build Launcher

### build_executable.bat
**Create standalone .exe file**

```bash
Double-click: build_executable.bat
```

**What it does:**
1. Installs PyInstaller
2. Builds executable
3. Takes 2-5 minutes
4. Creates: `../Build/dist/YOLO_Masker.exe`

**Use when:**
- You want a standalone executable
- Sharing with others who don't have Python
- Don't need to modify code

---

## ⚙️ Setup (If Needed)

If you haven't set up GPU yet:

```bash
1. Run: ../Setup/FIX_GPU_OFFICIAL.bat
2. Restart computer
3. Run: ../Setup/verify_cuda.py
4. Then use: run_gui.bat
```

---

## 📂 File Organization

```
Launchers/
├── README.md               ← This file
├── run_gui.bat            ← GUI (main launcher)
├── run_masker.bat         ← CLI launcher
└── build_executable.bat   ← Build standalone exe
```

---

## 🎯 Quick Workflow

### First Time
```
1. Double-click: run_gui.bat
2. Select input folder (PNG/JPG images)
3. Select output folder
4. Click "START PROCESSING"
5. Wait for completion
6. Check output folder for results
```

### With GPU Setup
```
1. Run: ../Setup/FIX_GPU_OFFICIAL.bat
2. Restart computer
3. Double-click: run_gui.bat
4. Processing is 10-30x faster!
```

### Building Executable
```
1. Double-click: build_executable.bat
2. Wait 2-5 minutes
3. Find: ../Build/dist/YOLO_Masker.exe
4. Double-click to run (no Python needed!)
```

---

## ✅ Troubleshooting

**"Python not found"**
- Install Python 3.10-3.14 from python.org
- Add Python to PATH during install

**"GPU not detected"**
- Run: `../Setup/FIX_GPU_OFFICIAL.bat`
- Restart computer

**"Module not found"**
- Script should auto-install
- If not, run manually:
  ```bash
  pip install -r ../App/requirements_gui.txt
  ```

**"Permission denied"**
- Right-click bat file → Run as administrator

---

## 📚 Documentation

- **Quick guide:** `../Guides/QUICKSTART.md`
- **Full guide:** `../README.md`
- **GPU help:** `../Guides/OFFICIAL_PYTORCH_FIX.md`

---

**Ready? Just double-click run_gui.bat! 🚀**
