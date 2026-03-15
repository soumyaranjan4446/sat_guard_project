# 🛰️ SAT-GUARD: AI-Based Defense Surveillance System

## 📌 Project Overview
SAT-GUARD is an AI-powered prototype designed for automated detection of military and strategic assets from satellite imagery. 

Unlike standard object detection models that use axis-aligned boxes, this system implements **Oriented Bounding Boxes (OBB)** using YOLOv8. This allows the model to accurately capture the precise angle and orientation of assets (like aircraft, ships, and infrastructure) regardless of the satellite's viewing angle.

This repository contains the **Proof of Concept (v1.0)**, featuring a local training pipeline and an interactive Streamlit dashboard for real-time threat intelligence reporting.

---

## 🚀 Features (Prototype v1.0)
* **Oriented Bounding Box (OBB) Detection:** Captures the exact rotation of targets in aerial imagery.
* **Rapid CPU-Based Training:** Includes a lightweight script to automatically fetch and train on a miniature test dataset (`dota8`).
* **Interactive Intelligence Dashboard:** Built with Streamlit to visualize satellite feeds, overlay detection metrics, and generate instant confidence reports.

---

## 🛠️ Tech Stack
* **Computer Vision:** YOLOv8-OBB (Ultralytics)
* **Framework:** PyTorch
* **Frontend Dashboard:** Streamlit
* **Language:** Python 3.x

---

## ⚙️ Local Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/sat_guard_project.git](https://github.com/yourusername/sat_guard_project.git)
cd sat_guard_project