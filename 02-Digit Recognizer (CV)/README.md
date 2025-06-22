# 🔢 Handwritten Digit Recognizer

A computer vision project that uses deep learning to classify grayscale images of handwritten digits (0–9) from the classic MNIST dataset.
🏆 [Based on this Kaggle Competition.](https://www.kaggle.com/competitions/digit-recognizer)

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

- `digit-recognizer.ipynb`: Complete training workflow using CNN.
- `submission.csv`: Predicted labels for test set.
- `simple_cnn_model.pth`: Last trained model to make inferences or keep on training.
- `README.md`: Project summary.

## 📌 Notes

- Dataset source: [Kaggle Digit Recognizer](https://www.kaggle.com/competitions/digit-recognizer)
- GPU-accelerated training on Kaggle for better performance.

---
