import cv2 as cv
import sys

img = cv.imread('M.jpg')

if img is None:
    sys.exit('File not found.')

BrushSiz = 5                         # Brush size
LColor, RColor = (255, 0, 0), (0, 0, 255)  # Blue and red colors


def painting(event, x, y, flags, param):

    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), BrushSiz, LColor, -1)
        # Left mouse button click -> blue

    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), BrushSiz, RColor, -1)
        # Right mouse button click -> red

    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x, y), BrushSiz, LColor, -1)
        # Move while holding the left button -> blue

    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x, y), BrushSiz, RColor, -1)
        # Move while holding the right button -> red

    cv.imshow('Painting', img)
    # Display the modified image again


cv.namedWindow('Painting')
cv.imshow('Painting', img)

cv.setMouseCallback('Painting', painting)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break