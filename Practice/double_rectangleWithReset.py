import cv2 as cv
import sys

# 1. Load image and keep a pristine copy
img = cv.imread('M.jpg')
if img is None:
    sys.exit('File not found.')

original = img.copy()

# Store coordinates for left (Red) and right (Blue) boxes
points_red = []
points_blue = []

def click_event(event, x, y, flags, param):
    # Map events to their respective point list, dot color, and box color
    if event == cv.EVENT_LBUTTONDOWN:
        pts, dot_color, box_color, btn_name = points_red, (0, 0, 255), (0, 0, 255), "Left"
    elif event == cv.EVENT_RBUTTONDOWN:
        pts, dot_color, box_color, btn_name = points_blue, (255, 0, 0), (255, 0, 0), "Right"
    else:
        return  # Ignore all other mouse movements/events immediately

    if len(pts) < 2:
        pts.append((x, y))
        print(f"{btn_name}-Clicked Point {len(pts)}: ({x}, {y})")

        # Draw indicator dot
        cv.circle(img, (x, y), 3, dot_color, -1)

        # Draw bounding box and text once 2 points are selected
        if len(pts) == 2:
            p1, p2 = pts[0], pts[1]
            cv.rectangle(img, p1, p2, box_color, 2)
            cv.putText(
                img,
                'Monkey is laughing',
                (p1[0], p1[1] - 7),
                cv.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

        # Update display only when an event alters the image
        cv.imshow('Draw', img)

# Initialize display window and mouse listener
cv.imshow('Draw', img)
cv.setMouseCallback('Draw', click_event)

print("Left-click 2 points -> RED box")
print("Right-click 2 points -> BLUE box")
print("Press 'r' to reset | Press 'q' to quit")

def redraw_image():
    global img
    img[:] = original.copy()

    # Redraw Red Box if 2 points exist
    if len(points_red) == 2:
        p1, p2 = points_red[0], points_red[1]
        cv.rectangle(img, p1, p2, (0, 0, 255), 2)
        cv.putText(img, 'Monkey is laughing', (p1[0], p1[1] - 7),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Redraw Blue Box if 2 points exist
    if len(points_blue) == 2:
        p1, p2 = points_blue[0], points_blue[1]
        cv.rectangle(img, p1, p2, (255, 0, 0), 2)
        cv.putText(img, 'Monkey is laughing', (p1[0], p1[1] - 7),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv.imshow('Draw', img)

# 2. Optimized Event Loop (Blocking wait, ~0% CPU usage)
while True:
    key = cv.waitKey(0) & 0xFF

    if key == ord('r'):
        points_red.clear()
        redraw_image()  # Function to redraw remaining points
        print("\n[Reset] Red points cleared.")

    elif key == ord('b'):
        points_blue.clear()
        redraw_image()  # Function to redraw remaining points
        print("\n[Reset] Blue points cleared.")

    elif key == ord('q'):
        break

cv.destroyAllWindows()