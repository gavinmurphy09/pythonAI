import cv2
import face_recognition as FR
import mediapipe as mp
print(cv2.__version__)

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)



hands = mp.solutions.hands.Hands(False ,2, .5,.5)            #(staticimg = false, 2(no. of hands),tracking confidence, tracking confidence ratio)
mpDraw = mp.solutions.drawing_utils




while True:
    ignore, frame = cam.read()
    myHands = []
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)

    frame = cv2.resize(frame, (width, height))
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks != None:   # dont do anything if == none, if != none, draw landmarks
        for handLandMarks in results.multi_hand_landmarks: #multi_hand_landmarks is for all hands,  step through the hands
            #print(handLandMarks)
            myHand = []
            #mpDraw.draw_landmarks(frame, handLandMarks, mp.solutions.hands.HAND_CONNECTIONS)   
            for Landmark in handLandMarks.landmark:   #step through the points
                #print((Landmark.x,Landmark.y))
                myHand.append((int(Landmark.x*width), int(Landmark.y*height))) #an array of tuples for each point on 
            #print('')
            #print(myHand)
            cv2.circle(frame, myHand[17],8,(255,0,255),-1)
            cv2.circle(frame, myHand[18],8,(255,0,255),-1)
            cv2.circle(frame, myHand[19],8,(255,0,255),-1)
            cv2.circle(frame, myHand[20],8,(255,0,255),-1)
            myHands.append(myHand) #an array of 2 hands
            print(myHands)
            print('')

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()

