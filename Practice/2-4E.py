import cv2 as cv 
import sys

cap = cv.VideoCapture(r"C:\Users\OWNER\Downloads\12195666_1080_1920_60fps.mp4")
if not cap.isOpened():
    sys.exit("Camera connection failed")

while True:
    ret,frame = cap.read()
    
    if not ret:
        print("Failed to acquire a frame. Exiting the loop.")
        break
    
    cv.imshow("Video Display", frame)
    
    key = cv.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv.destroyAllWindows()