import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0)  #set up camera object parameter is position
while True:
    ignore,  frame = cam.read()   #read frame from logitech webcame
  # grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #bgr to gray frame make a new fram convert from BGR to gray
    cv2.imshow('my WEBcam', frame)   #show a frame
    cv2.moveWindow('my WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):   #if key'q' is pressed break loop, ordinance is numerical value of letter 'q', wait 1millisecond
        break
cam.release()   
