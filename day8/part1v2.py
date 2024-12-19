def findAntiNodes(listToUse: list, coords: int, foundCoords: set, onTop: int):
    targetNode = listToUse[coords[0]][coords[1]]
    coordsToFind = []

    for i in range(len(listToUse)):
        for j in range(len(listToUse[i])): 
            if (i, j) == coords: 
                continue
            elif listToUse[i][j] == targetNode:
                if (coords, (i, j)) in foundCoords or ((i, j), coords) in foundCoords:
                    continue
                else:
                    coordsToFind.append((i, j))
                    foundCoords.add((coords, (i, j)))

    for i in coordsToFind:
        yDistance = abs(coords[0] - i[0])
        xDistance = abs(coords[1] - i[1])

        if coords[0] > i[0]:
            if coords[1] > i[1]:
                try: 
                    if listToUse[coords[0] + yDistance][coords[1] + xDistance] == ".":
                        listToUse[coords[0] + yDistance][coords[1] + xDistance] = "#"
                    
                    else:
                        onTop += 1

                except:
                    pass

                try: 
                    if listToUse[i[0] - yDistance][i[1] - xDistance] == ".":
                        listToUse[i[0] - yDistance][i[1] - xDistance] = "#"
                    
                    else:
                        onTop += 1

                except:
                    pass

            else:
                try: 
                    if listToUse[coords[0] + yDistance][coords[1] - xDistance] == ".":
                        listToUse[coords[0] + yDistance][coords[1] - xDistance] = "#"
                    
                    else:
                        onTop += 1

                except:
                    pass

                try: 
                    if listToUse[i[0] - yDistance][i[1] + xDistance] == ".":
                        listToUse[i[0] - yDistance][i[1] + xDistance] = "#"
                    
                    else:
                        onTop += 1
                    
                except: 
                    pass

        else:
            if i[1] > coords[1]:
                if i[1] > coords[1]:
                    try: 
                        if listToUse[i[0] + yDistance][i[1] + xDistance] == ".":
                            listToUse[i[0] + yDistance][i[1] + xDistance] = "#"
                        
                        else:
                            onTop += 1

                    except:
                        pass

                    try: 
                        if listToUse[coords[0] - yDistance][coords[1] - xDistance] == ".":
                            listToUse[coords[0] - yDistance][coords[1] - xDistance] = "#"
                        
                        else:
                            onTop += 1

                    except:
                        pass

                else:
                    try: 
                        if listToUse[i[0] + yDistance][i[1] - xDistance] == ".":
                            listToUse[i[0] + yDistance][i[1] - xDistance] = "#"
                        
                        else:
                            onTop += 1

                    except:
                        pass

                    try: 
                        if listToUse[coords[0] - yDistance][coords[1] + xDistance] == ".":
                            listToUse[coords[0] - yDistance][coords[1] + xDistance] = "#"
                        
                        else:
                            onTop += 1
                        
                    except: 
                        pass

            else:
                pass
    
    return listToUse, foundCoords, onTop

def printBoard(board):
    for i in board:
        for j in i:
            print(j, end="")

        print()

with open("day8/testInput.txt", "r") as f:
    contents = [[j for j in i.replace("\n", "")] for i in f.readlines()]

foundCoords = set()
onTop = 0

for i in range(len(contents)):
    for j in range(len(contents[i])):
        if contents[i][j] == "." or contents[i][j] == "#":
            continue
        else:
            contents, foundCoords, onTop = findAntiNodes(contents, (i, j), foundCoords, onTop)

printBoard(contents)

print()

totalAntiNodes = 0

for i in contents:
    for j in i:
        if j == "#":
            totalAntiNodes += 1

print(onTop)
print(totalAntiNodes + onTop)