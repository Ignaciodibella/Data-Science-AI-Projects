# Computer Vision Calculator
Gesture controlled calculator using computer vision with python.
<div align="center">
     <img src = "https://github.com/Ignaciodibella/ComputerVisionCalculator/blob/main/cvcalc.gif">
</div>

<br>

<div align="center">
     <img src = "https://github.com/Ignaciodibella/ComputerVisionCalculator/blob/main/handrecognition.png" width = 507 height = 284>
</div>

### 💡 How to use it:
1. Download the `CVCalculator.py` file.
2. See the **Requirement** section for installation requirements.
3. Once it's up and running you'll notice the front camera will open up and a window will pop up.
4. Your index finger will serve as a mouse. Also, al line will be "connecting" your index and your middle finger. <br>
   If you put both fingers together you'll be simulating a click event.<br>
   **The closer to the screen you are, less click sensitivity and the further away, the greater sensitivity.**
5. There are two special keys in the calculator keyboard:
  <br>**D:** It is used to delete the last number or operator entered,
  <br>**C:** It is used to clear the calculator screen.
6. To keep in mind:
   <br> The 2**3 input will work as a power operator, so the result will be 8.
   <br> Two minus signs will end up being interpreted as a sum and a (5 - - 5 = 10)
   <br> And something similar happens if you mix +/- endig up in a substraciont (5 +- 2 = 3)

### ⚠️Requirements: 
You'll need to install the following
- `cvzone` (here i'm using the 1.5.6 version)
- `opencv-python` (i'm using the 4.7.0.72 version)
- `mediapipe`

This project was made using `Python 3.9`.

### 🛠️Configuration:
- At line 82 you'll see a line containing: `#print(length)`
<br> If you uncomment this line and run the project, you'll notice that as you move your index finger closer to (or further from) your middle finger, a series of console outputs will display the distance between them.
<br> This is intended to adjust or calibrate the clic sensibility, but the default config should work just fine.
<br> Nonetheless, you can tweak this config at line 84: `if length < 47:`

<div align="center">
<img src ="https://github.com/Ignaciodibella/ComputerVisionCalculator/blob/main/length.PNG">
</div>
