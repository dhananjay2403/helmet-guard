import streamlit as st
import os
import tempfile
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np


# Load YOLOv8 model
model_path = os.path.join(os.path.dirname(__file__), "runs", "detect", "full_training", "weights", "best.pt")
model = YOLO(model_path)


# Title
st.markdown(
    "<h1 style='text-align: center;'>HelmetGuard - Helmet Detection</h1>",
    unsafe_allow_html=True
)


# Sidebar for upload type
option = st.sidebar.selectbox("Choose input type", ["Image", "Video"])


# Image detection

if option == "Image":
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image).convert("RGB")  # Ensure 3-channel RGB
        image_np = np.array(image)
        image_np = cv2.resize(image_np, (640, 640))  # Resize to match training size

        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Run detection
        with st.spinner("Running Helmet Detection..."):
            results = model.predict(image_np, conf=0.5)
            result_img = results[0].plot()  # Draw boxes on result

        st.image(result_img, caption="Detection Result", use_container_width=True)



# Video detection
elif option == "Video":
    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
    if uploaded_video is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        video_path = tfile.name

        st.video(video_path)

        if st.button("Run Detection"):
            stframe = st.empty()
            cap = cv2.VideoCapture(video_path)

            with st.spinner("Processing video..."):
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
                    frame_resized = cv2.resize(frame, (640, 640))   # Resize to model input size
                    
                    results = model.predict(frame_resized, conf=0.5)
                    result_frame = results[0].plot()

                    # Convert BGR to RGB for Streamlit display (YOLO output is in BGR)
                    result_frame = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)

                    stframe.image(result_frame, use_container_width=True)

                cap.release()
            st.success("Detection Complete ✅")



# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>" \
        "Created by Dhananjay Tiwari — Helmet Detection with YOLOv8"
    "</div>",
    unsafe_allow_html=True                  # to centre align
)
