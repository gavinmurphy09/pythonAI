import cv2
from cv2 import COLOR_BGR2GRAY
from cv2 import resize
print(cv2.__version__)

rows = int(input('Boss, how many rows do you want?'))
columns = int(input('Boss, how many columns do you want?'))


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #parameter is for port webcam is on,'CAP_DSHOW' = capture directshow, tell windows we are capturing frame to show it

#all this code helps camera run smoother
width = 1280  
height = 720
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)   # capture property frame width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #capture prop fram height
cam.set(cv2.CAP_PROP_FPS, 5)   #set fps
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))  #setting the codec, format so camera runs smoothly on windows

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (int(width/columns), int(height/columns)))  #divide by columns to mantain ratio of picture
    for i in range(0, rows):
        for j in range(0, columns):
            windName = 'Window'+str(i)+' x '+str(j)+'  '+str((height/columns+30)*i)
            cv2.imshow(windName, frame)
            cv2.moveWindow(windName, int(width/columns)*j, int(height/columns+30)*i) #by columns to maintain original box size





    if cv2.waitKey(1) & 0xff == ord('q'):
        break
