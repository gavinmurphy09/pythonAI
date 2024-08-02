import cv2
print(cv2.__version__)
import numpy as np

width = 640
height = 360


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

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound1 = np.array([hueLow1, satLow1, valLow1])
    upperBound1 = np.array([hueHigh1, satHigh1, valHigh1])
    lowerBound2 = np.array([hueLow2, satLow1, valLow1])
    upperBound2 = np.array([hueHigh2, satHigh1, valHigh1])

    myMask1 = cv2.inRange(frameHSV, lowerBound1, upperBound1)
    myMask2 = cv2.inRange(frameHSV, lowerBound2, upperBound2)

    myMaskComp = myMask1 | myMask2 
    
    
    #new code for contours arrays
    myContours, junk = cv2.findContours(myMaskComp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  #generates contours array
    #cv2.drawContours(frame, myContours, -1, (0,255,0), 3)        #draws all contours on frame
    
    for contour in myContours:      #steps through contour arrays, in range of myContours
        area = cv2.contourArea(contour) #only draws contours of area greater than 100
        if area>=200:
            myContour = [contour]   #put contour[] array into myContour array as 'drawContours argument takes only 2d array
            cv2.drawContours(frame, myContour,0,(255,0,0),1)
            x,y,w,h = cv2.boundingRect(contour)  #returns x, y of top left corner and width and height of rectangle
            cv2.rectangle(frame, (x, y),(x+w, y+h),(0,0,255),1)

    ############


    myObject = cv2.bitwise_and(frame, frame, mask = myMaskComp)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)


   # cv2.imshow('myObject', myObject)
   # cv2.moveWindow('myObject', width, 0)
    myMaskSmall1 = cv2.resize(myMask1, (int(width/2), int(height/2)))
    cv2.imshow('myMask1', myMaskSmall1)
    cv2.moveWindow('myMask1', 0, height + 70)
    myMaskSmall2 = cv2.resize(myMask2, (int(width/2),int(height/2)))
    cv2.imshow('myMask2', myMaskSmall2)
    cv2.moveWindow('myMask2', int(width/2), height + 70)



    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()