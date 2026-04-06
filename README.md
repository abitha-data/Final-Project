# 🚧 Automated Road Damage Detection using Deep Learning

## 📌 Overview

Road infrastructure plays a critical role in transportation safety and economic development. Manual inspection of road conditions is time-consuming, costly, and prone to human error.

This project presents an **AI-powered solution** that automatically detects and classifies road damages such as **cracks, potholes, and manholes** using deep learning techniques. The system is designed to work in real-world environments and can be extended for smart city applications.

---

## 🎯 Key Features

* 🚀 Real-time road damage detection using deep learning
* 📦 Object detection with bounding box visualization
* 🧠 Hybrid model experimentation (YOLO + MobileNet)
* 🎨 Clean and interactive UI using Streamlit
* ⚡ High-performance inference with optimized models
* ☁️ Deployment-ready architecture

---

## 🧠 Model Architecture

This project follows a hybrid deep learning approach combining detection and classification models:

### 🔹 YOLOv8 (Primary Model)

* Used for **object detection**
* Detects road damage regions with bounding boxes
* Provides real-time performance and high accuracy

### 🔹 MobileNetV2 (Secondary Model)

* Used for **classification of cropped damage regions**
* Lightweight and efficient architecture
* Evaluated for improving classification performance

### 🔗 Combined Workflow

1. YOLO detects damage regions in the image
2. Detected regions are optionally passed to MobileNet for classification
3. Final output includes damage type and location

> YOLOv8 demonstrated superior end-to-end performance and is used as the primary model in deployment.

---

## 🧪 Model Experimentation

The following models were implemented and evaluated:

* Custom CNN
* MobileNetV2
* ResNet50
* EfficientNetB0
* YOLOv8

YOLOv8 achieved the best results in terms of **accuracy, speed, and real-time usability**, making it the final choice for deployment.

---

## 🛠️ Tech Stack

* Python
* YOLOv8 (Ultralytics)
* TensorFlow / Keras
* OpenCV
* Streamlit
* NumPy, Matplotlib, Seaborn
* Scikit-learn

---

## 📂 Project Structure

```
RoadDamage/
│
├── app.py                     # Streamlit web application
├── utils.py                  # Helper functions
│
├── models/
│   ├── yolo_best.pt          # YOLO trained model
│   └── road_damage_model.keras  # MobileNet model
│
├── dataset/                  # YOLO dataset (train/val/test)
├── cnn_dataset/              # Cropped dataset for classification
├── runs/                     # YOLO training outputs
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/road-damage-detection.git
cd road-damage-detection
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run Application

```
streamlit run app.py
```

---

## 📸 Usage

1. Upload a road image
2. Model detects damages
3. Bounding boxes are displayed
4. Damage type is identified (Crack / Pothole / Manhole)

---

## 📊 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🚀 Future Enhancements

* 📱 Mobile application (Flutter integration)
* 🌍 Map-based damage tracking with GPS
* 📊 Dashboard analytics for smart city monitoring
* 📷 Live camera detection
* ☁️ Cloud deployment (Streamlit / AWS / GCP)

---

## 🌍 Use Cases

* Smart City Infrastructure Monitoring
* Government Road Maintenance Systems
* Transportation Safety Analysis
* Public Damage Reporting Platforms

---

## 👩‍💻 Author

**Abitha Jesuraj**

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.

