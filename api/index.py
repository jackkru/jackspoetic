import sys
import os

# Add parent directory to path so we can import app
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# Change to parent directory so relative paths work correctly
os.chdir(parent_dir)

from app import app

# Export the Flask app for Vercel
# Vercel's Python runtime will automatically use this as a WSGI application

