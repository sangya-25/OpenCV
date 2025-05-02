import cv2 as cv
import numpy as np
blank = np.zeros((700,700,3),dtype='uint8')
cv.imshow('Blank',blank)
#to paint the image some colour
blank[:]=0,255,0
cv.imshow('Green',blank) # a green blank frame
blank[200:300,300:400]=0,0,255
cv.imshow('red',blank) # a green blank frame with another frame of certain range
# to draw rectangles:
cv.rectangle(blank,(0,0),(350,300),(255,0,0),thickness=2  )
cv.imshow("rectangle",blank)
#filled rectangle
cv.rectangle(blank,(50,50),(250,500),(250,255,0),thickness=cv.FILLED)
cv.imshow("coloured rectangle",blank)
#to draw a circle:
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 100 , (255,0,255),thickness=-1)
cv.imshow("circle",blank)
#to draw a line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('line',blank)
#to write any text on the image
cv.putText(blank,"Hello, I'm Sangya Ojha",(170,350),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),2,cv.LINE_8)
cv.imshow('text',blank)
cv.waitKey(0)