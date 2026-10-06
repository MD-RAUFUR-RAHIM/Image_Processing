import cv2 as cv
import sys 

img = cv.imread('wolf.jpg')

if img is None:
    sys.exit("The image does not exist")
    
cv.imshow("Image Display", img)

cv.waitKey()
cv.destroyAllWindows()