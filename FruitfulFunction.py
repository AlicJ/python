#-------------------------------------------------------------------------------
# Name:        Fruitful Function Practice
# Purpose:     Excercise after Chapter 6 - Fruitful Functions
#
# Author:      Alic Jiang
#
# Created:     24/12/2013
# Copyright:   (c) Alic Jiang 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def test(did_pass):
    lineNum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(lineNum)
    else:
        msg = "Test at line {0} FAILED.".format(lineNum)
    print(msg)


def turn_clockwise(direction):
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"


def day_name(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"


def day_num(day):
    if day == "Sunday":
        return 0
    elif day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6


# Used recursion, but is not necessary
#def day_add(day,delta):
#    if day_num(day) + delta >= 7:
#        newNum = delta - 7
#        day_add(day,newNum)
#        return day_add(day,newNum)
#    else:
#        day = day_name(delta+day_num(day))
#        return day


def day_add(day,delta):
    add = abs(delta) % 7
    if delta < 0:
        new = day_num(day) - add
    else:
        new = day_num(day) + add
    if new < 0:
        new += 7
    return day_name(new)


def days_in_month(month):
    if month == "January" or month == "Jan" or month == 1:
        return 31
    if month == "February" or month == "Feb" or month == 2:
        return 28
    if month == "March"  or month == "Mar" or month == 3:
        return 31
    if month == "April" or month == "Apr" or month == 4:
        return 30
    if month == "May" or month == 5:
        return 31
    if month == "June" or month == 6:
        return 30
    if month == "July" or month == 7:
        return 31
    if month == "August" or month == "Aug" or month == 8:
        return 31
    if month == "September" or month == "Sep" or month == 9:
        return 30
    if month == "October" or month == "Oct" or month == 10:
        return 31
    if month == "November" or month == "Nov" or month == 11:
        return 30
    if month == "December" or month == "Dec" or month == 12:
        return 31


def to_secs(hours,minutes,seconds):
    return int(hours * 3600 + minutes * 60 + seconds)


def hours_in(seconds):
    return int(seconds / 3600)


def minutes_in(seconds):
    return int((seconds - hours_in(seconds) * 3600)/60)


def seconds_in(seconds):
    return int(seconds - hours_in(seconds) * 3600 - minutes_in(seconds) * 60)


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def hypotenuse(adj, opp):
    return (adj ** 2 + opp ** 2) ** 0.5


def slope(x1, y1, x2, y2):
    if y1 - y2 == 0:
        slp = 0
    elif x1 - x2 == 0:
        slp = "infinity"
    else:
        slp = (y1 - y2) / (x1 - x2)
    return slp

def intercept(x1, y1, x2, y2):
    slp = slope(x1, y1, x2, y2)
    return y1 - slp * x1


def is_even(n):
    if abs(n) % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    if is_even(n):
        return False
    else:
        return True


def is_factor(f,n):
    if n % f == 0:
        return True
    else:
        False


def is_multiple(m,n):
    return is_factor(n,m)


def f2c(t):
    return round((t - 32) * 5 / 9)


def c2f(t):
    return round(t * 9 / 5 + 32)



