import numpy as np
import cv2

capture=cv2.VideoCapture(0) #Video Capture Device (0 indicates the number of the capture device. Since we have only one webcam--->0)

while (True):
    ret, frame= capture.read() #ret tells whether frame was captured, frame gives the frame---> 2 return values
    width=int(capture.get(3)) # 3 indicates width and 4 indicates height
    height=int(capture.get(4))

    image=np.zeros(frame.shape,np.uint8)
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)

    rotated_frame_A=cv2.rotate(smaller_frame,cv2.ROTATE_90_CLOCKWISE)

    rotated_frame_B=cv2.rotate(smaller_frame,cv2.ROTATE_90_COUNTERCLOCKWISE)

    rotated_frame_C=cv2.rotate(smaller_frame,cv2.ROTATE_180)

    image[0:height//2, 0:width//2]=smaller_frame
    image[0:height//2, width//2:width]=rotated_frame_C
    image[height//2:height, 0:width//2]=rotated_frame_C
    image[height//2:height, width//2:width]=smaller_frame
    cv2.imshow('frame',image)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()