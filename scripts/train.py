from ultralytics import YOLO

# Load pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

model.train()