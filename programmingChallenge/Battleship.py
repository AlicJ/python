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
from math import *


def get_input():
    num_lines = eval(input())
    global data
    data = []
    for i in range(num_lines):
        data.append(input().split())
        for j in range(2):
            data[i][j] = int(data[i][j])

    return data


def main():
    data = get_input()
    target = data[0]
    obstacle = []
    speed = 150
    fly_thru = []
    global proj_y
    proj_y = 0
    ob_x = 0
    ob_y = 0

    for i in range(1,len(data),1):
        obstacle.append(data[i])
    for prop in range(1,7,1):
        for degree in range(76):
            new_dg = radians(degree)
            hv = speed * prop * cos(new_dg)
            vv = speed * prop * sin(new_dg)
            for ob in range(len(obstacle)):
                ob_x = obstacle[ob][0]
                ob_y = obstacle[ob][1]

                time = ob_x / (hv)
                proj_y = vv*time + 0.5 * (-9.81) * (time**2)

                if proj_y <= (ob_y + 10):
                    break
            time = target[0] / hv
            proj_y = vv*time + 0.5 * (-9.81) * (time**2)
            if proj_y >= target[1]-10 and proj_y <= target[1] +10:
                break
        if proj_y >= target[1]-10 and proj_y <= target[1] +10:
            print(degree, prop)
            break




main()








