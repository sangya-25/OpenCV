import cv2 as cv
import numpy as np
img=cv.imread('Photos/person.jpg')
cv.imshow('person',img)
#image translation: 
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])  #width,height
    return cv.warpAffine(img,transMat,dimensions)
# -x(negative value of x) ----> shifts left , else right
# -y(negative value of y) ----> shifts up, else down
translate=translate(img,100,100)
cv.imshow('translated',translate)

#to rotate the img:
def rotate(img, angle, rotPoint=None):
    (height , width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,180)  #rotoates the img by 180 degree
rotated_rotate=rotate(rotated,180)
cv.imshow('rotated',rotated)
cv.imshow('rotated_rotate',rotated_rotate)#this will now return the original image angle(0 deg) due to 180-180 degrees
resize=cv.resize(img,(700,500),interpolation=cv.INTER_CUBIC)  # cubic for high quality image
cv.imshow('resize',resize)

#to flip an image
flip=cv.flip(img,flipCode=-1)  #flips the img vertically, 1 --> flips the img horizontally and -1 --->flips the img both vertically and horizontally
cv.imshow('flip',flip)

cv.waitKey(0)