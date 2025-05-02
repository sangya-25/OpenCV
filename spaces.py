import cv2 as cv
import matplotlib .pyplot as plt
img=cv.imread('Photos/person.jpg')
cv.imshow('person',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray scale',gray)
#BGR to HSV colour space
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv image',hsv)
#BGR to Lab color space
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

plt.imshow(img)  # to display the img in matplotlib with by default RGB color space
plt.show()
 
#BGR to RGB color space
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
#plotting rgb images into matplotlib which will convert it into again bgr(due to color inversion)
plt.imshow(rgb)
plt.show()

#from HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr',hsv_bgr)
#from LAB to BGR
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('lab to bgr',lab_bgr)
cv.waitKey(0)