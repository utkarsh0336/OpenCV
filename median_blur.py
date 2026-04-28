import cv2  # Import OpenCV library for image processing

# Read the image from the current folder
# Make sure "pic.png" exists in the same directory as this Python file
img = cv2.imread("pic.png")

# Apply Median Blur to the image
# Arguments:
# 1. img -> input image
# 2. 5   -> kernel size
# Kernel size must be an odd number greater than 1, like 3, 5, 7, 9
blurred = cv2.medianBlur(img, 5)

# Show the original image in a window
cv2.imshow("Original Image", img)

# Show the median blurred image in another window
cv2.imshow("Median Blur", blurred)

# Wait indefinitely until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()