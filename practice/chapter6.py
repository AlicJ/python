#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     30/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *


def drawFace(x,y , r, win):
    face = Circle(Point(x,y), r)
    face.setFill('yellow')
    leye = Circle(Point(x-r*0.5,y-r*0.4),r//10)
    leye.setFill('black')
    reye = Circle(Point(x+r*0.5,y-r*0.4),r//10)
    reye.setFill('black')
    mouth = Rectangle(Point(x-r*0.6,y+r*0.2),Point(x+r*0.6,y+r*0.6))
    mouth.setFill('red')
    face.draw(win)
    leye.draw(win)
    reye.draw(win)
    mouth.draw(win)


def distance(x1,y1,x2,y2):
    dx = x1 - x2
    dy = y1 - y2
    distance = (dx**2 + dy**2)**0.5
    return distance

def main():
    image = input("Please enter the name of the image: ")
    #image ="image.gif"

    win = GraphWin("I do not know!!!",800,600)
    Image(Point(400,300),image).draw(win)
    #drawFace(680,360,500,win)
    while True:
        p1 = win.getMouse()
        cx = p1.getX()
        cy = p1.getY()
        p2 = win.getMouse()
        rx = p2.getX()
        ry = p2.getY()
        print(cx,cy)
        radius = distance(cx,cy,rx,ry)
        drawFace(cx,cy,radius,win)



if __name__ == '__main__':
    main()
