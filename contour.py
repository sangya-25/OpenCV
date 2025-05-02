import cv2 as cv
import numpy as np
img=cv.imread('Photos/lion.jpg')
cv.imshow('lion',img)
blank=np.zeros(img.shape, dtype='uint8')
cv.imshow('blank',blank)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
cv.imshow('gray scaled image',gray)
blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)
ret, thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#it return two things
# first the contour i,e a python list with all the coordinate points of contour present in the frame
# second the hierarchy: hierarchial configuration of contours in the img
print(f'{len(contours)} contour(s) found!')

#drawing contours on a blank img
cv.drawContours(blank,contours,-1,(255,0,0),1)  
#will draw contours with the same coordinates as of lion.jpg img using blue colour with thickness of 2 , -1 shows that to draw all contours from the contour set
cv.imshow('draw_contoured',blank)
cv.waitKey(0)