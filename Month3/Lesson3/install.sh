#!/bin/bash
# =============================================================================
# This script installs build dependencies for OpenCV and other useful libraries,
# along with Picamera2, TensorFlow Lite runtime, and the OpenCV Python package.
#
# Run this script as root or using sudo. You can save it as install.sh and execute:
#   sudo bash install.sh
# =============================================================================

# -----------------------------------------
# 1. Install Build and Library Dependencies
# -----------------------------------------
# These packages include development tools, compilers, and necessary libraries
# required for building computer vision applications with OpenCV.
sudo apt update && sudo apt upgrade -y
sudo apt install -y \
    build-essential \
    cmake \
    git \
    pkg-config \
    libgtk-3-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    gfortran \
    openexr \
    libatlas-base-dev \
    python3-dev \
    python3-numpy \
    libtbb2 \
    libtbb-dev \
    libdc1394-22-dev

# -----------------------------------------
# 2. Install Picamera2 for Raspberry Pi Camera Interface
# -----------------------------------------
sudo apt install -y python3-picamera2

# -----------------------------------------
# 3. Install TensorFlow Lite Runtime
# -----------------------------------------
# This package is used for running TensorFlow Lite models on resource-constrained devices.
sudo pip install --break-system-packages tflite-runtime

# -----------------------------------------
# 4. Install OpenCV Python Package
# -----------------------------------------
# OpenCV is used for image processing and computer vision tasks.
sudo pip install --break-system-packages opencv-python
