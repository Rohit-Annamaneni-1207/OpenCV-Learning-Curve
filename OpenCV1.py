import cv2

# cv2.IMREAD_COLOR ----> -1
# cv2.IMREAG_GRAYSCALE -----> 0
#cv2.IMREAD_UNCHANGED ------> 1
img = cv2.imread('assets/comic.png',1)
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25) #Image resize
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE) #Image rotating
cv2.imwrite('New_file.png',img) #Save Image
cv2.imshow('SomeLabel',img) #display image
cv2.waitKey(0) # Waits for infinite time for key click
cv2.destroyAllWindows() #Closes the image window