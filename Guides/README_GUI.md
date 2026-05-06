# 🎨 YOLO Image Masker - GUI Application

A professional graphical interface for masking humans and cars in equirectangular images for photogrammetry and Gaussian splatting.

## 📦 What You Get

Two ways to run the application:

1. **Python Script** (`yolo_masker_gui.py`) - Requires Python installed
2. **Standalone Executable** (`YOLO_Masker.exe`) - No Python required

---

## 🚀 Quick Start - Run Python Version

### 1. Install Dependencies
```bash
pip install -r requirements_gui.txt
```

### 2. Launch Application
**Option A - Batch File (Easiest):**
Double-click: `run_gui.bat`

**Option B - Command Line:**
```bash
python yolo_masker_gui.py
```

### 3. Use the Application
- Click **Browse** to select input folder (PNG/JPG/JPEG images)
- Click **Browse** to select output folder
- Adjust settings (model, confidence)
- Click **▶ START PROCESSING**
- Watch progress in real-time
- Check results in output folder

---

## 📦 Build Standalone Executable

Create a `.exe` file that runs without Python installed.

### 1. Install Build Tools
```bash
pip install -r requirements_gui.txt
```

### 2. Build Executable
**Option A - Batch File (Recommended):**
Double-click: `build_executable.bat`

**Option B - Command Line:**
```bash
pyinstaller --onefile --windowed --name "YOLO_Masker" yolo_masker_gui.py
```

### 3. Wait for Build
- Takes 2-5 minutes
- Creates `dist` folder
- Executable: `dist\YOLO_Masker.exe`

### 4. Run Executable
- Double-click `dist\YOLO_Masker.exe`
- OR run from command line: `dist\YOLO_Masker.exe`
- First run: Downloads YOLO model (~800MB)

### 5. Distribute (Optional)
- Copy `dist\YOLO_Masker.exe` to other computers
- No Python installation needed on target computers
- Model downloads on first run

---

## 🎯 Using the GUI Application

### Interface Layout

```
╔════════════════════════════════════════════════════════╗
║  YOLO Image Masker                                     ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  📁 Input Folder (PNG/JPG/JPEG):  [path]  [Browse]   ║
║  📁 Output Folder:                 [path]  [Browse]   ║
║                                                        ║
║  🤖 YOLO Model:                    [Dropdown ▼]       ║
║  🎯 Confidence Threshold:          [======●===]  0.50 ║
║                                                        ║
║  [▶ START PROCESSING]  [❌ CANCEL]                    ║
║                                                        ║
║  📊 Progress: [████████░░░░░░░░░░░░]  50%            ║
║  Status: Processing...                                 ║
║                                                        ║
║  📝 Log Output:                                        ║
║  ✅ frame_001.png                                      ║
║  ✅ frame_002.png                                      ║
║  Processing: 2/150 - frame_003.png                     ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```

### Step-by-Step Usage

1. **Select Input Folder**
   - Click "Browse" button next to "Input Folder"
   - Navigate to folder with PNG/JPG/JPEG images
   - Click "Open"

2. **Select Output Folder**
   - Click "Browse" button next to "Output Folder"
   - Choose where to save masks and processed images
   - Click "Open"

3. **Configure Settings (Optional)**
   - **Model**: Choose between yolo11n/s/m
   - **Confidence**: Drag slider to adjust detection sensitivity

4. **Start Processing**
   - Click "▶ START PROCESSING"
   - Watch real-time progress and log
   - Processing uses GPU automatically

5. **View Results**
   - Two folders created in output location:
     - `masks/` - Binary mask files (White=keep, Black=mask)
     - `masked_images/` - Processed images with masked regions removed

---

## 🎨 Mask Logic

### WHITE = KEEP | BLACK = MASK

```
Input Image          +  Binary Mask        =  Masked Output
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Person      │     │ ████ BLACK   │     │              │
│  Car ░░░░░░  │  +  │ ░░░░ WHITE   │  =  │              │
│  Background  │     │ ░░░░ WHITE   │     │ Background   │
└──────────────┘     └──────────────┘     └──────────────┘
```

- **WHITE pixels in mask** = Keep this region (no masking)
- **BLACK pixels in mask** = Remove this region (mask out humans/cars)

This is the standard masking convention used in professional image editing.

---

## ⚙️ System Requirements

### Minimum (CPU)
- Python 3.8+
- 4GB RAM
- 5GB disk space

