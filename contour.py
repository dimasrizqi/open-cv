#Import OpenCV
import cv2
#Import Numpy
import numpy as np
#Baca gambar
img = cv2.imread('c:/Intel/python/test1/blobs2.jpeg')
#Konversi RGB ke HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#Range warna hijau segmentasi/klasifikasi
#referensi mencari warna https://www.ivanjul.com/nilai-kisaran-warna-hsv-untuk-deteksi-objek/
lower = np.array([50, 100, 100], dtype=np.uint8)
upper = np.array([70, 255, 255] , dtype=np.uint8)

mask = cv2.inRange(hsv, lower, upper)
kernel = np.ones((10,10),np.uint8)
#Dipertembal piksel objek
dilation = cv2.dilate(mask,kernel,iterations = 1)
#Diperkecil supaya tidak berdempet piksel objeknya
erosion = cv2.erode(img,kernel,iterations = 10)

#Temukan kontur
# contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#Kopi gambar asli ke variable resultImg
resultImg = (img).copy()
#Array kontur
contour = []
#Perulangan untuk kontur
for i in range(len(contours)):
    #Banyaknya kontur ke variable cnt
    cnt = contours[i]
    #Mencari radius untuk menggambar lingkaran
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    #Pusat lingkaran
    center = (int(x),int(y))
    #Jika radius(kontur ukuran > 35 px ) diaanggap bukan ukuran cap
    if(int(radius) > 35 ):
        contour.append(cnt)
        #Gambar lingkaran
        resultImg = cv2.circle(resultImg,center,int(radius),(255,0,0),3)

if len(contour) == 24:
    #add text
    text = "Jumlah Botol pas : " + str(len(contour)) + " pcs" 
    cv2.putText(resultImg, text, (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) 
    cv2.imshow('image',resultImg)
elif len(contour) > 24:
    #add text
    text = "Jumlah Botol lebih : " + str(len(contour)) + " pcs" 
    cv2.putText(resultImg, text, (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,255), 2) 
    cv2.imshow('image',resultImg)
else:
    #add text
    text = "Jumlah Botol kurang : " + str(len(contour)) + " pcs" 
    cv2.putText(resultImg, text, (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 
    cv2.imshow('image',resultImg)





cv2.waitKey(0)
cv2.destroyAllWindows()