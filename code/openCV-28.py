import cv2
import pickle
import face_recognition as FR
print(cv2.__version__)



font = cv2.FONT_HERSHEY_PLAIN
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with open ('train.pkl', 'rb') as f:
    names = pickle.load(f)
    knownEncodings = pickle.load(f)


while True:
    ignore, unKnownFace = cam.read()

    unKnownFaceRGB = cv2.cvtColor(unKnownFace, cv2.COLOR_BGR2RGB)
    faceLocations = FR.face_locations(unKnownFaceRGB)
    unknownEncodings = FR.face_encodings(unKnownFaceRGB, faceLocations)

    for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
        top, right, bottom, left = faceLocation
        cv2.rectangle(unKnownFace, (left, top), (right, bottom), (0,255,0),1)
        name = 'Unknown Person'
        matches = FR.compare_faces(knownEncodings, unknownEncoding)
        if True in matches:
            g = matches.index(True)
            name = names[g]
        cv2.putText(unKnownFace, name,(left, top), font, .5,(255,0,0), 1)


    cv2.imshow('my WEBcam', unKnownFace)
    cv2.moveWindow('my WEBcam', 0, 0)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()