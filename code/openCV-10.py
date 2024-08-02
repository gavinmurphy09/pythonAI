import cv2
print(cv2.__version__)

width = 640
height = 360

snipW = 120
snipH = 60

boxCR = int(height/2)
boxCC = int (width/2)

#speed of box movement for row and column of array
deltaRow = 1
deltaColumn = 1

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frameROI = frame[int(boxCR - snipH/2):int(boxCR + snipH/2), int(boxCC - snipW/2): int(boxCC + snipW/2)]
    
    #convert to gray and back to color so snip fits shape of frame array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  #frame now is still grayscale but grayscale represented by tuple(#,#,#) so frameROI can fit into frame array as frameROI is BGR tuple

    boxCR = boxCR + deltaRow
    boxCC = boxCC + deltaColumn

    frame[int(boxCR - snipH/2): int(boxCR + snipH/2), int(boxCC -snipW/2):int(boxCC + snipW/2)] = frameROI

    if boxCR - snipH/2 <= 0:
        deltaRow = deltaRow * (-1)
    if boxCC - snipW/2 <= 0:
        deltaColumn = deltaColumn * (-1)
    if boxCR + snipH/2 >= height:
        deltaRow = deltaRow * (-1)
    if boxCC + snipW/2 >= width:
        deltaColumn = deltaColumn * (-1)



    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI', width, 0)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()