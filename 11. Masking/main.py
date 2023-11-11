import cv2 as cv
import numpy as np

img = cv.imread('0. Photos\Balloon.jpg')
cv.imshow('balloon', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[0]//2 + 28, img.shape[1]//2), 28, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img,img, mask=mask)
cv.imshow('masked image', masked)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()