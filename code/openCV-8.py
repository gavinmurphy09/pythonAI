import cv2
print(cv2.__version__)
import numpy as np
import time

fps = 0
myText = 'FPS = '


#frame size
width = 1280
height =  720

x = np.zeros([300,300,3], dtype = np.uint8)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  #codec

fps = 10
timeStamp  = time.time()
time.sleep(.1)
while True:
    ignore, frame = cam.read()
    loopTime = time.time()-timeStamp
    timeStamp = time.time()
    fpsNEW = 1/loopTime
    fps = (.9*fps) +(.1 * fpsNEW) 

    cv2.putText(frame, myText + str(fps),(120, 60), cv2.FONT_HERSHEY_COMPLEX,2,(250,0,0),2)
    cv2.rectangle(frame, (0,0),(120,35),(0,0,255),-1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam' , 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()

