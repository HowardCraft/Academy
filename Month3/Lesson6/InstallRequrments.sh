#!/usr/bin/env bash
# TinyLLaMA Setup Script for Raspberry Pi (for beginner students)

set -e  # Exit immediately if a command exits with a non-zero status

echo "1️⃣  Updating package lists and installing build tools..."
sudo apt update
sudo apt install -y build-essential cmake python3-pip wget

echo
echo "2️⃣  Creating a directory for your TinyLLaMA model files..."
MODEL_DIR="$HOME/tinyllama-models"
mkdir -p "${MODEL_DIR}"
cd "${MODEL_DIR}"

echo
echo "3️⃣  Downloading the TinyLLaMA 1.1B chat model (Q8_0 quantized)..."
echo "   • This file is ~1.17 GB. Be patient—download may take several minutes."
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf

echo
echo "4️⃣  Installing the Python bindings (llama-cpp-python)..."
pip3 install --user llama-cpp-python

echo
echo "✅  Setup complete! You can now import llama_cpp in your own Python scripts."
