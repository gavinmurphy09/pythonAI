import os
import cv2
import pickle
import face_recognition as FR
from numpy import full
print(cv2.__version__)

encodings = []
names = []
imageDir ='C:\\Users\gavin\Documents\python\haar\demoImages\known'

for root, dirs, files in os.walk(imageDir):
    print(root)
    print(dirs)
    print(files)   
    for file in files:
        print(file)
        fullFilePath = os.path.join(root, file)
        print(fullFilePath)
        myPicture = FR.load_image_file(fullFilePath)
        encoding = FR.face_encodings(myPicture)[0]
        name = os.path.splitext(file)[0]
        encodings.append(encoding)
        names.append(name)
with open('train.pkl', 'wb')as f:
    pickle.dump(names, f)
    pickle.dump(encodings, f)



