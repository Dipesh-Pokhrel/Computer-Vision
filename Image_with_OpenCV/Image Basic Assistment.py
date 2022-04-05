import cv2
import numpy as np

# Function
def create_circle(event,x,y,flag,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),radius = 100,color =(0,0,255),thickness = 10)

# Reading Image 
img = cv2.imread('dog_backpack.png')
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.namedWindow(winname='dog')
cv2.setMouseCallback('dog',create_circle)

while True:
    cv2.imshow('dog',img_rgb)
    if cv2.waitKey(20) & 0xFF==27:
        break

cv2.destroyAllWindows()