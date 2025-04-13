#!/bin/bash

# Step 1: Activate the virtual environment
echo "Activating virtual environment..."
source yolo11_env/bin/activate

# Step 2: Export the yolo11n model
yolo export model=yolo11n.pt              

# Step 3: Run predication using yollo
echo "Predication start..."
yolo predict model='yolo11n.torchscript' source='path/to/video.mp4'

# Step 4: Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "YOLOv11 predication example complete."
