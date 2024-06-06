import cv2
import numpy as np

img = cv2.imread('test5.png')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
blur = cv2.medianBlur(gray, 3)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=90, param2=90, minRadius=30, maxRadius=100)
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        print(r)

cv2.imshow("Image1", blur)
cv2.imshow("Image", img)
cv2.waitKey(0)