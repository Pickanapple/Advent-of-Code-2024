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

def findAntiNodes(listToUse, coords, alreadyFoundPairs: set, foundCoords: set):
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
                if (coords, (i, j)) in alreadyFoundPairs or ((i, j), coords) in alreadyFoundPairs:
                    continue
                else:
                    coordsToFind.append((i, j))
    
    for i in coordsToFind:
        func = findFunction(coords, i)
        
        xDistance = abs(i[1] - coords[1])

        if coords[1] > i[1]:
            x1, x2 = coords[1] + xDistance, i[1] - xDistance
        else:
            x1, x2 = coords[1] - xDistance, i[1] + xDistance

        y1, y2 = func(x1), func(x2)

        try: 
            if float(x1).is_integer() and y1.is_integer():
                if listToUse[int(y1)][int(x1)] == ".":
                    listToUse[int(y1)][int(x1)] = "#"

                    if abs(int(x1)) == int(x1) and abs(int(y1)) == int(y1):
                        foundCoords.add((int(y1), int(x1)))
                        alreadyFoundPairs.add((coords, (int(y1), int(x1))))

                elif listToUse[int(y1)][int(x1)] != "#" and (int(y1), int(x1)) != coords and (int(y1), int(x1)) != i and (int(x1), int(y1)) not in foundCoords:
                    print("At an antenna")

                    if abs(int(y1)) == int(y1) and abs(int(x1)) == int(x1):
                        alreadyFoundPairs.add((coords, (int(y1), int(x1))))
                        foundCoords.add((int(y1), int(x1)))
        except IndexError:
            pass

        try:
            if float(x2).is_integer() and float(y2).is_integer():
                if listToUse[int(y2)][int(x2)] == ".":
                    if abs(int(y2)) == int(y2) and abs(int(x2)) == int(x2):
                        print("At an antenna")
                        listToUse[int(y2)][int(x2)] = "#"
                        foundCoords.add((int(y2), int(x2)))
                        alreadyFoundPairs.add((coords, (int(y2), int(x2))))

            elif listToUse[int(y2)][int(x2)] != "#" and (int(y2), int(x2)) != coords and (int(y2), int(x2)) != i and (int(x2), int(y2)) not in foundCoords:
                    # print((int(y2), int(x2)) in foundCoords)
                    
                    if abs(int(y2)) == int(y2) and abs(int(x2)) == int(x2):
                        foundCoords.add((int(y2), int(x2)))
                        alreadyFoundPairs.add((coords, (int(y2), int(x2))))

        except IndexError: 
            pass

    return listToUse, alreadyFoundPairs, foundCoords

def printBoard(board):
    for i in board:
        for j in i:
            print(j, end="")

        print()

with open("day8/testInput.txt", "r") as f:
    contents = [[j for j in i.replace("\n", "")] for i in f.readlines()]

foundCoordPairs = set()
foundCoords = set()

onTop = 0

for i in range(len(contents)):
    for j in range(len(contents[i])):
        if contents[i][j] == "." or contents[i][j] == "#":
            continue
        else:
            contents, foundCoordPairs, foundCoords = findAntiNodes(contents, (i, j), foundCoordPairs, foundCoords)
            # print(foundCoords)

printBoard(contents)

print()

print(len(foundCoords))
# print(foundCoords)