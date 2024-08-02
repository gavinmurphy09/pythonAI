import cv2
print(cv2.__version__)
import numpy as np

#frame size
width = 640
height = 360

#circle
mycolor = [0,0,0]
myThick = 2
myColor =(0,0,0)
myRadius = 30


#rectangle
upperLeft = (250, 140)
lowerRight = (390, 220)
lineW = 4

#text
myText = 'gavin is boss'
myFont = cv2.FONT_HERSHEY_COMPLEX
myFontHeight = 2
myFontThickness = 2
myFontColor = (255,0,0)

#numpy array
x = np.zeros([200,200,3], dtype = np.uint8)

#cam object of type videocapture
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#functions for setting parameters of object type Cam, frame size,fps nd codecs
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame[140:220,250:390] = [0,0,255]  #in an array rows corresponds to y axis and columns to x axis

    cv2.rectangle(frame, upperLeft, lowerRight,(0,255,0), lineW)   #parameters for function are 'pos(x1, y1), (x2, y2),color(###), line thickness
    cv2.circle(frame, (int(width/2), int(height/2)), myRadius ,myColor , myThick)  #centre, radius, color, thickness
    cv2.putText(frame, myText,(120, 60), myFont, myFontHeight, myFontColor, myFontThickness)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):   #if 'q' key is pressed break while loop and terminate program
        break
cam.release()   #release cam object

