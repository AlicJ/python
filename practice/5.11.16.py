#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     27/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import *
from graphics import *

def write(num):
    outFile = open("5.11.16.txt","w")
    for i in range(num):
        score = randint(0,10)
        print(score,file=outFile)
    outFile.close()


def main():
    write(100)
    score = []
    inFile = open("5.11.16.txt","r")

    for i in range(1,11,1):
        score.append([i,0])

    for i in range(100):
        s = int(inFile.readline())
        score[s-1][1] +=1
    print(score)

    win = GraphWin("Score Count", 800, 600)
    left = 50
    intv = 75
    width = 10
    top = 550
    for i in range(10):
        Text(Point(left+intv*i,top), score[i][0]).draw(win)
        Rectangle(Point(left+intv*i-width,top - 20), Point(left+intv*i+width, top -20 - score[i][1]*10)).draw(win)
        #Rectangle(Point(leftBar,textY+intv*i-height), Point(leftName+student[i][1]*7,textY+intv*i+height)).draw(win)
    win.getMouse()


    inFile.close()

if __name__ == '__main__':
    main()




