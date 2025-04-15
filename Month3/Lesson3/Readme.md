# lesson3: Live Object Detection on Raspberry Pi with TensorFlow Lite & Picamera2

This lesson demonstrates how to set up your Raspberry Pi for real-time object detection using TensorFlow Lite and Picamera2. In this lesson, you will learn to:


- Install Picamera2 and OpenCV for camera integration.
- Test your Raspberry Pi camera.
- Run a live demo that shows a real-time object detection feed with an FPS (Frames Per Second) counter.


## Installation

you need to install install.sh 

./install.sh

## Test Camera

to test camera you need to run:

libcamera-hello



this line of code will bring up your camera for 5 seconds. Now Run this code to ensure PiCamera Depenceis are installed correctly

'python3 piCameraTest.py'

## Run Live Demo:
If camera works fine you can run :

'python3 tflite_object_detection_live.py'
