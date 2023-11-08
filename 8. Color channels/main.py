import cv2 as cv
import numpy as np

img = cv.imread('0. Photos\BGR.jpg')

resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized',resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')

b,g,r = cv.split(resized) #lưu vị trí

blue = cv.merge([r,b,g]) #nếu 3 thông số cùng là b hay cùng r hay cùng g thì ở vị trí tương ứng màu trắng

cv.imshow("blue",blue)

print(resized.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)