

import torch
import cv2

# Load YOLOv5s model from ultralytics (pretrained on COCO)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Set confidence threshold (optional)
model.conf = 0.5  # Confidence threshold
model.iou = 0.45  # IoU threshold for NMS

# Start video capture from webcam (0 is default camera)
cap = cv2.VideoCapture(0)

# Set custom resolution if needed (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Press 'q' to exit the webcam window...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    # Convert BGR to RGB (YOLOv5 expects RGB input)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Inference with YOLOv5
    results = model(img)

    # Render detections
    annotated_frame = results.render()[0]  # Get annotated image
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

    # Display the frame
    cv2.imshow('YOLOv5 Real-Time Object Detection', annotated_frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
