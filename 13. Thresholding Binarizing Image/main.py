import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img = cv.imread('0. Photos\Cat.jpg')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Simple thresholding
# ret, thresh1 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# ret, thresh2 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)

# titles = ['Original Image','Binary' , 'Binary_INV']
# images = [gray, thresh1, thresh2]

# for i in range(3):
#     plt.subplot(1, 3, i+1), plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

# Adaptive thresholding
'''
Thuật toán simple thresholding hoạt động khá tốt.
Tuy nhiên, nó có 1 nhược điểm là giá trị ngưỡng bị/được gán toàn cục.
Thực tế khi chụp, hình ảnh chúng ta nhận được thường bị ảnh hưởng của nhiễu,
 ví dụ như là bị phơi sáng, bị đèn flask, …

Một trong những cách được sử dụng để giải quyết vấn đề trên
là chia nhỏ bức ảnh thành những vùng nhỏ (region),
và đặt giá trị ngưỡng trên những vùng nhỏ đó
-> adaptive thresholding ra đời.

'''
img = cv.imread('0. Photos\Page.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
th1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,5)
cv.imshow('Adaptive Threshold GAUSSIAN', th1)
th2 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,5)
cv.imshow('Adaptive Threshold MEAN', th2)

cv.waitKey(0)