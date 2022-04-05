import cv2
import numpy as np

# Variables 
drawing=False # True while mouse button down, false while mouse button up.
ix,iy =-1,-1 # Upper left corner point variable
# Function
def draw_rectangle(event,x,y,flag,param):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy = x,y # Locating the current point on the mouse
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.rectangle(img,(ix,iy),(x,y),color = (255,0,0),thickness= -1)
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),color = (255,0,0),thickness= -1)

# Creating Black Image
img = np.zeros(shape=(512,512,3))

cv2.namedWindow(winname='my_rectangle')
cv2.setMouseCallback('my_rectangle',draw_rectangle)

while True:
    cv2.imshow('my_rectangle',img)
# Cheeks for ESC key
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()