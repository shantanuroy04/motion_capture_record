import cv2
import mediapipe as mp
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QMessageBox, QFileDialog, QHBoxLayout, QComboBox
from PyQt5.QtGui import QImage, QPixmap, QTransform
from PyQt5.QtCore import QTimer, Qt
import logging
import json
import os

class HolisticApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(960, 540)
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            logging.error("Error: Unable to open camera.")
            QMessageBox.critical(self, "Error", "Unable to open camera.")
            return
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.top_layout = QHBoxLayout()
        self.layout.addLayout(self.top_layout)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.comboBox = QComboBox()
        self.comboBox.addItem("Whole Body")
        self.comboBox.addItem("Face")
        self.comboBox.addItem("Hands")
        self.comboBox.addItem("Legs")
        self.top_layout.addWidget(self.comboBox)

        self.record_button = QPushButton("Start Recording")
        self.record_button.clicked.connect(self.start_recording)
        self.stop_button = QPushButton("Stop Recording")
        self.stop_button.clicked.connect(self.stop_recording)
        self.save_button = QPushButton("Save Key Points")
        self.save_button.clicked.connect(self.save_key_points)

        self.top_layout.addWidget(self.record_button)
        self.top_layout.addWidget(self.stop_button)
        self.top_layout.addWidget(self.save_button)

        self.stop_button.setEnabled(False)
        self.save_button.setEnabled(False)

        self.is_recording = False
        self.key_points = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(33)

    def update(self):
        ret, frame = self.capture.read()
        if not ret:
            logging.error("Error: Unable to read frame from camera.")
            return
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.holistic.process(frame_rgb.copy())

        # Draw landmarks on the frame
        frame_rgb = self.draw_landmarks(frame_rgb, results)

        h, w, c = frame_rgb.shape
        q_image = QImage(frame_rgb.data, w, h, w * c, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)

        self.image_label.setPixmap(pixmap.scaled(
            self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        if self.is_recording:
            self.extract_key_points(results)

    def draw_landmarks(self, frame_rgb, results):
        selected_part = self.comboBox.currentText()
        if selected_part == "Whole Body":
            if results.pose_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame_rgb, results.pose_landmarks, mp.solutions.holistic.POSE_CONNECTIONS,
                    mp.solutions.drawing_utils.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                )
            if results.face_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame_rgb, results.face_landmarks, mp.solutions.holistic.FACEMESH_TESSELATION,
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1)
                )
            if results.left_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame_rgb, results.left_hand_landmarks, mp.solutions.holistic.HAND_CONNECTIONS,
                    mp.solutions.drawing_utils.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                )
            if results.right_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame_rgb, results.right_hand_landmarks, mp.solutions.holistic.HAND_CONNECTIONS,
                    mp.solutions.drawing_utils.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                )
        elif selected_part == "Face":
            if results.face_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame_rgb, results.face_landmarks, mp.solutions.holistic.FACEMESH_TESSELATION,
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=1, circle_radius=1)
                )
        elif selected_part == "Hands":
            if results.left_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame_rgb, results.left_hand_landmarks, mp.solutions.holistic.HAND_CONNECTIONS,
                    mp.solutions.drawing_utils.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                )
            if results.right_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame_rgb, results.right_hand_landmarks, mp.solutions.holistic.HAND_CONNECTIONS,
                    mp.solutions.drawing_utils.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                )
        elif selected_part == "Legs":
            if results.pose_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame_rgb, results.pose_landmarks, mp.solutions.holistic.POSE_CONNECTIONS,
                    mp.solutions.drawing_utils.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                    mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                )
        return frame_rgb

    def start_recording(self):
        self.is_recording = True
        self.record_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.save_button.setEnabled(False)

    def stop_recording(self):
        self.is_recording = False
        self.record_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.save_button.setEnabled(True)
        # Debugging: Print the size of key_points list after stopping recording
        print("Key points recorded:", len(self.key_points))

    def extract_key_points(self, results):
            selected_part = self.comboBox.currentText()
            key_points = {}
    
            if selected_part == "Whole Body":
                key_points["pose_landmarks"] = self.normalize_landmarks(results.pose_landmarks)
                key_points["face_landmarks"] = self.normalize_landmarks(results.face_landmarks)
                key_points["right_hand_landmarks"] = self.normalize_landmarks(results.right_hand_landmarks)
                key_points["left_hand_landmarks"] = self.normalize_landmarks(results.left_hand_landmarks)
            elif selected_part == "Face":
                key_points["face_landmarks"] = self.normalize_landmarks(results.face_landmarks)
            elif selected_part == "Hands":
                key_points["right_hand_landmarks"] = self.normalize_landmarks(results.right_hand_landmarks)
                key_points["left_hand_landmarks"] = self.normalize_landmarks(results.left_hand_landmarks)
            elif selected_part == "Legs":
                key_points["pose_landmarks"] = self.normalize_landmarks(results.pose_landmarks)
            else:
                QMessageBox.warning(self, "Invalid Selection", "Please select a valid body part.")
                return
    
            self.key_points.append(key_points)

    def normalize_landmarks(self, landmarks):
        if landmarks is None:
            return None
        normalized_landmarks = []
        for landmark in landmarks.landmark:
            normalized_landmarks.append((landmark.x, landmark.y, landmark.z))
        return normalized_landmarks

    def save_key_points(self):
        if self.key_points:
            filename, _ = QFileDialog.getSaveFileName(self, "Save Key Points", "", "JSON Files (*.json)")
            if filename:
                try:
                    with open(filename, "w") as f:
                        json.dump(self.key_points, f)
                    QMessageBox.information(self, "Key Points Saved", "Key points data saved successfully")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed to save key points: {str(e)}")
                    logging.error(f"Failed to save key points: {str(e)}")
        else:
            QMessageBox.warning(self, "No Key Points", "No key points data recorded")
    


    def closeEvent(self, event):
        self.capture.release()
        self.holistic.close()

if __name__ == '__main__':
    app = QApplication([])
    window = HolisticApp()
    window.show()
    app.exec_()