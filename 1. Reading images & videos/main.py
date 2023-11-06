import cv2 as cv

#Reading Photos
#img = cv.imread('Photos/Cat.jpg')

#cv.imshow('Cat',img)

#cv.waitKey(0)

#Reading Videos
capture = cv.VideoCapture('Videos/Dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


