import cv2 as cv
import numpy as np
import time


def main():

    # Initialize webcam
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Allow camera to warm up
    print("Initializing camera...")
    print("Please step out of the frame.")
    time.sleep(2)

    # --------------------------------------------------
    # 1. Capture and average 30 background frames
    # --------------------------------------------------

    background_frames = []

    for _ in range(30):

        ret, frame = cap.read()

        if ret:
            # Flip frame horizontally
            frame = cv.flip(frame, 1)

            background_frames.append(frame)

    # Calculate average background ONLY ONCE
    if len(background_frames) > 0:
        background = np.mean(
            background_frames, axis=0
        ).astype(np.uint8)
    else:
        background = None

    if background is None:
        print("Error: Failed to capture background.")
        cap.release()
        return

    print("Background captured successfully!")
    print("You can now enter the frame with your GREEN cloth.")
    print("Press 'q' or ESC to exit.")

    # --------------------------------------------------
    # 2. Define GREEN color in HSV
    # --------------------------------------------------

    lower_bound = np.array([140, 50, 50])
    upper_bound = np.array([179, 255, 255])
    
    #lower_bound = np.array([36, 50, 50])
    #upper_bound = np.array([85, 255, 255])

    # Create kernel ONCE
    kernel = np.ones((5, 5), np.uint8)

    # --------------------------------------------------
    # 3. Main webcam loop
    # --------------------------------------------------

    while cap.isOpened():

        ret, current_frame = cap.read()

        if not ret:
            break

        # Flip webcam like a mirror
        current_frame = cv.flip(current_frame, 1)

        # Convert BGR to HSV
        hsv_frame = cv.cvtColor(
            current_frame,
            cv.COLOR_BGR2HSV
        )

        # Detect GREEN cloth
        mask = cv.inRange(
            hsv_frame,
            lower_bound,
            upper_bound
        )

        # --------------------------------------------------
        # 4. Clean the mask
        # --------------------------------------------------

        # Remove small noise
        mask = cv.morphologyEx(
            mask,
            cv.MORPH_OPEN,
            kernel,
            iterations=2
        )

        # Make the detected cloth area slightly larger
        mask = cv.dilate(
            mask,
            kernel,
            iterations=1
        )

        # --------------------------------------------------
        # 5. Create the invisibility effect
        # --------------------------------------------------

        # Invert mask
        mask_inv = cv.bitwise_not(mask)

        # Background where GREEN cloth is detected
        res1 = cv.bitwise_and(
            background,
            background,
            mask=mask
        )

        # Current frame everywhere except GREEN cloth
        res2 = cv.bitwise_and(
            current_frame,
            current_frame,
            mask=mask_inv
        )

        # Combine both parts
        final_output = cv.add(res1, res2)

        # --------------------------------------------------
        # 6. Display results
        # --------------------------------------------------

        cv.imshow("Original Webcam", current_frame)
        cv.imshow("Green Cloth Mask", mask)
        cv.imshow("Invisibility Cloak", final_output)

        # --------------------------------------------------
        # 7. Exit
        # --------------------------------------------------

        key = cv.waitKey(1) & 0xFF

        if key == ord('q') or key == 27:
            break

    # --------------------------------------------------
    # 8. Release resources
    # --------------------------------------------------

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()