### Recommended (GPU)
- Python 3.8+
- 8GB RAM
- 10GB disk space
- **NVIDIA GPU** with CUDA 11.8+
- **GPU VRAM**: 4GB+ (depends on model)

### For Executable
- No Python needed
- 2GB+ disk space (executable ~1GB, models ~800MB)
- Windows 7+ or equivalent

---

## 📊 Performance Metrics

### Processing Speed (per 1000 images)

| Setup | yolo11n-seg | yolo11s-seg | yolo11m-seg |
|-------|------------|------------|------------|
| GPU (NVIDIA) | 10-15 min | 15-20 min | 25-30 min |
| CPU | 100-200 min | 150-300 min | 200-400 min |

**Recommendation**: Use GPU for best experience

---

## 🔧 Advanced Configuration

### Custom Model Size

Edit `yolo_masker_gui.py` to add more options:

```python
self.model_var = ttk.Combobox(
    model_frame,
    values=[
        "yolo11n-seg (Fastest)",
        "yolo11s-seg (Balanced)",
        "yolo11m-seg (Best)",
        "yolo11l-seg (Maximum)"  # Add this
    ],
    ...
)
```

### Detect Additional Objects

Modify TARGET_CLASSES in `yolo_masker_gui.py`:

```python
self.TARGET_CLASSES = {
    0: "person",
    2: "car",
    15: "dog",      # Add dog
    16: "cat",      # Add cat
    20: "airplane", # Add airplane
}
```

[Full COCO class list](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/datasets/coco.yaml)

---

## 🐛 Troubleshooting

### GUI Won't Start

**Error**: "ModuleNotFoundError: No module named 'tkinter'"

**Solution**:
```bash
# Windows
python -m pip install tk

# macOS
brew install python-tk@3.11

# Linux
sudo apt-get install python3-tk
```

### GPU Not Detected

**Error**: Processing only on CPU

**Solution 1 - Check GPU:**
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

**Solution 2 - Install GPU Support:**
```bash
# NVIDIA CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Out of Memory

**Error**: CUDA out of memory

**Solution**: 
- Use smaller model: yolo11n-seg
- Close other applications
- Restart computer

### Build Fails

**Error**: PyInstaller build error

**Solution**:
```bash
# Reinstall PyInstaller
pip uninstall pyinstaller
pip install pyinstaller==6.0.0
python -m PyInstaller --version  # Verify
```

---

## 📁 File Structure

```
Automasker/
├── yolo_masker_gui.py           # Main GUI application
├── yolo_equirectangular_masker.py # Command-line version
├── requirements_gui.txt          # Python dependencies
├── requirements.txt              # CLI dependencies
├── run_gui.bat                   # Launch GUI (Python)
├── build_executable.bat          # Build .exe file
├── GUI_APPLICATION_GUIDE.md      # Detailed documentation
├── README_GUI.md                 # This file
└── dist/                         # Created after build
    └── YOLO_Masker.exe          # Standalone executable
```

---

## 📚 Documentation

- **GUI_APPLICATION_GUIDE.md** - Comprehensive GUI documentation
- **SETUP_AND_USAGE.md** - Command-line version guide
- **README_GUI.md** - This file

---

## 🎓 Typical Workflow

1. **Capture Images**
   - Record video with Insta360 X5
   - Extract frames as PNG or JPG

2. **Prepare Input**
   - Create folder with all frames
   - Ensure PNG/JPG format

3. **Run Masker**
   - Launch `YOLO_Masker.exe` or Python version
   - Select folders
   - Process images

4. **Use Output**
   - Feed `masked_images/` to photogrammetry software
   - OR use `masks/` for manual refinement
   - Then process with Gaussian Splatting

---

## 💡 Tips

### For Best Results
- Use GPU for faster processing
- Start with confidence=0.5, adjust if needed
- Use yolo11n-seg for speed, yolo11m-seg for accuracy

### For Large Batches
- Process overnight for 1000+ images
- Monitor with `nvidia-smi` (GPU monitor)
- Don't close application until complete

### For Manual Refinement
- Open masks in Photoshop/GIMP
- Use brush to add/remove masked areas
- Save refined masks
- Use with custom pipeline

---

## 🚀 Next Steps

1. **For Python Version**: `run_gui.bat` or `python yolo_masker_gui.py`
2. **For Executable**: `build_executable.bat` (takes 2-5 minutes)
3. **Full Guide**: Read `GUI_APPLICATION_GUIDE.md`

---

**Ready to mask your images? Let's go! 🎯**
