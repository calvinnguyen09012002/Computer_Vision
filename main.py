#Tổng Quan Không Gian Màu trong OpenCV
import cv2 as cv

path = r'C:\Visual Studio Code\Computer_Vision\Bai3\RGB.png'

img = cv.imread(path)

B, G, R = cv.split(img)

cv.imshow('original',img)
cv.imshow('blue',B)
cv.imshow('green',G)
cv.imshow('red',R)

cv.waitKey(0)
cv.destroyWindow()