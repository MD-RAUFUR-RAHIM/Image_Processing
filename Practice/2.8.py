import cv2 as cv
import sys

img = cv.imread('M.jpg')

if img is None:
    sys.exit('File not found.')


def draw(event, x, y, flags, param):

    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:  # Save the initial position when the left mouse button is pressed
        ix, iy = x, y

    elif event == cv.EVENT_LBUTTONUP:  # Draw a rectangle when the left mouse button is released
        cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)

    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while True:

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break