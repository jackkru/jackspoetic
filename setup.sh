#!/bin/bash

echo "Setting up Flask application..."

# Check if pip is available, install if not
if ! python3 -m pip --version > /dev/null 2>&1; then
    echo "Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py --user
    rm get-pip.py
fi

# Install dependencies
echo "Installing Python dependencies..."
python3 -m pip install --user -r requirements.txt

# Start the Flask application
echo "Starting Flask application..."
echo "The app will be available at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
python3 app.py 