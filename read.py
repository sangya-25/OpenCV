import cv2 as cv
# to read images
# img=cv.imread('Photos/ronaldo.jpg')
# cv.imshow('dhoni',img)  
# cv.waitKey(0) 
# to read videos 
capture=cv.VideoCapture('Videos/vid1.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):  # i.e if the letter d is pressed break the loop and stop the video display
        break
capture.release()
cv.destroyAllWindows()