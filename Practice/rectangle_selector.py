import cv2 as cv
import sys

# Load the image
img = cv.imread('M.jpg')

# Check if the image was successfully loaded
if img is None:
    sys.exit('File not found.')

# Store clicked points
points = []

# Mouse click function
def click_event(event, x, y, flags, param):

    if event == cv.EVENT_LBUTTONDOWN and len(points) < 2:
        points.append((x, y))

        print(f"Clicked Point {len(points)}: ({x}, {y})")
        cv.circle(img, (x, y), 3, (0, 0, 255), -1)
        
        if len(points) == 2:
            p1, p2 = points[0], points[1]
            cv.rectangle(img, p1, p2, (0, 0, 255), 2)
            cv.putText(img,'Monkey is laughing',(p1[0], p1[1] - 7),cv.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0),2)

            print("\n" + "=" * 50)
            print("Rectangle code:")
            print(f"cv.rectangle(img, {p1}, {p2}, (0, 0, 255), 2)")
            print("=" * 50 + "\n")

        # Update the displayed image
        cv.imshow('Draw', img)


# Display the image
cv.imshow('Draw', img)

# Tell OpenCV to monitor mouse clicks
cv.setMouseCallback('Draw', click_event)

# Wait for a key press
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()