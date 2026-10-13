import cv2 as cv
import numpy as np


def main():
    # Initialize webcam
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Step out of the frame.")
    print("Press 's' to capture the background, or 'q' to quit.")

    background = None

    # Step 1: Interactive background capture loop
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read webcam frame.")
            break

        frame = cv.flip(frame, 1)
        cv.imshow("Setup - Press 's' to Capture Background", frame)

        key = cv.waitKey(1) & 0xFF
        if key == ord("s"):
            print("Capturing background frames (please hold still)...")
            background_frames = []

            # Capture 30 frames for temporal averaging to eliminate noise
            for _ in range(30):
                ret, bg_frame = cap.read()
                if ret:
                    background_frames.append(cv.flip(bg_frame, 1))

            if len(background_frames) > 0:
                background = np.mean(background_frames, axis=0).astype(
                    np.uint8
                )
                print("Background captured successfully!")
                break
        elif key == ord("q"):
            cap.release()
            cv.destroyAllWindows()
            return

    cv.destroyWindow("Setup - Press 's' to Capture Background")

    print("You can now enter the frame with your GREEN cloth.")
    print("Press 'q' to exit.")

    # Step 2: Define GREEN color in HSV
    lower_green = np.array([36, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Create kernel for morphological operations
    kernel = np.ones((5, 5), np.uint8)

    # Step 3: Main processing loop
    while cap.isOpened():
        ret, current_frame = cap.read()
        if not ret:
            print("Error: Could not read webcam frame.")
            break

        current_frame = cv.flip(current_frame, 1)

        # Convert BGR to HSV
        hsv_frame = cv.cvtColor(current_frame, cv.COLOR_BGR2HSV)

        # Detect GREEN cloth
        mask = cv.inRange(hsv_frame, lower_green, upper_green)

        # Clean the mask using morphological filtering
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=2)
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=1)
        mask = cv.dilate(mask, kernel, iterations=1)

        # Step 4: Create the invisibility effect
        mask_inv = cv.bitwise_not(mask)

        # Extract background where the green cloth is present
        res1 = cv.bitwise_and(background, background, mask=mask)

        # Extract current frame everywhere except where the green cloth is
        res2 = cv.bitwise_and(current_frame, current_frame, mask=mask_inv)

        # Combine both parts for final output
        final_output = cv.add(res1, res2)

        # Step 5: Display results
        cv.imshow("Original Webcam", current_frame)
        cv.imshow("Green Cloth Mask", mask)
        cv.imshow("Invisibility Cloak", final_output)

        # Exit on 'q' or ESC
        key = cv.waitKey(1) & 0xFF
        if key == ord("q") or key == 27:
            break

    # Step 6: Release resources
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()