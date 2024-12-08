"""The first thing that I did is export the path to inputWithPath.txt
This makes the code running time quicker

Code used: 
startcoords = coords[::]

Code block to generate path

actualContents[startcoords[0]][startcoords[1]] = "^"

with open("day6/inputWithPath.txt", "w") as save:
    for i in actualContents:
        for j in i:
            save.write(j)

        save.write("\n")"""

#I am assuming that if it takes more than MAXCHECKINGTIME seconds per obstacle that it is stuck in a loop, and therefore automatically
#Counting it. This was not required in the end

import copy
import time

MAXCHECKINGTIME = 100
STARTTIME = time.time()

skippedBecauseOfTimeout = 0

def placeObstacle(location, listToUse):
    listToModify = copy.deepcopy(listToUse)

    listToModify[location[0]][location[1]] = "O"
    return listToModify


def rotate(direction):
    """
    Using rotation matrix 
    [0  1
    -1 0]
    """
    x = direction[1]
    y = direction[0]

    direction[0] = x
    direction[1] = -y

    return direction

def move(direction, listToUse, currentCoord, timesMetObstacle):
    global startTime
    
    if time.time() > startTime + MAXCHECKINGTIME:
        global skippedBecauseOfTimeout
        skippedBecauseOfTimeout += 1
        print(f"Skipped because time was more than {MAXCHECKINGTIME}")

        raise RecursionError("Infinite loop!")

    if (currentCoord[0] + direction[0]) < 0 or (currentCoord[1] + direction[1]) < 0:
        raise IndexError("Out of list")

    while listToUse[currentCoord[0] + direction[0]][currentCoord[1] + direction[1]] == "#" or listToUse[currentCoord[0] + direction[0]][currentCoord[1] + direction[1]] == "O":
        direction = rotate(direction)
    
    if listToUse[currentCoord[0] + direction[0]][currentCoord[1] + direction[1]] == "*":
        timesMetObstacle += 1

        if timesMetObstacle > len(listToUse) * len(listToUse[0]): #Could probably be more efficient, but it works
            raise RecursionError("Infinite loop!")

    listToUse[currentCoord[0] + direction[0]][currentCoord[1] + direction[1]] = "*"
    
    return listToUse, (currentCoord[0] + direction[0], currentCoord[1] + direction[1]), list(direction), timesMetObstacle

with open("day6/inputWithPath.txt", "r") as inputText:
    contents = [i for i in inputText.readlines()]

    actualContents = [list(line.strip()) for line in contents]
    
for x, y in enumerate(actualContents):
    if "^" in y:
        coords = [x, y.index("^")]
        break

startCoords = coords[::]
validObstacles = 0

for i in range(len(actualContents)):
    for j in range(len(actualContents[i])):
        if actualContents[i][j] == "X":
            startTime = time.time()
            # print(f"Found place for obstacle {i, j}. {len(actualContents)}")
            listToUse = placeObstacle((i, j), actualContents[::])
            coords = startCoords
            direction = [-1, 0]
            timesMetObstacle = 0

            while True:
                try:
                    listToUse, coords, direction, timesMetObstacle = move(direction, listToUse, coords, timesMetObstacle)
                except IndexError:    
                    break
                except RecursionError:
                    validObstacles += 1
                    break

print("\n------------\n")

print(f"validObstacles: {validObstacles}\nSkipped because of time: {skippedBecauseOfTimeout}")
print(f"Took {(time.time() - STARTTIME):.3f} seconds")