# YOLO Equirectangular Image Masker

Professional image masking pipeline for removing humans and cars from equirectangular images for photogrammetry and Gaussian splatting applications.

## 📁 Folder Structure

```
Automasker/
├── App/                          # Main application files
│   ├── yolo_masker_gui.py       # GUI application (recommended)
│   ├── yolo_equirectangular_masker.py # Command-line version
│   ├── requirements_gui.txt      # GUI dependencies
│   └── requirements.txt          # CLI dependencies
│
├── Setup/                         # Installation and setup
│   ├── FIX_GPU_OFFICIAL.bat     # Automatic GPU setup
│   ├── verify_cuda.py           # GPU verification script
│   ├── fix_gpu_v2.bat           # Alternative GPU setup
│   ├── check_gpu.bat            # GPU diagnostics
│   └── diagnose_python.py       # Python compatibility check
│
├── Guides/                        # Documentation
│   ├── QUICKSTART.md            # Start here!
│   ├── GUI_APPLICATION_GUIDE.md # GUI detailed guide
│   ├── OFFICIAL_PYTORCH_FIX.md  # PyTorch setup guide
│   ├── GPU_SETUP_GUIDE.md       # Comprehensive GPU guide
│   └── SETUP_AND_USAGE.md       # CLI guide
│
├── Models/                        # Pre-trained YOLO models
│   ├── yolo11n-seg.pt           # Nano (fastest, lowest VRAM)
│   ├── yolo11s-seg.pt           # Small (balanced)
│   └── yolo11m-seg.pt           # Medium (best accuracy)
│
├── Launchers/                     # Quick start scripts
│   ├── run_gui.bat              # Launch GUI application
│   ├── run_masker.bat           # Launch CLI application
│   └── build_executable.bat     # Create standalone .exe
│
├── Build/                         # Build artifacts
│   ├── dist/                    # Generated executable
│   ├── build/                   # Build files
│   └── YOLO_Masker.spec        # PyInstaller config
│
└── README.md                      # This file
```

## 🚀 Quick Start

### Option 1: GUI Application (Recommended)
```bash
Double-click: Launchers/run_gui.bat
```

**Features:**
- No command line required
- Visual folder selection
- Real-time progress
- Settings adjustment
- GPU acceleration

### Option 2: Command Line
Edit `App/yolo_equirectangular_masker.py` and update:
```python
INPUT_DIR = r"<YOUR_INPUT_FOLDER_PATH>"
OUTPUT_DIR = r"<YOUR_OUTPUT_FOLDER_PATH>"
```

Then run:
```bash
python App/yolo_equirectangular_masker.py
```

---

## 🎮 GPU Setup

### First Time Setup

1. **Check GPU:**
   ```bash
   python Setup/verify_cuda.py
   ```

2. **If GPU not detected, fix it:**
   ```bash
   Double-click: Setup/FIX_GPU_OFFICIAL.bat
   ```

3. **Restart computer**

4. **Verify:**
   ```bash
   python Setup/verify_cuda.py
   ```

Should show: `✅ GPU IS READY!`

---

## 📖 Documentation

| Guide | Purpose |
|-------|---------|
| **Guides/QUICKSTART.md** | Start here - basic usage |
| **Guides/GUI_APPLICATION_GUIDE.md** | Detailed GUI features |
| **Guides/OFFICIAL_PYTORCH_FIX.md** | GPU setup (official) |
| **Guides/GPU_SETUP_GUIDE.md** | Troubleshooting GPU |
| **Guides/SETUP_AND_USAGE.md** | Command-line usage |

---

## 🎨 Features

✅ **Multi-format support** - PNG, JPG, JPEG  
✅ **GPU acceleration** - 10-30x faster with NVIDIA GPU  
✅ **Mask expansion** - Adjustable pixel expansion (0-150px)  
✅ **Output options** - Save masks only, images only, or both  
✅ **Resolution modes** - Full, half, or quarter resolution  
✅ **Real-time progress** - Visual progress bar and logging  
✅ **Batch processing** - Process hundreds of images automatically  

---

## 💻 System Requirements

**Minimum:**
- Python 3.10-3.14
- 4GB RAM
- 5GB disk space

**Recommended (GPU):**
- NVIDIA RTX GPU (20 series or newer)
- 8GB+ VRAM
- NVIDIA drivers (latest)
- CUDA support in PyTorch

---

## ⚡ Performance

**Processing Speed (per 8K image):**

