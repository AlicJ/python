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

def goDown(turtle,pixel):  #travels downward without drawing
    turtle.penup()
    turtle.right(90)
    turtle.forward(pixel)
    turtle.left(90)
    turtle.pendown()

def goUp(turtle,pixel): #travels upward without drawing
    turtle.penup()
    turtle.left(90)
    turtle.forward(pixel)
    turtle.right(90)
    turtle.pendown()

precision = input("Enter preferable precision (2 to 8), or type any other number for demostration: ")

pNc = [
    (4,"red"),
    (8,"orange"),
    (16,"yellow"),
    (32,"green"),
    (64,"cyan"),
    (128,"blue"),
    (256,"purple"),
    (512,"white")
]

precision = int(precision)

turtle.setup(1280,400)
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("black")
wn.title("Tess & Alex")

circ = turtle.Turtle()       # Create alex
circ.color("blue")
circ.pensize(1)

alex = turtle.Turtle

if precision >= 2 and precision <= 8:
    prec = 2**precision
    poly = 360 / prec
    for i in range (prec):
        circ.forward(poly)
        circ.left(poly)
    goDown(circ,20)
    circ.write("Percision: " + str(precision), font=('Courier', 10, 'normal'))
    goDown(circ,16)
    circ.write(str(prec) + " sided polygon", font=('Courier', 10, 'normal'))


else:
    circ.penup()
    circ.forward(-600)     # This moves alex, but no line is drawn
    circ.pendown()
    for count in range(8):
        for i in range(pNc[count][0]):
            poly = 360 / pNc[count][0]
            circ.color(pNc[count][1])
            circ.forward(poly)
            circ.left(poly)

        goDown(circ,20)

        circ.write("Percision: " + str(count+2), font=('Courier', 10, 'normal'))

        goDown(circ,16)

        circ.write(str(pNc[count][0]) + " sided polygon", font=('Courier', 10, 'normal'))

        goUp(circ,36)

        circ.penup()
        circ.forward(160)
        circ.pendown()


wn.mainloop()


