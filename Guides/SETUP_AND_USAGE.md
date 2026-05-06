# YOLO Equirectangular Image Masking Pipeline

A Python pipeline for masking humans and cars in equirectangular images from Insta360 X5 cameras, optimized for photogrammetry and Gaussian splatting preprocessing.

## Features

✅ **Multi-Format Support**: Processes PNG, JPG, and JPEG images  
✅ **Automatic Detection**: Uses YOLO11-seg to detect and segment humans and cars  
✅ **Binary Masks**: Generates precise mask files for each image  
✅ **Masked Images**: Creates processed images with masked regions removed  
✅ **Batch Processing**: Handles entire folders of images efficiently  
✅ **Progress Tracking**: Real-time progress bar for processing status  
✅ **Robust Error Handling**: Gracefully handles corrupted or invalid images  

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Note**: This will install:
- `ultralytics` - YOLO11 model framework
- `opencv-python` - Image processing
- `torch` & `torchvision` - Deep learning backends
- `numpy` & `pillow` - Array and image handling
- `tqdm` - Progress bars

### 2. First Run Setup

The first time you run the script, it will automatically:
1. Download the YOLO11n-seg pre-trained model (~800MB)
2. Cache it locally for future runs
3. Begin processing your images

**Initial download may take 2-5 minutes depending on internet speed.**

## Usage

### Basic Usage

```bash
python yolo_equirectangular_masker.py
```

### What It Does

The script will:

1. **Scan** `D:\Insta360 X5 Data\Qalandrabad\VID_20260503_074527_00_037\frames` for all PNG, JPG, and JPEG images
2. **Process** each image with YOLO11-seg to detect humans and cars
3. **Generate** two outputs for each image:
   - **Binary Mask** (e.g., `frame_001_mask.png`) - White pixels = masked regions, Black = keep
   - **Masked Image** (e.g., `frame_001_masked.png` or `frame_001_masked.jpg`) - Original image with masked areas turned black
4. **Save** all outputs to:
   - Masks: `D:\Insta360 X5 Data\Qalandrabad\VID_20260503_074527_00_037\masks\masks\`
   - Masked Images: `D:\Insta360 X5 Data\Qalandrabad\VID_20260503_074527_00_037\masks\masked_images\`

**Note**: PNG input images are saved as PNG output, JPG/JPEG inputs are saved as JPG output

### Output Structure

```
masks/
├── masks/
│   ├── frame_001_mask.png
│   ├── frame_002_mask.png
│   └── ...
└── masked_images/
    ├── frame_001_masked.jpg
    ├── frame_002_masked.jpg
    └── ...
```

## Performance Notes

### Processing Speed

Using YOLO11n-seg (lightweight model):
- **GPU** (NVIDIA/CUDA): ~50-100 images/minute
- **CPU**: ~5-10 images/minute

Total time estimates for 1000 frames:
- GPU: 10-20 minutes
- CPU: 100-200 minutes

### Model Variants

You can modify the model in the script for different speed/accuracy trade-offs:

```python
# In yolo_equirectangular_masker.py, change:
model_name="yolo11n-seg"  # Current: nano (fastest, lowest VRAM)
# to:
model_name="yolo11s-seg"  # Small (better accuracy, more VRAM)
model_name="yolo11m-seg"  # Medium (best accuracy, high VRAM)
```

**VRAM Requirements**:
- `yolo11n-seg`: 2GB
- `yolo11s-seg`: 4GB
- `yolo11m-seg`: 8GB+

## Integration with Gaussian Splatting

### Using the Masks

The generated masks can be used with popular Gaussian Splatting pipelines:

**For Direct Integration**:
- Feed `masked_images/` folder directly to your NeRF/GS pipeline
- The black regions will be naturally ignored

**For Fine-Grained Control**:
- Use the binary masks from `masks/` folder
- Integrate mask files into your custom GS preprocessing

### Next Steps

1. ✅ Run this script to generate masks
2. ⬜ (Optional) Use Clean-GS for post-processing of GS reconstruction
3. ⬜ Feed masked images to your photogrammetry software (Metashape, etc.)
4. ⬜ Process with Gaussian Splatting (3DGS, COLMAP, etc.)

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'ultralytics'"

**Solution**: Make sure you installed requirements.txt

```bash
pip install -r requirements.txt
```

### Issue: Out of Memory (OOM) Error

**Solution**: Switch to lighter model:

```python
model_name="yolo11n-seg"  # Already using lightest model
```

Or process in smaller batches with custom script modification.

### Issue: Slow Processing (CPU Only)

**Solution**: Install GPU support:

```bash
# For NVIDIA CUDA GPUs
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For Apple Silicon (MPS)
# Automatic - no extra install needed
```

### Issue: No Masks Generated / All Black Masks

**Possible Causes**:
- Confidence threshold too high (currently 0.5)
- Images are not equirectangular format
- YOLO not detecting humans/cars in your specific scenes

**Debug Step**: Check if YOLO detects anything:
```python
# Add to the script temporarily:
results = self.model(image, conf=0.3)  # Lower confidence
print(results[0].boxes)  # See what was detected
```

## Advanced Customization

### Adjust Detection Confidence

In `yolo_equirectangular_masker.py`, find and modify:

```python
results = self.model(image, conf=0.5)  # Change 0.5 to desired threshold
```

- Lower values (0.3-0.4): More detections, more false positives
- Higher values (0.6-0.7): Fewer detections, more reliable

### Mask Additional Classes

To mask additional objects (sky, animals, etc.), modify the TARGET_CLASSES:

```python
self.TARGET_CLASSES = {
    0: "person",
    2: "car",
    15: "bird",      # Add bird class
    16: "cat",       # Add cat class
}
```

[Full COCO class list](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/datasets/coco.yaml)

### Custom Fill Methods

The script supports transparent fills. Modify the call in `process_image()`:

```python
# For transparent PNG output (requires PNG writing):
masked_image = self.apply_mask_to_image(image, mask, fill_method="transparent")
```

## Requirements & Dependencies

- **Python**: 3.8 or higher
- **GPU** (Optional but recommended): NVIDIA CUDA 11.8+ or Apple Silicon
- **Disk Space**: ~5GB (model cache + outputs)
- **RAM**: 4GB minimum (8GB+ for smoother operation)

## References

- [Ultralytics YOLO Documentation](https://docs.ultralytics.com/)
- [YOLO Instance Segmentation](https://docs.ultralytics.com/tasks/segment/)
- [COCO Dataset Classes](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/datasets/coco.yaml)

## License

This pipeline uses YOLO11, which is licensed under AGPL-3.0. Ensure compliance with your use case.

---

**Need Help?**

1. Check the troubleshooting section above
2. Review the console output for specific error messages
3. Verify image formats are JPEG in the input folder
4. Ensure paths use raw strings (r"...") for Windows paths
