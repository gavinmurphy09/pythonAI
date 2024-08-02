import cv2
print(cv2.__version__)
import numpy as np

def onTrack1(val):
    global hueLow1
    hueLow1 = val
def onTrack2(val):
    global hueHigh1
    hueHigh1 = val
def onTrack3(val):
    global hueLow2
    hueLow2 = val
def onTrack4(val):
    global hueHigh2
    hueHigh2 = val
def onTrack5(val):
    global satLow1
    satLow1 = val
def onTrack6(val):
    global satHigh1
    satHigh1 = val
def onTrack7(val):
    global valLow1
    valLow1 = val
def onTrack8(val):
    global valHigh1
    valHigh1 = val


width = 640
height = 360



cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)



cv2.namedWindow('myTracker')
cv2.resizeWindow('myTracker', width, height+100)
cv2.moveWindow('myTracker', int(width*2), 0)

cv2.createTrackbar('hueLow1', 'myTracker', 10, 179, onTrack1)
cv2.createTrackbar('hueHigh1', 'myTracker', 20, 179, onTrack2)
cv2.createTrackbar('hueLow2', 'myTracker', 10, 179, onTrack3)
cv2.createTrackbar('hueHIGH2', 'myTracker', 20, 179, onTrack4)
cv2.createTrackbar('satLow', 'myTracker', 10, 255, onTrack5)
cv2.createTrackbar('satHigh', 'myTracker', 250, 255, onTrack6)
cv2.createTrackbar('valLow', 'myTracker', 10, 255, onTrack7)
cv2.createTrackbar('valHigh', 'myTracker', 250, 255, onTrack8)



while True:

    ignore, frame = cam.read()
    lowerBound1 = np.array([hueLow1, satLow1, valLow1])
    upperBound1 = np.array([hueHigh1, satHigh1, valHigh1])
    lowerBound2 = np.array([hueLow2, satLow1, valLow1])
    upperBound2 = np.array([hueHigh2, satHigh1, valHigh1])

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    myMask1 =cv2.inRange(frameHSV, lowerBound1, upperBound1)
    myMaskSmall1 = cv2.resize(myMask1, (int(width/2),int(height/2)))
    myMask2 = cv2.inRange(frameHSV, lowerBound2, upperBound2)
    myMaskSmall2 = cv2.resize(myMask2, (int(width/2),int(height/2)))

    #myMaskComp = myMask1 | myMask2  #reason you can do this is because masks are 1 bit , so if you logical or every bit it will only keep the 1's
    #myMaskComp = cv2.add(myMask1, myMask2)  #calculates the sum of two arrays of same size
 

    myObject = cv2.bitwise_and(frame, frame, mask = myMaskComp)



 
    


    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    cv2.imshow('MASKcam', myObject)
    cv2.moveWindow('MASKcam', width, 0)

    cv2.imshow('MASKcam1', myMaskSmall1)
    cv2.moveWindow('MASKcam1', 0, height + 70)
    
    cv2.imshow('MASKcam2', myMaskSmall2)
    cv2.moveWindow('MASKcam2', int(width/2), height + 70)

    if cv2.waitKey(1)& 0xff == ord('q'):
        break
cv2.destroyAllWindows()
