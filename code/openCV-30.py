from turtle import width
import cv2
print(cv2.__version__)
from mpHands import mpHands

width = 1280
height = 720

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

findHands = mpHands(1) #create object of type mpHands


"""
def parseLandmarks(frame):
    myHands = []
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMark in results.multi_hand_landmarks:   #step through hands
            myHand = []                                                     #clears array on each run through loop
            for landMark in handLandMark.landmark:   #step through points
                myHand.append((int(landMark.x * width),int(landMark.y * height)))
            myHands.append(myHand)      #append myHand array to myHands, so it becomes index[0]
    return myHands
"""


while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(width, height))
    handData, results = findHands.Marks(frame)
    for hand, result in zip(handData, results):  #step 2 variable through 2 arrays , need zip
        if result == 'Right':       #step through an array of strings, ('Right', 'Left'.....)returned by mpHands.Marks()
            handColor = (0,255,0)
            print('Right')
        if result == 'Left':
            handColor = (0,0,255)
            print('Left')
        for ind in [0,5,6,7,8]:    #ind steps though array indices shown
            cv2.circle(frame, hand[ind] ,25,handColor,3)
 
    

        
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    cv2.waitKey(300)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()