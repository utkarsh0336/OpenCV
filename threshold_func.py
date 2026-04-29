import cv2  # Import OpenCV library for image processing

# Read the image in grayscale mode
# cv2.IMREAD_GRAYSCALE converts the image into black-and-white format
# Thresholding usually works on grayscale images
img = cv2.imread("pic.png", cv2.IMREAD_GRAYSCALE)

# Apply binary thresholding
# Arguments:
# 1. img              -> input grayscale image
# 2. 120              -> threshold value
# 3. 255              -> maximum value assigned to pixels above threshold
# 4. cv2.THRESH_BINARY -> thresholding type
#
# Rule:
# If pixel value > 120, it becomes 255 (white)
# If pixel value <= 120, it becomes 0 (black)
#
# ret        -> stores the threshold value used, here 120
# thresh_img -> stores the final thresholded image
ret, thresh_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

# Show the original grayscale image
cv2.imshow("Original Image", img)

# Show the thresholded black-and-white image
cv2.imshow("Thresholded Value", thresh_img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()