import cv2
from ultralytics import YOLO
#from google.colab.patches import cv2_imshow  # Use cv2_imshow for displaying images in Colab
import numpy as np

# Load the YOLOv8 model
model = YOLO("/content/drive/MyDrive/Bitirme Projesi/train1_29-5-epocks50-yolov8n-best.pt")  # Update with the path to your trained model

# Open the video file
video_path = "/content/drive/MyDrive/beeTest.mp4"  # Update with the path to your video file
cap = cv2.VideoCapture(video_path)

# Get video details
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create a VideoWriter object to save the output video
output_path = "/content/drive/MyDrive/epocks50-yolov8n-best.mp4"  # Update with the path to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 file
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection on the frame
    results = model(frame)

    # Annotate the frame
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"
            # Draw the box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Put the label
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Write the annotated frame to the output video
    out.write(frame)

    # Display the frame with detections (optional)
    #cv2_imshow(frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()
