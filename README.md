# 🌿 Plant Disease Detection API (YOLOv8 + FastAPI)

A high-performance, production-ready REST API for detecting plant diseases from leaf images using state-of-the-art **YOLOv8** object detection. This project bridges the gap between advanced Deep Learning models and scalable web deployment.

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## ✨ Features

- 🎯 **High Accuracy:** Fine-tuned YOLOv8 model achieving **91.7% mAP50** on the Tomato Leaf Disease dataset.
- ⚡ **Blazing Fast:** Built with FastAPI for asynchronous, high-speed inference.
- 🧹 **Clean Output:** Returns structured, easy-to-parse JSON responses.
- 🐳 **Docker Ready:** Fully containerized architecture for seamless deployment (Dockerfile included).
- 🛠️ **Extensible:** Easy to swap the model weights for other plant diseases or custom datasets.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Web Framework:** FastAPI + Uvicorn
- **Deep Learning:** YOLOv8 (Ultralytics), PyTorch
- **Image Processing:** OpenCV, NumPy
- **Containerization:** Docker

---

## 📁 Project Structure

```text
plant-disease-yolo/
├── app.py              # FastAPI application and inference logic
├── train.py            # Script for training/fine-tuning the YOLO model
├── Dockerfile          # Docker configuration for containerization
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
