# Accessing the live feed from your camera
import cv2
from datetime import datetime

# creates object which captures video from storage / laptop camera / IP based camera (wireless)
# constructor argument is 0/1/2 etc. for default computer camera or a video file name like "video.mp4"
# returns a VideoCapture object which represents the input video stream
# can be used to read frames from the video input source, set properties and release resources
cap = cv2.VideoCapture(0)

# read the frames from VideoCapture object
while True:
    # reads frame from video stream capture object
    # ret - boolean saying whether frame is available
    # frame - numpy array image object
    ret, frame = cap.read()
    
    # string of current time
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    
    # write text on image
    font = cv2.FONT_HERSHEY_SIMPLEX
    # the image object, string, xy position, font, scale, colour, thickness
    cv2.putText(frame, now, (50, 50), font, 1, (255, 255, 255), 2)
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    cv2.imshow("camera feed", hsv)
    # use waitKey(1) meaning each frame is displayed for 1 millisecond before it is killed and a new image is read...
    # ...basically a video feed
    # if we did waitKey(0), it would display a still image every time we closed it
    # it returns ascii/unicode of key pressed!
    key = cv2.waitKey(1)
    
    # ord basically gets the ascii/unicode of the character
    if key == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()