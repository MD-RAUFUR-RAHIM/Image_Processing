import cv2 as cv
import numpy as np

# Step 1: Open webcam
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam could not be opened.")
    exit()

print("Stay out of the camera frame.")
print("Press 's' to capture the background.")

background = None

# Step 2: Capture the empty background
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read webcam frame.")
        cap.release()
        cv.destroyAllWindows()
        exit()

    frame = cv.flip(frame, 1)

    cv.imshow("Capture Background", frame)

    key = cv.waitKey(1) & 0xFF

    if key == ord('s'):
        background = frame.copy()
        print("Background captured successfully!")
        break

    elif key == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        exit()

cv.destroyWindow("Capture Background")

# Step 3: Define blue cloth color in HSV
lower_pink = np.array([140, 50, 50])
upper_pink = np.array([179, 255, 255])

# Step 4: Process webcam frames
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read webcam frame.")
        break

    frame = cv.flip(frame, 1)

    # Convert BGR image to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Create a mask for blue cloth
    mask = cv.inRange(hsv, lower_pink, upper_pink)

    # Remove small noise from the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

    # Replace blue cloth pixels with background pixels
    result = np.where(mask[:, :, None] > 0, background, frame)

    # Display the results
    cv.imshow("Original Webcam", frame)
    cv.imshow("Cloth Mask", mask)
    cv.imshow("Invisibility Cloak", result)

    # Press q to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# Step 5: Release webcam and close windows
cap.release()
cv.destroyAllWindows()