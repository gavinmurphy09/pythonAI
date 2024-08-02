import cv2
print(cv2.__version__)
import mediapipe as mp

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

width = 1280
height = 640

circleRadius = 10
circleColor = (255,0,0)
circleThickness = 4

eyeColor = (0,255,0)
eyeRadius = 8
eyeThickness = -1

pose = mp.solutions.pose.Pose(False, False, True, .5, .5)
mpDraw = mp.solutions.drawing_utils

while True:
    ignore, frame = cam.read() 
    frame = cv2.resize(frame,(width, height))
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    #print(results)

    #if results.pose_landmarks != None:
        #mpDraw.draw_landmarks(frame, results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)   #draw landmarks, don't need for loop as only 1 person is analysed
    landMarks = []

    if results.pose_landmarks != None:
        #print(results.pose_landmarks)

        for lm in results.pose_landmarks.landmark:
            landMarks.append((int(lm.x*width), int(lm.y*height)))
            #print(lm.x, lm.y)
        cv2.circle(frame, landMarks[0], circleRadius,circleColor, circleThickness)
        cv2.circle(frame, landMarks[2], eyeRadius, eyeColor, eyeThickness)
        cv2.circle(frame, landMarks[5], eyeRadius, eyeColor, eyeThickness)
    print(landMarks)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()