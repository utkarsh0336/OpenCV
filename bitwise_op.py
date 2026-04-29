import cv2              # Import OpenCV for image processing
import numpy as np      # Import NumPy to create blank images/arrays

# Create a black image of size 300x300
# dtype="uint8" means pixel values range from 0 to 255
# 0 represents black
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# Draw a white filled circle on img1
# Arguments:
# 1. img1       -> image on which circle is drawn
# 2. (150,150)  -> center of circle
# 3. 100        -> radius
# 4. 255        -> color white in grayscale
# 5. -1         -> filled circle
cv2.circle(img1, (150, 150), 100, 255, -1)

# Draw a white filled rectangle on img2
# Arguments:
# 1. img2          -> image on which rectangle is drawn
# 2. (100,100)     -> top-left corner
# 3. (250,250)     -> bottom-right corner
# 4. 255           -> color white in grayscale
# 5. -1            -> filled rectangle
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

# Bitwise AND keeps only the common white area between img1 and img2
# Output will be white only where both circle and rectangle overlap
bitwise_and = cv2.bitwise_and(img1, img2)

# Bitwise OR combines white areas from both img1 and img2
# Output will be white wherever either circle or rectangle is white
bitwise_or = cv2.bitwise_or(img1, img2)

# Bitwise NOT inverts img1
# White becomes black, black becomes white
bitwise_not = cv2.bitwise_not(img1)

# Display the first image containing the circle
cv2.imshow("Original Image 1", img1)

# Display the second image containing the rectangle
cv2.imshow("Original Image 2", img2)

# Display the result of bitwise AND
cv2.imshow("Bitwise AND", bitwise_and)

# Display the result of bitwise OR
cv2.imshow("Bitwise OR", bitwise_or)

# Display the result of bitwise NOT
cv2.imshow("Bitwise NOT", bitwise_not)

# Wait until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()