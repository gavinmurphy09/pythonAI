import cv2
print(cv2.__version__)
import numpy as np
import time

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)


faceCascade = cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haar\haarcascade_eye.xml')

fps = 10
timeStamp = time.time()

while True:
    ignore, frame = cam.read()

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #returns array of arrays with faceposition in each array, arrays have a bounding rectangle(x,y,w,h)
    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)         #return array of arrays containing bounding rectangle


    #print(faces)

    for face in faces:
        
        x, y, w, h = face   #face = [x, y, w, h]
        #print('x=', x, 'y=', y, 'width', w, 'height', h)
        cv2.rectangle(frame, (x, y), (x+w, y+h),(255, 0, 0),3)
        
        #create ROI frame for purpose of checking for eyes
        frameROI = frame[y:y+h,x:x+w]
        frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
        eyes = eyeCascade.detectMultiScale(frameROIGray)  #looks for eyes only in the facebox

        #only checks for eyes in [face] array
        for eye in eyes:
            xeye, yeye, weye, heye = eye
            cv2.rectangle(frame[y:y+h,x:x+w], (xeye, yeye), (xeye+weye, yeye+heye),(255, 0, 0), 3)

    



    loopTime = time.time()-timeStamp
    timeStamp = time.time()
    fpsNEW = 1/loopTime
    fps = (.9*fps) +(.1 * fpsNEW)    #putting 90% confidence in the filter, and 10% in the reading



    cv2.putText(frame, str(fps)+' fps',(5,30),cv2.FONT_HERSHEY_PLAIN, 1,(255,0,0),2) 

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()