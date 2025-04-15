# ================================================================================
# TensorFlow Lite Object Detection with Multiple Input Modes (Live, Image, Video)
#
# This script loads a pre-trained TensorFlow Lite object detection model,
# prepares it for inference, and processes inputs from either a live camera feed,
# an image file, or a video file.
#
# The code is broken into sections:
#   1. Importing necessary libraries and modules
#   2. Parsing command-line arguments to select input mode and model parameters
#   3. Loading the TFLite model and allocating its tensors
#   4. Extracting input details, output details, and model shape requirements
#   5. Loading label names for the classes
#   6. Running inference:
#         a) For live camera input (using Picamera2)
#         b) For a single image input
#         c) For video file inference
#
# Each section includes detailed comments for educational clarity.
# ================================================================================

# ---------------------------------------------
# 1. Import Necessary Libraries
# ---------------------------------------------
import argparse                    # For parsing command-line options and arguments
import tflite_runtime.interpreter as tflite  # TensorFlow Lite interpreter for running inference
import numpy as np                 # For numerical operations and array handling
import cv2                         # OpenCV for image processing and display
from utils import check_tf_version, load_labels, process_frame, process_frame_live
                                  # Custom utility functions:
                                  #   - check_tf_version: to adjust output indices based on TF version
                                  #   - load_labels: to load the label map from a file
                                  #   - process_frame & process_frame_live: functions for preprocessing,
                                  #     inference, and postprocessing each frame
import time                        # For measuring timing and calculating FPS

# Set numpy print precision for clean output (optional)
np.set_printoptions(precision=2)

# ---------------------------------------------
# 2. Parse Command-Line Arguments
# ---------------------------------------------
# This allows users to pass various parameters to the script.
parser = argparse.ArgumentParser(description="TFLite Object Detection Script (Image, Video, or Live Camera)")

# Path to the TensorFlow Lite model file (default is a quantized SSD Mobilenet model).
parser.add_argument("--model", type=str, default="coco_ssd_mobilenet_v1_1.0_quant_2018_06_29/detect.tflite",
                    help="Path to the .tflite model file.")

# Path to the labelmap file (contains class names).
parser.add_argument("--labels", type=str, default="coco_ssd_mobilenet_v1_1.0_quant_2018_06_29/labelmap.txt",
                    help="Path to the labelmap.txt file.")

# Path to an input image (for image-based inference).
parser.add_argument("--image", type=str, default="samples/image.jpg",
                    help="Path to the input image.")

# Path to an input video file (for video-based inference).
parser.add_argument("--video", type=str, help="Path to input video file")

# Confidence threshold for displaying detected objects.
parser.add_argument("--threshold", type=float, default=0.5,
                    help="Confidence threshold for displaying detections.")

# Path to output file for saving the processed image or video.
parser.add_argument("--output", type=str, default="outputImg.jpg",
                    help="Output image or video file path")

# Boolean flag indicating video processing mode (if True, process video file input).
parser.add_argument("--VideoProcessing", type=bool, default=False,
                    help="Set to True for video processing mode.")

# Boolean flag indicating live camera mode (if True, use Picamera2 for live inference).
parser.add_argument("--Live", type=bool, default=True,
                    help="Set to True for live camera processing mode.")

# Parse the provided arguments.
args = parser.parse_args()


# ---------------------------------------------
# 3. Load the TensorFlow Lite Model
# ---------------------------------------------
# Initialize the TFLite interpreter with the given model path.
interpreter = tflite.Interpreter(model_path=args.model)
# Allocate memory for the model tensors.
interpreter.allocate_tensors()

# ---------------------------------------------
# 4. Retrieve Input and Output Details of the Model
# ---------------------------------------------
# This information includes the expected input tensor shape.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Extract the expected model input height and width.
input_height = input_details[0]['shape'][1]
input_width = input_details[0]['shape'][2]

# Determine the correct output tensor indices by checking the TF version.
# Different TF Lite models may output detection boxes, classes, and scores in different order.
boxes_idx, classes_idx, scores_idx = check_tf_version(output_details)

