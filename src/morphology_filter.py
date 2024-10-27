import cv2
import numpy as np

kernel = np.ones((10, 10), np.uint8)

low_green = (25, 52, 72)
high_green = (102, 255, 255)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, low_green, high_green)
    
    coloured_mask = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("no filter", coloured_mask)
    
    # Morphological opening (removes small noise)
    cleaned_mask = cv2.morphologyEx(coloured_mask, cv2.MORPH_OPEN, kernel)
    # Morphological closing (fills small holes)
    cleaned_mask = cv2.morphologyEx(cleaned_mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("filter", cleaned_mask)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    