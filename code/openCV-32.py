import cv2
print(cv2.__version__)

width = 1280
height = 640

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)




class mpPose:
    import mediapipe as mp
    
    def __init__(self, still = False, upperBody = False, smoothData = True, tol1 = .5, tol2 = .5):
        self.myPose = self.mp.solutions.pose.Pose(still, upperBody, smoothData, tol1, tol2)

    def Marks(self, frame):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.myPose.process(frameRGB) #
        poseLandmarks = []
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
            print(poseLandmarks)
        return poseLandmarks

class mpHands:
    import mediapipe as mp
    
    def __init__(self, maxHands = 2, tol1 = .5, tol2 = .5):
        self.hands = self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    
    def Marks(self, frame):
        myHands = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
                
        return myHands

findHands = mpHands(2)
findPose = mpPose()

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(width, height))
    handData = findHands.Marks(frame)
    poseData = findPose.Marks(frame)
    for hand in handData:
        for ind in [0,5,6,7,8]:
            cv2.circle(frame,hand[ind],5,(255,0,255),-1)
    if len(poseData) != 0:
        cv2.circle(frame, poseData[0], 5,(0,255,0),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()



