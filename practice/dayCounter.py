#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     02/03/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from graphics import *
# Add GUI!!!

def leap(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 ==0:
        leap = True
    return leap


def days(month, year):
    small_month = [4, 6, 9, 11]
    if month in small_month:
        return 30
    elif month == 2:
        if leap(year):
            return 29
        else:
            return 28
    else:
        return  31


def monthDiff(startMonth, startYear, startDay, endDay):
    # add the days left in the start month
    # add the days before the deadline in the end month
    return days(startMonth, startYear) - startDay + endDay -1


def calculation(startDay, startMonth, startYear, endDay, endMonth, endYear):
    dayCount = 0
    # if there is a difference between years
    if endYear != startYear:
        dayCount += monthDiff(startMonth, startYear, startDay, endDay)
        # add the days left in the start year
        for i in range(startMonth + 1, 12+1, 1):
            dayCount += days(i, startYear)
        # add days before the deadline in the end year
        for i in range(1, endMonth, 1):
            dayCount += days(i, endYear)
        # if the difference between years are greater than 2
        if endYear - startYear >= 2:
            for i in range(1, endYear - startYear, 1):
                if leap(startYear + i):
                    dayCount += 366
                else:
                    dayCount += 365
        # if they are neighbor years
        else:
            dayCount += monthDiff(startMonth, startYear, startDay, endDay)
    # if they are in the same year
    else:
        # if there is a difference between month
        if endMonth != startMonth:
            dayCount += monthDiff(startMonth, startYear, startDay, endDay)
            if endMonth - startMonth >= 2:
                # add the days between the two months
                for i in range(1, endMonth - startMonth, 1):
                    dayCount += days(startMonth + i, startYear)
        # if they are in the same month:
        else:
            dayCount = endDay - startDay - 1
    return dayCount


def shadowBox(x1, y1, x2, y2, win):
    bg1 = Rectangle(Point(x1,y1), Point(x2,y2))
    bg1.setOutline("black")
    bg2 = Rectangle(Point(x1,y1), Point(x2-1,y2-1))
    bg2.setOutline(color_rgb(223,223,223))
    bg3 = Rectangle(Point(x1+1,y1+1), Point(x2-1,y2-1))
    bg3.setOutline(color_rgb(128,128,128))
    bg4 = Rectangle(Point(x1+1,y1+1), Point(x2-2,y2-2))
    bg4.setOutline("white")
    b = Rectangle(Point(x1+2,y1+2), Point(x2-2,y2-2))
    b.setOutline(color_rgb(192,192,192))
    b.setFill(color_rgb(192,192,192))

    bg1.draw(win)
    bg2.draw(win)
    bg3.draw(win)
    bg4.draw(win)
    b.draw(win)


def main():
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    winX = 600
    winY = 480
    winMargin = 20
    x = 200
    y = winY//4
    dw = 40
    dh = 30
    run = True
    buttonX = x
    buttonY = 180
    buttonW = 200
    buttonH = 50

    win = GraphWin("Date counter - Alic Jiang", winX,winY)
    win.setBackground(color_rgb(0,128,128))
    shadowBox(winMargin+3,winMargin+3,winX-winMargin,winY-winMargin,win)

    # draw the blue title
    titleBox = Rectangle(Point(winMargin+7,winMargin+7), Point(winX-winMargin-4,winMargin+24))
    titleBox.setOutline(color_rgb(0,0,128))
    titleBox.setFill(color_rgb(0,0,128))
    titleBox.draw(win)
    # draw the title text
    title = Text(Point(70,36), "Date Counter")
    title.setSize(10)
    title.setStyle("bold")
    title.setFill("white")
    title.draw(win)
    # draw the close button
    clX = winX-winMargin-21
    clY = winMargin+9
    clW = 16
    clH = 14
    shadowBox(clX, clY, clX+clW, clY+clH, win)
    cha = Text(Point(clX+8,clY+7),"X")
    cha.setSize(10)
    cha.setFace("courier")
    cha.setStyle("bold")
    cha.draw(win)

    Text(Point(x, y), "Start date:").draw(win)
    Text(Point(x, y+dh), "End date:").draw(win)
    Text(Point(x+dw*3.4, y-dh), "dd       mm        yyyy").draw(win)
    __startDay = Entry(Point(x+dw*2, y), 3)
    __startMonth = Entry(Point(x+dw*3.2, y), 3)
    __startYear = Entry(Point(x+dw*4.7, y), 5)
    __endDay = Entry(Point(x+dw*2, y+dh), 3)
    __endMonth = Entry(Point(x+dw*3.2, y+dh), 3)
    __endYear = Entry(Point(x+dw*4.7, y+dh), 5)
    __startDay.draw(win)
    __startMonth.draw(win)
    __startYear.draw(win)
    __endDay.draw(win)
    __endMonth.draw(win)
    __endYear.draw(win)

    shadowBox(buttonX,buttonY,buttonX+buttonW,buttonY+buttonH,win)
    Text(Point(buttonX+buttonW*0.5,buttonY+buttonH*0.5),"Calculate!").draw(win)

    while run:
        click = win.getMouse()

        #if click on the button
        if click.getX() >= buttonX and click.getX()<= buttonX+buttonW and click.getY() >= buttonY and click.getY() <= buttonY+buttonH:
            startDay = eval(__startDay.getText())
            startMonth = eval(__startMonth.getText())
            startYear = eval( __startYear.getText())
            endDay = eval(__endDay.getText())
            endMonth = eval(__endMonth.getText())
            endYear = eval( __endYear.getText())

            result = calculation(startDay, startMonth, startYear, endDay, endMonth, endYear)
            text = "There are " + str(result) + " days between " + str(startDay) + " " + month[startMonth-1] + " " + str(startYear) + " and " + str(endDay) + " " + month[endMonth-1] + " " + str(endYear) + "."
            Text(Point(winX//2,winY//2+25), text).draw(win)

        elif click.getX() >= clX and click.getX()<= clX+clW and click.getY() >= clY and click.getY() <= clY+clH:
            run=False

    win.close()


if __name__ == '__main__':
    main()
