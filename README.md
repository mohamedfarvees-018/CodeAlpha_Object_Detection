Object Detection and Tracking using YOLO
Project Overview
This project implements object detection and tracking in video using the YOLO (You Only Look Once) model and OpenCV.

The system processes an input video, detects objects in each frame, tracks the detected objects, and generates an annotated output video with bounding boxes, object labels, and confidence scores.

Features
Real-time object detection from video
Object tracking across video frames
Bounding boxes around detected objects
Object class labels
Confidence scores for detections
Annotated output video generation
Technologies Used
Python
YOLOv8
Ultralytics
OpenCV
Project Structure
CodeAlpha_Object_Detection/ │ ├── object_detection.py ├── object_detection_input.mp4 ├── object_detection_output.mp4 ├── yolov8n.pt ├── requirements.txt └── README.md

Requirements
Make sure Python is installed on your system.

Install the required libraries using:

pip install -r requirements.txt

How to Run
Open the project folder in Visual Studio Code.

Install the required dependencies:

pip install -r requirements.txt

Run the Python program:
python object_detection.py

The program will process the input video and generate an annotated output video.
Input
The project uses object_detection_input.mp4 as the input video.

Output
The processed video is saved as object_detection_output.mp4.

The output video contains detected objects with bounding boxes, labels, and confidence scores.

YOLO Model
This project uses the yolov8n.pt YOLO model for object detection.

Project Purpose
This project was developed as part of the CodeAlpha Internship – Object Detection and Tracking Task to gain practical experience in computer vision, object detection, and video processing using Python.

Author
mohamed farvees s 

B.tech CSE(IOT)
