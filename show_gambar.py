import cv2
#jadi grayscale
# image = cv2.imread('c:/Intel/python/test1/blobs2.jpeg', cv2.IMREAD_GRAYSCALE)
# _, threshold = cv2.threshold(image,155,255,cv2.THRESH_BINARY)

#show biasa
image = cv2.imread('c:/Intel/python/test1/jeruk.png')
cv2.imshow('test',image)
#cv2.imshow('test',threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()