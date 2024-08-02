import os
import cv2
import face_recognition as FR
from numpy import full
print(cv2.__version__)

imageDir = 'C:\\Users\gavin\Documents\python\haar\demoImages\known'

for root, dirs,files in os.walk(imageDir):
    print('my Working Folder (root): ',root)
    print('dirs in root: ', dirs)
    print('My files in root: ', files)
    for file in files:
        print('your guy is: ', file)
        fullFilePath = os.path.join(root, file)   #concatinate path with file name
        print(fullFilePath)
        name = os.path.splitext(file)[0]
        print(name)
        myPicture = FR.load_image_file(fullFilePath)
        myPicture = cv2.cvtColor(myPicture, cv2.COLOR_RGB2BGR)
        cv2.imshow(name, myPicture)
        cv2.moveWindow(name, 0, 0)
        cv2.waitKey(500)
        cv2.destroyAllWindows()