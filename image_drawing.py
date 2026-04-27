import cv2


file_loc = input("Give me the file location : ")

img = cv2.imread(file_loc)

choice = int(input('''
        Type 0 if you want to make a line.
        Type 1 if you want to make a rectangle.
        Type 2 if you want to make a circle.
        Type 3 if you want to write a text.
'''))

if choice == 0:
# cv2.line() is used to draw a straight line on an image.

# Syntax
# cv2.line(image, pt1, pt2, color, thickness)
# Arguments
# cv2.line(img, (x1, y1), (x2, y2), (B, G, R), thickness)
# Argument	Meaning
# img	Image on which line is drawn
# pt1	Starting point: (x1, y1)
# pt2	Ending point: (x2, y2)
# color	Line color in BGR, not RGB
# thickness	Thickness of line in pixels

    x1 = int(input("Give the x corrdinate of point 1 : "))
    y1 = int(input("Give the y corrdinate of point 1 : "))

    x2 = int(input("Give the x corrdinate of point 2 : "))
    y2 = int(input("Give the y corrdinate of point 2 : "))

    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),-1)
    cv2.imshow("Image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
if choice == 1:

# cv2.rectangle() is used to draw a rectangle on an image.

# Syntax
# cv2.rectangle(image, pt1, pt2, color, thickness)
# Arguments
# cv2.rectangle(img, (x1, y1), (x2, y2), (B, G, R), thickness)
# Argument	Meaning
# img	Image on which rectangle is drawn
# pt1	Top-left corner: (x1, y1)
# pt2	Bottom-right corner: (x2, y2)
# color	Rectangle color in BGR, not RGB
# thickness	Border thickness in pixels

    x1 = int(input("Give the x corrdinate of top-left corner : "))
    y1 = int(input("Give the y corrdinate of top-left corner : "))

    x2 = int(input("Give the x corrdinate of bottom-right corner : "))
    y2 = int(input("Give the y corrdinate of bottom-right corner : "))

    cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0))
    cv2.imshow("Image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if choice == 2:
# cv2.circle() is used to draw a circle on an image.

# Syntax
# cv2.circle(image, center, radius, color, thickness)
# Arguments
# cv2.circle(img, (x, y), radius, (B, G, R), thickness)
# Argument	Meaning
# img	Image on which circle is drawn
# center	Center point of circle: (x, y)
# radius	Radius of circle in pixels
# color	Circle color in BGR, not RGB
# thickness	Border thickness in pixels

    x = int(input("Give me the x coordinate of the center : "))
    y = int(input("Give me the y coordinate of the center : "))

    r = int(input("Give me the radius of the circle : "))

    fill = int(input("Type 1 if you want to fill the circle else Type 0 : "))
    filling = -1 if fill == 1 else 0

    cv2.circle(img,(500,500),200,(0,0,255),filling)

    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if choice == 3:
# cv2.putText()

# It is used to write text on an image.

# Syntax
# cv2.putText(image, text, org, fontFace, fontScale, color, thickness)
# Arguments
# cv2.putText(img, "Hello", (x, y), font, fontScale, (B, G, R), thickness)
# Argument	Meaning
# img	Image on which text is written
# text	Text string to display
# org	Bottom-left position of text: (x, y)
# fontFace	Font style
# fontScale	Size of the text
# color	Text color in BGR
# thickness	Thickness of text
    text = input("Enter the text you want to show : ")
    x = int(input("Give the x coordinate of the bottom-left corner : "))
    y = int(input("Give the y coordinate of the bottom-left corner : "))

    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(155,240,134))

    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()