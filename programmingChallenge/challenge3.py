#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     25/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import trunc

def convert(string):
    string = string.split()
    time = []
    for i in range(0,3,2):
        hour, minute = string[i].split(":")
        if string[i+1] == "AM":
            minute = eval(hour) * 60 + eval(minute)
        else:
            if hour == '12':
                minute = eval(hour) * 60 + eval(minute)
            else:
                minute = (eval(hour) + 12) * 60 + eval(minute)
        time.append(minute)
    return time

def area(start,end):
    money = 0
    loop = True
    if start >= 420 and start < 1320 and (end - start) > 60:
        money += 2
    start += 60

    while loop:
        if start >= 0 and start < 420:
            if end < 420:
                loop = False
            start = 420

        elif start >= 420 and start < 720:
            if end < 720:
                money += ((end - start) / 30)*0.5
                loop = False
            else:
                money += ((719 - start) / 30)*0.5
            start = 720

        elif start >= 720 and start < 1020:
            if end < 1020:
                money += ((end - start) / 20) * 0.5
                loop = False
            else:
                money += ((1019 - start) / 20) * 0.5
            start = 1020

        elif start >= 1020 and start < 1320:
            if end < 1320:
                money += ((end - start) / 60) * 0.75
                loop = False
            else:
                money += ((1319 - start) / 60) * 0.75
            start = 1320

        else:
            money  += 0
            loop = False

    money = trunc(money*100)/100
    money = round(money,2)
    print("$" + str(money))



def main():
    time = convert(input())
    area(time[0],time[1])

if __name__ == '__main__':
    main()
