#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     04/02/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from timeTest import *

a = 1
b = 2


def m1():
    if a > b:
        return b
    else:
        return a


def m2():
    return min(a,b)


def m3():
    return (a + b - abs(a - b)) // 2


timeTest(m1())
timeTest(m2())
timeTest(m3())
