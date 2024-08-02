import cv2
print(cv2.__version__)
import numpy as np

evt = 0
xVal = 0
yVal = 0

def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global xVal
    global yVal

    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt = event
        xVal = xPos
        yVal = yPos
    if event == cv2.EVENT_RBUTTONUP:
        evt = event
        print(event)

width = 1280
height = 640

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'mJPG'))

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)


while True:

    ignore, frame = cam.read()

    if evt == 1:        #generate ROI when mouse evt 1 is clicked
        x = np.zeros([250,250,3],dtype=np.uint8)  #data type is 8 bit unsigned intiger

    
        cv2.imshow('Color Picker', x)
        cv2.moveWindow('Color Picker', width, 0)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()