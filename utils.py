import cv2
import numpy as np
from ultralytics import YOLO

# Class names (same as training)
CLASS_NAMES = ["Crack", "Pothole", "Manhole"]

# ---------------- LOAD MODEL ----------------
def load_model():
    model = YOLO("models/yolo_best.pt")
    model = MobileNet("models/road_damage_model.h5")
    return model

# ---------------- LOAD IMAGE ----------------
def load_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    return img

# ---------------- DETECT + DRAW ----------------
def detect_and_draw(model, image):

    results = model(image, conf=0.5)  # increase confidence (reduce false detection)

    img_copy = image.copy()
    detections = []

    for r in results:
        boxes = r.boxes

        if boxes is None:
            continue

        for box in boxes:
            conf = float(box.conf[0])

            # ❌ Skip low confidence
            if conf < 0.5:
                continue

            cls = int(box.cls[0])
            label = CLASS_NAMES[cls]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append((label, conf))

            # ✔ Bright green box
            cv2.rectangle(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # ✔ Label text
            text = f"{label} ({conf:.2f})"
            cv2.putText(img_copy, text, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    return img_copy, detections
