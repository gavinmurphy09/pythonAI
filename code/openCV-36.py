import cv2
print(cv2.__version__)
from mpHands import mpHands


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
lbl = ''
width = 1280
height = 640

fontColor = (255,0,0)
font = cv2.FONT_HERSHEY_SIMPLEX

class mpFace:
    import mediapipe as mp
    def __init__(self):
        self.myFace = self.mp.solutions.face_detection.FaceDetection()

    def Marks(self, frame):
        faceBoxes = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.myFace.process(frameRGB)
        if results.detections != None:
            for face in results.detections:
                bBox = face.location_data.relative_bounding_box
                
                topLeft = ((int(bBox.xmin*width),int(bBox.ymin*height)))
                bottomRight = ((int((bBox.xmin + bBox.width)*width), int((bBox.ymin + bBox.height)*height)))
                faceBoxes.append((topLeft, bottomRight))
         
        return faceBoxes 

class mpPose:
    import mediapipe as mp
    
    def __init__(self, still = False, upperBody = False, smoothData = True, tol1 = .5, tol2 = .5):
        self.myPose = self.mp.solutions.pose.Pose(still, upperBody, smoothData, tol1, tol2)

    def Marks(self, frame):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.myPose.process(frameRGB) #
        poseLandmarks = []
        if results.pose_landmarks:          
            for lm in results.pose_landmarks.landmark:    #step through landmarks and add them to array
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
            print(poseLandmarks)
        return poseLandmarks               


findFace = mpFace()
findHands = mpHands()
findPose = mpPose()

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(width, height))
    handsLM, handsType = findHands.Marks(frame)
    faceData = findFace.Marks(frame)
    poseLM = findPose.Marks(frame)
    #print(faceData)
    if len(poseLM) != 0:             #only need 1 for loop as poseLM is only 1 person
        for ind in [13,14,15,16]:    #elbow, wrist, draw circle
            cv2.circle(frame, poseLM[ind] ,5,(255,0,0),2)
    for face in faceData:
        cv2.rectangle(frame,face[0],face[1],(255,0,0),2)  #face[0] = topleft [1] = bottomRight
    for hand, handType in zip(handsLM, handsType):
        if handType ==  'Right':
            lbl = 'Right'
        if handType == 'Left':
            lbl = 'Left'
        cv2.putText(frame, lbl, (hand[8]),font,2, fontColor, 2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()