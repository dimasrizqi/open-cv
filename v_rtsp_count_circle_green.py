import cv2
import numpy as np
#video = cv2.VideoCapture("rtsp://10.10.1.240:8080/video/h264")
video = cv2.VideoCapture("rtsp://view:futami2020@10.10.1.21:554/Streaming/Channels/102")

while True:
    ret, frame = video.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    lower = np.array([50, 50, 50], dtype=np.uint8)
    upper = np.array([70, 255, 255] , dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)
    kernel = np.ones((10,10),np.uint8)
    #Dipertembal piksel objek
    dilation = cv2.dilate(mask,kernel,iterations = 1)
    #Diperkecil supaya tidak berdempet piksel objeknya
    erosion = cv2.erode(frame,kernel,iterations = 10)
    #Temukan kontur
    # contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #Kopi gambar asli ke variable resultImg
    resultImg = (frame).copy()
    #Array kontur
    contour = []

    #perulangan untuk kontur
    for i in range(len(contours)):
        #Banyaknya kontur ke variable cnt
        cnt = contours[i]
        #Mencari radius untuk menggambar lingkaran
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        #Pusat lingkaran
        center = (int(x),int(y))
        #Jika radius(kontur ukuran > 35 px ) diaanggap bukan ukuran cap
        if int(radius) > 35 and int(radius) < 100 :
            contour.append(cnt)
            #Gambar lingkaran
            resultImg = cv2.circle(resultImg,center,int(radius),(255,0,0),3)
    text = "Jumlah Tutup Botol Hijau : " + str(len(contour)) + " pcs" 
    cv2.imshow('Gray',gray)
    cv2.imshow('HSV', hsv)

    cv2.putText(resultImg, text, (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 
    cv2.imshow('result',resultImg)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()