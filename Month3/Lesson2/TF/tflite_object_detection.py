# import necessary libraries
import argparse
import tflite_runtime.interpreter as tflite
import numpy as np
import cv2
from utils import check_tf_version, load_labels, process_frame


# Set numpy print precision for clean output (optional)
np.set_printoptions(precision=2)




# ----------------------------
# Argument Parser
# ----------------------------
parser = argparse.ArgumentParser(description="TFLite Object Detection Script (Image or Video)")


parser.add_argument("--model", type=str, default="coco_ssd_mobilenet_v1_1.0_quant_2018_06_29/detect.tflite",
                   help="Path to the .tflite model file.")
parser.add_argument("--labels", type=str, default="coco_ssd_mobilenet_v1_1.0_quant_2018_06_29/labelmap.txt",
                   help="Path to the labelmap.txt file.")
parser.add_argument("--image", type=str, default="samples/image.jpg",
                   help="Path to the input image.")
parser.add_argument("--video", type=str, help="Path to input video file")
parser.add_argument("--threshold", type=float, default=0.5,
                   help="Confidence threshold for displaying detections.")
parser.add_argument("--output", type=str, default="outputImg.jpg",
                   help="Output image or video file path")
parser.add_argument("--VideoProcessing", type=bool, default=False,
                   help="Todo Video Processing set True")
args = parser.parse_args()


# -------------------------------------------------------
# Load the TensorFlow Lite model and allocate tensors
# -------------------------------------------------------
interpreter = tflite.Interpreter(model_path=args.model)
interpreter.allocate_tensors()




# -------------------------------------------------------
# Get input and output details of the model
# -------------------------------------------------------
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


# Get input shape (height & width expected by model)
input_height = input_details[0]['shape'][1]
input_width = input_details[0]['shape'][2]




# Check output layer name to determine if this model was created with TF2 or TF1,
# because outputs are ordered differently for TF2 and TF1 models
boxes_idx, classes_idx, scores_idx = check_tf_version(output_details)     






# -------------------------------------------------------
# Load labels (class names)
# -------------------------------------------------------


labels = load_labels(args.labels)  # Load labels from labelmap file
if labels is None:
   raise FileNotFoundError(f"Label file not found at {args.labels}")


# -------------------------------------------------------
# Image interface
# -------------------------------------------------------
if not(args.VideoProcessing):
  
   # If image is provided, load it
   image = cv2.imread(args.image)
   if image is None:
       raise FileNotFoundError(f"Image not found at {args.image}")


   image = process_frame(image, input_width, input_height, interpreter, input_details, output_details, labels, boxes_idx, classes_idx, scores_idx, args.threshold)
   cv2.imwrite(args.output,image)
# ----------------------------
# Video Inference
# ----------------------------
elif args.video is not None:
   # If video is provided, open it
   cap = cv2.VideoCapture(args.video)
   if not cap.isOpened():
       raise FileNotFoundError(f"Video not found at {args.video}")
   # Get properties from the input video
   fps = cap.get(cv2.CAP_PROP_FPS)
   frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
   frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  
   # Define the codec and create VideoWriter object
   # Here we use the 'XVID' codec; you can change this codec (e.g., to 'mp4v') if needed.
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   output_filename = 'output.avi'
   out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))


   while True:
       ret, frame = cap.read()
       if not ret:
           break


       # Process the frame for object detection
       image = process_frame(frame, input_width, input_height, interpreter, input_details, output_details, labels, boxes_idx, classes_idx, scores_idx, args.threshold)
       # Write the processed frame to the output video
       out.write(image)


   out.release()
   cap.release()


else:
   print("Please provide either --image or --video input.")