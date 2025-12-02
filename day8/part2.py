#I love how my overcomplicated solution for part 1 was perfect for part 2!

from functools import cache, lru_cache

@cache
def distance(index1: tuple, index2: tuple):
    return ((index1[0] - index2[0])**2 + (index1[1] - index2[1])**2) ** (1/2)

@cache
def findFunction(point1: tuple, point2: tuple):
    if point2[1] > point1[1]:
        gradiant = (point2[0] - point1[0]) / (point2[1] - point1[1]) #Our 2d list has y before x
    elif point2[1] < point1[1]: 
        gradiant = (point1[0] - point2[0]) / (point1[1] - point2[1]) #Our 2d list has y before x
    else:
        gradiant = 0

    #y - y1 = m(x - x1)
    return lambda x: gradiant * (x - point1[1]) + point1[0]

def findAntiNodes(listToUse, coords, foundCoords: set):
    """
    Returns: 
        listToUse, alreadyFound Pairs
    """

    targetNode = listToUse[coords[0]][coords[1]]
    coordsToFind = []

    for i in range(len(listToUse)):
        for j in range(len(listToUse[i])): 
            if (i, j) == coords: 
                continue
            elif listToUse[i][j] == targetNode:
                if (coords, (i, j)) in foundCoords:
                    continue
                else:
                    coordsToFind.append((i, j))
    
    for i in coordsToFind:
        func = findFunction(coords, i)
        
        for j in range(0, len(listToUse[0])):
            y = float(func(j))

            try:
                if y.is_integer() and (int(y), j) not in foundCoords and listToUse[int(y)][j] and int(y) >= 0 and j >= 0:
                    foundCoords.add((int(y), j))
                    
                    if listToUse[int(y)][j] == ".":
                        listToUse[int(y)][j] = "#"

            except IndexError:
                continue

    return listToUse, foundCoords

def printBoard(board):
    for i in board:
        for j in i:
            print(j, end="")

        print()

with open("day8/input.txt", "r") as f:
    contents = [[j for j in i.replace("\n", "")] for i in f.readlines()]

foundCoords = set()

onTop = 0

for i in range(len(contents)):
    for j in range(len(contents[i])):
        if contents[i][j] == "." or contents[i][j] == "#":
            continue
        else:
            contents, foundCoords = findAntiNodes(contents, (i, j), foundCoords)
            # print(foundCoords)

printBoard(contents)

print()

print(len(foundCoords))
# print(foundCoords)