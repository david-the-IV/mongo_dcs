import cv2
import os
import time

# Configuration
rtsp_url = "rtsp://admin:DDFDYF@192.168.170.49:554/H.264"  # Replace with your RTSP URL
save_directory = "/app/img"  # Directory to save images

# Create directory if it doesn't exist
# if not os.path.exists(save_directory):
#     os.makedirs(save_directory)
os.makedirs(save_directory, exist_ok=True)

# Start capturing from the RTSP stream

try:
    while True:
        # Wait for user input to capture an image
        input("Press Enter to capture an image...")

        # Capture frame-by-frame
        cap = cv2.VideoCapture(rtsp_url)
        
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture image.")
            break
        
        # Generate filename based on the current time
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(save_directory, f"image_{timestamp}.jpg")
        
        # Save the captured image
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")

except KeyboardInterrupt:
    print("Image capture stopped.")

finally:
    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()