# ---------------------------------------------
# 5. Load Labels (Class Names)
# ---------------------------------------------
# Load the class names from the label file.
labels = load_labels(args.labels)
if labels is None:
    raise FileNotFoundError(f"Label file not found at {args.labels}")

# ---------------------------------------------
# 6. Run Inference Based on the Input Mode
# ---------------------------------------------
# The script supports three modes:
#   a) Live camera processing using Picamera2.
#   b) Image processing (when a single image is provided).
#   c) Video file processing.

# ----- a) Live Camera Processing (Using Picamera2) -----
if args.Live:
    # Import Picamera2 for Raspberry Pi camera access.
    from picamera2 import Picamera2
    # Create an instance of the Picamera2 object.
    picam2 = Picamera2()

    # Set desired frame dimensions for capturing video.
    # Note: Adjust these dimensions based on your camera's capability.
    frame_height = 1640
    frame_width = 1232
    picam2.preview_configuration.main.size = (frame_height, frame_width)
    picam2.preview_configuration.main.format = "RGB888"
    
    # Align configuration parameters based on camera sensor details.
    picam2.preview_configuration.align()
    
    # Start the camera (without configuring a specific mode like "preview" if not needed).
    picam2.start()
    
    # Variable to store the time when the previous frame was captured; for FPS calculation.
    prev_time =time.time()
    
    # Live processing loop: capture frames, run inference, and display results.
    while True:
        # Capture a frame (as a NumPy array) from the live camera.
        frame = picam2.capture_array()
        
        # Process the current frame using a live-specific processing function.
        # This function typically handles resizing, running the TFLite model,
        # and drawing bounding boxes/detections on the frame.
        image = process_frame_live(frame, input_width, input_height, interpreter,
                                   input_details, output_details, labels,
                                   boxes_idx, classes_idx, scores_idx, args.threshold)
        
        # Calculate the time difference between frames.
        current_time = time.time()
        dt = current_time - prev_time
        prev_time = current_time
        
        # Compute FPS (frames per second) as the inverse of the frame interval.
        fps = 1.0 / dt if dt > 0 else 0
        
        # Overlay the FPS value on the image using OpenCV.
        fps_text = f"FPS: {fps:.2f}"
        cv2.putText(image, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Display the processed frame with detections and FPS overlay.
        cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Camera", 800,600)

        cv2.imshow("Camera", image)
        
        # Exit loop when the user presses 'q'.
        if cv2.waitKey(1) == ord('q'):
            break
    
    # Clean up: close the display window.
    cv2.destroyAllWindows()

# ----- b) Image Processing Interface -----
elif not args.VideoProcessing:
    # Load an image from disk using OpenCV.
    image = cv2.imread(args.image)
    if image is None:
        raise FileNotFoundError(f"Image not found at {args.image}")

    # Process the image for object detection.
    # This function handles preprocessing the image, running inference, and drawing results.
    image = process_frame(image, input_width, input_height, interpreter,
                          input_details, output_details, labels,
                          boxes_idx, classes_idx, scores_idx, args.threshold)
    
    # Save the processed image to the specified output file.
    cv2.imwrite(args.output, image)

# ----- c) Video File Processing Interface -----
elif args.video is not None:
    # Open the video file using OpenCV's VideoCapture.
    cap = cv2.VideoCapture(args.video)
    if not cap.isOpened():
        raise FileNotFoundError(f"Video not found at {args.video}")
    
    # Retrieve video properties like FPS, frame width, and frame height.
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Define the video codec (e.g., 'XVID') and create a VideoWriter object for output.
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_filename = 'output.avi'
    out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))
    
    # Process each frame in the video file.
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process the current frame with object detection.
        image = process_frame(frame, input_width, input_height, interpreter,
                              input_details, output_details, labels,
                              boxes_idx, classes_idx, scores_idx, args.threshold)
        
        # Write the processed frame to the output video.
        out.write(image)
    
    # Release the video writer and capture objects.
    out.release()
    cap.release()

# If no valid input is provided, instruct the user on proper usage.
else:
    print("Please provide either --image or --video input.")
