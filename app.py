import os
import cv2
import torch
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from ultralytics import YOLO

app = Flask(__name__)

# Configure the upload folder and allowed extensions for both image and video
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_IMAGE_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['ALLOWED_VIDEO_EXTENSIONS'] = {'mp4', 'avi', 'mov', 'mkv'}

# Load your trained YOLO model
model = YOLO("/home/duy-ho-black/Downloads/archive/OceanPollution/runs/detect/train5/weights/best.pt")

# Ensure uploads and static directories exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Helper function to check valid file extensions
def allowed_file(filename, file_type):
    if file_type == "image":
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_IMAGE_EXTENSIONS']
    elif file_type == "video":
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_VIDEO_EXTENSIONS']
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if the image or video file is part of the request
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename, "image"):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                # Run inference on the uploaded image
                result = model.predict(filepath, iou=0.4)
                image_with_bboxes = result[0].plot()

                # Save the processed image to static folder
                output_filepath = os.path.join("static", "output_image.jpg")
                cv2.imwrite(output_filepath, image_with_bboxes)

                # Return the processed image in the response
                return render_template("index.html", image_url="static/output_image.jpg")
        elif 'video' in request.files:
            file = request.files['video']
            if file and allowed_file(file.filename, "video"):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                # Process the video and display it in real-time
                process_video(filepath)

                return render_template("index.html", message="Real-time video processing completed.")

    return render_template("index.html")


def process_video(input_video_path):
    video_capture = cv2.VideoCapture(input_video_path)

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


if __name__ == "__main__":
    app.run(debug=True)