| Setup | Time | Speedup |
|-------|------|---------|
| CPU | 30-60s | Baseline |
| GPU (Full Res) | 3-5s | 10x |
| GPU (Half Res) | 1-2s | 20x |
| GPU (Quarter Res) | 0.5-1s | 50x |

**Batch Processing (1000 images):**
- CPU: 8-15 hours
- GPU: 30-50 minutes

---

## 🎯 Mask Logic

- **WHITE pixels** = KEEP (do not mask)
- **BLACK pixels** = MASK/AVOID (remove)

This follows standard image editing conventions.

---

## 🔧 Installation

### Step 1: Install Python Dependencies

**For GUI:**
```bash
pip install -r App/requirements_gui.txt
```

**For CLI:**
```bash
pip install -r App/requirements.txt
```

### Step 2: GPU Setup (Optional but Recommended)

```bash
python Setup/verify_cuda.py
```

If GPU not available, run:
```bash
Setup/FIX_GPU_OFFICIAL.bat
```

### Step 3: Run Application

**GUI:**
```bash
Launchers/run_gui.bat
```

**CLI:**
```bash
python App/yolo_equirectangular_masker.py
```

---

## 📊 Output Structure

```
your_output_folder/
├── masks/
│   ├── image_001_mask.png       (White=keep, Black=mask)
│   ├── image_002_mask.png
│   └── ...
└── masked_images/
    ├── image_001_masked.png     (or .jpg)
    ├── image_002_masked.png
    └── ...
```

---

## 🐛 Troubleshooting

**GPU Not Detected:**
```bash
python Setup/verify_cuda.py
```

Then follow instructions in Setup/OFFICIAL_PYTORCH_FIX.md

**Processing is Slow:**
- Enable GPU (see above)
- Use "Half Resolution" mode in GUI
- Close other applications

**Images Not Masking:**
- Lower confidence threshold (try 0.2-0.3)
- Check images are in supported format (PNG, JPG, JPEG)
- Increase mask expansion value

**Out of Memory:**
- Switch to smaller YOLO model (yolo11n-seg)
- Use "Quarter Resolution" mode
- Reduce batch size

---

## 📚 Model Selection

| Model | Speed | Accuracy | VRAM | Best For |
|-------|-------|----------|------|----------|
| yolo11n-seg | Fastest | Good | 2GB | Speed priority |
| yolo11s-seg | Balanced | Better | 4GB | Balanced |
| yolo11m-seg | Slower | Best | 8GB+ | Accuracy |

---

## 🎓 Typical Workflow

1. **Capture:** Record video with equirectangular camera
2. **Extract:** Convert video to image frames (PNG/JPG)
3. **Mask:** Run YOLO masker on frames
4. **Refine:** (Optional) Edit masks manually
5. **Photogrammetry:** Feed to SfM software (Colmap, Metashape)
6. **Splatting:** Process with Gaussian Splatting (3DGS)

---

## 📝 Configuration

### Confidence Threshold
- **Default:** 0.3
- **Range:** 0.0-1.0
- **Lower:** More detections (more false positives)
- **Higher:** Fewer detections (more accurate)

### Mask Expansion
- **Default:** 0 pixels
- **Range:** 0-150 pixels
- **Purpose:** Expand mask boundary for safety margin

### Processing Resolution
- **Full:** Original image size (best quality, slowest)
- **Half:** 0.5x resolution (good balance)
- **Quarter:** 0.25x resolution (fastest, lowest quality)

---

## 🔗 Links

- **PyTorch:** https://pytorch.org/get-started/locally/
- **CUDA Drivers:** https://www.nvidia.com/Download/driverDetails.aspx
- **YOLO Documentation:** https://docs.ultralytics.com/

---

## 💡 Tips

1. **Start with GUI** - easier than command line
2. **Enable GPU** - game changer for speed
3. **Use half resolution** - good balance for 8K images
4. **Monitor GPU** - run `nvidia-smi -l 1` in another window
5. **Save masks only** - faster if you don't need images

---

## ✅ Checklist Before First Run

- [ ] Python 3.10-3.14 installed
- [ ] Dependencies installed (`pip install -r requirements_gui.txt`)
- [ ] GPU verified (optional but recommended)
- [ ] Input folder contains PNG/JPG images
- [ ] Output folder selected or will be created
- [ ] Read QUICKSTART.md guide

---

## 📧 Support

For issues:
1. Check **Guides/** folder for relevant documentation
2. Run **Setup/verify_cuda.py** to diagnose GPU issues
3. Review troubleshooting section above
4. Check error messages in GUI log output

---

**Ready to mask images? Start with:** `Launchers/run_gui.bat` 🚀
