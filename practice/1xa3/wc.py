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

def main():
    fileName = input("Please enter a file name: ")
    #fileName = "article.txt"
    file = open(fileName,"r")
    article = file.read()
    article = article.split("\n")

    numOfLines = len(article)
    numOfWrods = 0
    numOfChars = 0
    numOfChars2 = 0

    for line in article:
        for word in line:
            for char in word:
                numOfChars2 += 1

    for lines in range(len(article)):
        line = article[lines].split()

        numOfWrods += len(line)
        for words in line:
            for chars in words:
                numOfChars += 1

    print("There are", numOfLines, "lines,",numOfWrods, "words,",numOfChars,"characters (without space),","and",numOfChars2,"characters(with spaces).")

if __name__ == '__main__':
    main()
