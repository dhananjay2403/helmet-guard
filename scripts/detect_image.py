import os
from ultralytics import YOLO


# Detect objects in a single image using a trained YOLOv8 model & save the annotated output image
def detect_image(image_filename = 'test.jpg',                                         # Name of the input image file in the test_images folder
                 model_weights = '../runs/detect/full_training/weights/best.pt',      # Path to the trained YOLOv8 model weights file
                 confidence_threshold = 0.5):                                         # Minimum confidence score for detections

    # Create full path to image from the test_images folder
    image_path = os.path.join('..', 'test_images', image_filename)

    # Load the model
    model = YOLO(model_weights)

    # Run prediction on image
    model.predict(
        source = image_path,
        show = True,                          # Display image while processing
        save = True,                          # Save the annotated image
        conf = confidence_threshold,
        line_width = 2,                       # Bounding box thickness
        project = "../results",               # Save results to this folder
        name = "helmet_detection_image"
    )

    print(f"Output saved to ../results/helmet_detection_image/{os.path.basename(image_filename)}")

if __name__ == "__main__":
    detect_image(image_filename='test_image.jpg')                # Change this to an actual image filename in your test_images folder
   