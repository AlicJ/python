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
from graphics import *

def main():
    file = open("5.11.15.txt","r")
    numOfLines = file.readline()
    global student
    student = []

    for i in range(int(numOfLines)):
        student.append(file.readline().split())
    print(student)

    for i in range(len(student)):
        student[i][1] = int(student[i][1])

    win = GraphWin("Student score", 800, 600)
    leftName = 50
    leftBar = leftName+50
    textY = 40
    intv = 40
    height = 10
    for i in range(len(student)):
        Text(Point(leftName,textY+intv*i), student[i][0]).draw(win)
        Rectangle(Point(leftBar,textY+intv*i-height), Point(leftName+student[i][1]*7,textY+intv*i+height)).draw(win)
    win.getMouse()

    file.close()

if __name__ == '__main__':
    main()


