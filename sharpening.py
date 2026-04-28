import cv2              # Import OpenCV for image processing
import numpy as np      # Import NumPy to create the sharpening kernel matrix

# Read the image from the current folder
# Make sure "pic.png" exists in the same directory as this Python file
img = cv2.imread("pic.png")

# Create a sharpening kernel/filter
# This kernel increases the importance of the center pixel
# and subtracts nearby surrounding pixels, making edges/details sharper
sharpen_kernel = np.array([
    [0, -1,  0],
    [-1, 5, -1],
    [0, -1,  0]
])

# Apply the sharpening filter to the image
# Arguments:
# 1. img             -> input image
# 2. -1              -> output image depth same as input image
# 3. sharpen_kernel  -> filter/kernel to apply
sharpened_img = cv2.filter2D(img, -1, sharpen_kernel)

# Show the original image
cv2.imshow("Original Image", img)

# Show the sharpened image
cv2.imshow("Sharpen Image", sharpened_img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()