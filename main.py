import cv2

image = cv2.imread("./pic.png")

if image is None:
    print("Error Loading the image")

grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

name = input("Enter the name of the image to be saved in grey scale: ")

cv2.imwrite(name,grey_img)

print(grey_img.shape)

cv2.imshow("Bubu",grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()