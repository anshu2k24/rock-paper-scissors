# 🪨💄✂️ Rock Paper Scissors Detection (YOLOv8)

A **YOLO-based image detection model** that identifies **rock, paper, and scissors** hand gestures from images or videos.
Trained on a **Kaggle Rock-Paper-Scissors dataset**, this project demonstrates real-time classification using modern computer vision techniques.

---

## 🚀 Features

* 🎯 **YOLOv8 / YOLO11 models** fine-tuned for hand gesture detection
* 🧠 Detects **rock**, **paper**, and **scissors** postures from images or video streams
* 📸 Compatible with **OpenCV** for live camera or batch image inference
* 🧩 Ready-to-extend for integration into a **gesture-based game engine**

---

## 🧮 Tech Stack

* **Python 3.10+**
* **Ultralytics YOLOv8**
* **OpenCV**
* **PyTorch**
* **NumPy / Pandas**

---

## 📂 Project Structure

```
├── runs/detect/         # YOLO detection outputs
├── test.py              # Test script for inference
├── yolov8n.pt           # YOLOv8 model weights
├── yolo11n.pt           # Experimental YOLO11 model weights
└── README.md
```

---

## 🤪 Usage

### 1️⃣ Install Dependencies

```bash
pip install ultralytics opencv-python torch
```

### 2️⃣ Run Detection

Run inference on a folder of images:

```bash
python test.py --source path/to/images
```

Or test a single image:

```bash
python test.py --source sample.jpg
```

### 3️⃣ Output

Detected results (with bounding boxes + labels) are saved in:

```
runs/detect/
```

---

## 🧠 Model Info

* **Base Model:** YOLOv8n / YOLO11n
* **Dataset:** Kaggle Rock–Paper–Scissors Dataset
* **Classes:** `['rock', 'paper', 'scissors']`

---

## 🔮 Future Plans

* 🕹️ Add gameplay logic for AI vs Player
* 🌐 Build a Next.js dashboard for visual inference
* 📊 Add live webcam integration and analytics view

---

## 👨‍💻 Author

**Anshuman Pati**
[🔗 GitHub](https://github.com/anshu2k24) | [💼 LinkedIn](https://www.linkedin.com/in/anshuman-pati-5575bb34a/)

---

> ⚡ *“Where Computer Vision meets classic gameplay.”*
