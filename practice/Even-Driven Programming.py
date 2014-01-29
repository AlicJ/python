#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     29/12/2013
# Copyright:   (c) Alic Jiang 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def keyboard():
    turtle.setup(400,500)                # Determine the window size
    wn = turtle.Screen()                 # Get a reference to the window
    wn.title("Handling keypresses!")     # Change the window title
    wn.bgcolor("lightgreen")             # Set the background color
    tess = turtle.Turtle()               # Create our favorite turtle

    # The next four functions are our "event handlers".
    def h1():
       tess.forward(30)

    def h2():
       tess.left(45)

    def h3():
       tess.right(45)

    def h4():
        wn.bye()                        # Close down the turtle window

    # These lines "wire up" keypresses to the handlers we've defined.
    wn.onkey(h1, "Up")
    wn.onkey(h2, "Left")
    wn.onkey(h3, "Right")
    wn.onkey(h4, "q")

    # Now we need to tell the window to start listening for events,
    # If any of the keys that we're monitoring is pressed, its
    # handler will be called.
    wn.listen()
    wn.mainloop()


def mouse():
    turtle.setup(400,500)
    wn = turtle.Screen()
    wn.title("How to handle mouse clicks on the window!")
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("purple")
    tess.pensize(3)
    tess.shape("circle")

    def h1(x, y):
        wn.title("Got click at coords {0}, {1}".format(x, y))
        tess.goto(x, y)

    wn.onclick(h1)  # Wire up a click on the window.
    wn.mainloop()


def mouse2():
    turtle.setup(400,500)              # Determine the window size
    wn = turtle.Screen()               # Get a reference to the window
    wn.title("Handling mouse clicks!") # Change the window title
    wn.bgcolor("lightgreen")           # Set the background color
    tess = turtle.Turtle()             # Create two turtles
    tess.color("purple")
    alex = turtle.Turtle()             # Move them apart
    alex.color("blue")
    alex.forward(100)

    def handler_for_tess(x, y):
        wn.title("Tess clicked at {0}, {1}".format(x, y))
        tess.left(42)
        tess.forward(30)

    def handler_for_alex(x, y):
        wn.title("Alex clicked at {0}, {1}".format(x, y))
        alex.right(84)
        alex.forward(50)

    tess.onclick(handler_for_tess)
    alex.onclick(handler_for_alex)

    wn.mainloop()


def timer1():
    turtle.setup(400,500)
    wn = turtle.Screen()
    wn.title("Using a timer")
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("purple")
    tess.pensize(3)

    def h1():
        tess.forward(100)
        tess.left(56)

    wn.ontimer(h1, 2000)
    wn.mainloop()


def timer2():
    turtle.setup(400,500)
    wn = turtle.Screen()
    wn.title("Using a timer to get events!")
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("purple")

    def h1():
        tess.forward(100)
        tess.left(66)
        wn.ontimer(h1, 60)

    h1()
    wn.mainloop()