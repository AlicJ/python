#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     23/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This program creates a file of usernames from a file of names.")

    #infileName = input("What file are the names in? ")
    #outfileName = input("What file should the usernames go in? ")

    infileName = "names.txt"
    outfileName = "users.txt"

    infile = open(infileName, "r")
    outfile = open(outfileName, "w")


    line = infile.read()
    names = line.split("\n")
    for name in names:
        first, last = name.split()
        username = (last[:7]+first[0]).lower() + "@mcmaster.ca"
        print(username, file=outfile)

    infile.close()
    outfile.close()


if __name__ == '__main__':
    main()