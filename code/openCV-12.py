import cv2
from cv2 import namedWindow
from cv2 import setMouseCallback
print(cv2.__version__)
from cv2 import CAP_PROP_FPS

evt = 0
height = 360
width = 640
topLeft = (200,100)
bottomRight = (350,200)




def mouseClick(event, xPos, yPos, flags, params):

    global evt
    global pnt #pnt is a tuple


    if event == cv2.EVENT_LBUTTONDOWN:
        print('mouse event was: ', event)
        print('at Position: ', xPos, yPos)
        pnt = (xPos, yPos)
        evt = event
    if event == cv2.EVENT_LBUTTONUP:
        print('mouse event was: ', event)
        print('at Position: ', xPos, yPos)
        pnt = (xPos, yPos)
        evt = event
    if event == cv2.EVENT_RBUTTONDOWN:
        print('mouse event was: ', event)
        print('at Position :', xPos, yPos)
        pnt =(xPos, yPos)
        evt = event



cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) # videowriter_fourcc function requires a parameter for type of codec used

#cv2.namedWindow('myROI')
cv2.namedWindow('my CLICK')
cv2.setMouseCallback('my CLICK', mouseClick)

while True:
    ignore, frame = cam.read()

    #frameROI = frame[100:200,200:350]  

    if evt == 1:
        topLeft = pnt
        
    if evt == 4:      #only draws rectangle and update frameROI while evt==4 is true evt remains 4 aslong as another button isny pressed
        bottomRight = pnt

        cv2.rectangle(frame,topLeft,bottomRight,(0,0,255),2)
        frameROI = frame[topLeft[1]:bottomRight[1],topLeft[0]:bottomRight[0]]  #(x1 = 200,y1 = 100),(x2 = 350, y2 =200)
        cv2.imshow('my ROI', frameROI)
        cv2.moveWindow('my ROI', int(width *1.1), 0)
   
    if evt == 2:        #kill ROI window
        cv2.destroyWindow('my ROI')
        evt = 0    #so this if statement doesn't execute again causing cv2.destroyWindow to cause crash program        
    


    print('row :' , topLeft[1] , 'row: ' , bottomRight[1], 'column: ', topLeft[0], 'column :',bottomRight[0])


    cv2.imshow('my CLICK', frame)
    cv2.moveWindow('my CLICK', 0, 0)



    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()


