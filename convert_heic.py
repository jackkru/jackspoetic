#!/usr/bin/env python3
"""
Convert HEIC images to JPEG for web compatibility with folder organization
"""

import sys
import os
from PIL import Image
import pillow_heif
import glob

def convert_heic_to_jpeg(heic_path, output_folder=None, max_width=800):
    """Convert HEIC file to JPEG with resizing and organization"""
    try:
        # Register HEIF opener
        pillow_heif.register_heif_opener()
        
        # Get filename and create output path
        filename = os.path.basename(heic_path)
        name, ext = os.path.splitext(filename)
        
        # Create output folder if specified
        if output_folder:
            os.makedirs(output_folder, exist_ok=True)
            jpeg_path = os.path.join(output_folder, f"{name}.jpg")
        else:
            jpeg_path = heic_path.replace('.HEIC', '.jpg').replace('.heic', '.jpg')
        
        # Open HEIC image
        with Image.open(heic_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA'):
                img = img.convert('RGB')
            
            # Resize if too large
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                print(f"📏 Resized from {img.width}x{img.height} to {max_width}x{new_height}")
            
            # Save as JPEG
            img.save(jpeg_path, 'JPEG', quality=85, optimize=True)
            print(f"✅ Converted {heic_path} to {jpeg_path}")
            
            # Delete original HEIC file
            os.remove(heic_path)
            print(f"🗑️  Deleted original HEIC file: {heic_path}")
            
            return jpeg_path
            
    except Exception as e:
        print(f"❌ Error converting {heic_path}: {e}")
        return None

def organize_and_convert_images():
    """Find all HEIC files and convert them to organized folders"""
    # Find all HEIC files in static/images
    heic_files = glob.glob("static/images/*.HEIC") + glob.glob("static/images/*.heic")
    
    if not heic_files:
        print("No HEIC files found in static/images/")
        return
    
    print(f"Found {len(heic_files)} HEIC files to convert:")
    
    for heic_file in heic_files:
        # Determine folder based on filename or ask user
        filename = os.path.basename(heic_file)
        name, ext = os.path.splitext(filename)
        
        # For now, put all images in a general folder
        # You can customize this logic based on your needs
        output_folder = "static/images/general"
        
        convert_heic_to_jpeg(heic_file, output_folder, max_width=800)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Convert specific file
        heic_file = sys.argv[1]
        output_folder = sys.argv[2] if len(sys.argv) > 2 else None
        convert_heic_to_jpeg(heic_file, output_folder, max_width=800)
    else:
        # Convert all HEIC files
        organize_and_convert_images() 