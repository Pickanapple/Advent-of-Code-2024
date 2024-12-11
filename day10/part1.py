import sys
sys.setrecursionlimit(2147483647)

def search(listToCheck, coordinate, totalFound = 0):
    currentNum = listToCheck[coordinate[0]][coordinate[1]]

    newObject = 0

    if currentNum == 9:
        return 1
    
    else: 
        if coordinate[0] < len(listToCheck) - 1:
            if listToCheck[coordinate[0] + 1][coordinate[1]] == currentNum + 1: 
                newObject = search(listToCheck, (coordinate[0] + 1, coordinate[1]), totalFound)
                
                if currentNum == 0:
                    totalFound += newObject

        if coordinate[0] != 0:
            if listToCheck[coordinate[0] - 1][coordinate[1]] == currentNum + 1: 
                newObject = search(listToCheck, (coordinate[0] - 1, coordinate[1]), totalFound)
                
                if currentNum == 0:
                    totalFound += newObject

        if coordinate[1] < len(listToCheck[0]) - 1:
            if listToCheck[coordinate[0]][coordinate[1] + 1] == currentNum + 1: 
                newObject = search(listToCheck, (coordinate[0], coordinate[1] + 1), totalFound)
                
                if currentNum == 0:
                    totalFound += newObject

        if coordinate[1] != 0:
            if listToCheck[coordinate[0]][coordinate[1] - 1] == currentNum + 1: 
                newObject = search(listToCheck, (coordinate[0], coordinate[1] - 1), totalFound)
                
                if currentNum == 0:
                    totalFound += newObject

        else:
            return newObject
        
    return totalFound
        
with open("day10/testInput.txt", "r") as inputText: 
    contents = [[int(i) for i in j.removesuffix("\n")] for j in inputText.readlines()]

    total = 0

    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if contents[i][j] == 0:
                total += search(contents, (i, j))

    print(total)