from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Open the input video
video = cv2.VideoCapture("object_detection_input.mp4")

# Get video properties
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter(
    "object_detection_output.mp4",
    fourcc,
    fps,
    (width, height)
)

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Detect and track objects
    results = model.track(frame, persist=True)

    # Draw detections on the frame
    annotated_frame = results[0].plot()

    # Save the processed frame
    output.write(annotated_frame)

    # Display the frame
    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
output.release()
cv2.destroyAllWindows()