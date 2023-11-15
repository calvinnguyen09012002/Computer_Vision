import cv2 as cv
import numpy as np

haar_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

people = ['Elon Musk', 'Lionel Messi', 'Pham Nhat Vuong']

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face_LBPHFaceRecognizer.create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\Admin\Desktop\Thi giac may\Picture_test\Messi.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    labels, confidence = face_recognizer.predict(faces_roi)
    print(f'Labels = {people[labels]} with a confidence of {confidence}')

    cv.putText(img, str(people[labels]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)
