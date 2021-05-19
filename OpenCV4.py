import numpy as np
import cv2

capture= cv2.VideoCapture(0)

while (True):
    ret, frame = capture.read()
    width=int(capture.get(3))
    height=int(capture.get(4))

    # img=cv2.line(frame, (0,0),(width,height),(255,0,0),5)
    img=cv2.rectangle(frame,(100,100),(200,200),(0,0,128),5)
    # img=cv2.circle(frame,(300,300),60,(0,0,255),-1)
    font=cv2.FONT_HERSHEY_SIMPLEX
    # img=cv2.putText(frame,'Weeeee!!',(5,height-10),font,2,(0,0,255),5,cv2.LINE_AA)

    cv2.imshow('frame',img)
    # cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()