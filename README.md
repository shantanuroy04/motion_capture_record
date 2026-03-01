AI-Based Human Landmark Detection and Recording System
📖 Introduction

Human pose estimation is a core task in computer vision that involves detecting keypoints on the human body such as joints, facial landmarks, and hand positions.

This project implements a complete real-time keypoint detection pipeline with a professional GUI. The system captures webcam input, processes each frame using MediaPipe Holistic, and extracts landmark coordinates for selected body parts.

The extracted data is stored in JSON format and can be used for:

Machine Learning model training

Gesture recognition

Motion analysis

Human-computer interaction

Animation and game development

Biomechanics and sports analysis

🖼 System Overview
4
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
📑 Table of Contents

Features

Technologies Used

System Architecture

System Pipeline

Installation Guide

How to Run

How to Use

Applications

Example Machine Learning Use Case

Project Structure

Future Improvements

Troubleshooting

Dependencies

License

🚀 Features
✅ Real-Time Landmark Detection

Detects pose, face, and hand landmarks in real time

Uses MediaPipe Holistic for high-accuracy tracking

Processes video directly from webcam using OpenCV

✅ Selective Body Part Tracking

Users can select specific parts to track:

Whole Body

Face Only

Hands Only

Legs Only

Improves performance and enables targeted data collection.

✅ Landmark Data Recording

Records landmark coordinates frame-by-frame

Stores normalized 3D coordinates (x, y, z)

Saves data in JSON format for ML training

✅ Professional GUI Interface

Built using PyQt5, including:

Live video display

Start/Stop recording buttons

Save data functionality

Body part selection dropdown

🏗 Technologies Used
Programming Language

Python 3.9+

Computer Vision

OpenCV

MediaPipe Holistic

GUI Framework

PyQt5

Data Processing

NumPy

JSON

Logging

Python logging module

⚙ System Architecture
Step 1: Webcam Capture
self.capture = cv2.VideoCapture(0)
Step 2: Frame Processing
results = self.holistic.process(frame_rgb)

MediaPipe detects:

33 pose landmarks

468 face landmarks

21 landmarks per hand

Step 3: Landmark Extraction
normalized_landmarks.append((landmark.x, landmark.y, landmark.z))

Coordinates represent spatial positions of keypoints.

Step 4: Visualization

Landmarks are drawn using MediaPipe drawing utilities.

Step 5: Recording and Saving
json.dump(self.key_points, f)

Saved data can be reused for:

ML training

Motion analysis

Gesture recognition

💻 Installation Guide
1️⃣ Clone Repository
git clone https://github.com/yourusername/human-landmark-detection.git
cd human-landmark-detection
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install opencv-python mediapipe PyQt5 numpy
▶ How to Run
python main.py
🎮 How to Use

Launch the application

Webcam opens automatically

Select body part from dropdown

Click Start Recording

Perform movements

Click Stop Recording

Click Save Key Points

Save JSON file

📊 Applications
🤖 Machine Learning

Pose classification

Gesture recognition

Action detection

👁 Computer Vision

Motion tracking

Human behavior analysis

🎮 Game Development

Character animation

Motion capture

🏥 Healthcare

Physiotherapy monitoring

Movement analysis

🧠 Example Machine Learning Use Case

Collected keypoint data can train:

LSTM for action recognition

Random Forest for gesture classification

CNN-LSTM hybrid models

GRU or Transformer-based sequence models

Example Workflow

Collect keypoint data

Label dataset

Split into train/test sets

Train model

Evaluate accuracy

Deploy classifier

📁 Project Structure
project/
│
├── main.py
├── README.md
├── requirements.txt
🔮 Future Improvements

Dataset labeling tool

Export to CSV format

Integrated ML training module

Real-time gesture classification

Multi-person detection

🛠 Troubleshooting
Webcam Not Opening

Ensure no other app is using the camera

Try changing camera index:

cv2.VideoCapture(1)
MediaPipe Errors
pip install mediapipe==0.10.0
GUI Not Launching
pip install PyQt5
📦 Dependencies

Python 3.9+

opencv-python

mediapipe

PyQt5

numpy

👥 Contributors

Your Name

📄 License

This project is licensed under the MIT License.

⭐ If you find this project useful, consider giving it a star on GitHub!
