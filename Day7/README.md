

### **Day 7 - Real-Time Face Detection with OpenCV**  
This is part of my **#100DaysOfAI** challenge.  
On **Day 7**, I built a real-time face detection system using **OpenCV** and **Haar Cascade Classifier** to detect faces from a webcam feed.

---

###  **Goal**  
Detect human faces in real-time from live webcam input.

---

### **Technologies Used**

| Tool        | Purpose                      |
|-------------|------------------------------|
| Python      | Main programming language    |
| OpenCV      | Computer vision library      |
| Haar Cascades | Pre-trained face detection model |
| VS Code     | Code editor                  |

---

###  **Dataset / Input**  
- **Live webcam feed** (no static dataset used)  
- Haar cascade XML file: `haarcascade_frontalface_default.xml` (pre-trained model provided by OpenCV)

---

###  **How It Works**

1. Loaded the **Haar Cascade Classifier** provided by OpenCV for frontal face detection.
2. Accessed the **webcam** using `cv2.VideoCapture(0)`.
3. Processed each frame:
   - Converted it to **grayscale** for better performance.
   - Applied the face detector to identify bounding boxes for all detected faces.
4. Drew **blue rectangles** around detected faces in real time.
5. Displayed the output in a window that updates continuously.
6. Pressing `'q'` exits the webcam window.

---

###  **Highlights**

- Implemented **real-time computer vision** from scratch.
- Used **Haar Cascades** for face detection — lightweight and fast.
- Learned how to process frames continuously using OpenCV.

---

###  **What I Learned**

- How to use **OpenCV** for face detection with webcam input.
- How Haar Cascades detect visual patterns (like human faces).
- Real-time image processing with OpenCV.
- Frame-by-frame operations and key event handling in Python.

---

