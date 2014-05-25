#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     18/12/2013
# Copyright:   (c) Alic Jiang 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

polygonData = [
    (4,"red"),
    (8,"orange"),
    (16,"yellow"),
    (32,"green"),
    (64,"cyan"),
    (128,"blue"),
    (256,"purple"),
    (512,"white")
]

def moveDown(turtle,pixel):  #travels downward without drawing
    turtle.penup()
    turtle.right(90)
    turtle.forward(pixel)
    turtle.left(90)
    turtle.pendown()

def moveUp(turtle,pixel): #travels upward without drawing
    turtle.penup()
    turtle.left(90)
    turtle.forward(pixel)
    turtle.right(90)
    turtle.pendown()

def main():
    # get user input of precision
    precision = input("Enter preferable precision (2 to 8), or type any other number for demostration: ")
    if not precision:
        precision = 15
    else:
        precision = int(precision)
    # initialize window
    wn = turtle.Screen()         # Set up the window and its attributes
    wn.setup(1280,400)
    wn.bgcolor("black")
    wn.title("Tess & Alex")
    # initialize turtle
    polygon = turtle.Turtle()
    polygon.color("blue")
    polygon.pensize(1)
    polygon.speed(0)
    # start drawing the polygon(s)
    if precision >= 2 and precision <= 8:
        precision = 2**precision
        angle = 360 / precision
        for i in range (precision):
            polygon.forward(angle)
            polygon.left(angle)
        moveDown(polygon,20)
        polygon.write("Percision: " + str(precision), font=('Courier', 10, 'normal'))
        moveDown(polygon,16)
        polygon.write(str(precision) + " sided polygon", font=('Courier', 10, 'normal'))
    else:
        polygon.penup()
        polygon.forward(-600)     # This moves alex, but no line is drawn
        polygon.pendown()
        for shape in range(8):
            for i in range(polygonData[shape][0]):
                angle = 360 / polygonData[shape][0]
                polygon.color(polygonData[shape][1])
                polygon.forward(angle)
                polygon.left(angle)

            moveDown(polygon,20)
            polygon.write("Percision: " + str(shape+2), font=('Courier', 10, 'normal'))
            moveDown(polygon,16)
            polygon.write(str(polygonData[shape][0]) + " sided polygon", font=('Courier', 10, 'normal'))
            goUp(polygon,36)

            polygon.penup()
            polygon.forward(160)
            polygon.pendown()


    wn.mainloop()

if __name__ == '__main__':
    main()