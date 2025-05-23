# Helmet-guard

HelmetGuard is an AI-driven safety sentinel for construction sites, harnessing the power of computer vision and YOLOv8 deep learning to automatically spot workers missing critical protective gear like helmets and vests. By transforming ordinary site footage into actionable safety insights, HelmetGuard helps create smarter, safer workplaces—one frame at a time.

## 🚀 Detection Results

### 🎥 Video Demo

![Helmet Detection Demo](results/helmet_detection_video1/test_video_gif.gif)

<p align="center"><i>
Watch HelmetGuard in action as it scans construction site footage, instantly highlighting workers with and without safety gear!
</i></p>

---

### 🖼️ Image Detection Demo

<div align="center">
  <img src="results/helmet_detection_image/test_image.jpg" width="32.6%" />
  <img src="results/helmet_detection_image3/001766.jpg" width="32.6%" /> 
  <img src="results/helmet_detection_image4/002098.jpg" width="32.6%" />
</div>

<p align="center"><i>
HelmetGuard accurately detects helmets and vests in static images—making safety compliance visible, frame by frame.
</i></p>

---

<div align="center">

## Model Performance

</div>

![Training Metrics](runs/detect/full_training/metrics.png)

**Key Results after 25 Training Epochs:**

| Metric        | Value      | Description                                      |
|:-------------:|:----------:|:-------------------------------------------------|
| 🎯 **Precision** <br> (Helmet Detection) | **91.6%**   | High reliability of positive detections           |
| 🔎 **Recall** <br> (Head Detection)     | **90.5%**   | Strong ability to find relevant objects           |
| 🏆 **mAP@0.5**                          | **89.3%**   | Robust overall detection capability               |
| 📊 **mAP@0.5:0.95**                     | **76.7%**   | Good localization accuracy across IoU thresholds  |

> These results confirm HelmetGuard’s effectiveness for construction site safety monitoring, with particularly strong performance in detecting safety-critical equipment like helmets.

## Installation Guide

```bash
# Clone this repository
git clone https://github.com/yourusername/helmet-guard.git
cd helmet-guard

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

The requirements.txt file contains all necessary Python packages for this project:

- ultralytics (for YOLOv8)
- opencv-python (OpenCV)
- And their dependencies

If you encounter issues with the installation, you can install the core dependencies manually:

```bash
pip install ultralytics opencv-python torch torchvision
```

## Usage

To train the model:

```bash
cd scripts
python train.py
```

To run detection on a video:

```bash
cd scripts
python detect_video.py
```

## 📊 Dataset

This project uses the **"Hardhat + Vests"** dataset from Kaggle.

<a href="https://www.kaggle.com/datasets/muhammetzahitaydn/hardhat-vest-dataset-v3?resource=download">
  <img src="https://img.shields.io/badge/Kaggle-Dataset-20BEFF?style=for-the-badge&logo=kaggle" alt="Kaggle Dataset"/>
</a>

### Setup Instructions:

1. **Download** the dataset from Kaggle
2. **Extract** contents to the `datasets/helmet_data` directory
3. **Verify** directory structure matches `config/data.yaml`

## 🎬 Test Videos

<a href="https://www.pexels.com/search/videos/construction%20workers/">
  <img src="https://img.shields.io/badge/Pexels-Videos-05A081?style=for-the-badge&logo=pexels" alt="Pexels Videos"/>
</a>

This project uses free stock videos from Pexels for testing and demonstration purposes.  

Please respect their [license terms](https://www.pexels.com/license/) when using this content.

## 🔍 Extended Applications

<table>
  <tr>
    <td width="50%" align="center"><h3>🛣️ Road Safety</h3></td>
    <td width="50%" align="center"><h3>🏭 Other Safety Applications</h3></td>
  </tr>
  <tr valign="top">
    <td>
      <ul>
        <li><b>🏍️ Motorcycle Helmet Detection</b>: Monitor compliance with helmet laws</li>
        <li><b>🚲 Bicycle Safety Gear</b>: Identify cyclists without proper equipment</li>
        <li><b>🚦 Traffic Violation Monitoring</b>: Create automated detection systems</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>🦺 Industrial Compliance</b>: Adapt for different PPE requirements</li>
        <li><b>🚗 License Plate Recognition</b>: Identify and log vehicle plates</li>
        <li><b>👥 Crowd Safety Analysis</b>: Monitor protocols in public gatherings</li>
      </ul>
    </td>
  </tr>
</table>

<div align="center">
  <i>The YOLOv8 architecture provides a flexible foundation that can be retrained on different datasets to address these varied safety challenges with minimal code changes.</i>
</div>