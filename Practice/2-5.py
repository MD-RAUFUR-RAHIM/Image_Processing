import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # Try to connect to the camera

if not cap.isOpened():
    sys.exit('Camera connection failed')

frames = []

while True:
    ret, frame = cap.read()  # Acquire a frame that makes up the video

    if not ret:
        print('Failed to acquire a frame. Exiting the loop.')
        break

    cv.imshow('Video display', frame)

    key = cv.waitKey(1)  # Wait 1 millisecond for keyboard input

    if key == ord('c'):  # If the 'c' key is pressed, add the frame to the list
        frames.append(frame)

    elif key == ord('q'):  # If the 'q' key is pressed, exit the loop
        break

cap.release()  # Disconnect from the camera
cv.destroyAllWindows()

if len(frames) > 0:  # If frames have been collected
    imgs = frames[0]

    for i in range(1, min(2, len(frames))):  # Join a maximum of 2 images
        imgs = np.hstack((imgs, frames[i]))

    cv.imshow('collected images', imgs)

    cv.waitKey()
    cv.destroyAllWindows()

