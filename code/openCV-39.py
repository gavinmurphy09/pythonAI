import cv2
print(cv2.__version__)
from mpHands import mpHands

lowerLimit = 0
upperLimit = 0

def setLower(val):
    global lowerLimit
    lowerLimit = val

def setUpper(val):
    global upperLimit
    upperLimit = val

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
lbl = ''
width = 1280
height = 640

font = cv2.FONT_HERSHEY_PLAIN
fontSize = .5
fontThick = 1
fontColor = (255,0,0)

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', width+50, 0)
cv2.resizeWindow('Trackbars', 400, 150)

cv2.createTrackbar('lowerLimit', 'Trackbars', 0, 468, setLower)
cv2.createTrackbar('upperLimit', 'Trackbars', 468, 468, setUpper)

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


findFace = mpFace()
findHands = mpHands()
findPose = mpPose()
findMesh = mpMesh(drawMesh = False)

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(width, height))
    handsLM, handsType = findHands.Marks(frame)
    faceData = findFace.Marks(frame)
    poseLM = findPose.Marks(frame)
    meshData = findMesh.Marks(frame)
    #print(faceData)
    for mesh in meshData:
        cnt = 0
        for lm in mesh:
            if cnt >= lowerLimit and cnt <= upperLimit:
                cv2.putText(frame, str(cnt),(lm),font,fontSize,fontColor, fontThick)
                cnt = cnt +1

    
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