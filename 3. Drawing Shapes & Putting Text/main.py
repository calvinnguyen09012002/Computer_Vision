import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')

# 1. Paint the image a certain colour
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green', blank)

# 2. Draw a Rectangle
#cv.rectangle(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2), (255,0,0), thickness=2)
#cv.imshow('Rectangle', blank)

# 3. Draw a Rectangle
#cv.circle(blank, (blank.shape[0]//2,blank.shape[1]//2), 40, (255,0,0), thickness=-1)
#cv.imshow('Circle', blank)

# 4. Draw a line
#cv.line(blank,(100,250), (300, 400), (0,255,0), thickness=3)
#cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Phuc <3', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),thickness=2)
cv.imshow('TEXT', blank)
cv.waitKey(0)