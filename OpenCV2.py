import cv2
import random

img = cv2.imread('assets/comic.png',1)

#print(img) will give a numpy array

# print(type(img)) #'numpy.ndarray'

# print(img.shape) #no of rows, no of columns, no of channels
#Normally colors are coded RGB but in OpenCV, BGR
'''
[
    [[0,0,0],[255,255,255]],
    [[0,0,0],[255,255,255]]
]
This represtents 2 rows, 2 cols, 3 channels

'''
#Look at row 257 of our image
# print(img[257][45:400])

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j]=[random.randint(1,255),random.randint(1,255),random.randint(1,255)]

copied_portion=img[200:600][250:650]

img[100:500][100:500]=copied_portion

cv2.imshow('random',img)
cv2.waitKey(0)
cv2.destroyAllWindows()