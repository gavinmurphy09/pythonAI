from turtle import width
import cv2
from cv2 import imshow
from cv2 import moveWindow
print(cv2.__version__)



width = 640
height = 360

cam= cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))



while True:

    ignore, frame = cam.read()
    frameROI = frame[150:210, 250:390]   #take region of interest from frame and create a new frameobject called 'frameROI'
    frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)  #grayscale has only 1 number to represent pixel instead of 3'tuple'
    frameROIBGR = cv2.cvtColor(frameROIGray, cv2.COLOR_GRAY2BGR)  #converts back into tuple [125,125,125]
    frame[0:60, 0:140] = frameROI  #moves array back into original image



    cv2.imshow('my BGR ROI', frameROIBGR)
    cv2.moveWindow('my BGR ROI', 650,250)

    cv2.imshow('myROI', frameROI)
    cv2.moveWindow('myROI', 650, 0)

    cv2.imshow('my grayROI', frameROIGray)
    cv2.moveWindow('my grayROI', 650, 150)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()