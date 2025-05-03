import cv2 as cv
img=cv.imread('Photos/eye.jpg')
cv.imshow('eye',img)

#averaging blur method
average=cv.blur(img,(5,5))  # this (3,3) is the kernel size of the window(row * coloumn)
cv.imshow('average',average)

#gaussian blur method
Gaussian_blur=cv.GaussianBlur(img,(5,5),0)
cv.imshow('blur',Gaussian_blur)

#Median Blur
median=cv.medianBlur(img,7)  #openCV itself assumes that the kernel size is 5 by 5
cv.imshow('median_blur',median)

#Bilateral Blur: unlike other blurring methods, it keeps the edges original and preserved and smoothen the img
bb=cv.bilateralFilter(img,20,40,40) # 20 is the diameter, 40 is the sigmaColor i.e the intensity differnce btw the pixels and 
#another 40 is the sigma distance btw pixels
cv.imshow('bilateral',bb)
cv.waitKey(0)