import cv2

img = cv2.imread('c://Intel//python//test1//blobs2.jpeg')

# crop image[y_min:y_max , x_min:x_max]
img_crop = img[60:160, 320:420] 

# show image
cv2.imshow('image crop',img_crop)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()