import cv2
#rtsp using camon live streaming android
#video = cv2.VideoCapture("rtsp://10.10.1.240:8080/video/h264")
#rtsp using hikvision ds2cd1021-i 
video = cv2.VideoCapture("rtsp://view:futami2020@10.10.1.21:554/Streaming/Channels/102")

while True:
    ret, frame = video.read()
    cv2.imshow('video', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()