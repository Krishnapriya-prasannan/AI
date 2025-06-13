
### ** AI for Real-Time Object Detection (YOLOv5)**  
 I implemented a **real-time object detection system** using the powerful **YOLOv5** (You Only Look Once v5) architecture. This model detects multiple objects in a single frame with high speed and accuracy.

---

### **Goal**  
To perform **real-time object detection** using a **pre-trained YOLOv5 model**, identifying multiple objects simultaneously from a live webcam feed.

---

### **Technologies Used**

| Tool/Library     | Purpose                                              |
|------------------|-------------------------------------------------------|
| Python           | Core programming language                            |
| PyTorch          | Deep learning framework for loading YOLOv5 model     |
| OpenCV           | Capturing webcam feed and drawing bounding boxes     |
| YOLOv5           | Real-time object detection (via Ultralytics repo)    |
| COCO Dataset     | Pre-trained model weights based on this dataset      |

---

### **How It Works**

1. **Install YOLOv5**
   - Cloned the official [Ultralytics YOLOv5 GitHub repo](https://github.com/ultralytics/yolov5)
   - Installed dependencies using `requirements.txt`

2. **Load the Pre-trained Model**
   - Used YOLOv5s (small) model with weights trained on the **COCO** dataset.
   - The model can detect 80 common objects (like person, car, dog, bottle, etc.)

3. **Capture Webcam Feed**
   - OpenCV is used to access the webcam stream in real-time.

4. **Detect and Annotate Objects**
   - Each frame is passed through the YOLO model.
   - The model returns bounding boxes, labels, and confidence scores.
   - Results are drawn live on the video feed.

5. **Display Results**
   - Live video feed is displayed with bounding boxes and labels for detected objects.

---

### **Highlights**

- Integrated **state-of-the-art object detection model** into a real-time application.
- Used **YOLOv5s** model for fast inference while maintaining good accuracy.
- Reinforced concepts of **model inference**, **image processing**, and **bounding box visualization**.
- Detected multiple object types (like people, chairs, laptops) from webcam input.

---

### **What I Learned**

- How to load and use **pre-trained object detection models** with PyTorch.
- Capturing and processing **live video frames** using OpenCV.
- Applying YOLO’s **confidence thresholds and non-max suppression** for better predictions.
- Real-world uses of object detection in **surveillance**, **retail analytics**, **robotics**, and **autonomous vehicles**.
- Hands-on with the **Ultralytics YOLOv5 pipeline**, which makes deploying object detection simpler.



