# YOLO Masker GUI Application

A user-friendly graphical interface for masking humans and cars in equirectangular images.

## 🎨 Features

✅ **Easy-to-Use Interface** - No command line required  
✅ **Folder Selection** - Browse and select input/output folders with GUI buttons  
✅ **Real-Time Progress** - Visual progress bar and status updates  
✅ **Model Selection** - Choose between YOLO11n/s/m variants  
✅ **Configurable Settings** - Adjust confidence threshold on the fly  
✅ **Live Log Output** - See processing results in real-time  
✅ **Inverted Mask Logic** - WHITE = keep, BLACK = mask/avoid  
✅ **Multi-Format Support** - Process PNG, JPG, and JPEG files  

## 📋 Mask Logic

**IMPORTANT: This GUI uses inverted mask logic:**

- 🟡 **WHITE pixels** = KEEP (do not mask/remove)
- ⚫ **BLACK pixels** = MASK/AVOID (remove this region)

This is opposite from the command-line version and is more intuitive for image processing workflows.

## 🚀 Option 1: Run as Python Script

### Requirements
```bash
pip install -r requirements_gui.txt
```

### Run Application
```bash
python yolo_masker_gui.py
```

**Pros:**
- No build process needed
- Can easily modify the code
- Lighter weight

**Cons:**
- Requires Python installed
- Slightly slower to start

---

## 📦 Option 2: Build as Executable (.exe)

Create a standalone executable that doesn't require Python.

### Build Steps

1. **Install Build Dependencies**
   ```bash
   pip install -r requirements_gui.txt
   ```

2. **Run Build Script**
   Double-click `build_executable.bat`
   
   OR from command line:
   ```bash
   build_executable.bat
   ```

3. **Wait for Build** (2-5 minutes)
   - PyInstaller will package everything
   - First run downloads YOLO model automatically
   - Progress will be shown in console

4. **Executable Created**
   - Location: `dist\YOLO_Masker.exe`
   - Can be moved/distributed independently
   - No Python required to run

**Pros:**
- Standalone executable
- No Python installation needed
- Can distribute to others
- Professional appearance

**Cons:**
- Larger file size (~1-2GB with models)
- Longer build time
- First run still downloads YOLO model

---

## 🎯 How to Use the GUI

### Step 1: Select Input Folder
1. Click **"Browse"** next to "Input Folder"
2. Navigate to folder containing your PNG/JPG images
3. Click **"Open"**

### Step 2: Select Output Folder
1. Click **"Browse"** next to "Output Folder"
2. Choose where you want to save masks and masked images
3. Click **"Open"**

### Step 3: Configure Settings (Optional)
- **YOLO Model**: Select model variant
  - `yolo11n-seg` (Default) - Fastest, uses 2GB VRAM
  - `yolo11s-seg` - Balanced, uses 4GB VRAM
  - `yolo11m-seg` - Best accuracy, uses 8GB+ VRAM

- **Confidence Threshold**: Drag slider to adjust
  - Lower (0.3-0.4) = More detections, more false positives
  - Higher (0.6-0.7) = Fewer detections, more reliable
  - Default: 0.5

### Step 4: Start Processing
1. Click **"▶ START PROCESSING"**
2. Watch progress bar and log output
3. Processing happens on GPU automatically

### Step 5: View Results
When complete:
- Check the output folder
- Two subfolders created:
  - `masks/` - Binary mask files
  - `masked_images/` - Processed images

---

## 📊 Output Structure

```
your_output_folder/
├── masks/
│   ├── frame_001_mask.png      (White=keep, Black=mask)
│   ├── frame_002_mask.png
│   └── ...
└── masked_images/
    ├── frame_001_masked.png    (or .jpg)
    ├── frame_002_masked.png
    └── ...
```

---

## ⚙️ System Requirements

### Minimum (CPU Processing)
- Python 3.8+
- 4GB RAM
- 5GB disk space
- Processor: Modern multi-core CPU

### Recommended (GPU Processing)
- Python 3.8+
- 8GB RAM
- 10GB disk space
- **GPU**: NVIDIA with CUDA 11.8+
- GPU VRAM: 4GB+ (depending on model)

