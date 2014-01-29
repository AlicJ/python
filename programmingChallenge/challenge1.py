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
from string import punctuation


def main():
    stri = input()
    string = stri.split()
    new_string = []
    new_word = ""
    counter = 0
    global punc
    global puncL
    punc = []
    puncL = []
    n = 0

    for words in string:
        for letter in words:
            if letter in punctuation:
                counter += 1
                punc.append(letter)
                puncL.append(n)
                words = words.replace(letter,"")
                puncL.reverse()

        for i in range(len(words)-1,-1,-1):
            new_word += words[i]
        new_string.append(new_word)
        new_word = ""
        n += 1

    for i in range(len(punc)):
        new_string[puncL[i]] += punc[i]

    output = " ".join(new_string)
    print(output)
    return output



if __name__ == '__main__':
    main()