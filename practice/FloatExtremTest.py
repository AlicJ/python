
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     23/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import timeTest


def main(ty=True):
    num = 1
    store = 0
    count = 0
    if ty:
        while num != 0:
            store = num
            num /= 2
            count += 1
        print(store, count)
    else:
        while float(num) != float("inf"):
            store = num
            num *= 1.001
            count += 1
        print(store, count)


if __name__ == '__main__':
    timeTest.timeTest(main())
    timeTest.timeTest(main(False))
