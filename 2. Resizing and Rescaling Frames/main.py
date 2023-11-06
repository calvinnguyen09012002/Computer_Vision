import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

#Reading Photos
img = cv.imread('Photos/Cat.jpg')
cv.imshow('Cat',img)

cv.waitKey(0)
resized_image =  rescaleFrame(img, scale = 0.2)
cv.imshow = ('Image', resized_image)

cv.waitKey(0)
#Reading Videos
capture = cv.VideoCapture('Videos/Dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = 0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

