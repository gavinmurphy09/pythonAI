from cmath import sqrt
import cv2
print(cv2.__version__)
from mpHands import mpHands
import numpy as np

width = 1280
height = 640
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

lbl=''

def findDistances(handData):
    distMatrix = np.zeros([len(handData),len(handData)], dtype = np.float)
    for row in range(0, len(handData)):
        for col in range(0, len(handData)):
            distMatrix[row][col] = ((handData[row][0] - handData[col][0])**2 + (handData[row][1] - handData[col][1])**2)**(1./2.)  #distance from(d0 to d0)
    return distMatrix

def findError(gestureMatrix, unknownMatrix, keyPoints):
    error = 0
    for row in keyPoints:
        for col in keyPoints:
            error = error + abs(gestureMatrix[row][col] - unknownMatrix[row][col])  #returns summation of all distances between known and unknown matrices ie hand gestures
    return error

class mpMesh:
    import mediapipe as mp
    def __init__(self, still = False, maxFace = 3, tol1 = .5, tol2 = .5, drawMesh = True):
        self.myMesh = self.mp.solutions.face_mesh.FaceMesh(still, maxFace, tol1, tol2)
        self.myDraw = self.mp.solutions.drawing_utils
        self.draw = drawMesh     


    def Marks(self, frame):
        multiMeshLM = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.myMesh.process(frameRGB)
        if results.multi_face_landmarks != None:
            for faceLandmarks in results.multi_face_landmarks:    #outer array is for many faces
                meshLM = []
                if self.draw == True:
                    self.myDraw.draw_landmarks(frame, faceLandmarks,self.mp.solutions.face_mesh.FACE_CONNECTIONS)
                for lm in faceLandmarks.landmark:
                    meshLM.append((int(lm.x*width), int(lm.y*height)))
                multiMeshLM.append(meshLM)
        return multiMeshLM 



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

findHands = mpHands()
findPose = mpPose()
findFace = mpFace()
findFace = mpMesh(drawMesh = True)

cv2.namedWindow('my WEBcam')

keyPoints = [0,4,5,9,13,17,8,12,16,20] 

train = True

while True:
    ignore, frame = cam.read()
    frame =  cv2.resize(frame,(width, height))
    handsData, handsType = findHands.Marks(frame)
    if train == True:
        if handsData != []:   #if there is data
            print('show your gesture, press t when ready')
            if cv2.waitKey(1) & 0xff == ord('t'):
                knownGesture = findDistances(handsData[0])  #for 1 hand
                train = False
                print(knownGesture)    #print distance matrix of known gesture
    if train == False:
        if handsData != []:
            unknownGesture = findDistances(handsData[0])
            error = findError(knownGesture, unknownGesture, keyPoints)   #compare distances of both matrices and return absolute value
            cv2.putText(frame, str(round(error,0)),(100,175),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),8)

    for hand in handsData:
        
        for ind in keyPoints:
        
            cv2.circle(frame,hand[ind],4,(255,0,0),2)
           # cv2.putText(frame, lbl, (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),2)

    cv2.moveWindow('my WEBcam', 0,0)
    cv2.imshow('my WEBcam', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()