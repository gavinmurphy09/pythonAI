import cv2
import face_recognition as FR
print(cv2.__version__)

font = cv2.FONT_HERSHEY_SIMPLEX

donFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/known/Donald Trump.jpg')
faceLoc1 = FR.face_locations(donFace)[0]  #returns array of arrays containing 4 points
donFaceEncode = FR.face_encodings(donFace)[0]  #0 index to return a single array

print(faceLoc1)

nancyFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/known/Nancy Pelosi.jpg')
faceLoc2 = FR.face_locations(nancyFace)[0]
nancyFaceEncode = FR.face_encodings(nancyFace)[0]

knownEncodings = [donFaceEncode, nancyFaceEncode]
names = ['Donald Trump', 'Nancy Pelosi']

unknownFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/unknown/u3.jpg')
unKnownFaceBGR = cv2.cvtColor(unknownFace, cv2.COLOR_RGB2BGR)
faceLocations = FR.face_locations(unKnownFaceBGR)
unknownEncodings = FR.face_encodings(unKnownFaceBGR, faceLocations)  #encodings of all the faces it finds and bounding boxes of each one

for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
    top, right, bottom, left = faceLocation
    print(faceLocation)
    cv2.rectangle(unKnownFaceBGR, (left, top),(right, bottom),(255, 0, 0),1)  #box every face
    name = 'unKnown person'
    
    matches = FR.compare_faces(knownEncodings, unknownEncoding)
    print(matches)


for faceLocation in faceLocations:
    x, y, w, h = faceLocation
    cv2.rectangle(unKnownFaceBGR, (x, y), (x+ w, y+ h),(255,0, 0), 1)


cv2.imshow('frame', unKnownFaceBGR)


cv2.imshow('my Window',donFaceEncode)

cv2.imshow('my Window2', nancyFaceEncode)

cv2.waitKey(5000)