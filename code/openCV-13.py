from pickletools import read_unicodestring1
import cv2
print(cv2.__version__)

width = 1280
height = 720

xPos = int(width/2)
yPos = int(height/2)
radius = 25
myThick = 2

def myCallBack1(val):
    global xPos

    print('x Position is = ' ,val)
    xPos = val
def myCallBack2(val):
    global yPos

    print('y Position is = ', val)
    yPos = val
def myCallBack3(val):
    global radius

    print('radius is = ', val)
    radius = val
def myCallBack4(val):
    global myThick

    print('thickness is =', myThick)
    myThick = val

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars', 400, 200)
cv2.moveWindow('myTrackbars', int(width*1.1), 0)
cv2.createTrackbar('xPos', 'myTrackbars', xPos, 1920, myCallBack1)   #trackbar name, window name, initial value, max number, callback function
cv2.createTrackbar('yPos','myTrackbars', yPos, 1920, myCallBack2)
cv2.createTrackbar('radius','myTrackbars', radius, int(height/2), myCallBack3)
cv2.createTrackbar('thickness','myTrackbars',myThick,7,myCallBack4)


while True:
    ignore, frame = cam.read()
    if myThick == 0:
        myThick = (-1)
    cv2.circle(frame, (xPos, yPos),radius,(0,255,0),myThick)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
