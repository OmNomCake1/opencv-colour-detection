import cv2

# reads a file image, takes in a file name
# returns a numpy array of pixels.
image = cv2.imread("shark_cat.png")

# opens a small window displaying image. 
# takes a title and image object
cv2.imshow("Shark cat", image)

# w x h size of image and value representing number of channels (rgb, hsv etc)
print(image.shape)

# waitKey displays the window for given milliseconds or until any key is pressed
# argument is number of milliseconds
# if argument is 0, means display STILL image indefinitely until any key is pressed
# default is 0
# it returns ascii of key pressed
cv2.waitKey()
cv2.destroyAllWindows()

# save an image object as a file to your system
cv2.imwrite("new_cat.png", image)

