import cv2 as cv
img=cv.imread('Photos/group3.jpg')
cv.imshow('image',img)

#convert the coloured image into gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_scaled image',gray)

#to read haarcased (.xml) file and store it into an varibale(here, haar_cascade)
haar_cascade=cv.CascadeClassifier('haar_face.xml')

#the method detectMultiScale use to read an image and detect the rectangular coordinates and return it to the faces_rect variable as a list
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=6)

#print the no of faces found in the img by print the length of the list obtained
print(f'Number of faces found : {len(faces_rect)}')
print(faces_rect) #will return the coordinates of around the img

#we can now use the list we have obtain that contains the rectangular coordinate of the faces which we can perform loop over the edges to draw a rectangular frame
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('rectangular frame',img)

#detect edges of the image using 
cv.waitKey(0)