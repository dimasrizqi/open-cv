import cv2

#load image
img = cv2.imread('c:/Intel/python/test1/blobs2.jpeg')

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#show image
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()