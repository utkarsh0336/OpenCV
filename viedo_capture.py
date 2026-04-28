import cv2  # Import OpenCV library for camera, image, and video processing

# Open the default webcam
# 0 means the primary/default camera of your laptop
camera = cv2.VideoCapture(0)

# Start an infinite loop to continuously read frames from the webcam
while True:
    # Read one frame from the camera
    # ret = True/False, tells whether frame was successfully captured
    # frame = actual image/frame captured from webcam
    ret, frame = camera.read()

    # If frame is not captured properly, stop the loop
    if not ret:
        print("Could not read frame")
        break

    # Display the current frame in a window named "Webcam Feed"
    cv2.imshow("Webcam Feed", frame)

    # cv2.waitKey(1) waits 1 millisecond for a key press
    # 0xFF extracts the last 8 bits of the key code
    # ord('q') gives ASCII value of 'q'
    # If user presses 'q', exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

# Release the webcam so other apps can use it
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()