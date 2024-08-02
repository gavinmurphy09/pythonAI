import cv2
print(cv2.__version__)
from mpHands import mpHands

width = 1280
height = 720

paddleWidth = 125
paddleHeight = 25
paddleColor = (0,255,0)


ballRadius = 8
ballPosX = int(width/2)
ballPosY = int(height/2)
ballColor = (255,0,0)
deltaX = 10
deltaY = 10
ind = 8


lives = 5
score = 0






findHands = mpHands(1)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)






while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (width, height))
    
    handData = findHands.Marks(frame)
    
    for hand in handData:  #hand is an array of Landmarks(landmark.x, landmark.y)
        cv2.rectangle(frame,(int(hand[8][0] - paddleWidth/2), 0),(int(hand[8][0]+ paddleWidth/2), paddleHeight),paddleColor, -1)

    
    #draw ball
    cv2.circle(frame, (ballPosX, ballPosY), ballRadius, ballColor,-1)

    
    ballPosX = ballPosX + deltaX
    ballPosY = ballPosY + deltaY
    
    #by using these ball boundry variables we can reference ball edge to frame 
    topEdgeBall = ballPosY - ballRadius
    bottomEdgeBall = ballPosY + ballRadius
    leftEdgeBall = ballPosX - ballRadius
    rightEdgeBall = ballPosX + ballRadius



    #if ball touches top or sides reverse direction of ball
    if leftEdgeBall <= 0 or rightEdgeBall >= width:
        deltaX = deltaX*(-1)
    if bottomEdgeBall >= height:
        deltaY = deltaY*(-1)
    

    #if ball touches paddle
    if topEdgeBall <= paddleHeight:
        if ballPosX >= int(hand[ind][0]- paddleWidth/2) and ballPosX <= int(hand[ind][0]+paddleWidth/2):
            deltaY = deltaY*(-1)
            score = score +1
        else:
            ballPosX = int(width/2)
            ballPosY = int(height/2)
            lives = lives -1

    

    
    cv2.putText(frame, str(lives), (1000,200), cv2.FONT_HERSHEY_SIMPLEX,5,(255,0,0),2)
    cv2.putText(frame, str(score), (100,200), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,255),2)
    
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    
    if lives == 0:
        cv2.destroyWindow('my WEBcam')
        frameROI = frame[300:720,100:1280]
        frameROI[:] = (0,0,0) 
        cv2.putText(frameROI, 'Game Over',(200, 200),cv2.FONT_HERSHEY_SIMPLEX, 3,(255,0,0),3)
        cv2.imshow('my deathScreen', frameROI)
        cv2.moveWindow('my deathScreen', 0, 0)
        cv2.waitKey(5000)
        break

        
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()