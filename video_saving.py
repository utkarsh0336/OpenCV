import cv2  # Import OpenCV library for camera/video processing

# Open the default webcam
# 0 means primary/default camera
camera = cv2.VideoCapture(0)

# Get the width and height of frames captured by the camera
# camera.get() returns float values, so we convert them to int
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the video codec
# XVID is commonly used for .avi video files
codec = cv2.VideoWriter_fourcc(*'XVID')

# Create a VideoWriter object to save the recorded video
# Arguments:
# 1. Output file name
# 2. Codec
# 3. Frames per second
# 4. Frame size as (width, height)

recorder = cv2.VideoWriter(
    "my_video.avi",
    codec,
    20,
    (frame_width, frame_height)
)

# Start an infinite loop to continuously capture video frames
while True:
    # Read one frame from the webcam
    # success = True/False, tells whether frame was captured successfully
    # frame = actual image/frame captured from webcam
    success, frame = camera.read()

    # If frame is not captured properly, stop recording
    if not success:
        print("Failed to get the frames")
        break

    # Write the current frame into the video file
    recorder.write(frame)

    # Show the live webcam feed while recording
    cv2.imshow("Recording Live 🔴", frame)

    # cv2.waitKey(1) waits 1 millisecond for a key press
    # 0xFF extracts the last 8 bits of the key code
    # ord('q') gives ASCII value of 'q'
    # If user presses 'q', stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

# Release the webcam so other apps can use it
camera.release()

# Release the video recorder
# This is important to properly save/finalize the video file
recorder.release()

# Close all OpenCV windows
cv2.destroyAllWindows()