### Apple Silicon
- Python 3.9+ (native ARM64)
- 8GB RAM
- 10GB disk space
- Automatic Metal Performance Shaders (MPS) support

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'ultralytics'"

**Solution:**
```bash
pip install -r requirements_gui.txt
```

### Issue: GUI doesn't start

**Solution:**
```bash
# Try running with verbose output
python yolo_masker_gui.py
```

If error occurs, check console output and ensure tkinter is installed:
```bash
# Windows
python -m pip install tk

# macOS
brew install python-tk

# Linux
sudo apt-get install python3-tk
```

### Issue: Out of Memory Error

**Solution:**
1. Switch to lighter model: `yolo11n-seg`
2. Close other applications
3. Reduce batch size (requires code modification)

### Issue: GPU not detected

**Check GPU:**
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

**Install GPU support:**
```bash
# NVIDIA CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Apple Silicon (auto-enabled)
# No extra steps needed
```

### Issue: Processing is very slow

**Check if using GPU:**
- Look at first few log lines
- Should show GPU model name
- If CPU, install CUDA as above

---

## 📝 Advanced: Build Customization

### Change Application Icon

Create or find a `.ico` file (e.g., `app_icon.ico`) in the same folder, then run:

```bash
pyinstaller --onefile --windowed --icon=app_icon.ico yolo_masker_gui.py
```

### Build with Console Window

Remove `--windowed` flag to keep console visible:

```bash
pyinstaller --onefile --icon=app_icon.ico yolo_masker_gui.py
```

### Include Additional Files

Modify build command:

```bash
pyinstaller --onefile --windowed --add-data "your_file.txt:." yolo_masker_gui.py
```

---

## 🔄 Mask Logic Explanation

### Why Inverted?

**Command-line version (original):**
- BLACK = keep
- WHITE = mask

**GUI version (intuitive):**
- WHITE = keep (natural color, typically means "keep this")
- BLACK = mask (dark color, typically means "remove")

This follows common image editing conventions (e.g., Photoshop masks, Blender UV masks).

### How It Works

1. YOLO detects humans and cars
2. Creates mask where detections occur
3. **Inverts the mask** so:
   - Detection regions become BLACK (mask/avoid)
   - Non-detection regions become WHITE (keep)
4. Saves both:
   - Binary mask file (for reference/manual adjustment)
   - Masked image (with black regions filled in)

---

## 📚 Integration with Photogrammetry Pipelines

### Direct Use
Feed `masked_images/` directly to your photogrammetry software:
- Metashape
- PhotoScan
- RealityCapture
- Colmap + 3DGS

Black regions will be naturally ignored during reconstruction.

### Advanced Use
Use mask files separately:
```python
# Example: Use masks in custom pipeline
from PIL import Image
import cv2

mask = cv2.imread("frame_001_mask.png", cv2.IMREAD_GRAYSCALE)
image = cv2.imread("frame_001.png")

# Apply mask
masked = cv2.bitwise_and(image, image, mask=mask)
```

---

## 🎓 Tips & Tricks

### Processing Large Batches
- Process overnight for 1000+ images
- Monitor GPU memory with `nvidia-smi` (Windows/Linux)
- Close other applications

### Adjusting Sensitivity
- **Too many false positives?** Increase confidence threshold (0.6-0.7)
- **Missing detections?** Decrease confidence threshold (0.3-0.4)
- **Wrong detections?** Try different YOLO model size

### Manual Mask Refinement
After processing:
1. Open masks in image editor (Photoshop, GIMP)
2. Edit with brush tools
3. Use edited masks in your pipeline

---

## 📞 Support

For issues or feature requests:
1. Check troubleshooting section above
2. Review error messages in log output
3. Verify input folder contains valid images
4. Ensure GPU drivers are up to date

---

## License

This application uses:
- **YOLO11** - AGPL-3.0 License
- **OpenCV** - Apache 2.0 License
- **PyTorch** - BSD License

Ensure compliance with these licenses for your use case.

---

**Happy Processing! 🚀**
