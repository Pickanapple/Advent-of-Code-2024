import sys
sys.setrecursionlimit(2147483647)

def search(listToCheck, coordinate):
    global foundCoord

    currentNum = listToCheck[coordinate[0]][coordinate[1]]
    somethingHappened = False

    totalFound = 0

    if currentNum == 9:
        if coordinate in foundCoord:
            return 0
        
        foundCoord.append(coordinate)
        return 1

    if coordinate[0] < len(listToCheck) - 1:
        if listToCheck[coordinate[0] + 1][coordinate[1]] == currentNum + 1: 
            totalFound += search(listToCheck, (coordinate[0] + 1, coordinate[1]))
            somethingHappened = True

    if coordinate[0] != 0:
        if listToCheck[coordinate[0] - 1][coordinate[1]] == currentNum + 1: 
            totalFound += search(listToCheck, (coordinate[0] - 1, coordinate[1]))
            somethingHappened = True

            
    if coordinate[1] < len(listToCheck[0]) - 1:
        if listToCheck[coordinate[0]][coordinate[1] + 1] == currentNum + 1: 
            totalFound += search(listToCheck, (coordinate[0], coordinate[1] + 1))
            somethingHappened = True
            
    if coordinate[1] != 0:
        if listToCheck[coordinate[0]][coordinate[1] - 1] == currentNum + 1: 
            totalFound += search(listToCheck, (coordinate[0], coordinate[1] - 1))
            somethingHappened = True

    if not somethingHappened:
        return 0
    
    return totalFound
        
with open("day10/input.txt", "r") as inputText: 
    contents = [[int(i) for i in j.removesuffix("\n")] for j in inputText.readlines()]

    total = 0

    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if contents[i][j] == 0:
                foundCoord = []
                total += search(contents, (i, j))

    print(total)