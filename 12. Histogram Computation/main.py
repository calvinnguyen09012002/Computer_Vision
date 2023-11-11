import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('0. Photos\Cat.jpg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('the number of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('the number of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)