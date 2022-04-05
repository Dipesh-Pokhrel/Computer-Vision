import cv2
import numpy as np 

## FUNCTION ####

def draw_circle(event,x,y,flag,param):
  if event == cv2.EVENT_LBUTTONDOWN:
    cv2.circle(img,(x,y),100, color=(0,255,0),thickness=-1)
cv2.namedWindow(winname='my_drawing') 
# Connect this function into the image callback
cv2.setMouseCallback('my_drawing',draw_circle)


## SHOWING IMAGE WITH OPENCV ### 

img = np.zeros(shape=(512,512,3),dtype=np.int8)
while True: 
  cv2.imshow('my_drawing',img)
  if cv2.waitKey(20) & 0xFF ==27:
    break
cv2.destroyAllwindows()