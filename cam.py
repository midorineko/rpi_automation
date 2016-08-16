from cv2 import *
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    destroyWindow("cam-test")
    imwrite("/home/pi/rpi_automation/public/images/last_capture.jpg",img) #save image
