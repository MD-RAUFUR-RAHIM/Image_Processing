import cv2 as cv
import sys

# Load the image
img = cv.imread('M.jpg')

if img is None:
    sys.exit('File not found.')

# Keep the original image
original = img.copy()

# Store points
points = []


def click_event(event, x, y, flags, param):

    if event == cv.EVENT_LBUTTONDOWN:

        # Allow only two points
        if len(points) < 2:

            points.append((x, y))

            print(f"Clicked Point {len(points)}: ({x}, {y})")

            # Draw small red dot
            cv.circle(img, (x, y), 3, (0, 0, 255), -1)

            # After two clicks, draw rectangle
            if len(points) == 2:

                p1 = points[0]
                p2 = points[1]

                cv.rectangle(
                    img,
                    p1,
                    p2,
                    (0, 0, 255),
                    2
                )

                # Add text
                cv.putText(
                    img,
                    'Monkey is laughing',
                    (p1[0], p1[1] - 7),
                    cv.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2
                )

            cv.imshow('Draw', img)


# Show image
cv.imshow('Draw', img)

# Enable mouse clicks
cv.setMouseCallback('Draw', click_event)

print("Click two points to create a rectangle.")
print("Press 'r' to reset and try again.")
print("Press 'q' to quit.")

while True:

    key = cv.waitKey(1) & 0xFF

    # Press R to reset
    if key == ord('r'):

        points.clear()

        # Restore original image
        img[:] = original.copy()

        cv.imshow('Draw', img)

        print("Reset! Click two new points.")

    # Press Q to quit
    elif key == ord('q'):
        break


cv.destroyAllWindows()