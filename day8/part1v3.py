def antiNodes(listToUse, coords, foundCoords):
    signalToFind = listToUse[coords[0]][coords[1]]

    for i in range(len(listToUse)):
        for j in range(len(listToUse[i])):
            if (i, j) == coords or listToUse[i][j] != signalToFind:
                continue

            yDistance, xDistance = abs(coords[0] - i), abs(coords[1] - j)

            if coords[0] > i:
                y1, y2 = coords[0] + yDistance, i - yDistance

            else:
                y1, y2 = coords[0] - yDistance, i + yDistance

            if coords[1] > j:
                x1, x2 = coords[1] + xDistance, j - xDistance

            else: 
                x1, x2 = coords[1] - xDistance, j + xDistance 

            if 0 <= y1 < len (listToUse) and 0 <= x1 < len (listToUse[y1]):
                if listToUse[y1][x1] == ".":
                    listToUse[y1][x1] = "#"

                if (y1, x1) not in foundCoords:
                    foundCoords.add((y1, x1))

            if 0 <= y2 < len (listToUse) and 0 <= x2 < len (listToUse[y2]):
                if listToUse[y2][x2] == ".":
                    listToUse[y2][x2] = "#"

                if (y2, x2) not in foundCoords:
                    foundCoords.add((y2, x2))

    return listToUse, foundCoords
    
def printBoard(board):
    for i in board:
        for j in i:
            print(j, end="")

        print()

with open("day8/input.txt", "r") as f:
    contents = [[j for j in i.replace("\n", "")] for i in f.readlines()]

foundCoords = set()

for i in range(len(contents)):
    for j in range(len(contents[i])):
        if contents[i][j] == "." or contents[i][j] == "#":
            continue
        else:
            contents, foundCoords = antiNodes(contents, (i, j), foundCoords)
            # print(foundCoords)

printBoard(contents)

print()

print(len(foundCoords))
# print(foundCoords)