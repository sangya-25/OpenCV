import cv2 as cv
def rescaleFrame(frame, scale=0.45): # a function to rescale the original video/image
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
  
img=cv.imread('Photos/ronaldo.jpg')
image_resize=rescaleFrame(img)
#original image without scaling
cv.imshow('ronaldo',img)
#image with scaling/ resized image 
cv.imshow('image',image_resize)

capture=cv.VideoCapture('Videos/vid1.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame)
    # cv.imshow('Video',frame)
    cv.imshow('video resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):  # i.e if the letter d is pressed break the loop and stop the video display
        break
capture.release()
cv.destroyAllWindows()
