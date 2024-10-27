import cv2
import numpy as np

low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
        
    # convert frame to another image type
    # args: image object, cv2.macro - something like COLOR_BGR2HSV converts bgr to hsv
    # returns: new image object converted to that image colour type
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # create a colour mask
    # args: image object, lower bound array HSV/anything, upper bound array HSV/anything
    # returns: image object, pixels are 255 if in range, otherwise 0 (white or black)
    # hsv is preferred for image filtering
    mask = cv2.inRange(hsv, low_green, high_green)
    
    # using mask = mask, this takes the original coloured frame and applies the mask to it by AND-ing all the pixels
    # since mask is only b/w, it basically keeps all pixels from o.g. frame where mask is white
    # good for colour masking then converting to image with ONLY COLOUR and BLACK
    coloured_mask = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("no filter", coloured_mask)
    
    
    # find contours (the outline of the colour mask blobs)
    # use binary images
    # args: image, contour retreival mode, contour approximation method
    # returns: contours (list of contours (numpy arrays of boundary points)) and hierarchy - ??
    # use RETR_EXTERNAL for external contours only. CHAIN_APPROX_SIMPLE/NONE tells how many points to store, saving memory
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # draw contours on o.g. frame
    # args: image object, contours list/single contour, index of contour to draw (-1 for all), colour in rgb, thickness
    # cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)
    
    # draw rectangle around contours which are big enough (filter out noise)
    for c in contours:
        # for all contours, get contour area
        area = cv2.contourArea(c)
        # remove noise - small sections
        if area > 3000:
            # get x,y position, width height of bounding rectangle bounding contour c 
            # x y of TOP LEFT of rect
            x, y, w, h = cv2.boundingRect(c)
            # draw a rectangle on frame
            # args: image, starting points (x, y), ending points (x + w, y + h), RGB colour, width
            cv2.rectangle(coloured_mask, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.drawContours(coloured_mask, c, -1, (255, 0, 255), 2)
    
    cv2.imshow("with filtering", coloured_mask)
    

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    