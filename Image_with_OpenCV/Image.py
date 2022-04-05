import cv2
img = cv2.imread('Puppy1')
while True:
    cv2.imshow('Puppy',img)
    # If we wited at least 1ms and we, pressed the ESC key. 27 is the symbol for ESC key
    if cv2.waitKet(1) & 0xFF ==27:
        break
cv2.destroyAllWindows()