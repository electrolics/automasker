#!/usr/bin/env python3
"""
YOLO Equirectangular Image Masking Pipeline - GUI Version
Mask humans and cars in equirectangular images with intuitive GUI interface

Mask Logic:
- WHITE pixels = KEEP (do not mask)
- BLACK pixels = AVOID/MASK (remove this region)
"""

import os
import cv2
import numpy as np
import threading
from pathlib import Path
from tkinter import Tk, Frame, Label, Button, Entry, filedialog, messagebox, Scrollbar, Text, DoubleVar, StringVar
from tkinter import ttk
import tkinter.font as tkFont
from tqdm import tqdm
from ultralytics import YOLO
import torch


class MaskerGUI:
    """GUI Application for YOLO-based Image Masking"""

    def __init__(self, root):
        self.root = root
        self.root.title("YOLO Equirectangular Image Masker")
        self.root.geometry("750x900")
        self.root.resizable(True, True)

        # Variables
        self.input_dir = None
        self.output_dir = None
        self.is_processing = False
        self.model = None

        # Target classes: person and car
        self.TARGET_CLASSES = {0: "person", 2: "car"}

        # Check GPU availability
        self.gpu_available = torch.cuda.is_available()
        self.gpu_name = torch.cuda.get_device_name(0) if self.gpu_available else "None"

        # Set style
        self.setup_ui()

    def setup_ui(self):
        """Setup UI components"""

        # Header
        header_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
        gpu_color = "#27ae60" if self.gpu_available else "#e74c3c"
        gpu_text = f"✓ GPU: {self.gpu_name}" if self.gpu_available else "✗ GPU: Not Available (CPU Mode)"

        header_frame = Frame(self.root, bg="#2c3e50")
        header_frame.pack(fill="x")

        title_label = Label(
            header_frame,
            text="YOLO Image Masker",
            font=header_font,
            bg="#2c3e50",
            fg="white",
            pady=5
        )
        title_label.pack(anchor="w", padx=10)

        gpu_label = Label(
            header_frame,
            text=gpu_text,
            bg="#2c3e50",
            fg=gpu_color,
            font=("Courier", 9),
            pady=5
        )
        gpu_label.pack(anchor="w", padx=10)

        # Main frame
        main_frame = Frame(self.root, bg="white")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Information Box
        info_frame = Frame(main_frame, bg="#ecf0f1", relief="sunken", bd=1)
        info_frame.pack(fill="x", pady=10)

        info_text = """MASK LOGIC:
🟡 WHITE pixels = KEEP (do not mask)
⚫ BLACK pixels = MASK/AVOID (remove)"""

        info_label = Label(info_frame, text=info_text, bg="#ecf0f1", fg="#2c3e50", justify="left", font=("Courier", 10))
        info_label.pack(anchor="w", padx=10, pady=10)

        # Input Folder Selection
        input_frame = Frame(main_frame, bg="white")
        input_frame.pack(fill="x", pady=10)

        Label(input_frame, text="📁 Input Folder (PNG/JPG/JPEG):", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")

        input_button_frame = Frame(input_frame, bg="white")
        input_button_frame.pack(fill="x", pady=5)

        self.input_entry = Entry(input_button_frame, width=50, font=("Courier", 9))
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        Button(
            input_button_frame,
            text="Browse",
            command=self.select_input_folder,
            bg="#3498db",
            fg="white",
            padx=15,
            relief="raised",
            cursor="hand2"
        ).pack(side="left")

        # Output Folder Selection
        output_frame = Frame(main_frame, bg="white")
        output_frame.pack(fill="x", pady=10)

        Label(output_frame, text="📁 Output Folder:", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")

        output_button_frame = Frame(output_frame, bg="white")
        output_button_frame.pack(fill="x", pady=5)

        self.output_entry = Entry(output_button_frame, width=50, font=("Courier", 9))
        self.output_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        Button(
            output_button_frame,
            text="Browse",
            command=self.select_output_folder,
            bg="#3498db",
            fg="white",
            padx=15,
            relief="raised",
            cursor="hand2"
        ).pack(side="left")

        # Model Selection
        model_frame = Frame(main_frame, bg="white")
        model_frame.pack(fill="x", pady=10)

        Label(model_frame, text="🤖 YOLO Model:", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")

        self.model_var = ttk.Combobox(
            model_frame,
            values=["yolo11n-seg (Fastest, Lower VRAM)", "yolo11s-seg (Balanced)", "yolo11m-seg (Best Accuracy)"],
            state="readonly",
            width=40,
            font=("Helvetica", 9)
        )
        self.model_var.current(0)
        self.model_var.pack(fill="x", pady=5)

        # Confidence Threshold
        conf_frame = Frame(main_frame, bg="white")
        conf_frame.pack(fill="x", pady=10)

        Label(conf_frame, text="🎯 Confidence Threshold (0.0-1.0):", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")
        Label(conf_frame, text="Lower = More detections | Higher = More accurate", bg="white", font=("Courier", 8), fg="#7f8c8d").pack(anchor="w")

        self.conf_var = ttk.Scale(conf_frame, from_=0.0, to=1.0, orient="horizontal")
        self.conf_var.set(0.3)  # Lowered default for equirectangular images
        self.conf_var.pack(fill="x", pady=5)

        self.conf_label = Label(conf_frame, text="0.30", bg="white", fg="#27ae60", font=("Courier", 10))
        self.conf_label.pack(anchor="e")

        self.conf_var.config(command=self.update_confidence_label)

        # Mask Expansion
        expand_frame = Frame(main_frame, bg="white")
        expand_frame.pack(fill="x", pady=10)

        Label(expand_frame, text="📏 Mask Expansion (pixels):", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")
        Label(expand_frame, text="Expand mask boundary outward | 0 = No expansion", bg="white", font=("Courier", 8), fg="#7f8c8d").pack(anchor="w")

        self.expand_var = ttk.Scale(expand_frame, from_=0, to=150, orient="horizontal")
        self.expand_var.set(0)
        self.expand_var.pack(fill="x", pady=5)

        self.expand_label = Label(expand_frame, text="0 px", bg="white", fg="#e67e22", font=("Courier", 10))
        self.expand_label.pack(anchor="e")

        self.expand_var.config(command=self.update_expansion_label)

        # Output Options
        output_opts_frame = Frame(main_frame, bg="white")
        output_opts_frame.pack(fill="x", pady=10)

        Label(output_opts_frame, text="💾 Output Options:", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")

        self.save_masks_var = StringVar(value="both")

        option_inner_frame = Frame(output_opts_frame, bg="white")
        option_inner_frame.pack(fill="x", padx=0, pady=5)

        ttk.Radiobutton(
            option_inner_frame,
            text="Both (Masks + Images)",
            variable=self.save_masks_var,
            value="both"
        ).pack(anchor="w")

        ttk.Radiobutton(
            option_inner_frame,
            text="Masks Only (Faster)",
            variable=self.save_masks_var,
            value="masks_only"
        ).pack(anchor="w")

        ttk.Radiobutton(
            option_inner_frame,
            text="Masked Images Only",
            variable=self.save_masks_var,
            value="images_only"
        ).pack(anchor="w")

        # Processing Speed Options
        speed_frame = Frame(main_frame, bg="white")
        speed_frame.pack(fill="x", pady=10)

        Label(speed_frame, text="⚡ Processing Speed (For 8K Images):", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")
        Label(speed_frame, text="For faster processing of large images", bg="white", font=("Courier", 8), fg="#7f8c8d").pack(anchor="w")

        self.resize_var = StringVar(value="full")

        speed_inner_frame = Frame(speed_frame, bg="white")
        speed_inner_frame.pack(fill="x", padx=0, pady=5)

        ttk.Radiobutton(
            speed_inner_frame,
            text="Full Resolution (Slow, Best Quality)",
            variable=self.resize_var,
            value="full"
        ).pack(anchor="w")

        ttk.Radiobutton(
            speed_inner_frame,
            text="Half Resolution (Balanced)",
            variable=self.resize_var,
            value="half"
        ).pack(anchor="w")

        ttk.Radiobutton(
            speed_inner_frame,
            text="Quarter Resolution (Fast, GPU Recommended)",
            variable=self.resize_var,
            value="quarter"
        ).pack(anchor="w")

        # Start Button
        button_frame = Frame(main_frame, bg="white")
        button_frame.pack(fill="x", pady=20)

        self.start_button = Button(
            button_frame,
            text="▶ START PROCESSING",
            command=self.start_processing,
            bg="#27ae60",
            fg="white",
            font=("Helvetica", 12, "bold"),
            padx=20,
            pady=10,
            relief="raised",
            cursor="hand2"
        )
        self.start_button.pack(side="left", padx=5)

        Button(
            button_frame,
            text="❌ CANCEL",
            command=self.cancel_processing,
            bg="#e74c3c",
            fg="white",
            font=("Helvetica", 12, "bold"),
            padx=20,
            pady=10,
            relief="raised",
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Progress Section
        progress_frame = Frame(main_frame, bg="white")
        progress_frame.pack(fill="both", expand=True, pady=10)

        Label(progress_frame, text="📊 Progress:", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")

        self.progress_var = DoubleVar()
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            variable=self.progress_var,
            maximum=100,
            length=400,
            mode="determinate"
        )
        self.progress_bar.pack(fill="x", pady=5)

        self.status_label = Label(progress_frame, text="Ready", bg="white", fg="#2c3e50", font=("Courier", 9))
        self.status_label.pack(anchor="w", pady=5)

        # Log Output
        log_frame = Frame(main_frame, bg="white")
        log_frame.pack(fill="both", expand=True, pady=10)

        Label(log_frame, text="📝 Log Output:", bg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")

        # Scrollbar for text widget
        scrollbar = Scrollbar(log_frame)
        scrollbar.pack(side="right", fill="y")

        self.log_text = Text(
            log_frame,
            height=10,
            width=60,
            font=("Courier", 8),
            bg="#ecf0f1",
            fg="#2c3e50",
            yscrollcommand=scrollbar.set
        )
        self.log_text.pack(fill="both", expand=True)
        scrollbar.config(command=self.log_text.yview)

    def update_confidence_label(self, value):
        """Update confidence label"""
        self.conf_label.config(text=f"{float(value):.2f}")

    def update_expansion_label(self, value):
        """Update expansion label"""
        pixels = int(float(value))
        self.expand_label.config(text=f"{pixels} px")

    def select_input_folder(self):
        """Select input folder"""
        folder = filedialog.askdirectory(title="Select Input Folder (containing PNG/JPG images)")
        if folder:
            self.input_dir = folder
            self.input_entry.delete(0, "end")
            self.input_entry.insert(0, folder)
            self.log("Input folder selected: " + folder)

    def select_output_folder(self):
        """Select output folder"""
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_dir = folder
            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, folder)
            self.log("Output folder selected: " + folder)

    def log(self, message):
        """Add message to log"""
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.root.update()

    def start_processing(self):
        """Start processing in separate thread"""
        if not self.input_dir or not self.output_dir:
            messagebox.showerror("Error", "Please select both input and output folders!")
            return

        if not Path(self.input_dir).exists():
            messagebox.showerror("Error", "Input folder does not exist!")
            return

        self.start_button.config(state="disabled")
        self.is_processing = True

        # Start processing in background thread
        thread = threading.Thread(target=self.process_images)
        thread.daemon = True
        thread.start()

    def cancel_processing(self):
        """Cancel processing"""
        self.is_processing = False
        self.start_button.config(state="normal")
        self.log("Processing cancelled by user")
        self.status_label.config(text="Cancelled", fg="#e74c3c")

    def get_image_files(self):
        """Get all image files"""
        image_extensions = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG']
        image_files = []

        for ext in image_extensions:
            image_files.extend(Path(self.input_dir).glob(f'*{ext}'))

        return sorted(image_files)

    def create_binary_mask(self, result, image_height, image_width, expand_pixels=0):
        """
        Create binary mask from YOLO results
        Inverted logic: BLACK = mask/avoid, WHITE = keep

        Args:
            result: YOLO detection result
            image_height: Image height in pixels
            image_width: Image width in pixels
            expand_pixels: Number of pixels to expand mask outward
        """
        # Start with WHITE (all keep)
        mask = np.ones((image_height, image_width), dtype=np.uint8) * 255

        if result.masks is None:
            return mask

        # Get class indices and masks
        class_indices = result.boxes.cls.cpu().numpy().astype(int)
        masks = result.masks.data.cpu().numpy()

        # Apply masks for target classes - BLACK = mask/avoid
        for idx, class_idx in enumerate(class_indices):
            if class_idx in self.TARGET_CLASSES:
                # Get mask - it comes as float [0.0-1.0]
                detection_mask = masks[idx]

                # Convert float mask [0.0-1.0] to [0-255]
                detection_mask_uint8 = (detection_mask * 255).astype(np.uint8)

                # Resize mask to match image dimensions
                # cv2.resize takes (width, height) not (height, width)
                resized_mask = cv2.resize(
                    detection_mask_uint8,
                    (image_width, image_height),
                    interpolation=cv2.INTER_LINEAR
                )

                # Expand mask if requested
                if expand_pixels > 0:
                    # Create dilation kernel (circular structuring element)
                    kernel_size = (expand_pixels * 2 + 1, expand_pixels * 2 + 1)
                    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
                    # Dilate the mask to expand detected regions
                    resized_mask = cv2.dilate(resized_mask, kernel, iterations=1)

                # Set detected regions to BLACK (0)
                # Use threshold to convert to binary
                mask[resized_mask > 127] = 0

        return mask

    def apply_mask_to_image(self, image, mask):
        """Apply mask to image (black fill for masked regions)"""
        masked_image = image.copy()

        # Ensure mask is uint8
        if mask.dtype != np.uint8:
            mask = mask.astype(np.uint8)

        # Create 3-channel version of mask for BGR image
        mask_3channel = np.stack([mask, mask, mask], axis=2)

        # Where mask is BLACK (0), set image to black
        masked_image[mask_3channel == 0] = 0

        return masked_image

    def process_images(self):
        """Process all images"""
        try:
            self.log_text.delete(1.0, "end")
            self.log("=" * 50)
            self.log("YOLO Image Masking Pipeline Started")
            self.log("=" * 50)

            # Get model variant
            model_mapping = {
                0: "yolo11n-seg",  # Nano - Fastest
                1: "yolo11s-seg",  # Small - Balanced
                2: "yolo11m-seg"   # Medium - Best accuracy
            }
            model_name = model_mapping[self.model_var.current()]

            # Load model
            self.log(f"\n📥 Loading {model_name} model...")
            self.status_label.config(text="Loading model...", fg="#f39c12")

            # Determine device
            device = 0 if self.gpu_available else "cpu"  # 0 = GPU, "cpu" = CPU
            self.model = YOLO(model_name)
            self.model.to(device)

            if self.gpu_available:
                self.log(f"✅ Model loaded on GPU: {self.gpu_name}")
            else:
                self.log(f"✅ Model loaded on CPU (GPU not available)")

            # Create output directories
            output_path = Path(self.output_dir)
            masks_dir = output_path / "masks"
            masked_images_dir = output_path / "masked_images"

            masks_dir.mkdir(parents=True, exist_ok=True)
            masked_images_dir.mkdir(parents=True, exist_ok=True)

            self.log(f"\n📁 Output Directories Created:")
            self.log(f"   Masks: {masks_dir}")
            self.log(f"   Masked Images: {masked_images_dir}")

            # Get image files
            image_files = self.get_image_files()

            if not image_files:
                self.log("\n❌ No PNG/JPG images found in input folder!")
                self.status_label.config(text="No images found", fg="#e74c3c")
                self.start_button.config(state="normal")
                return

            self.log(f"\n🖼️  Found {len(image_files)} images to process")

            conf_threshold = float(self.conf_var.get())
            expand_pixels = int(float(self.expand_var.get()))
            save_option = self.save_masks_var.get()
            resize_option = self.resize_var.get()

            # Calculate resize scale
            resize_scale = 1.0
            if resize_option == "half":
                resize_scale = 0.5
            elif resize_option == "quarter":
                resize_scale = 0.25

            self.log(f"🎯 Confidence Threshold: {conf_threshold:.2f}")
            self.log(f"📏 Mask Expansion: {expand_pixels} pixels")
            self.log(f"💾 Save Option: {save_option.replace('_', ' ').title()}")
            self.log(f"⚡ Processing Scale: {resize_option.replace('_', ' ').title()}")
            self.log(f"🤖 Target Classes: person, car")
            if self.gpu_available:
                self.log(f"✓ GPU Acceleration: Enabled ({self.gpu_name})")
            else:
                self.log(f"⚠ GPU Acceleration: Disabled (Using CPU)")
            self.log("")

            successful = 0
            failed = 0
            total_detections = 0

            # Process images
            for idx, image_path in enumerate(image_files):
                if not self.is_processing:
                    break

                progress = (idx / len(image_files)) * 100
                self.progress_var.set(progress)
                self.status_label.config(
                    text=f"Processing: {idx + 1}/{len(image_files)} - {image_path.name}",
                    fg="#3498db"
                )

                try:
                    # Read image
                    image = cv2.imread(str(image_path))
                    if image is None:
                        failed += 1
                        continue

                    # Handle PNG with alpha channel
                    if image.shape[2] == 4:
                        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
                    elif len(image.shape) == 2:
                        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

                    height, width = image.shape[:2]
                    original_height, original_width = height, width

                    # Resize for faster processing if requested
                    if resize_scale < 1.0:
                        new_height = int(height * resize_scale)
                        new_width = int(width * resize_scale)
                        image_for_detection = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
                        detection_height, detection_width = new_height, new_width
                    else:
                        image_for_detection = image
                        detection_height, detection_width = height, width

                    # Run YOLO detection
                    results = self.model(image_for_detection, conf=conf_threshold)
                    result = results[0]

                    # Debug: Check what was detected
                    num_boxes = len(result.boxes) if result.boxes is not None else 0
                    num_targets = 0
                    if result.boxes is not None:
                        class_indices = result.boxes.cls.cpu().numpy().astype(int)
                        num_targets = sum(1 for c in class_indices if c in self.TARGET_CLASSES)

                    # Get expansion value
                    expand_pixels = int(float(self.expand_var.get()))

                    # Create binary mask with expansion (using detection dimensions)
                    mask = self.create_binary_mask(result, detection_height, detection_width, expand_pixels=expand_pixels)

                    # Scale mask back to original resolution if needed
                    if resize_scale < 1.0:
                        mask = cv2.resize(mask, (original_width, original_height), interpolation=cv2.INTER_LINEAR)

                    # Log detection info
                    total_detections += num_targets
                    masked_pixels = np.sum(mask == 0)
                    total_pixels = height * width
                    masked_percent = (masked_pixels / total_pixels) * 100

                    if num_targets > 0:
                        self.log(f"   ✓ {image_path.name} - {num_targets} target(s) | {masked_percent:.1f}% masked")
                    elif num_boxes > 0:
                        self.log(f"   ~ {image_path.name} - {num_boxes} object(s) found (not target)")
                    else:
                        self.log(f"   - {image_path.name} - No detections")

                    # Apply mask to image only if needed
                    if save_option in ["both", "images_only"]:
                        masked_image = self.apply_mask_to_image(image, mask)
                    else:
                        masked_image = None

                    # Save outputs
                    stem = image_path.stem

                    # Save mask if requested
                    if save_option in ["both", "masks_only"]:
                        mask_path = masks_dir / f"{stem}_mask.png"
                        cv2.imwrite(str(mask_path), mask)

                    # Save masked image if requested
                    if save_option in ["both", "images_only"]:
                        if image_path.suffix.lower() == '.png':
                            masked_image_path = masked_images_dir / f"{stem}_masked.png"
                            cv2.imwrite(str(masked_image_path), masked_image)
                        else:
                            masked_image_path = masked_images_dir / f"{stem}_masked.jpg"
                            cv2.imwrite(str(masked_image_path), masked_image, [cv2.IMWRITE_JPEG_QUALITY, 95])

                    successful += 1
                    self.log(f"✅ {image_path.name}")

                except Exception as e:
                    failed += 1
                    self.log(f"❌ Error processing {image_path.name}: {str(e)}")

            # Complete
            self.progress_var.set(100)
            self.log("\n" + "=" * 50)
            self.log("PROCESSING COMPLETE!")
            self.log("=" * 50)
            self.log(f"✅ Successfully processed: {successful}/{len(image_files)} images")
            if failed > 0:
                self.log(f"❌ Failed: {failed} images")
            self.log(f"\n🎯 Detection Summary:")
            self.log(f"   Total targets detected: {total_detections}")
            self.log(f"   Confidence threshold: {conf_threshold:.2f}")
            self.log(f"   Mask expansion: {expand_pixels} pixels")

            # Troubleshooting advice
            if total_detections == 0:
                self.log(f"\n⚠️  WARNING: No humans/cars detected!")
                self.log(f"   Possible reasons:")
                self.log(f"   1. Confidence threshold too high (try 0.2-0.3)")
                self.log(f"   2. Equirectangular distortion makes detection hard")
                self.log(f"   3. No humans/cars actually present in images")
                self.log(f"\n   Try again with lower confidence threshold")

            self.log(f"\n📍 Output Location:")
            self.log(f"   {output_path}")

            self.status_label.config(text=f"Complete: {successful}/{len(image_files)} processed, {total_detections} targets found", fg="#27ae60")
            self.start_button.config(state="normal")

            messagebox.showinfo("Success", f"Processing complete!\n\n✅ {successful} images processed\n❌ {failed} failed\n🎯 Targets detected: {total_detections}\n\nOutputs saved to:\n{output_path}")

        except Exception as e:
            self.log(f"\n❌ ERROR: {str(e)}")
            self.status_label.config(text="Error occurred", fg="#e74c3c")
            self.start_button.config(state="normal")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")


def main():
    root = Tk()
    app = MaskerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
