import cv2  # Import OpenCV library for image processing

# Read the image from the current folder
# Make sure "pic.png" exists in the same directory as this Python file
img = cv2.imread("pic.png")

# Convert the image from BGR color format to grayscale
# Contour detection usually works on binary/grayscale images
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
# Pixels greater than 200 become 255 white
# Pixels less than or equal to 200 become 0 black
#
# _     -> stores threshold value returned by OpenCV, here 200
# thres -> stores the final binary thresholded image
_, thres = cv2.threshold(grey_img, 200, 255, cv2.THRESH_BINARY)

# Find contours from the thresholded image
# contours  -> list of detected object boundaries
# hierarchy -> relationship between contours, such as parent/child contours
#
# cv2.RETR_TREE retrieves all contours and builds full hierarchy
# cv2.CHAIN_APPROX_SIMPLE removes unnecessary points and keeps only important boundary points
contours, hierarchy = cv2.findContours(
    thres,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw all detected contours on the grayscale image
# Arguments:
# 1. grey_img     -> image on which contours will be drawn
# 2. contours     -> list of contours found
# 3. -1           -> draw all contours
# 4. (0,255,0)    -> contour color; green in BGR
# 5. 3            -> contour thickness
#
# Note:
# Since grey_img is grayscale, the color tuple may not show as green.
# To see green contours, draw on the original color image instead of grey_img.
cv2.drawContours(grey_img, contours, -1, (0, 255, 0), 3)

# Show the image with contours
cv2.imshow("Contours", grey_img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()