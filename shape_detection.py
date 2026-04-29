import cv2  # Import OpenCV library for image processing

# Read the image from the current folder
# Make sure "pic.png" exists in the same directory as this Python file
img = cv2.imread("pic.png")

# Convert the image from BGR color format to grayscale
# Contour detection usually works better on grayscale/binary images
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
# Pixels greater than 200 become 255 white
# Pixels less than or equal to 200 become 0 black
#
# _     -> threshold value returned by OpenCV, here 200
# thres -> final binary thresholded image
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
# -1 means draw all contours
#
# Note:
# Since grey_img is grayscale, (0, 255, 0) may not appear as green.
# To see green color properly, draw on original color image instead of grey_img.
cv2.drawContours(grey_img, contours, -1, (0, 255, 0), 3)

# Loop through each detected contour to identify the shape
for contour in contours:

    # Calculate the perimeter/arc length of the contour
    # True means the contour is closed
    perimeter = cv2.arcLength(contour, True)

    # Approximate the contour shape using fewer points
    # 0.01 * perimeter controls approximation accuracy
    # Smaller value = more accurate shape, more points
    # Larger value = less accurate shape, fewer points
    approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)

    # Count the number of corner points in the approximated contour
    corners = len(approx)

    # Identify shape based on number of corners
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"

    # Draw the approximated contour
    # [approx] is used because drawContours expects a list of contours
    # 0 means draw the first contour from the list [approx]
    # 2 is the thickness of the contour line
    cv2.drawContours(grey_img, [approx], 0, (0, 255, 0), 2)

    # Get x and y coordinates from the first point of the approximated contour
    # approx is a multi-dimensional array, so ravel() flattens it
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    # Write the detected shape name near the contour
    # Arguments:
    # 1. grey_img                 -> image on which text is written
    # 2. shape_name               -> text to display
    # 3. (x, y)                   -> text position
    # 4. cv2.FONT_HERSHEY_COMPLEX -> font style
    # 5. 0.6                      -> font scale/size
    # 6. (0, 255, 0)              -> text color
    # 7. 3                        -> text thickness
    cv2.putText(
        grey_img,
        shape_name,
        (x, y),
        cv2.FONT_HERSHEY_COMPLEX,
        0.6,
        (0, 255, 0),
        3
    )

# Show the final image with contours and shape names
cv2.imshow("Contours", grey_img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()