# Imports
from tkinter import Button, Canvas, messagebox
from PIL import Image, ImageTk

import torchvision.transforms as transforms
import torch.nn as nn
import tkinter as tk
import pandas as pd
import numpy as np
import torch

MODEL_PATH = 'simple_cnn_model.pth'

class CustomMNISTDataset(torch.utils.data.Dataset):
    def __init__(self, csv_file, transform=None, is_test=False):
        self.data_frame = pd.read_csv(csv_file)
        self.transform = transform
        self.is_test = is_test

    def __len__(self):
        return len(self.data_frame)

    def __getitem__(self, index):
        item = self.data_frame.iloc[index]

        if self.is_test:
            image = item.values.reshape(28, 28).astype(np.uint8)
            label = None
        else:
            image = item[1:].values.reshape(28, 28).astype(np.uint8)
            label = item.iloc[0]

        image = transforms.ToPILImage()(image)

        if self.transform is not None:
            image = self.transform(image)

        if self.is_test:
            return image
        else:
            return image, label

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(128 * 7 * 7, 128)
        #self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(128, 20)
        self.fc3 = nn.Linear(20, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.pool(x)
        x = x.view(-1, 128 * 7 * 7) # Flattening directly to the known size
        x = self.fc1(x)
        x = self.relu(x)
        # x = self.dropout(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x

# Define the device (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

class MNISTDrawer:
    def __init__(self, master):
        self.master = master
        master.title("Draw MNIST-like Symbol and Infer")

        self.scale_factor = 10
        self.image_size = 28
        self.canvas_size = self.image_size * self.scale_factor

        self.drawing_active = False
        self.image_data = np.zeros((self.image_size, self.image_size), dtype=np.uint8)

        self.canvas = Canvas(master, width=self.canvas_size, height=self.canvas_size, bg="black", bd=2, relief="sunken")
        self.canvas.pack(pady=10)

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=5)

        self.ok_button = Button(self.button_frame, text="Infer", command=self.confirm_and_infer)
        self.ok_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = Button(self.button_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.cancel_button = Button(self.button_frame, text="Exit", command=self.cancel_input)
        self.cancel_button.pack(side=tk.LEFT, padx=5)

        self.result_image = None
        self.inferred_digit_label = tk.Label(master, text="Inferred Digit: ", font=("Helvetica", 16))
        self.inferred_digit_label.pack(pady=10)

        # Load the pre-trained model
        self.model = SimpleCNN().to(device)
        try:
            self.model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
            self.model.eval() # Set model to evaluation mode
            print(f"Model loaded successfully from {MODEL_PATH}")
        except FileNotFoundError:
            messagebox.showerror("Model Error", f"Model file not found at {MODEL_PATH}. Please ensure it's in the correct directory.")
            self.master.destroy()
            return
        except Exception as e:
            messagebox.showerror("Model Load Error", f"Error loading model: {e}")
            self.master.destroy()
            return

        # Define the transformations for inference (must match your test_data transforms)
        self.inference_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

    def start_draw(self, event):
        self.drawing_active = True
        self.draw(event) # Draw a single point if clicked

    def draw(self, event):
        if not self.drawing_active:
            return

        x, y = event.x, event.y
        # Convert canvas coordinates to image data coordinates
        img_x = int(x / self.scale_factor)
        img_y = int(y / self.scale_factor)

        # Draw a circle on the canvas
        brush_size = 2 * self.scale_factor # Adjust brush size for drawing on canvas
        self.canvas.create_oval(x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2, fill="white", outline="white")

        # Update the underlying image data (28x28)
        # Apply a small "brush" to the 28x28 array for smoother drawing
        for i in range(-1, 2):  # Simple 3x3 brush in image data
            for j in range(-1, 2):
                nx, ny = img_x + i, img_y + j
                if 0 <= nx < self.image_size and 0 <= ny < self.image_size:
                    self.image_data[ny, nx] = 255 # Set pixel to white (0-255 grayscale)

    def stop_draw(self, event):
        self.drawing_active = False

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image_data = np.zeros((self.image_size, self.image_size), dtype=np.uint8)
        self.mnist_data_output = None

    def confirm_and_infer(self):
        if np.sum(self.image_data) == 0: # Check if canvas is empty
            messagebox.showwarning("No Drawing", "Please draw a digit before confirming.")
            return

        # Convert the numpy array to a PIL Image (28x28 grayscale)
        pil_image = Image.fromarray(self.image_data)
        self.result_image = pil_image.convert("L") # Ensure it's L (grayscale)

        # Apply transformations for inference
        input_tensor = self.inference_transform(self.result_image)
        input_tensor = input_tensor.unsqueeze(0).to(device) # Add batch dimension and move to device

        # Perform inference
        with torch.no_grad():
            output = self.model(input_tensor)
            _, predicted = torch.max(output.data, 1)
            inferred_digit = predicted.item()

        self.inferred_digit_label.config(text=f"Inferred Digit: {inferred_digit}")
        #print(f"Inferred Digit: {inferred_digit}") # Print inference in console (debugging)
        #messagebox.showinfo("Inference Result", f"The model inferred: {inferred_digit}") # Show a pop up window with the inference

    def cancel_input(self):
        self.result_image = None
        self.mnist_data_output = None
        print("Input cancelled.")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MNISTDrawer(root)
    root.mainloop()