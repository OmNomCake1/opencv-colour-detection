import cv2
import numpy as np

# callback function for trackbars (x is trackbar current val)
# does nothing
def trackbar_callback(x):
    pass


# create window objects
cv2.namedWindow("Calibrator")

# create trackbar objects
cv2.createTrackbar("h-Min", "Calibrator", 0, 255, trackbar_callback)
cv2.createTrackbar("s-Min", "Calibrator", 0, 255, trackbar_callback)
cv2.createTrackbar("v-Min", "Calibrator", 0, 255, trackbar_callback)
cv2.createTrackbar("h-Max", "Calibrator", 0, 255, trackbar_callback)
cv2.createTrackbar("s-Max", "Calibrator", 0, 255, trackbar_callback)
cv2.createTrackbar("v-Max", "Calibrator", 0, 255, trackbar_callback)

starting_lower = np.array([25, 52, 72])
starting_upper = np.array([102, 255, 255])
cv2.setTrackbarPos("h-Min", "Calibrator", starting_lower[0])
cv2.setTrackbarPos("s-Min", "Calibrator", starting_lower[1])
cv2.setTrackbarPos("v-Min", "Calibrator", starting_lower[2])
cv2.setTrackbarPos("h-Max", "Calibrator", starting_upper[0])
cv2.setTrackbarPos("s-Max", "Calibrator", starting_upper[1])
cv2.setTrackbarPos("v-Max", "Calibrator", starting_upper[2])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower = np.array([0, 0, 0])
    upper = np.array([0, 0, 0])
    
    lower[0] = cv2.getTrackbarPos("h-Min", "Calibrator")
    lower[1] = cv2.getTrackbarPos("s-Min", "Calibrator")
    lower[2] = cv2.getTrackbarPos("v-Min", "Calibrator")
    upper[0] = cv2.getTrackbarPos("h-Max", "Calibrator")
    upper[1] = cv2.getTrackbarPos("s-Max", "Calibrator")
    upper[2] = cv2.getTrackbarPos("v-Max", "Calibrator")
    
    # colour mask
    mask = cv2.inRange(hsv, lower, upper)
    coloured_mask = cv2.bitwise_and(frame, frame, mask=mask)
     
    cv2.imshow("Calibrator", coloured_mask)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()