# Lesson 2

HandsOn task for lesson 2 of month 3
Install and Run pretrained Object detection task on Raspberry Pi with [YOLO](https://github.com/ultralytics/ultralytics) and [tensorflow Lite](https://www.tensorflow.org/api_docs/python/tf/lite)

due to file size limit please download the video here https://craftingtable.com/pages/downloads
## YOLO

### Install 
you can install necessery libraries automaticly or manualy:

1. automaticly
    Run yolo/install_yolo_dependencies.sh, this bash file will run all required libraies.

```bash
cd yolo/
sudo ./install_yolo_dependencies.sh
```


2. Manual:

    1. Update package list and upgrade installed packages
        
```bash
sudo apt update && sudo apt upgrade -y
```

    2. Install Python3 and pip if not already installed
 ```bash
sudo apt install -y python3.11
sudo apt install -y python3-pip
pip3 install --upgrade pip
```

    3. Install virtualenv to create isolated Python environments
```bash
python3.11 pip install virtualenv
```

    4. Create a virtual environment named 'yolo11_env'
 ```bash
virtualenv yolo11_env
```

    5. Activate the virtual environment
```bash
source yolo11_env/bin/activate
```

    6. Install Ultralytics YOLO package with export dependencies
```bash
pip install -r requirment.txt
```
    7. Deactivate the virtual environment
```bash
deactivate
```
### Run example
Same as Install step you can Run Example automaticly or manualy:

1. automaticly
    Run yolo/ObjectDetection.sh, this bash file will Create model and run example of prediction on sample image 'Bus'.
```bash
./ObjectDetection.sh
```

    *You can put your images in samples directory and run this code- you need to replace your file name with **image.jpg**:
```bash
./ObjectDetectionYours.sh $(pwd)/samples/image.jpg

    
./ObjectDetectionYours.sh $(pwd)/samples/video.mp4
```

2. Manual:
    1. Activate the virtual environment
```bash
source yolo11_env/bin/activate
```
    2. Export the yolo11n model
```bash
yolo export model=yolo11n.pt
```
    3. Run predication using yollo
```bash
yolo predict model='yolo11n.torchscript' source='https://ultralytics.com/images/bus.jpg'
```
    4. Deactivate the virtual environment
```bash
deactivate
```
## TF lite

-- How to Run -- Same steps as yolo:

1- Run  
```bash
./install_tflite_dependencies.sh
```

2-  Activate your enviroment
```bash
source tf_env/bin/activate
```

3- Run `python3 tflite_oblect_detection.py` to do default image processing with `/samples/image.jpg`

4- Run example for Image :
```bash
python tflite_object_detection.py  --video=samples/image.jpg --VideoProcessing=False
```

5- Run example for video :
```bash
python tflite_object_detection.py  --video=samples/video.mp4 --VideoProcessing=True
```


# FAQ

Q: I get a permission error when running a script. What should I do?
A: Try giving execute permission first:
```bash
chmod +x script_name.sh
```