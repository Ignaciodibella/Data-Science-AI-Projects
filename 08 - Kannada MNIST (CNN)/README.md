# 🔢 Handwritten Digit Recognizer

A computer vision project that uses deep learning to classify grayscale images of handwritten digits (0–9) in Kannada-MNIST dataset.

🏆 [Based on this Kaggle Competition.](https://www.kaggle.com/competitions/Kannada-MNIST)

This uses a similar CNN that the one seen at [02-Digit Recognizer (CV)](https://github.com/Ignaciodibella/Data-Science-AI-Projects/tree/main/02-Digit%20Recognizer%20(CV))

## 🎯 Objective

Build a neural network model to recognize digits from image data using supervised learning techniques.

## 🧰 Technologies & Tools

- Python
- NumPy, pandas
- PyTorch
- Matplotlib

## 🔍 Workflow Overview

1. 📥 Load and preprocess pixel data from CSV
2. 📊 Normalize and reshape image arrays (28x28)
3. 🧠 Train a CNN using PyTorch
4. 🧪 Evaluate model performance
5. 📩 Generate predictions for submission

## 📁 Files

- `kannada-mnist-cnn.ipynb`: Complete training workflow using CNN.
- `kannada_submission.csv`: Predicted labels for test set.
- `README.md`: Project summary.

## 📌 Notes

- Dataset source: [Kaggle Digit Recognizer](https://www.kaggle.com/competitions/digit-recognizer)
- GPU-accelerated training on Kaggle for better performance.

---
