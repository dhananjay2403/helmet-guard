from ultralytics import YOLO

def train_model():
    model = YOLO('yolov8n.pt')
    model.train(
        data='../config/data.yaml', 
        # epochs=1,                  # initially trained model with epoch = 1 
        # imgsz=320,                 # used reduced image size initially
        # fraction=0.05              # Use only 5% of dataset initially

        epochs = 25,                   # initially trained model with epoch = 1 
        imgsz = 640,                   # image size
        batch = 16,                  # default batch size for full training 
        fraction = 0.5,              # Using 50% of dataset for training
        name = 'full_training'       # custom name for O/P folder
    )

if __name__ == "__main__":
    train_model()
    