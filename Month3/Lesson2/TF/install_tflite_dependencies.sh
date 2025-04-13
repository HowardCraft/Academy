#!/bin/bash

# Step 1: Update package list and upgrade installed packages
echo "Updating package list and upgrading installed packages..."
sudo apt update && sudo apt upgrade -y

# Step 2: Install Python3 and pip if not already installed
echo "Checking for Python3 and pip..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing Python3..."
    sudo apt install -y python3
else
    echo "Python3 is already installed."
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 not found. Installing pip3..."
    sudo apt install -y python3-pip
else
    echo "pip3 is already installed."
fi

# Upgrade pip to the latest version
echo "Upgrading pip to the latest version..."
pip3 install --upgrade pip

# Step 3: Install virtualenv to create isolated Python environments
echo "Installing virtualenv..."
pip3 install virtualenv

# Step 4: Create a virtual environment named 'yolo11_env'
echo "Creating virtual environment 'tf_env'..."
virtualenv tf_env

# Step 5: Activate the virtual environment
echo "Activating virtual environment..."
source tf_env/bin/activate

# Step 6: Install TensorFlow Lite runtime
pip install tflite-runtime

# Step 7: Install OpenCV for image processing
pip install opencv-python

# Step 8: Install numpy for numerical operations
pip install numpy

# Step 9: Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "All dependencies have been installed successfully."
