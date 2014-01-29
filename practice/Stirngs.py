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

def find(string, char, start=0, end=None):
    ix = start
    if end is None:
        end = len(string)
    while ix < end:
        if string[ix] == ch:
            return ix
        ix += 1
    return -1


def ducks():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "uack")
        else:
            print(letter + suffix)


def reverse(string):
    newStr = ""
    for n in range(len(string)-1,-1,-1):
        newStr += string[n]
    return newStr


def mirror(string):
    return string + reverse(string)


def remove_letter(char, string):
    newStr = ""
    for letter in string:
        if letter != char:
            newStr += letter
    return newStr


def is_palindorme(string):
    return string == reverse(string)