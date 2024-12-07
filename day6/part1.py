def move(direction, listToUse, currentCoord):
    listToUse[currentCoord[0]][currentCoord[1]] = "X"

    if listToUse[currentCoord[0] + direction[0]][currentCoord[1] + direction[1]] == "#" and currentCoord[0] != 0 and currentCoord[1] != 0:
        """
        Using rotation matrix 
        [0  1
        -1 0]
        """
        x = direction[1]
        y = direction[0]

        direction[0] = x
        direction[1] = -y

        listToUse[currentCoord[0] + direction[0]][currentCoord[1] + direction[1]] = "^"

        return listToUse, (currentCoord[0] + direction[0], currentCoord[1] + direction[1]), list(direction)

    else:

        listToUse[currentCoord[0] + direction[0]][currentCoord[1] + direction[1]] = "^"
        return listToUse, (currentCoord[0] + direction[0], currentCoord[1] + direction[1]), list(direction)

with open("day6/input.txt", "r") as inputText:
    contents = [i for i in inputText.readlines()]

    actualContents = [list(line.strip()) for line in contents]
    
for x, y in enumerate(actualContents):
    if "^" in y:
        coords = [x, y.index("^")]
        break

direction = [-1, 0]

while True:
    try:
        actualContents, coords, direction = move(direction, actualContents, coords)
    except:    
        timesAppearing = 0
        for i in actualContents:
            for j in i:
                if j == "X":
                    timesAppearing += 1

        print(timesAppearing)
        break