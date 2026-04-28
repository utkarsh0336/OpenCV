import cv2  # Import OpenCV library for image processing

# Read the image from the current folder
# Make sure "pic.png" exists in the same directory as this Python file
img = cv2.imread("pic.png")

# Apply Gaussian Blur to the image
# Arguments:
# 1. img      -> input image
# 2. (7, 7)   -> kernel size; must be odd numbers like (3,3), (5,5), (7,7)
# 3. 3        -> sigmaX; controls how strong/smooth the blur is in X direction
blurred = cv2.GaussianBlur(img, (7, 7), 3)

# Show the original image in a window
cv2.imshow("Original image", img)

# Show the blurred image in another window
cv2.imshow("Blurred image", blurred)

# Wait indefinitely until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()