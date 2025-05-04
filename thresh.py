import cv2 as cv
img = cv.imread('Photos/ronaldo2.jpg')
cv.imshow('person',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Simple Thresholding;
threshold_value, thresh=cv.threshold(gray,120,255,cv.THRESH_BINARY)
cv.imshow('thresholded img',thresh)

#thresh inverse:
threshold_value, thresh_inv=cv.threshold(gray,120,255,cv.THRESH_BINARY_INV)
cv.imshow('thresholded inverse img',thresh_inv)

#Adatptive Thresholding: it finds the optimal thresholded value by itself instead of hardcoded value
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
adaptive_thresh_img=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,7,0)
cv.imshow('adaptive thresholded',adaptive_thresh)
cv.imshow('adaptive',adaptive_thresh_img)


cv.waitKey(0)
 