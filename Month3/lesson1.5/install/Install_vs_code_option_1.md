# Install VS Code for Rasperbiy Pi in few steps

## Download the VS Code Package:
    Open your web browser and go to [Visual Studio Code Download](https://code.visualstudio.com/Download).

    choose ARM64 (.deb) for 64‑bit Raspberry Pi OS.

## Open Terminal and Navigate to the Download Folder:
    Open the Terminal on your Raspberry Pi.

    Change to your Downloads folder (or the folder where the file was saved):
 `cd ~/Downloads`

## Update Your Package List:
`sudo apt update`

## Install the Downloaded Package:
Replace <filename>.deb with the actual name of the downloaded file:
    `sudo apt install ./<filename>.deb`
    
## Launch VS Code:
You can now start VS Code from the application menu, or by typing:

`code`
