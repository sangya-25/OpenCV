import cv2 as cv
img=cv.imread('Photos/ronaldo2.jpg')
cv.imshow('ronanldo',img)
#converting BGR images into grayscale images
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
img2=cv.imread('Photos/lion.jpg')
gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow('gray scale image',gray2)

#how to blur an image
img3=cv.imread('Photos/eye.jpg')
blur=cv.GaussianBlur(img3,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blurred img',blur)

#Edge cascade:
canny=cv.Canny(blur,50,175)
cv.imshow('canny',canny)

#Dilating the image
dilated=cv.dilate(canny,(11,11),iterations=7)
cv.imshow('dilated',dilated)

#eroding
eroded=cv.erode(dilated,(13,13),iterations=1)
cv.imshow('eroded',eroded)

#resize:
resized=cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow('resize',resized)

#cropping images
crop=img[10:500,100:900]
cv.imshow('cropped',crop)
cv.waitKey(0)
