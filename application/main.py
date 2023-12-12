import sys
import time
import requests
import cv2
import numpy as np
import imutils


device=0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS=30
url = "http://192.168.43.172:8080/shot.jpg"

cap = cv2.VideoCapture(device)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,FRAME_HEIGHT)
cap.set(cv2.CAP_PROP_FPS,FPS)

print(cap.isOpened())

pos=0
first=True

while True:
    t = time.time()
    for i in range(0, 30):
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        #img = imutils.resize(img, width=1000, height=1000)
        cv2.imshow("Android_cam", img)

        # Press Esc key to exit
        if cv2.waitKey(1) == 27:
            break
    t = time.time() - t
    print("FPS", 30 / t)
cv2.destroyAllWindows()



