#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     09/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

def timeTest(code):
    t0 = time.clock()
    eval(code)
    t1 = time.clock()
    print("It takes", t1-t0, "seconds to excute the code.")