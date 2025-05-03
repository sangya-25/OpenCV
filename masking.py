import cv2 as cv
import numpy as np
img=cv.imread('Photos/women.webp')
cv.imshow('person',img)
blank=np.zeros(img.shape[:2],dtype='uint8')

#creating a circle over the blank img and considering it as a mask
mask=cv.circle(blank,(img.shape[1]//2,230),135,255,-1)
cv.imshow('masking',mask)
print(img.shape[1]//2)
masked_img=cv.bitwise_and(img,img,mask=mask) 
cv.imshow('masked_image',masked_img)

#weird shape masked image (using bitwise operators)
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2-30),140,255,-1)
rectangle=cv.rectangle(blank.copy(),(50,30),(440,200),255,-1)
weird_shape=cv.bitwise_and(rectangle,circle)
masking=cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('new_masking',masking)
cv.waitKey(0)