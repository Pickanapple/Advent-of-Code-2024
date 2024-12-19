def readString(string):
    list = []
    id = 0
    for i in range(len(string)):
        if i % 2 == 0:
            for j in range(int(string[i])):
                list.append(id)
            
            id += 1
        
        else:
            for j in range(int(string[i])):
                list.append(".")
    return list

def move(listToUse: list, coord1, coord2):
    ID = listToUse[coord1]
    length = coord2 - coord1 + 1
    listAsString = ""

    for i in listToUse:
        if i == ".": 
            listAsString += "."
        else: 
            listAsString += "#"

    dots = "." * length

    if dots not in listAsString[:coord1]:
        return listToUse
    else:
        movedSegment = listToUse[coord1:coord2 + 1]
        
        for i in range(len(listToUse)):
            if listToUse[i] == ID:
                listToUse[i] = "."
        
        startCoord = listAsString.find(dots)
        
        for i in range(length):
            listToUse[startCoord + i] = movedSegment.pop(0)
    
        return listToUse

def calculate(listToUse: list):
    total = 0
    for i in range(len(listToUse)):
        try: 
            total += int(listToUse[i]) * i
        except: 
            continue

    return total

with open("day9/input.txt", "r") as inputText:
    contents = inputText.readline().removesuffix("\n")

listOfIDs = readString(contents)

maxNum = 0

for i in listOfIDs:
    try: 
        if int(i) > maxNum:
            maxNum = int(i)

    except: 
        continue

for i in range(maxNum, 0, -1):
    print(i)
    startCoord = listOfIDs.index(i)

    for j in range(len(listOfIDs) - 1, -1, -1):
        if listOfIDs[j] == i:
            endCoord = j
            break

    listOfIDs = move(listOfIDs, startCoord, endCoord)

print(calculate(listOfIDs))