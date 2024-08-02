import cv2
print(cv2.__version__)

width = 1280
height = 720
windowPosX = 0
windowPosY = 0


def myCallback2(val):# scales the height to 9/16 ratio and uses cam.set functions for h and w
    width = val
    height = int(width*9/16)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
def myCallback3(val):
    global windowPosX

    print('position x of the window is ', val)
    windowPosX = val
def myCallback4(val):
    global windowPosY

    print('Position y of the window is ', val)
    windowPosY = val



#camset values from the track bar
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars', 400, 200)
cv2.moveWindow('myTrackbars', int(width*1.1), 0)

cv2.createTrackbar('width', 'myTrackbars', width, 2000, myCallback2)    #my camera only goes to 1280
cv2.createTrackbar('windowPosX', 'myTrackbars', windowPosX, 2000, myCallback3)
cv2.createTrackbar('windowPosY', 'myTrackbars', windowPosY, 2000, myCallback4)


while True:
    ignore, frame = cam.read()


  
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', windowPosX, windowPosY)
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()  