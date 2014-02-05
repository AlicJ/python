#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     27/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ex4():
    phrase = input("Please enter a phrase: ")
    phrase = phrase.split()
    acronym= ""

    for i in phrase:
        acronym +=i[0].upper()

    print(acronym)


def ex5():
    name = input("Please enter your name: ").lower()
    name = name.split()
    sum = 0
    for ele in name:
        for letter in ele:
            sum += ord(letter)-96
    print (sum)