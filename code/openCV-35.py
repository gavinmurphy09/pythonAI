import cv2
print(cv2.__version__)
import mediapipe as mp


width = 1280
height = 720

boxColor = (255,0,0)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

findFace = mp.solutions.face_detection.FaceDetection()
drawFace = mp.solutions.drawing_utils

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(width, height))
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = findFace.process(frameRGB)
    #print(results.detections)
    if results.detections != None:
        for face in results.detections:
            #drawFace.draw_detection(frame, face)
            bBox = face.location_data.relative_bounding_box  #returns bounding box of face in x, y, h format bBox.x
            topLeft = (int(bBox.xmin*width),int(bBox.ymin*height))
            bottomRight = (int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
            print(bBox)
        cv2.rectangle(frame, (topLeft),(bottomRight),boxColor, 3)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()