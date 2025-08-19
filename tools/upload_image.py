#!/usr/bin/env python3
"""
Script to help upload images for blog posts
Usage: python3 upload_image.py image.jpg "Carros de Foc"
"""

import sys
import os
import shutil
from datetime import datetime

def upload_image(image_path, post_title):
    """Upload an image and return the markdown link"""
    if not os.path.exists(image_path):
        print(f"❌ Error: Image file '{image_path}' not found!")
        return None
    
    # Create a clean filename
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    
    # Create a unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{name}_{timestamp}{ext}"
    
    # Copy to static/images
    dest_path = f"static/images/{new_filename}"
    shutil.copy2(image_path, dest_path)
    
    print(f"✅ Image uploaded: {dest_path}")
    print(f"📝 Use this in your markdown:")
    print(f"![{post_title}](/static/images/{new_filename})")
    
    return f"/static/images/{new_filename}"

def list_images():
    """List all uploaded images"""
    images_dir = "static/images"
    if not os.path.exists(images_dir):
        print("No images uploaded yet.")
        return
    
    images = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]
    
    if not images:
        print("No images found in static/images/")
        return
    
    print("📸 Available images:")
    for img in sorted(images):
        print(f"  - /static/images/{img}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 upload_image.py image.jpg 'Post Title'  # Upload image")
        print("  python3 upload_image.py --list                  # List images")
        sys.exit(1)
    
    if sys.argv[1] == "--list":
        list_images()
    else:
        image_path = sys.argv[1]
        post_title = sys.argv[2] if len(sys.argv) > 2 else "Image"
        upload_image(image_path, post_title) 