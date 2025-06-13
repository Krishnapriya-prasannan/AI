#   Image Classification with ResNet50 (or MobileNet)

This project is part of my **#100DaysOfAI** challenge. On **Day 2**, I built an image classifier using deep learning models (ResNet50 or MobileNet) from TensorFlow Keras. The model takes an image as input and predicts its class based on the ImageNet dataset.

---

##  Project Goal

- Understand the basics of image classification using Convolutional Neural Networks (CNNs)
- Learn how to use pre-trained models like **ResNet50** and **MobileNet**
- Explore how models trained on ImageNet can classify real-world images
- Practice image preprocessing, prediction, and displaying results using OpenCV

---

## Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python       | Main programming language |
| TensorFlow / Keras | Deep learning framework and pre-trained models |
| NumPy        | Numerical operations on image data |
| OpenCV       | Display image and overlay predicted label |
| ImageNet     | Dataset used for model pre-training |
| VS Code      | Code editor |

---

##  How It Works

1. Load a pre-trained model (either **ResNet50** or **MobileNet**) with ImageNet weights.
2. Load an input image and resize it to `224x224` (model requirement).
3. Convert the image to a NumPy array and preprocess it using the model-specific `preprocess_input()` function.
4. Pass the image to the model and get predictions.
5. Use `decode_predictions()` to convert model output into human-readable labels.
6. Display the image using OpenCV with the top prediction label overlayed.

---

## Model Info

| Model     | Description |
|-----------|-------------|
| **ResNet50** | 50-layer deep CNN, high accuracy, slower, better for high-performance environments |
| **MobileNet** | Lightweight and fast, optimized for mobile and edge devices |
