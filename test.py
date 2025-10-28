import cv2
from ultralytics import YOLO

# Load the trained model (change path if your model is elsewhere)
model = YOLO("runs/detect/train/weights/best.pt")  # or your custom model path

# Open webcam
cap = cv2.VideoCapture(0)  # 0 is usually the default webcam

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Run YOLOv8 inference on the frame
    results = model.predict(frame, conf=0.5, show=False)

    # Annotate the frame with detection results
    annotated_frame = results[0].plot()

    # Show the annotated frame
    cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
