import cv2 as cv
import numpy as np
img=cv.imread('Photos/women.webp')
cv.imshow('women',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#canny image:
canny=cv.Canny(gray,150,175)
cv.imshow('canny',canny)

#Laplacian Method: for edge detection, returns kind of pencile shading sort of img
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

#Sobel Method
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('sobel x',sobelx)
cv.imshow('sobel Y',sobely)
#combining sobel x and sobel y
combined_sobel=cv.bitwise_and(sobelx,sobely)
cv.imshow('combined img',combined_sobel)
 
cv.waitKey(0)