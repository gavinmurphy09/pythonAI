import cv2
print(cv2.__version__)
import numpy as np

boardSize = int(input('what size is your board, boss?'))
numSquares =int(input('and Sir, how many Squares? '))
squareSize = int(boardSize/numSquares)

while True:
    x = np.zeros([boardSize, boardSize,3],dtype = np.uint8)
    cv2.imshow('my checkerboard', x)

    darkColor = (0,0,0)  #tuples are array with paranthesis
    lightColor = (0,0,255)
    nowColor = darkColor  # first element in numpy array 

    for row in range(0, numSquares):   #rows
        for column in range(0, numSquares):  #columns
            x[squareSize*row:squareSize* (row + 1), squareSize * column:squareSize*(column +1)] = nowColor #slice indices must be integers

            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor
      
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor

    cv2.imshow('my checkerboard', x)
            





    if cv2.waitKey(1) & 0xff == ord('q'):
        break
