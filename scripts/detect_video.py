import os
from ultralytics import YOLO


# Detect objects in a video using a trained YOLOv8 model & save the annotated output video
def detect_video(video_filename = 'test_video.mp4',                                     # Name of the input video file in the 'videos/' folder
                 model_weights = '../runs/detect/full_training/weights/best.pt',        # Path to the trained YOLOv8 model weights file
                 confidence_threshold = 0.45):                                          # Minimum confidence score for detections

    # Create full path to video
    video_path = os.path.join('..', 'videos', video_filename)
    
    # Load the model
    model = YOLO(model_weights)
    
    # Run prediction on video
    model.predict(
        source = video_path,
        show = True,                      # Display frames while processing
        save = True,                      # Save the annotated video
        conf = confidence_threshold,
        line_width = 2,                   # Bounding box thickness
        project = "../results",  
        name = "helmet_detection"
    )
    
    print(f"Output saved to ../results/helmet_detection/{video_filename}")

if __name__ == "__main__":
    detect_video(video_filename='test_video.mp4')                # Change this to an actual video filename in your videos folder
   