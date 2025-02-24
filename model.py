
import numpy as np
from ultralytics import YOLO  # Ensure ultralytics is installed: pip install ultralytics

# Load your trained YOLO model
model = YOLO("/home/duy-ho-black/Downloads/archive/OceanPollution/runs/detect/train5/weights/best.pt")

result = model.predict("/home/duy-ho-black/Downloads/archive/underwater_plastics/test/images/istockphoto-1254710473-170667a_jpg.rf.f6ecaea0c377cd5c3e50a830316a12bd.jpg", iou=0.4)

image_with_bboxes = result[0].plot()

cv2.imshow("Predicted Image", image_with_bboxes)

while True:
    if cv2.waitKey(1) & 0xFF != 255:  # If any key is pressed
        break
    
cv2.destroyAllWindows()
