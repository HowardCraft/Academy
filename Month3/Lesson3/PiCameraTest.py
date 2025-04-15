# ============================================================
# This script demonstrates how to use Picamera2 with OpenCV.
# It captures video frames from a Raspberry Pi camera and
# displays them in a window, overlaying a live video feed.
#
# The code includes detailed comments explaining the purpose
# of each section, which is ideal for an educational setting.
# ============================================================

# Import OpenCV, a powerful library for image processing and computer vision.
import cv2

# Import os to work with environment variables.
import os


# ------------------------------------------------------------
# Import Picamera2 from the picamera2 library. This class is used to interface
# with the Raspberry Pi camera hardware.
# ------------------------------------------------------------
from picamera2 import Picamera2

# Create an instance of Picamera2. This object will handle the camera operations.
picam2 = Picamera2()

# ------------------------------------------------------------
# Configure the Camera Preview
# ------------------------------------------------------------
# The camera has several configuration options. Here we adjust the preview settings:
#   - Set the output image size to 1024x1024 pixels.
#   - Set the pixel format to "RGB888" (red, green, blue with 8 bits per channel).
# These settings can be customized as needed.
picam2.preview_configuration.main.size = (1024, 1024)
picam2.preview_configuration.main.format = "RGB888"

# 'align()' adjusts the preview configuration based on the underlying sensor parameters.
picam2.preview_configuration.align()

# Apply the "preview" configuration to the camera.
picam2.configure("preview")

# Start the camera. The camera begins capturing data after this command.
picam2.start()

# ------------------------------------------------------------
# Continuous Video Capture and Display Loop
# ------------------------------------------------------------
# This loop captures individual frames from the camera and displays them
# in a window using OpenCV. Press 'q' to exit the loop and close the window.
while True:
    # Capture a frame from the camera as a NumPy array.
    im = picam2.capture_array()
    
    # Display the captured frame in a window titled "Camera".
    cv2.imshow("Camera", im)
    
    # Wait 1 millisecond for a key press. If 'q' is pressed, break out of the loop.
    if cv2.waitKey(1) == ord('q'):
        break

# Clean up: When the loop is exited, close any OpenCV windows that were opened.
cv2.destroyAllWindows()
