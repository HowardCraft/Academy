from ultralytics import YOLO

# Load a pre-trained YOLOv11 model
model = YOLO('yolo11n.pt')  # You can choose other variants like yolo11s.pt, yolo11m.pt, etc.

# Train the model on your custom dataset
model.train(data='data.yaml', epochs=5, imgsz=64)
