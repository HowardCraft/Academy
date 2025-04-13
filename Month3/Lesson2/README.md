# Lesson 2

HandsOn task for lesson 2 of month 3
Install and Run pretrained Object detection task on Raspberry Pi with [YOLO](https://github.com/ultralytics/ultralytics) and [tensorflow Lite](https://www.tensorflow.org/api_docs/python/tf/lite)


## YOLO

### Install 
you can install necessery libraries automaticly or manualy:

1. automaticly
    Run yolo/install_yolo_dependencies.sh, this bash file will run all required libraies.

    `cd yolo/`
    `sudo ./install_yolo_dependencies.sh`

    at the end you must see this:


    If you have issue check [FAQ]()

2. Manual:

    1. Update package list and upgrade installed packages
        
        `sudo apt update && sudo apt upgrade -y`

    2. Install Python3 and pip if not already installed

        `sudo apt install -y python3.11`
        `sudo apt install -y python3-pip`
        `pip3 install --upgrade pip`

    3. Install virtualenv to create isolated Python environments

        `python3.11 pip install virtualenv`

    4. Create a virtual environment named 'yolo11_env'

        `virtualenv yolo11_env`

    5. Activate the virtual environment

        `source yolo11_env/bin/activate`

    6. Install Ultralytics YOLO package with export dependencies

        `pip install -r requirment.txt`

    7. Deactivate the virtual environment

        `deactivate`

### Run example
Same as Install step you can Run Example automaticly or manualy:

1. automaticly
    Run yolo/ObjectDetection.sh, this bash file will Create model and run example of prediction on sample image 'Bus'.

    `sudo ./yolo/ObjectDetection.sh`

        Output:


2. Manual:
    1. Activate the virtual environment

        `source yolo11_env/bin/activate`

    2. Export the yolo11n model
        `yolo export model=yolo11n.pt` 
    3. Run predication using yollo
        `yolo predict model='yolo11n.torchscript' source='https://ultralytics.com/images/bus.jpg'`

    4. Deactivate the virtual environment

        `deactivate`

## TF lite

-- How to Run --



# FAQ

Q: I get a permission error when running a script. What should I do?
A: Try giving execute permission first:

    `chmod +x script_name.sh`