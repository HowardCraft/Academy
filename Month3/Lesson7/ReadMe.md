# 🍌 Banana Object Detection with TensorFlow

This project uses a custom banana dataset from Roboflow to train and evaluate an object detection model using TensorFlow and TFLite.

---

## 📦 Dataset

You can collect your images or download it from sources:

 we use in this lesson: https://universe.roboflow.com/cuenta-2/platanos-jxxqb/dataset/7

You need to Download yolo11 version

important note:
ensure the path to dataset in data.yaml are correct:
train: /home/pi/Downloads/Academy-main/Month3/Lesson7/train/images/

val: /home/pi/Downloads/Academy-main/Month3/Lesson7/valid/images/



##  Train
Run install_yolo_dependencies.sh, this bash file will run all required libraies.
```bash
sudo ./install_yolo_dependencies.sh`
source yolo11_env/bin/activate 
python3 train_yolo.py provide code to train
```


## Test


  *You can put your images in samples directory and run this code- you need to replace your file name with **image.jpg**:
  ```bash 
  ./ObjectDetectionYours.sh $(pwd)/test.jpg`
  ```
