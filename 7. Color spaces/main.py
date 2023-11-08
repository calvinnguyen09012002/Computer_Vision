import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('0. Photos\SaiGon.jpg')
cv.imshow('img', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv --> bgr', hsv_bgr)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)