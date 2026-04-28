import cv2  # Import OpenCV library for image processing

# Read the image in grayscale mode
# cv2.IMREAD_GRAYSCALE converts the image into black-and-white format
# Canny edge detection usually works on grayscale images
img = cv2.imread("pic.png", cv2.IMREAD_GRAYSCALE)

# Apply Canny Edge Detection
# Arguments:
# 1. img -> input grayscale image
# 2. 50  -> lower threshold
# 3. 150 -> upper threshold
#
# Pixels with gradient value above 150 are considered strong edges
# Pixels below 50 are rejected
# Pixels between 50 and 150 are kept only if connected to strong edges
edge_detection_img = cv2.Canny(img, 50, 150)

# Show the original grayscale image
cv2.imshow("Original image", img)

# Show the edge-detected image
cv2.imshow("Edged-Image", edge_detection_img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()