import cv2 as cv
import numpy as np
img=cv.imread('Photos/ronaldo2.jpg')
cv.imshow('person',img)
blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)  #it splits the image into blue, green and red color channel
# cv.imshow('blue',b)  #depicts the img into grayscale with intensity low for those areas having this specific color pixel
# cv.imshow('green',g)
# cv.imshow('red',r)

print(img.shape) #(1053, 805, 3) here 3 represents the 3 color channel
print(b.shape)
print(g.shape)
print(r.shape)

merge=cv.merge([b,g,r])  # will merge the images with all these b,g,r colour channels ----> original img
cv.imshow('merged',merge)

blue=cv.merge([b,blank,blank]) # it will only display the blue color channel and will keep blank for the other channels(green and red)
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

cv.waitKey(0)
