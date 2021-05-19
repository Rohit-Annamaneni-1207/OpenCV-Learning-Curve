import numpy as np
import cv2

img=cv2.imread('assets/soccer_practice.jpg')
template=cv2.imread('assets/ball.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template_gray=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
height,width=template_gray.shape

methods=[cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2=img_gray.copy()
    result=cv2.matchTemplate(img_gray,template_gray,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF_NORMED,cv2.TM_SQDIFF]:
        location=min_loc
    else:
        location=max_loc

    bottom_right=(location[0]+width,location[1]+height)
    img=cv2.rectangle(img,location,bottom_right,(255,255,255),3)
    cv2.imshow('match',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()