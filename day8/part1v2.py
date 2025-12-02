def findAntiNodes(listToUse, coords, foundNodes):
    target = listToUse[coords[0]][coords[1]]

    for i in range(len(listToUse)):
        for j in range(len(listToUse[i])):
            if (i, j) == coords or listToUse[i][j] != target:
                continue

            pass
    
    return listToUse, foundNodes

def printBoard(board):
    for i in board:
        for j in i:
            print(j, end="")

        print()

with open("day8/testInput.txt", "r") as f:
    contents = [[j for j in i.replace("\n", "")] for i in f.readlines()]

foundCoords = set()

for i in range(len(contents)):
    for j in range(len(contents[i])):
        if contents[i][j] == "." or contents[i][j] == "#":
            continue
        else:
            contents, foundCoords = findAntiNodes(contents, (i, j), foundCoords)
            print(foundCoords)

printBoard(contents)

print()

print(len(foundCoords))
print(foundCoords)