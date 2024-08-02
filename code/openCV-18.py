import cv2
print(cv2.__version__)
import numpy as np


width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def onTrack1(val):
    global hueLow
    print('hue low value is ', val)
    hueLow = val

def onTrack2(val):
    global hueHigh
    print('hue High value is ', val)
    hueHigh = val

def onTrack3(val):
    global satLow
    print('sat low value is ' , val)
    satLow = val

def onTrack4(val):
    global satHigh
    print('sat High value is ', val)
    satHigh = val

def onTrack5(val):
    global valLow
    print('val low value is ', val)
    valLow = val

def onTrack6(val):
    global valHigh
    print('val high value is ', val)
    valHigh = val


cv2.namedWindow('myTracker')
cv2.moveWindow('myTracker', width, 0)
cv2.resizeWindow('myTracker', width, height)

cv2.createTrackbar('Hue Low', 'myTracker', 10, 179, onTrack1)
cv2.createTrackbar('Hue High', 'myTracker', 20, 179, onTrack2)
cv2.createTrackbar('Sat Low', 'myTracker', 10, 255, onTrack3)
cv2.createTrackbar('sat High', 'myTracker', 250, 255, onTrack4)
cv2.createTrackbar('val Low', 'myTracker', 10, 255, onTrack5)
cv2.createTrackbar('val High', 'myTracker', 250, 255, onTrack6)

while True:
    ignore, frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow, satLow, valLow]) #tuple defined by values in function 'onTrack'
    upperBound = np.array([hueHigh, satHigh, valHigh])

    #keep all the pixels in range between upperBound and lowerBound, if in range the bit is flipped white, if not range flipped bit is black
    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)  #make a mask array by looking at 'frameHSV' array and keep everything in defined range
    
    myMask = cv2.bitwise_not(myMask) #keeps inverse of what color i want, it's a logical 'not' of the mask
    myObject = cv2.bitwise_and(frame, frame, mask = myMask)#create new img called 'myObject' use bitwise_and function, 'and' betweeen frame and mask to keep only mask pixels and store in new img
    
    myObjectSmall = cv2.resize(myObject, (int(width/2),int(height/2)))
    cv2.imshow('my Object', myObjectSmall)
    cv2.moveWindow('my Object',int(width/2), height+ 80)

   
    
    myMaskSmall = cv2.resize(myMask, (int(width/2), int(height/2)))
    cv2.imshow('myMASK cam', myMaskSmall)
    cv2.moveWindow('myMASK cam', 0, height + 80)



    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()