import cv2
print(cv2.__version__)
import face_recognition as FR



cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)




font = cv2.FONT_HERSHEY_COMPLEX


jayFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/known/jay_rosalim.jpg')
faceLoc1 = FR.face_locations(jayFace)[0]
jayFaceEncode = FR.face_encodings(jayFace)[0]

#gavinFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/known/gavin4.jpg')
#faceLoc2 = FR.face_locations(gavinFace)[0]
#gavinFaceEncode = FR.face_encodings(gavinFace)[0]

knownEncodings = [jayFaceEncode]
names = ['Jay Rosalim']


while True:

    ignore, unKnownFace = cam.read()

   


    unKnownFaceRGB = cv2.cvtColor(unKnownFace, cv2.COLOR_BGR2RGB)
    faceLocations = FR.face_locations(unKnownFaceRGB) #bounding box of each face
    faceEncodings = FR.face_encodings(unKnownFaceRGB, faceLocations)   #128 bit encoding for each face in img

    for facelocation, faceEncoding in zip(faceLocations, faceEncodings):
        top, right, bottom, left = facelocation
        cv2.rectangle(unKnownFace, (left, top),(right, bottom),(255,0,0),1)
        name = 'Unknown Person'
        matches = FR.compare_faces(knownEncodings, faceEncoding) #generate list of type boolean
        print(matches)
        if True in matches:
           g = matches.index(True)
           name = names[g]
        
        cv2.putText(unKnownFace, name,(left, top), font,0.5,(0,255,0),1)
           

    cv2.imshow('my CAM', unKnownFace)
    cv2.moveWindow('my CAM',0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()


