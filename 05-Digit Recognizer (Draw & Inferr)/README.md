# ✍️🧠 Handwritten Digit GUI Inference App

This project extends the **[02-Digit Recognizer (CV)](https://github.com/Ignaciodibella/Data-Science-AI-Projects/tree/main/02-Digit%20Recognizer%20(CV))** by providing a **Tkinter-based graphical interface** where you can draw a digit (0–9) with your mouse and get real-time inference using a pre-trained CNN model.

---

## 🎯 Objective

Allow users to interactively draw digits and use a trained PyTorch model to classify the handwritten input, simulating an MNIST-style recognition pipeline.

---

## 🖼️ Features

- 🖌️ Draw your digit on a 28×28 canvas (scaled for usability)
- 🧠 Get instant classification using a **custom-trained CNN**
- 🔁 Clear the canvas or retry easily
- 📦 Standalone UI — no Jupyter, just run and interact

---

## 🧰 Technologies Used

- Python 3
- Tkinter (GUI)
- PyTorch
- PIL / ImageTk
- NumPy, pandas

---

## ▶️ How to Run

### 1. 📦 Install dependencies

```bash
pip install torch torchvision pandas numpy pillow
