# Quick Start Guide - 5 Minutes to Masking

## 🎯 The Easiest Path

### 1️⃣ Run the GUI Application
```bash
Double-click: Launchers/run_gui.bat
```

You'll see a window with:
- Input folder selector
- Output folder selector
- Model selection dropdown
- Settings sliders
- Progress bar

### 2️⃣ Select Your Input Folder
Click **"Browse"** next to "Input Folder"
- Navigate to folder with your PNG/JPG images
- Click **"Open"**

### 3️⃣ Select Output Folder
Click **"Browse"** next to "Output Folder"
- Choose where to save masks and masked images
- Click **"Open"**

### 4️⃣ Configure Settings (Optional)
- **Model:** yolo11n-seg (default - fastest)
- **Confidence:** 0.3 (default - good balance)
- **Mask Expansion:** 0 px (default - no expansion)
- **Output:** Both (masks + images)
- **Processing Speed:** Full Resolution (default)

### 5️⃣ Click "▶ START PROCESSING"
Watch the progress bar and log output

### 6️⃣ Check Results
Two folders created:
- `masks/` - Binary mask files (White=keep, Black=mask)
- `masked_images/` - Processed images with masked areas removed

---

## 🚀 Expected Results

**For 8K images with GPU:**
- Time per image: 1-5 seconds
- 1000 images: 30-50 minutes

**For 8K images without GPU:**
- Time per image: 30-60 seconds
- 1000 images: 8-15 hours

---

## ⚡ GPU (Optional but Highly Recommended)

### Check if GPU Works
```bash
python Setup/verify_cuda.py
```

Should show: `✅ GPU IS READY!`

### If GPU Not Working
```bash
Setup/FIX_GPU_OFFICIAL.bat
```

Then restart computer.

---

## 📋 Settings Explained

### Model Selection
- **yolo11n-seg** ← Start here (fastest)
- **yolo11s-seg** - Balanced
- **yolo11m-seg** - Best accuracy (slower)

### Confidence Threshold
- **0.3** ← Recommended (good balance)
- **0.2** - More detections (sensitive)
- **0.5** - Fewer detections (conservative)

### Mask Expansion
- **0 px** ← Recommended (no expansion)
- **20-50 px** - Expand mask outward
- **150 px** - Maximum expansion

### Processing Speed
- **Full Resolution** - Original size (best quality)
- **Half Resolution** - 0.5x (balanced for 8K)
- **Quarter Resolution** - 0.25x (fastest)

### Output Options
- **Both** - Save masks AND images
- **Masks Only** - Faster (saves I/O time)
- **Images Only** - Skip masks

---

## 🎨 Output Files

### Mask Files
`image_001_mask.png`
- White = Keep this region
- Black = Remove this region (humans/cars)

### Masked Images
`image_001_masked.jpg`
- Original image with masked areas turned black
- Ready for photogrammetry software

---

## ❓ What If...

### "No images found"
- Check input folder contains PNG/JPG files
- Make sure files are actually images

### "Targets found but images look the same"
- Lower confidence threshold to 0.2-0.3
- Check images actually contain humans/cars

### "Processing very slow"
- Enable GPU (see above)
- Use "Half Resolution" or "Quarter Resolution"
- Use smaller model (yolo11n-seg)

### "GPU not detected"
- Run: `Setup/FIX_GPU_OFFICIAL.bat`
- Restart computer
- Run: `Setup/verify_cuda.py` to verify

---

## 📚 Next Steps

- **Want more details?** Read: `Guides/GUI_APPLICATION_GUIDE.md`
- **Having GPU issues?** Read: `Guides/OFFICIAL_PYTORCH_FIX.md`
- **Need command-line?** Read: `Guides/SETUP_AND_USAGE.md`
- **Full README:** Open `README.md`

---

## ✅ Checklist

- [ ] Python installed
- [ ] Opened `Launchers/run_gui.bat`
- [ ] Selected input folder with images
- [ ] Selected output folder
- [ ] Clicked "START PROCESSING"
- [ ] Results saved in output folder

---

**That's it! Happy masking! 🎉**

For detailed guides, see the **Guides/** folder.
