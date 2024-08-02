from turtle import width
import cv2

print(cv2.__version__)

class mpHands:
    import mediapipe as mp
    
    width = 1280
    height = 720
    resultsMH = []
    myHands = []

    #this is a constructor class, if no params are passed they are set as shown
    def __init__(self, maxHands = 2, tol1= .5, tol2 = .5):   #if you only pass method self, it constructs params as shown

        #constructor class creates and object of type shown below
        self.hands = self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    
    
    def Marks(self, frame):
        self.height
        self.width
        self.myHands = []
        handsType = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for hand in results.multi_handedness:
                #print(hand)
            #print(hand.classification)
            #print(hand.classification[0])
               #print(hand.classification[0].label)
               handType= hand.classification[0].label
               handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
             

                myHand = []
                for landmark in handLandMarks.landmark:
                    myHand.append((int(landmark.x*self.width),int(landmark.y*self.height)))
                self.myHands.append(myHand)
        #   print(self.myHands)
        return self.myHands, handsType





