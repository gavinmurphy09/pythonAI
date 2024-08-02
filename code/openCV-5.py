import cv2
print(cv2.__version__)
import numpy as np

redSquare = [0,0,255]
blackSquare = [0,0,0]
square = 100




frame = np.zeros([800,800,3],dtype =np.uint8)
while True:

    for i in range(0,8):
        
        """
        for j in range(0,8):
            square = square * j
            frame[square:,:] = redSquare
            #frame[:,:125]= blackSquare
            square = 100
        """
    cv2.imshow('My Window', frame)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break