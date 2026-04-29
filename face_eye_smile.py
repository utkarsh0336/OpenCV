import cv2  # Import OpenCV library for computer vision tasks


# Load Haar Cascade XML files
# These XML files contain pre-trained models for detecting faces, eyes, and smiles
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")


# Open the default webcam
# 0 means primary/default camera
cap = cv2.VideoCapture(0)


# Start an infinite loop to continuously read webcam frames
while True:
    # Read one frame from the webcam
    # ret   -> True if frame is captured successfully
    # frame -> actual image/frame captured from webcam
    ret, frame = cap.read()

    # If frame is not captured properly, stop the loop
    if not ret:
        print("Could not read frame")
        break

    # Convert the frame from BGR to grayscale
    # Haar Cascade detection works better on grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    # Arguments:
    # 1. gray -> input grayscale image
    # 2. 1.1  -> scaleFactor; how much image size is reduced at each scale
    # 3. 5    -> minNeighbors; higher value means fewer but more reliable detections
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Loop through all detected faces
    # x, y -> top-left corner of face rectangle
    # w, h -> width and height of face rectangle
    for (x, y, w, h) in faces:
        # Draw a green rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Create Region of Interest around the detected face
        # We search for eyes and smile only inside the face area
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes inside the face region
        # 1.1 -> scaleFactor
        # 10  -> minNeighbors; higher value reduces false eye detections
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)

        # If at least one eye is detected, write text on frame
        if len(eyes) > 0:
            cv2.putText(
                frame,
                "Eyes Detected",
                (x, y - 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Detect smile inside the face region
        # Smile detection usually needs a higher scaleFactor and minNeighbors
        # to reduce false positives
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)

        # If at least one smile is detected, write text on frame
        if len(smiles) > 0:
            cv2.putText(
                frame,
                "Smile Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Show the final frame with face/eye/smile detection
    # It is better to keep imshow outside the for-loop
    # so the frame is shown even when no face is detected
    cv2.imshow("Smart Frame Detector", frame)

    # Press q to quit the webcam window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break


# Release the webcam so other applications can use it
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()