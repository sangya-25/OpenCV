import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('Photos/eye.jpg')
cv.imshow('ronaldo',img)
blank=np.zeros(img.shape[:2],dtype='uint8')

# gray_scale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray_image',gray_scale)

#creating a masked image
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked_img',masked)

#GrayScale Histogram :it represents the distribution of pixel intesitites in an image
# gray_hist=cv.calcHist([gray_scale],[0],mask,[256],[0,256])
plt.figure()
plt.title('Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#Colored Histogram
colors=('b','g','r')
for i, col in enumerate(colors):  #to draw histogram for each colour channel i.e (r, g and b)
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)
