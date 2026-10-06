import cv2 as cv
import sys

img = cv.imread('wolf.jpg')

if img  is None:
    sys.exit("The image file doesn't exist")
    
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray,dsize=(0,0),fx=0.5,fy=0.5)


cv.imwrite('wolf_gray.jpg',gray)	
cv.imwrite('wolf_gray_small.jpg',gray_small)  
    
cv.imshow('Color image',img)
cv.imshow('Gray image',gray)
cv.imshow('Gray image small',gray_small)

cv.waitKey()
cv.destroyAllWindows()