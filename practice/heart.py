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
# add lines into a list and then draws them to see if it helps with the speed
from math import cos, sin, pi
from graphics import *
from random import randint
from time import sleep

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

    w = 20
    listOfPoints = []
    numOfPoints = 0
    numOfLines = 0
    totalLength = 0
    perimeter = 0
    pointStep = 0.1
    lineStep = 2
    preference = "" #random or ordered
    choice = " "
    outline = False
    listOfLinesLeft = []
    listOfLinesRight = []

    choice = input("Which one do you prefer, (a)order, (b)randomness, or (c)surprise me?\n")
##    if choice == "a" or choice == "A" or choice == "random" or choice == "1" or choice == "randomness": preference = "random"
##    else: preference = "order"

    win = GraphWin("Heart", 600, 600)
    win.setCoords(-w,-w,w,w)

    # draws the points on the heart
    for i in drange(-pi, pi, pointStep):
        point = heartEq(i)
        listOfPoints.append(point)
        #print(point.getX(),point.getY())
        #point.setFill("red")
        #point.draw(win)

    numOfPoints = len(listOfPoints)

    if outline:
        # draws the outline
        for i in range(numOfPoints-1):
            line = Line(listOfPoints[i], listOfPoints[i+1])
            perimeter +=  getLength(line)
            line.setFill("red")
            line.draw(win)


    if choice =="a": # order
        # connects the dots on the left half
        for i in range(numOfPoints//2):
            for j in range(1,numOfPoints//2,lineStep):
                line = Line(listOfPoints[j], listOfPoints[i])
                line.setFill("red")
                listOfLinesLeft.append(line)
                #totalLength +=  getLength(line)
                #numOfLines += 1

        # connects the dots on the right half
        for i in reversed(range(numOfPoints//2, numOfPoints,1)):
            for j in reversed(range(numOfPoints//2+1, numOfPoints,lineStep)):
                line = Line(listOfPoints[j], listOfPoints[i])
                line.setFill("red")
                listOfLinesRight.append(line)
                #numOfLines += 1
                #totalLength +=  getLength(line)

        for i in range(len(listOfLinesLeft)):
            listOfLinesLeft[i].draw(win)
            listOfLinesRight[i].draw(win)

    elif choice == "b": # random
        # connects the dots randomly
        for i in range(800):
            pt1 = randint(0, numOfPoints-1)
            pt2 = randint(0, numOfPoints-1)
            while abs(pt2-pt1) > 6 or abs(pt2-pt1) < 4:
                pt2 = randint(0, numOfPoints-1)
            line = Line(listOfPoints[pt1], listOfPoints[pt2])
            #totalLength +=  getLength(line)
            line.setFill("red")
            line.draw(win)
            sleep(0.0001)
            #numOfLines += 1

    elif choice == "c":
        for i in range(5,numOfPoints,1):
            for j in range(1,8,2):
                line = Line(listOfPoints[i], listOfPoints[i-j])
                line.setFill("red")
                line.draw(win)
                sleep(0.01)



    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
