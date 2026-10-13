import cv2 as cv
import sys

# Load your new image
img = cv.imread('M.jpg')  # Replace with your filename

if img is None:
    sys.exit('File not found.')

points = []

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Clicked Point {len(points)}: ({x}, {y})")
        
        # Draw a small circle where clicked to give visual feedback
        cv.circle(img_copy, (x, y), 3, (0, 0, 255), -1)
        cv.imshow('Click Top-Left then Bottom-Right', img_copy)
        
        # Once two points are collected, calculate and print the rectangle code
        if len(points) == 2:
            p1, p2 = points[0], points[1]
            print("\n" + "="*50)
            print("Copy and paste this line into your main script:")
            print(f"cv.rectangle(img, {p1}, {p2}, (0, 0, 255), 2)")
            print("="*50 + "\n")

img_copy = img.copy()
cv.imshow('Click Top-Left then Bottom-Right', img_copy)
cv.setMouseCallback('Click Top-Left then Bottom-Right', click_event)

print("Instructions:")
print("1. Click on the TOP-LEFT corner of the laughing face.")
print("2. Click on the BOTTOM-RIGHT corner of the laughing face.")
print("3. Press any key to close when finished.")

cv.waitKey(0)
cv.destroyAllWindows()