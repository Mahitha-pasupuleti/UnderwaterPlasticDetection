# Underwater Plastic Detection

This project detects underwater plastic pollution using a trained YOLO model. It allows users to upload images or videos and processes them to identify plastic waste in aquatic environments.

## Features
- Upload images or videos for real-time detection.
- Uses a YOLO model for accurate object detection.
- Displays processed images and videos with bounding boxes.
- Responsive web interface built with Flask.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Conda (Optional but recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/UnderwaterPlasticDetection.git
   cd UnderwaterPlasticDetection
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   conda create --name underwater_detection python=3.8 -y
   conda activate underwater_detection
   ```
   or using `venv`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the YOLO model is placed correctly inside the project directory:
   ```
   ├── static/
   ├── templates/
   ├── uploads/  # Stores uploaded test images/videos
   ├── models/
       ├── best.pt  # Your trained YOLO model
   ├── app.py  # Flask backend
   ├── requirements.txt
   ├── README.md
   ```

5. Run the Flask application:
   ```bash
   python app.py
   ```

6. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Click **Upload Image** or **Upload Video**.
- The processed output will be displayed on the right.
- Click **Download** to save the processed image/video.

## Dependencies
The project requires the following packages:
```
Flask
opencv-python
numpy
ultralytics  # For YOLO
```

You can install them using:
```bash
pip install -r requirements.txt
```

## Folder Structure
```
UnderwaterPlasticDetection/
├── static/
│   ├── css/
│   │   ├── styles.css
│   ├── uploads/
├── templates/
│   ├── index.html
├── uploads/  # Stores uploaded test images/videos
├── models/
│   ├── best.pt  # Your trained YOLO model
├── app.py  # Flask backend
├── requirements.txt
├── README.md
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss the proposed changes.

