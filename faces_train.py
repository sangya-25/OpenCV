import os
import cv2 as cv
import numpy as np
people=['sangya','Virat Kohli']
#another way to get the folders name:
# p=[]
# for i in os.listdir(r'C:\Users\ojhas\OneDrive\Desktop\openCV\Faces'):
#     p.append(i)
# print(p)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
DIR=r'C:\Users\ojhas\OneDrive\Desktop\openCV\Faces'
features=[]  #it contains the faces arrays
labels=[]  #it contains the name i.e the label for that correponding face

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        for img in os.listdir(path):  #it will traverse over every images inside the person's folder let say 'sangya'
            img_path=os.path.join(path,img)
            print(img_path)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=15)
            for x,y,w,h in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]  #cropped the image
                features.append(faces_roi)
                labels.append(label)
create_train()
print('Training done-----!')
features=np.array(features, dtype='object')
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()
#Train the recognizer on the features list and labels list
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)



