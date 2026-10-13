import cv2 as cv
import sys

img = cv.imread('M.jpg')

if img is None:
    sys.exit('File not found.')


def draw(event, x, y, flags, param):  # Callback function

    if event == cv.EVENT_LBUTTONDOWN:  # When the left mouse button is clicked
        cv.rectangle(img, (x, y), (x + 200, y + 200), (0, 0, 255), 2)

    elif event == cv.EVENT_RBUTTONDOWN:  # When the right mouse button is clicked
        cv.rectangle(img, (x, y), (x + 100, y + 100), (255, 0, 0), 2)

    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)  # Set the draw callback function for the Drawing window

while True:  # Infinite loop because we don't know when a mouse event will occur

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break