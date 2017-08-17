import cv2

cv2.imshow('frame',frame)

while (1):
    if cv2.waitKey() == ord('s'):
        print "START"
