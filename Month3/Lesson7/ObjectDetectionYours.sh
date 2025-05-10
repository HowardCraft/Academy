#!/bin/bash

imagepass="${1:-$(pwd)/samples/image.jpg}"
echo "$imagepass"
# Step 1: Activate the virtual environment
echo "Activating virtual environment..."
source yolo11_env/bin/activate            

# Step 3: Run predication using yollo
echo "Predication start..."
yolo predict model='best.pt' source=$imagepass conf=0.5

# Step 4: Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "YOLOv11 predication example complete."


