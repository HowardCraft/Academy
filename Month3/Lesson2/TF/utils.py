import cv2
import numpy as np

def check_tf_version(output_details):
    # -------------------------------------------------------
    # Detect TensorFlow version based on output tensor name
    # (TF1 and TF2 use different output ordering)
    # -------------------------------------------------------
    outname = output_details[0]['name']
    if 'StatefulPartitionedCall' in outname:  # TF2 model
        boxes_idx, classes_idx, scores_idx = 1, 3, 0
    else:  # TF1 model
        boxes_idx, classes_idx, scores_idx = 0, 1, 2

    return boxes_idx, classes_idx, scores_idx



def load_labels(label_path):
    # -------------------------------------------------------
    # Load labels from labelmap file
    # -------------------------------------------------------
    with open(label_path, 'r') as f:
        labels = [line.strip() for line in f.readlines()]
    # Some label files start with '???' as placeholder. Remove it if present
    if labels[0] == '???':
        labels.pop(0)    
    return labels

def draw_detections(image, boxes, classes, scores, labels, threshold=0.5):
    # -------------------------------------------------------
    # Draw bounding boxes and labels on the image
    # -------------------------------------------------------
    detections = []
    for i in range(len(scores)):
        if scores[i] >= threshold:
            box = boxes[i]
            class_id = int(classes[i])
            score = scores[i]
            label = labels[class_id]

            # Convert box coordinates from normalized to pixel values
            ymin, xmin, ymax, xmax = box
            ymin = int(ymin * image.shape[0])
            xmin = int(xmin * image.shape[1])
            ymax = int(ymax * image.shape[0])
            xmax = int(xmax * image.shape[1])

            # Draw bounding box and label on the image
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (200, 40, 0), 5)
            cv2.putText(image, f'{label}: {score:.2f}', (xmin, ymin - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 6, (200, 50, 200), 20)

            detections.append({
                'box': [xmin, ymin, xmax, ymax],
                'class_id': class_id,
                'score': score,
                'label': label
            })

    return detections


# ----------------------------
# Function to Run Inference on Frame
# ----------------------------
def process_frame(frame,input_width, input_height, interpreter, input_details, output_details, labels, boxes_idx, classes_idx, scores_idx, threshold=0.5):
    # -------------------------------------------------------
    # Preprocess the frame for model input
    # -------------------------------------------------------
    # Resize the frame to the input size expected by the model
    # and convert it to the appropriate data type
    
    frame_resized = cv2.resize(frame, (input_width, input_height))
    input_data = np.expand_dims(frame_resized, axis=0).astype(np.uint8)
    
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    boxes = interpreter.get_tensor(output_details[boxes_idx]['index'])[0]
    classes = interpreter.get_tensor(output_details[classes_idx]['index'])[0]
    scores = interpreter.get_tensor(output_details[scores_idx]['index'])[0]

    draw_detections(frame, boxes, classes, scores, labels, threshold=threshold)
    return frame