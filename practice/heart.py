#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     25/05/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import *
from graphics import *

def heartEq(t):
    x = 16*sin(t)**3
    y = 13*cos(t) - 5*cos(2*t) - 2*cos(3*t) - cos(4*t)
    p = Point(x,y)
    return p

def drange(start, stop, step):
     r = start
     l = []
     while r <= stop:
        l.append(r)
        r += step
     return l

def getLength(line):
    p1 = line.getP1()
    p2 = line.getP2()
    length =((p1.getX()-p2.getX())**2 + (p1.getY()-p2.getY())**2)**0.5
    return length


def main():
    win = GraphWin("Heart", 600, 600)
    w = 20
    win.setCoords(-w,-w,w,w)
    listOfPoints = []

    # draws the points on the heart
    for i in drange(-pi,pi,0.1):
        point = heartEq(i)
        #print(point.getX(),point.getY())
        listOfPoints.append(point)
        point.draw(win)

    numOfPoints = len(listOfPoints)
    numOfLines = 0
    totalLength = 0
    perimeter = 0
    step = 5

    # draws the outline
    for i in range(numOfPoints-1):
        line = Line(listOfPoints[i], listOfPoints[i+1])
        perimeter +=  getLength(line)
        line.setFill("red")
        line.draw(win)
    print(perimeter)

    # connects the dots on the left half
    for i in range(numOfPoints//2):
        for j in range(1,numOfPoints//2,step):
            line = Line(listOfPoints[j], listOfPoints[i])
            totalLength +=  getLength(line)
            line.setFill("red")
            line.draw(win)
            numOfLines += 1

    # connects the dots on the right half
    for i in reversed(range(numOfPoints//2, numOfPoints,1)):
        for j in reversed(range(numOfPoints//2+1, numOfPoints,step)):
            line = Line(listOfPoints[j], listOfPoints[i])
            totalLength +=  getLength(line)
            line.setFill("red")
            line.draw(win)
            numOfLines += 1


    print(totalLength)
    print(numOfLines)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
