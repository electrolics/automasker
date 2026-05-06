# Automasker - Project Index

## 📁 Organized Folder Structure

```
Automasker/
├── 📄 README.md                    ← Start here! Overview of everything
├── 📄 INDEX.md                     ← This file
│
├── 🚀 Launchers/                   ← Quick start scripts
│   ├── run_gui.bat                 # Start GUI application
│   ├── run_masker.bat              # Start CLI application
│   └── build_executable.bat        # Build standalone .exe
│
├── 💻 App/                         ← Main application source
│   ├── yolo_masker_gui.py          # GUI application (recommended)
│   ├── yolo_equirectangular_masker.py # CLI version
│   ├── requirements_gui.txt        # GUI dependencies
│   └── requirements.txt            # CLI dependencies
│
├── 🛠️ Setup/                        ← GPU & Installation setup
│   ├── FIX_GPU_OFFICIAL.bat        # Auto GPU setup (official method)
│   ├── verify_cuda.py              # Check if GPU works
│   ├── fix_gpu_v2.bat              # Alternative GPU setup
│   ├── check_gpu.bat               # GPU diagnostics
│   ├── diagnose_python.py          # Python version check
│   ├── diagnose_python.bat         # Run Python diagnostics
│   ├── fix_gpu.bat                 # Original GPU setup
│   └── fix_gpu_advanced.bat        # Advanced GPU setup
│
├── 📚 Guides/                      ← Documentation
│   ├── QUICKSTART.md               # ← Read first! (5 min start)
│   ├── GUI_APPLICATION_GUIDE.md    # Detailed GUI features
│   ├── OFFICIAL_PYTORCH_FIX.md     # Official GPU setup guide
│   ├── GPU_SETUP_GUIDE.md          # Comprehensive GPU guide
│   ├── SETUP_AND_USAGE.md          # CLI detailed guide
│   ├── README_GUI.md               # GUI overview
│   ├── GPU_FIX_QUICK_START.md      # Quick GPU fixes
│   └── PYTORCH_OFFICIAL_FIX.md     # PyTorch setup reference
│
├── 🤖 Models/                      ← Pre-trained YOLO models
│   ├── yolo11n-seg.pt              # Nano model (2GB, fastest)
│   ├── yolo11s-seg.pt              # Small model (4GB, balanced)
│   └── yolo11m-seg.pt              # Medium model (8GB, best)
│
└── 🔨 Build/                       ← Build artifacts (generated)
    ├── dist/                       # Executable output
    ├── build/                      # Build files
    └── YOLO_Masker.spec           # PyInstaller config
```

## 🎯 Quick Navigation

### I Want To...

**Run the masking application:**
→ Double-click: `Launchers/run_gui.bat`

**Set up GPU (first time):**
→ 1. Run: `Setup/FIX_GPU_OFFICIAL.bat`
→ 2. Restart computer
→ 3. Run: `Setup/verify_cuda.py`

**Learn how to use the GUI:**
→ Read: `Guides/QUICKSTART.md` (5 minutes)
→ Then: `Guides/GUI_APPLICATION_GUIDE.md` (detailed)

**Use command-line version:**
→ Edit: `App/yolo_equirectangular_masker.py`
→ Read: `Guides/SETUP_AND_USAGE.md`

**Fix GPU issues:**
→ Run: `Setup/verify_cuda.py`
→ Then: `Setup/FIX_GPU_OFFICIAL.bat`
→ Read: `Guides/OFFICIAL_PYTORCH_FIX.md`

**Create standalone executable:**
→ Run: `Launchers/build_executable.bat`
→ Output: `Build/dist/YOLO_Masker.exe`

**Install dependencies:**
```bash
# For GUI
pip install -r App/requirements_gui.txt

# For CLI
pip install -r App/requirements.txt
```

---

## 📋 File Purposes

### App Files
| File | Purpose |
|------|---------|
| `yolo_masker_gui.py` | Main GUI application with all features |
| `yolo_equirectangular_masker.py` | Command-line version for batch processing |
| `requirements_gui.txt` | All dependencies for GUI |
| `requirements.txt` | All dependencies for CLI |

### Setup Files
| File | Purpose |
|------|---------|
| `FIX_GPU_OFFICIAL.bat` | Automatic GPU setup (recommended) |
| `verify_cuda.py` | Verify GPU is working |
| `fix_gpu_v2.bat` | Alternative GPU setup with version detection |
| `check_gpu.bat` | Diagnostic GPU checker |

### Guide Files
| File | Purpose |
|------|---------|
| `QUICKSTART.md` | 5-minute beginner guide |
| `GUI_APPLICATION_GUIDE.md` | Detailed GUI documentation |
| `OFFICIAL_PYTORCH_FIX.md` | Official PyTorch setup guide |
| `SETUP_AND_USAGE.md` | Command-line usage guide |

### Model Files
| File | Size | Speed | Best For |
|------|------|-------|----------|
| `yolo11n-seg.pt` | 6MB | Fastest | Speed priority |
| `yolo11s-seg.pt` | 20MB | Balanced | Balanced use |
| `yolo11m-seg.pt` | 45MB | Slowest | Accuracy |

---

## ✅ Folder is Clean

**No personal information remaining:**
- ✓ No local file paths
- ✓ No user-specific data
- ✓ No hardcoded directories
- ✓ All paths are now placeholders or generic

**Ready for sharing:**
- ✓ Professional structure
- ✓ Clear documentation
- ✓ Organized by function
- ✓ Easy to navigate

---

## 🚀 First Time Use Checklist

- [ ] Extract to your computer
- [ ] Double-click: `Launchers/run_gui.bat`
- [ ] Read: `Guides/QUICKSTART.md`
- [ ] (Optional) Run: `Setup/FIX_GPU_OFFICIAL.bat` for GPU support
- [ ] Start masking images!

---

## 📞 Support

**For any issues, check:**

1. **Guides/** - Full documentation
2. **Setup/** - Troubleshooting scripts
3. **README.md** - Overall overview

All guides are self-contained and explain:
- How to use each feature
- Common problems and fixes
- Performance optimization tips
- GPU troubleshooting

---

## 🎉 You're All Set!

The folder is now:
- ✅ Professionally organized
- ✅ Fully documented
- ✅ Free of personal info
- ✅ Ready to share or deploy

**Start with:** `Guides/QUICKSTART.md` or `Launchers/run_gui.bat`

Happy masking! 🚀
