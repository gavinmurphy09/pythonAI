import cv2
print(cv2.__version__)
import numpy as np

x = np.zeros([256, 720, 3], dtype = np.uint8)    #(HSV) datatype 8 bit int, 256 numbers for saturation and vale, 180 numbers for hue

for row in range(0,256,1):
    for column in range(0,720,1):
        x[row, column] = (int(column/4),row,255)  #(hue,saturation,value)HSV

x = cv2.cvtColor(x,cv2.COLOR_HSV2BGR)   #need to convert back to RGB color space as openCV won't display HSV

y = np.zeros([256, 720, 3], dtype = np.uint8)
for row in range(0,256,1):
    for column in range(0,720,1):
        y[row, column] = (int(column/4),255,row)  #(hue,saturation,value)HSV

y = cv2.cvtColor(y,cv2.COLOR_HSV2BGR)   #need to convert back to RGB color space as openCV won't display HSV
#cvtColor methond has return type of 'mat' which is an image






cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)






while True:
    ignore, frame = cam.read()

    cv2.imshow('my WEBcam', x)
    cv2.moveWindow('my WEBcam', 0, 0)

    cv2.imshow('my WEBcam2', y)
    cv2.moveWindow('my WEBcam2', 0, 400)

   

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()