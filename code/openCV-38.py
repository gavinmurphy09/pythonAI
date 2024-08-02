import cv2
print(cv2.__version__)


def setLower(val):
    global lowerLimit
    lowerLimit = val


def setHigher(val):
    global upperLimit
    upperLimit = val



width = 1280
height = 720

circleRadius = 5
circleThickness = 2
circleColor = (0,255,0)

font = cv2.FONT_HERSHEY_PLAIN
fontSize = .5
fontThick = 1
fontColor = (255,0,0)

lowerLimit = 0
upperLimit = 468

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', width+50, 0)
cv2.resizeWindow('Trackbars', 400, 150)

cv2.createTrackbar('lowerLimit', 'Trackbars', 0, 468, setLower)
cv2.createTrackbar('upperLimit', 'Trackbars',468, 468, setHigher)

class mpMesh:
    import mediapipe as mp
    def __init__(self, still = False, maxFace = 3, tol1 = .5, tol2 = .5, drawMesh = True):
        self.myMesh = self.mp.solutions.face_mesh.FaceMesh(still, maxFace, tol1, tol2)
        self.myDraw = self.mp.solutions.drawing_utils
        self.draw = drawMesh     
        self.drawSpecCircle = self.myDraw.DrawingSpec(thickness = 0, circle_radius = 0, color = (255,0,0))
        self.drawSpecLine = self.myDraw.DrawingSpec(thickness = 3, circle_radius = 2, color = (0,0,255))

    def Marks(self, frame):
        multiMeshLM = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.myMesh.process(frameRGB)
        if results.multi_face_landmarks != None:
            for faceLandmarks in results.multi_face_landmarks:    #outer array is for many faces
                meshLM = []
                if self.draw == True:
                    self.myDraw.draw_landmarks(frame, faceLandmarks,self.mp.solutions.face_mesh.FACE_CONNECTIONS,self.drawSpecCircle,self.drawSpecLine)
                for lm in faceLandmarks.landmark:
                    meshLM.append((int(lm.x*width), int(lm.y*height)))
                multiMeshLM.append(meshLM)
        return multiMeshLM    
    
findMesh = mpMesh(drawMesh= False)

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(width, height))
    meshData = findMesh.Marks(frame)
    print(meshData)
    for mesh in meshData:
        cnt = 0
        for lm in mesh:
            if cnt >= lowerLimit and cnt <= upperLimit:
                cv2.putText(frame, str(cnt),lm,font,fontSize,fontColor,fontThick)
            cnt = cnt+1
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
    
    
