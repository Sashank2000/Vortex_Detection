import cv2 as cv
import numpy as np
import math



def get_objects(image):
	#converting to gray scale
	gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

	#applying canny edge detection
	edged = cv.Canny(image, 10, 250)

	#finding contours
	(_, cnts, _) = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	idx = 600
	for c in cnts:
		x,y,w,h = cv.boundingRect(c)
		if w>15 and h>15:
			idx+=1
			new_img=image[y:y+h,x:x+w]
			#cropping images
			cv.imwrite("cropped/"+str(idx)+ '.png', new_img)
	#cv2.imshow("Original Image",image)
	#cv2.imshow("Canny Edge",edged)

img = cv.imread('visit0006.png')

get_objects(img)



print('>> Objects Cropped Successfully!')
print(">> Check out 'cropped' Directory")
cv.waitKey(0)
