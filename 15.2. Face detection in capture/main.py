import cv2 as cv
import numpy as np

face_classifier = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Video Face detection', frame)

    k=  cv.waitKey(1) & 0xFF
    if k==27:
        break

cap.release()
cv.destroyAllWindows()




