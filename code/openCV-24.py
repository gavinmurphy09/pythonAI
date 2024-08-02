from cmath import nan
import cv2
from cv2 import FONT_HERSHEY_COMPLEX
import face_recognition as FR
print(cv2.__version__)

font = cv2.FONT_HERSHEY_SIMPLEX

donFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/known/Donald Trump.jpg')
faceLoc1 = FR.face_locations(donFace)[0]
donFaceEncode = FR.face_encodings(donFace)[0]

nancyFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/known/Nancy Pelosi.jpg')
faceLoc2 = FR.face_locations(nancyFace)[0]
nancyFaceEncode = FR.face_encodings(nancyFace)[0]

penceFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/known/Mike Pence.jpg')
faceLoc3 = FR.face_locations(penceFace)[0]
penceFaceEncode = FR.face_encodings(penceFace)[0]

knownEncodings = [donFaceEncode, nancyFaceEncode, penceFaceEncode]
names = ['Donald Trump', 'Nancy Pelosi', 'Mike Pence']

unKnownFace = FR.load_image_file('C:/Users/gavin/Documents/python/haar/demoImages/unknown/u1.jpg')
unKnownFaceBGR = cv2.cvtColor(unKnownFace, cv2.COLOR_RGB2BGR)
faceLocations = FR.face_locations(unKnownFace)
unKnownEncodings = FR.face_encodings(unKnownFace, faceLocations)


#step through facelocations in order to draw boxes on each face, step through unknownencodings in order to compare each index with knownencodings and generate a array of results
for faceLocation, unKnownEncoding in zip(faceLocations, unKnownEncodings):
    top, right, bottom, left = faceLocation
    print(faceLocation)
    cv2.rectangle(unKnownFaceBGR, (left, top), (right, bottom),(255,0,0),1)
    name = 'UnKnown Person'   #if no one is found, assign name as unknown person
    matches = FR.compare_faces(knownEncodings, unKnownEncoding)
    print(matches)
   
    

    #if donald is in frame output his name and put text in frame with his name
    if True in matches:     #if matches array contains a True boolean value
        matchIndex = matches.index(True)    #returns index of the 'True' and stores in matchIndex
        print(matchIndex)
        print(names[matchIndex])     #pass the true index to the names array, names array corresponds to matches array 1:1
        name = names[matchIndex]         #store index position in name
    
    cv2.putText(unKnownFaceBGR, name,(left,top),font,.5, (255,0,0),1)   #draw text for name


cv2.imshow('My faces', unKnownFaceBGR)











cv2.waitKey(5000)