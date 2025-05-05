import numpy as np
import cv2 as cv

haar_cascade=cv.CascadeClassifier('haar_face.xml')
 
 #from the trained model fetching features(faces) and labels(names) 
people=['sangya','Virat Kohli']
# features=np.load('features.npy',allow_pickel=True)
# labels=np.load('labels.npy')

face_recognixer=cv.face.LBPHFaceRecognizer_create()
face_recognixer.read('face_trained.yml')

img=cv.imread('Photos/virat2.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#First we gonna detect the face
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
for(x,y,w,h) in faces_rect:
    face_roi=gray[y:y+h,x:x+h]
    label, confidence=face_recognixer.predict(face_roi)
    print(f'Label={people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (30,30),cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,0), thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected Face',img)
cv.waitKey(0)
