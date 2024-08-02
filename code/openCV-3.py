import cv2
from cv2 import COLOR_BGR2GRAY
print(cv2.__version__)
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #parameter is for port webcam is on,'CAP_DSHOW' = capture directshow, tell windows we are capturing frame to show it

#all this code helps camera run smoother
width = 320   
height = 180
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)   # capture property frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #capture prop fram height
cam.set(cv2.CAP_PROP_FPS, 5)   #set fps
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))  #setting the codec, format so camera runs smoothly on windows


while True:
    return_value, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
  
   
    #1st row
    cv2.imshow('my WEBcam1', frame)
    cv2.moveWindow('my WEBcam1', 0, 0)
    cv2.waitKey(10)
    cv2.imshow('my WEBcam2', frame)
    cv2.moveWindow('my WEBcam2', 320, 0)
    cv2.waitKey(10)
    cv2.imshow('my WEBcam3', frame)
    cv2.moveWindow('my WEBcam3', 640, 0)
    cv2.waitKey(10)
    cv2.imshow('my WEBcam4', frame)
    cv2.moveWindow('my WEBcam4', 960, 0)
    cv2.waitKey(10)
    
    #2nd row
    """
    add 90 to height for window bar
    """
    cv2.imshow('my WEBcam5', frame)
    cv2.moveWindow('my WEBcam5', 0, 270)
    cv2.imshow('my WEBcam6', frame)
    cv2.moveWindow('my WEBcam6', 320, 270)
    cv2.imshow('my WEBcam7', frame)
    cv2.moveWindow('my WEBcam7', 640, 270)
    cv2.imshow('my WEBcam8', frame)
    cv2.moveWindow('my WEBcam8', 960, 270)
    #3rd row
    
    cv2.imshow('my WEBcam9', frame)
    cv2.moveWindow('my WEBcam9', 0, 540)
    cv2.imshow('my WEBcam10', frame)
    cv2.moveWindow('my WEBcam10', 320, 540)
    cv2.imshow('my WEBcam11', frame)
    cv2.moveWindow('my WEBcam11', 640, 540)
    cv2.imshow('my WEBcam12', frame)
    cv2.moveWindow('my WEBcam12', 960, 600)
    
    if cv2.waitKey(1) & 0xff == ord('q'):   # user press 'q' to terminate loop
        break
cam.release()