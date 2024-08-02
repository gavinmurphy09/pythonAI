from pickletools import uint8
import cv2
print(cv2.__version__)
import numpy as np

def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global xVal
    global yVal
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt = event
        xVal = xPos
        yVal = yPos

    if event == cv2.EVENT_RBUTTONDOWN:
        print(event)
        evt = event
        xVal = xPos
        yVal = yPos


evt = 0
xVal = 0
yVal = 0

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore, frame = cam.read()
 
    if evt == 1:
        x = np.zeros([250,250,3],dtype=np.uint8)
           #row is yVal, col is xVal
        
        y = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #convert y frame to HSV color space
        clr = y[yVal][xVal]
        x[::] = clr   #take tuple clr which is derived from frame window and store it in y array at every element
        print(clr)
        cv2.putText(x, str(clr),(0, 50), cv2.FONT_HERSHEY_COMPLEX,1 ,(0,0,0),1)
        cv2.imshow('color Picker', x)
        cv2.moveWindow('color Picker', width, 0)

        cv2.imshow('color Picker2', y)
        cv2.moveWindow('color Picker2', width*2, 0)

        evt = 0

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()



