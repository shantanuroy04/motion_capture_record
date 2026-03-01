# AI-Based Human Landmark Detection and Recording System

## 📖 Introduction

Human pose estimation is a core task in computer vision that involves detecting keypoints on the human body such as joints, facial landmarks, and hand positions.

This project implements a complete **real-time keypoint detection pipeline** with a professional GUI. The system captures webcam input, processes each frame using the **MediaPipe Holistic** model, and extracts landmark coordinates for selected body parts.

The extracted data is stored in JSON format and can be used for:

* Machine Learning model training
* Gesture recognition
* Motion analysis
* Human-computer interaction
* Animation and game development
* Biomechanics and sports analysis

---

## 🖼 System Overview

![Image](https://camo.githubusercontent.com/034c02b2e6aae3873f5a4dba10fc7a200ad5b161396f25709f07109df8ff1067/68747470733a2f2f6d65646961706970652e6465762f696d616765732f6d6f62696c652f706f73655f747261636b696e675f66756c6c5f626f64795f6c616e646d61726b732e706e67)

![Image](https://www.researchgate.net/publication/376909901/figure/fig3/AS%3A11431281414246560%401746009882739/MediaPipe-Face-Mesh-A-3D-Facial-Landmark-Detector-with-468-Landmarks.tif)

![Image](https://mediapipe.dev/images/mobile/hand_landmarks.png)

![Image](https://www.researchgate.net/publication/362871842/figure/fig1/AS%3A11431281084350163%401663153181104/MediaPipe-Hands-21-landmarks-13.ppm)

---

🔁 System Pipeline
Webcam Input
     ↓
OpenCV Frame Capture
     ↓
MediaPipe Holistic Processing
     ↓
Landmark Extraction
     ↓
GUI Visualization (PyQt5)
     ↓
JSON Data Storage

## 🚀 Features

### ✅ Real-Time Landmark Detection

* Detects **pose, face, and hand landmarks** in real time
* Uses **MediaPipe Holistic** model for high-accuracy tracking
* Processes video directly from webcam using OpenCV

### ✅ Selective Body Part Tracking

Users can select specific parts to track:

* Whole Body
* Face Only
* Hands Only
* Legs Only

This improves performance and allows targeted data collection.

### ✅ Landmark Data Recording

* Records landmark coordinates frame-by-frame
* Stores normalized 3D coordinates `(x, y, z)`
* Saves data in **JSON format** for ML training

### ✅ Professional GUI Interface

Built using **PyQt5**, including:

* Live video display
* Start/Stop recording buttons
* Save data functionality
* Body part selection dropdown

---

## 🏗 Tech Stack

### Programming Language

* Python 3.9+

### Computer Vision

* OpenCV
* MediaPipe Holistic

### GUI Framework

* PyQt5

### Data Processing

* NumPy
* JSON

### Logging and Error Handling

* Python `logging` module

---

## ⚙ System Architecture

### Step 1: Webcam Capture

```python
self.capture = cv2.VideoCapture(0)
```

### Step 2: Frame Processing

Each frame is converted to RGB and processed using MediaPipe:

```python
results = self.holistic.process(frame_rgb)
```

MediaPipe detects:

* 33 pose landmarks
* 468 face landmarks
* 21 landmarks per hand

---

### Step 3: Landmark Extraction

Coordinates are extracted and normalized:

```python
normalized_landmarks.append((landmark.x, landmark.y, landmark.z))
```

These coordinates represent spatial positions of keypoints.

---

### Step 4: Visualization

Landmarks are drawn on the frame using MediaPipe drawing utilities.

---

### Step 5: Recording and Saving

Landmark data is saved as JSON:

```python
json.dump(self.key_points, f)
```

This allows reuse for:

* Machine learning training
* Motion analysis
* Gesture recognition

---

## 💻 Installation Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/human-landmark-detection.git
cd human-landmark-detection
```

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install opencv-python mediapipe PyQt5 numpy
```

---

## ▶ How to Run

```bash
python main.py
```

---

## 🎮 How to Use

1. Launch the application
2. Webcam will open automatically
3. Select body part from dropdown
4. Click **Start Recording**
5. Perform movements
6. Click **Stop Recording**
7. Click **Save Key Points**
8. Save JSON file

---

## 📊 Applications

### 🤖 Machine Learning

* Pose classification
* Gesture recognition
* Action detection

### 👁 Computer Vision

* Motion tracking
* Human behavior analysis

### 🎮 Game Development

* Character animation
* Motion capture

### 🏥 Healthcare

* Physiotherapy monitoring
* Movement analysis

---

## 🧠 Example Machine Learning Use Case

Collected keypoint data can be used to train models such as:

* LSTM for action recognition
* Random Forest for gesture classification
* CNN-LSTM hybrid models
* GRU or Transformer-based sequence models

Example workflow:

1. Collect keypoint data
2. Label dataset
3. Split into train/test sets
4. Train deep learning model
5. Evaluate accuracy
6. Deploy real-time classifier

---

## 📁 Project Structure

```
project/
│
├── main.py
├── README.md
├── requirements.txt
```

---

## 🔮 Future Improvements

* Add dataset labeling tool
* Export to CSV format
* Add ML model training module
* Real-time gesture classification
* Multi-person detection

---

## 🛠 Troubleshooting

### Webcam Not Opening

* Ensure no other application is using the camera
* Try changing camera index:

```python
cv2.VideoCapture(1)
```

### MediaPipe Errors

* Make sure mediapipe version is compatible:

```bash
pip install mediapipe==0.10.0
```

### GUI Not Launching

* Ensure PyQt5 is properly installed:

```bash
pip install PyQt5
```

---

## 📦 Dependencies

* Python 3.9+
* opencv-python
* mediapipe
* PyQt5
* numpy

---

## 👥 Contributors

* Shantanu Roy
(shantanur003@gmail.com)

(Feel free to add contributors here.)

---

## 📄 License

This project is licensed under the MIT License.
You may modify and distribute it freely.

---

# ⭐ If you find this project useful, consider giving it a star on GitHub!
