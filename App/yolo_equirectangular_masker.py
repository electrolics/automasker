#!/usr/bin/env python3
"""
YOLO-based Equirectangular Image Masking Pipeline
Masks humans and cars in equirectangular images for photogrammetry/Gaussian splatting

Usage:
    python yolo_equirectangular_masker.py

Requirements:
    pip install ultralytics opencv-python numpy pillow tqdm
"""

import os
import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm
from PIL import Image
from ultralytics import YOLO


class EquirectangularMasker:
    """Mask humans and cars in equirectangular images using YOLO11-seg"""

    def __init__(self, input_dir, output_dir, model_name="yolo11n-seg"):
        """
        Initialize the masking pipeline

        Args:
            input_dir: Path to directory containing JPEG equirectangular images
            output_dir: Path to directory where masks and masked images will be saved
            model_name: YOLO model to use (yolo11n-seg, yolo11s-seg, etc.)
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.model_name = model_name

        # COCO class indices for person and car
        self.TARGET_CLASSES = {0: "person", 2: "car"}  # COCO dataset class indices

        # Create output directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.masks_dir = self.output_dir / "masks"
        self.masked_images_dir = self.output_dir / "masked_images"
        self.masks_dir.mkdir(exist_ok=True)
        self.masked_images_dir.mkdir(exist_ok=True)

        # Load YOLO model
        print(f"Loading {model_name} model...")
        self.model = YOLO(model_name)
        print("Model loaded successfully!")

    def get_image_files(self):
        """Get all image files (PNG, JPG, JPEG) from input directory"""
        image_extensions = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG']
        image_files = []

        for ext in image_extensions:
            image_files.extend(self.input_dir.glob(f'*{ext}'))

        return sorted(image_files)

    def create_binary_mask(self, result, image_height, image_width):
        """
        Create binary mask from YOLO segmentation results

        Args:
            result: YOLO prediction result
            image_height: Original image height
            image_width: Original image width

        Returns:
            Binary mask as numpy array (255 for masked regions, 0 for background)
        """
        mask = np.zeros((image_height, image_width), dtype=np.uint8)

        if result.masks is None:
            return mask

        # Get class indices and masks
        class_indices = result.boxes.cls.cpu().numpy().astype(int)
        masks = result.masks.data.cpu().numpy()

        # Apply masks only for target classes (person and car)
        for idx, class_idx in enumerate(class_indices):
            if class_idx in self.TARGET_CLASSES:
                # Get mask and ensure it's 2D
                detection_mask = masks[idx].astype(np.uint8)

                # Resize mask to match image dimensions
                # cv2.resize takes (width, height) not (height, width)
                resized_mask = cv2.resize(
                    detection_mask,
                    (image_width, image_height),
                    interpolation=cv2.INTER_LINEAR
                )

                # Ensure correct shape
                if resized_mask.shape != (image_height, image_width):
                    resized_mask = cv2.resize(
                        resized_mask,
                        (image_width, image_height),
                        interpolation=cv2.INTER_LINEAR
                    )

                mask = np.maximum(mask, resized_mask * 255)

        return mask

    def apply_mask_to_image(self, image, mask, fill_method="black"):
        """
        Apply mask to image

        Args:
            image: Original image (BGR)
            mask: Binary mask
            fill_method: How to fill masked regions ("black" or "transparent")

        Returns:
            Masked image
        """
        if fill_method == "transparent":
            # Convert BGR to BGRA and apply alpha channel
            image_bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
            image_bgra[:, :, 3] = (~mask.astype(bool)).astype(np.uint8) * 255
            return image_bgra
        else:  # black fill (default)
            masked_image = image.copy()
            masked_image[mask > 0] = 0
            return masked_image

    def process_image(self, image_path):
        """
        Process a single image (PNG, JPG, JPEG)

        Args:
            image_path: Path to input image

        Returns:
            Tuple of (success, mask, masked_image)
        """
        try:
            # Read image
            image = cv2.imread(str(image_path))
            if image is None:
                return False, None, None

            # Handle PNG with alpha channel (convert RGBA to BGR)
            if image.shape[2] == 4:  # RGBA image
                image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            elif len(image.shape) == 2:  # Grayscale image
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            height, width = image.shape[:2]

            # Run YOLO detection
            results = self.model(image, conf=0.5)
            result = results[0]

            # Create binary mask
            mask = self.create_binary_mask(result, height, width)

            # Apply mask to image (black fill)
            masked_image = self.apply_mask_to_image(image, mask, fill_method="black")

            return True, mask, masked_image

        except Exception as e:
            print(f"Error processing {image_path.name}: {e}")
            return False, None, None

    def save_outputs(self, image_path, mask, masked_image):
        """Save mask and masked image files"""
        stem = image_path.stem
        original_ext = image_path.suffix.lower()

        # Save binary mask (always as PNG for best quality)
        mask_path = self.masks_dir / f"{stem}_mask.png"
        cv2.imwrite(str(mask_path), mask)

        # Save masked image in original format or as JPG
        if original_ext in ['.png']:
            masked_image_path = self.masked_images_dir / f"{stem}_masked.png"
            cv2.imwrite(str(masked_image_path), masked_image)
        else:
            masked_image_path = self.masked_images_dir / f"{stem}_masked.jpg"
            cv2.imwrite(str(masked_image_path), masked_image, [cv2.IMWRITE_JPEG_QUALITY, 95])

        return mask_path, masked_image_path

    def process_batch(self):
        """Process all images in input directory"""
        image_files = self.get_image_files()

        if not image_files:
            print(f"No JPEG images found in {self.input_dir}")
            return

        print(f"\nFound {len(image_files)} images to process")
        print(f"Output directory: {self.output_dir}")
        print(f"Masks will be saved to: {self.masks_dir}")
        print(f"Masked images will be saved to: {self.masked_images_dir}\n")

        successful = 0
        failed = 0

        # Process with progress bar
        for image_path in tqdm(image_files, desc="Processing images"):
            success, mask, masked_image = self.process_image(image_path)

            if success:
                self.save_outputs(image_path, mask, masked_image)
                successful += 1
            else:
                failed += 1

        # Summary
        print(f"\n{'='*50}")
        print(f"Processing Complete!")
        print(f"Successfully processed: {successful}/{len(image_files)} images")
        if failed > 0:
            print(f"Failed: {failed} images")
        print(f"Output locations:")
        print(f"  Masks: {self.masks_dir}")
        print(f"  Masked Images: {self.masked_images_dir}")
        print(f"{'='*50}")


def main():
    """Main entry point"""

    # Configuration - UPDATE THESE PATHS
    INPUT_DIR = r"<YOUR_INPUT_FOLDER_PATH>"  # e.g., "C:\images\frames"
    OUTPUT_DIR = r"<YOUR_OUTPUT_FOLDER_PATH>"  # e.g., "C:\images\masks"

    # Validate input directory
    if not Path(INPUT_DIR).exists():
        print(f"Error: Input directory not found: {INPUT_DIR}")
        print(f"Please update INPUT_DIR with your actual folder path")
        return

    if INPUT_DIR == r"<YOUR_INPUT_FOLDER_PATH>":
        print("Error: Please update INPUT_DIR with your actual folder path")
        return

    # Initialize masker
    masker = EquirectangularMasker(INPUT_DIR, OUTPUT_DIR, model_name="yolo11n-seg")

    # Process all images
    masker.process_batch()


if __name__ == "__main__":
    main()
