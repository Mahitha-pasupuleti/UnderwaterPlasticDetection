import cv2
from ultralytics import YOLO

# Load your trained YOLO model
model = YOLO("/home/duy-ho-black/Downloads/archive/OceanPollution/runs/detect/train5/weights/best.pt")

# Path to your video file
video_path = "/home/duy-ho-black/Downloads/Water.mp4"  # Replace with your actual video file path

# Open the video file
video_capture = cv2.VideoCapture(video_path)

# Check if video is opened correctly
if not video_capture.isOpened():
    print("Error: Could not open video.")
else:
    print("Video opened successfully!")

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        print("End of video stream.")
        break

    # Run YOLO inference on the current frame
    results = model.predict(frame)

    # Annotate the frame with YOLO bounding boxes
    for result in results:
        annotated_frame = result.plot()  # Annotate the frame with bounding boxes

    # Display the annotated frame
    cv2.imshow("YOLO Detection", annotated_frame)

    # Wait for 1 ms and check if 'q' key is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close the window
video_capture.release()
cv2.destroyAllWindows()
