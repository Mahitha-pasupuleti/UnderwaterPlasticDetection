Underwater Plastic Detection

This project is an end-to-end implementation of an object detection model using YOLO to detect various types of underwater plastic pollution in images and videos. The model has been trained on a custom dataset and can be used to analyze oceanic environments for pollution detection.

Features

Upload an image or video for plastic pollution detection

Process and display detected objects in real-time

Responsive web interface for ease of use

Folder Structure

underwater-plastic-detection/
├── app.py                 # Main application script
├── model/                 # Folder containing trained YOLO model weights
│   └── best.pt            # Trained YOLO model file
├── requirements.txt       # Dependencies for the project
├── static/                # Static files like CSS and JavaScript
│   └── css/
│       └── styles.css
├── templates/             # HTML templates for the web interface
│   └── index.html
├── uploads/               # Folder for storing uploaded test images and videos
│   ├── images/            # Uploaded images
│   └── videos/            # Uploaded videos
├── README.md              # Project documentation

Installation and Setup

Prerequisites

Ensure you have Python installed (recommended: Python 3.8 or later). Install Conda if using a virtual environment.

Step 1: Clone the Repository

git clone https://github.com/your-repo/underwater-plastic-detection.git
cd underwater-plastic-detection

Step 2: Set Up a Virtual Environment (Recommended)

Using Conda:

conda create --name plastic-detection python=3.8 -y
conda activate plastic-detection

Or using venv:

python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Run the Application

python app.py

The application will start, and you can access it in your browser at http://127.0.0.1:5000/.

Dependencies

The project requires the following Python packages:

Flask (for the web interface)

OpenCV (for image and video processing)

NumPy (for array processing)

ultralytics (for YOLO object detection)

To install all dependencies, simply run:

pip install -r requirements.txt

Usage

Open the application in your browser.

Upload an image or video for detection.

View the processed output with detected plastic objects.

Dataset and Model

The model has been trained using a dataset containing 15 classes of underwater plastic waste. The trained YOLO model (best.pt) is stored in the model/ directory.

Testing

Test images and videos are stored in the uploads/ directory. You can use them to check the functionality of the model.

Contributing

Feel free to submit issues or contribute improvements via pull requests.

License

This project is open-source under the MIT License.
