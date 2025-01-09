import cv2
import os
import time

# Directory where images will be saved
image_directory = '/home/ubuntu/img'

# Ensure the directory exists
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# Initialize video capture object
cap = cv2.VideoCapture('rtsp://192.168.43.182:8080/h264.sdp')

# Check if the video capture is opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Set frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Time tracking for capturing images
last_capture_time = time.time()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame.")
        break
    
    # Display the video frame
    cv2.imshow("Capturing", frame)

    # Capture an image every 5 seconds
    current_time = time.time()
    if current_time - last_capture_time >= 5:
        # Capture the image
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime(current_time))
        image_filename = f"{image_directory}/image_{timestamp}.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Image saved as {image_filename}")
        
        # Update last capture time
        last_capture_time = current_time

    # Exit condition: Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
