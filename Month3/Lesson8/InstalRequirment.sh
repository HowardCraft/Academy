#!/bin/bash

# Step 1: Update package list and upgrade installed packages
echo "Updating package list and upgrading installed packages..."
sudo apt update && sudo apt upgrade -y
# Step 6: Install TensorFlow Lite runtime
pip3 install --break-system-packages sounddevice soundfile vosk
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf

echo "All dependencies have been installed successfully."