import cv2
import numpy as np
import imutils  

cap = cv2.imread('c:/Intel/python/test1/blobs3.jpeg')



while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([5, 90, 82])
    upper_blue = np.array([25, 110, 162])

    mask = cv2.imRange(hsv,lower_blue,upper_blue)

    cnts = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        area cv.contourArea(c)
        cv2.drawContours(frame,[c],-1,(0,255,0), 3)
        M - cv2.moments(c)
       cv2.imhow("frame",frame)

cv2.waitKey(0)
cv2.destroyAllWindows()