import math

def main():
    inputFile = open("input.txt","r")
    line = inputFile.read()

    grid = line.split("\n")
    grid[0] = int(grid[0])

    for i in range(grid[0]):
        if "p" in grid[i+1]:
            locationRow = i+1

    locationColumn = grid[locationRow].find("p")

    robot = math.floor(grid[0]/2)

    H = locationColumn - robot

    V = locationRow - 1 - robot

    if H < 0:
        for i in range(abs(H)):
            print("LEFT")
    else:
        for i in range(H):
            print("RIGHT")

    if V < 0:
        for i in range(abs(V)):
            print("UP")
    else:
        for i in range(V):
            print("DOWN")


main()