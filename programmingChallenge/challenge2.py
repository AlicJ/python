#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     25/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>

##Roman Numeral	Decimal Value
##I	1
##V	5
##X	10
##L	50
##C	100
##D	500
##M	1000
#-------------------------------------------------------------------------------
conversion = [("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)]
operation = ["+", "-", "*", "**", "/", "//", "%"]

def rToa(roma):
    arab = 0
    for i in range(len(conversion)):
        if conversion[i][0] in roma:
            arab += conversion[i][1] * roma.count(conversion[i][0])
    return str(arab)


def aTor(arab):
    roma = ""
    left_over = 0
    count = 0

    for i in range(len(conversion)-1,-1,-1):
        count = arab // conversion[i][1]
        left_over = arab % conversion[i][1]
        arab = left_over
        for j in range(count):
            roma += conversion[i][0]
    return roma


def get_input():
    numOfLines = eval(input())
    operation = []
    for i in range(numOfLines):
        operation.append(input())

    return operation


def main():
    get = get_input()
    for element in get:
        for numbers in element:
            if numbers in operation:
                element = element.split(numbers)
                for i in range(len(element)):
                    element[i] = rToa(element[i])
                result = eval(element[0] + numbers + element[1] )
                result = int(result - (result % 1))
                result = aTor(result)
                print(result)


if __name__ == '__main__':
    main()
