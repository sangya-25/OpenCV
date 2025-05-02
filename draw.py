import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
#to paint the image some colour
blank[:]=0,255,0
cv.imshow('Green',blank) # a green blank frame
blank[200:300,300:400]=0,0,255
cv.imshow('red',blank) # a green blank frame with another frame of certain range
# to draw rectangles:
cv.waitKey(0)