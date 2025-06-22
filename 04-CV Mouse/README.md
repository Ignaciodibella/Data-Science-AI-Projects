# 🖱️✋ Virtual Mouse with Hand Gestures

Control your mouse cursor with just your hand using this Computer Vision-powered virtual mouse!  
This project uses a webcam, hand-tracking via MediaPipe, and screen control with AutoPy.

---

## 🎯 Objective

Replace the physical mouse with intuitive hand gestures:
- Move the mouse with your index finger
- Perform clicks by pinching fingers together

## 🧰 Technologies Used

- 🐍 Python 3.8
- 📷 OpenCV
- 🖐️ MediaPipe (via custom `HandTrackingModule`)
- 🖱️ AutoPy (for controlling the actual cursor)

## 🖼️ Features

- 🖐️ **Hand detection** and finger landmark tracking
- 🎯 **Smooth movement** of the mouse using index finger
- 🟢 **Click gestures** by pinching index and middle fingers
- 🧭 Optional bounding box for motion control
- 📈 FPS counter displayed on screen

## ▶️ How to Run

1. Download `HandTrackingModule.py` and `CVVirtualMouse.py` files.
2. See the **Requirement** section for installation requirements.
3. Once it's up and running you'll notice the front camera will open up and a window will pop up.
4. Your index finger will serve as a mouse. 
   <br> Just leaving your index finger up will activate navigation or movement mode.
   <br> If you want to click on something raise your middle finger to do so.
   <br> I'm currently working on adding the drag-click and right-click to the project.

## ⚠️Requirements: 
You'll need to install the following
- `cvzone` (here i'm using the 1.5.6 version)
- `opencv-python` (i'm using the 4.7.0.72 version)
- `mediapipe`
