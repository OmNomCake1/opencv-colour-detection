import cv2

low_green = (25, 52, 72)
high_green = (102, 255, 255)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv2.imshow("original frame", frame)
    
    # convert frame to another image type
    # args: image object, cv2.macro - something like COLOR_BGR2HSV converts bgr to hsv
    # returns: new image object converted to that image colour type
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # create a colour mask
    # args: image object, lower bound array HSV/anything, upper bound array HSV/anything
    # returns: image object, pixels are 255 if in range, otherwise 0 (white or black)
    # hsv is preferred for image filtering
    mask = cv2.inRange(hsv, low_green, high_green)
    
    # I don't really get this but it uses the mask to show ONLy the masked colour instead of black and white
    coloured_mask = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("green mask", coloured_mask)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    