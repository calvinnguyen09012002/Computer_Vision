import cv2 as cv

img = cv.imread('0. Photos\Cat 2.jpg')
cv.imshow('Cat',img)

# Average
average = cv.blur(img, (7,7))
cv.imshow('average',average)

# Gaussian Blur -> lọc nhiễu hoặc nhiễu muối tiêu (salt and pepper), 
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian', gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

#Bilateral -> làm mịn mà vẫn giữ lại được biên của ảnh
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)