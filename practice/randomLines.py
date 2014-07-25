#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     06/06/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
from random import *
from time import *

def randomNum(_range, _status=2):
    # status: 0 for 0~_range , 1 for -_range~0, 2 for -_range~_range
    if _status == 0:
        num = randint(0,_range)
    elif _status == 1:
        num = randint(-_range,0)
    elif _status == 2:
        num = randint(-_range, _range)
    else:
        num = _range
    return num

def main():
    numOfPoints = 5000
    deltDistance = 3
    startX = 19
    startY = 19
    listOfPoints = []
    status = 2
    # status: 0 for 0~_range , 1 for -_range~0, 2 for -_range~_range
    w = 300
    timeStep = 0
    test = True

    if not test:
        numOfPoints = eval(input("How many points do you want?"))
        deltDistance = eval(input("What is the maximum distance between points?"))
        startX = eval(input("What is the x-coordinate of the initial point?"))
        startY = eval(input("What is the y-coordinate of the initial point?"))
        ##status = eval(input("Do you want 1.positive deltX/deltY only, 2.negative deltX/deltY only, or 3.mixed?")) -1
        timeStep = eval(input("What is the time interval between drawing each line? (in milliseconds, 0 for no inerval)"))

    win = GraphWin("Random lines", w*2, w*2)
    win.setCoords(-w,-w,w,w)

    p1 = Point(startX, startY)
    listOfPoints.append(p1)

    t0 = clock()

    for i in range(numOfPoints):
        deltX = randomNum(deltDistance, status)
        deltY = randomNum(deltDistance, status)
        p2 = Point(p1.getX()+deltX, p1.getY()+deltY)
        p2X = p2.getX()
        p2Y = p2.getY()
        while not (p2X > -w and p2X < w and p2Y > -w and p2Y < w):
            deltX = randomNum(deltDistance, status)
            deltY = randomNum(deltDistance, status)
            p2 = Point(p1.getX()+deltX, p1.getY()+deltY)
            p2X = p2.getX()
            p2Y = p2.getY()

        listOfPoints.append(p2)
        p1 = p2

    t1 = clock()

    for i in range(1, len(listOfPoints), 1):
        color = color_rgb(randomNum(255,0),randomNum(255,0),randomNum(255,0))
        line = Line(listOfPoints[i-1], listOfPoints[i])
        line.setFill(color)
        line.draw(win)
        sleep(timeStep/1000)

    t2 = clock()
    print(t1-t0)
    print(t2-t1)
    print(t2-t0)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
##    win = GraphWin("Random lines", 600, 600)
##    Line(Point(15,15),Point(30,30)).draw(win)
##    win.getMouse()
##    win.close()


