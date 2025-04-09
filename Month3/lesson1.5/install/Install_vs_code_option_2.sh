#!/bin/bash

# Install Visual Studio Code on Raspberry Pi OS
# This script is designed to be run on Raspberry Pi OS (64-bit) and will install the latest version of Visual Studio Code.
# Make sure to run this script with sudo privileges
# Check if the script is run with sudo
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi
# Check if the system is 64-bit
if [ "$(uname -m)" != "aarch64" ]; then
    echo "This script is designed to run on Raspberry Pi OS (64-bit)."
    exit 1
fi
# Add the Microsoft GPG key and repository
sudo apt-get install -y wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg 
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=arm64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get update
sudo apt-get install -y code
rm microsoft.gpg
