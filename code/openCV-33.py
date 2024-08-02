import cv2
print(cv2.__version__)
from mpHands import mpHands

width = 1280
height = 640

font = cv2.FONT_HERSHEY_COMPLEX
fontHeight = 5
fontWeight = 5
fontColor = (0,0,255)

yLeftTip = 0
yRightTip = 0
scoreLeft = 0
scoreRight = 0

xPos = int(width/2)
yPos = int(height/2)
deltaX = 3
deltaY = 3

ballRadius = 5
ballColor = (0,0,255)

paddleWidth = 25
paddleHeight = 125
paddleColor = (0,255,0)




xPos = int(width/2)
yPos= int(height/2)

findHands = mpHands()

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (width, height))
    cv2.circle(frame,(xPos, yPos), ballRadius, ballColor, -1)
    cv2.putText(frame, str(scoreLeft),(150,125),font, fontHeight, fontColor, fontWeight)
    cv2.putText(frame, str(scoreRight),(1130,125),font, fontHeight, fontColor, fontWeight)

    handsData, handsType = findHands.Marks(frame)   #returns right and left hand

    for hand, handType in zip(handsData, handsType):

        if handType == 'Right':
            handColor  = (255, 0, 0)
        if handType == 'Left':
            handColor = (0,255,0)

 
        if handType == 'Left':
            yLeftTip = hand[8][1]
        if handType == 'Right':
            yRightTip = hand[8][1]

    cv2.rectangle(frame, (0, int(yLeftTip- paddleHeight/2)), (paddleWidth, int(yLeftTip + paddleHeight/2)), paddleColor, -1)
    cv2.rectangle(frame, (width - paddleWidth, int(yRightTip - paddleHeight/2)),(width, int(yRightTip + paddleHeight/2)), paddleColor, -1)






    xPos = xPos + deltaX
    yPos = yPos + deltaY

    topBallEdge = yPos - ballRadius
    bottomBallEdge = yPos + ballRadius
    rightBallEdge = xPos + ballRadius
    leftBallEdge = xPos - ballRadius



    if topBallEdge <= 0:
        deltaY = deltaY * (-1)
        
    if bottomBallEdge >= height:
        deltaY = deltaY * (-1)
        
    if leftBallEdge <= paddleWidth:
        if bottomBallEdge >= int(yLeftTip - paddleHeight/2) and topBallEdge <= int(yLeftTip + paddleHeight/2):
            deltaX = deltaX * (-1)

        else:
            xPos = int(width/2)
            yPos = int(height/2)

            scoreRight = scoreRight + 1
    if rightBallEdge >= (width - paddleWidth):
        if yPos >= int(yRightTip - paddleHeight/2) and yPos <= int(yRightTip + paddleHeight/2):
            deltaX = deltaX * (-1)
        else:
            xPos = int(width/2)
            yPos = int(height/2)
                
            scoreLeft = scoreLeft +1


    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0 , 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()