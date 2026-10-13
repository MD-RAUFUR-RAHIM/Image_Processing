import cv2 as cv
import sys

# Load the image
img = cv.imread('M.jpg') 

# Check if the image was successfully loaded
if img is None:
    sys.exit('File not found.')

# Draw a rectangle around the target area
cv.rectangle(img, (169, 187), (443, 430), (0, 0, 255), 2)

# Put text on the image
cv.putText(img, 'Monkey is laughing', (169, 180), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Display the image in a window
cv.imshow('Draw', img)

# Wait for a key press and close windows
cv.waitKey(0)
cv.destroyAllWindows()
