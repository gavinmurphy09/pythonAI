import cv2
print(cv2.__version__)
import mediapipe as mp

width = 1280
height = 640

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceMesh = mp.solutions.face_mesh.FaceMesh(False, 3, .5, .5)    #(static img, no of face, tracking parameters, trackng parameters)
mpDraw = mp.solutions.drawing_utils

drawSpecCircle = mpDraw.DrawingSpec(thickness = 0, circle_radius = 0, color = (255,0,0))
drawSpecLine = mpDraw.DrawingSpec(thickness = 3, circle_radius = 2, color = (0,0,255))

font = cv2.FONT_HERSHEY_COMPLEX
fontSize = .5
fontColor = (0,255,255)


while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(width, height))
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(frame)
    print(results.multi_face_landmarks)
    if results.multi_face_landmarks != None:
        for faceLandmarks in results.multi_face_landmarks:   
            #mpDraw.draw_landmarks(frame, faceLandmarks,mp.solutions.face_mesh.FACE_CONNECTIONS,drawSpecCircle,drawSpecLine)  #draw face landmarks, draw connections
            indx = 0
            for lm in faceLandmarks.landmark:
                indx = indx + 1
       
                cv2.putText(frame, str(indx), (int(lm.x*width), int(lm.y*height)),cv2.FONT_HERSHEY_COMPLEX,.2,(255,0,0),1)
               # print(lm)
               
    #mpDraw.draw_landmarks(frame)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0 , 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()