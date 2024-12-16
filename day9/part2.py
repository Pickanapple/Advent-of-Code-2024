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
    length = coord2 - coord1
    listAsString = ""

    for i in listToUse:
        if i == ".": 
            listAsString += "."
        else: 
            listAsString += "#"

    if "." not in listAsString[:coord1]:
        return listToUse
    else:
        print(True)
    

def calculate(listToUse: list):
    total = 0
    for i in range(len(listToUse)):
        total += listToUse[i] * i
    return total

with open("day9/input.txt", "r") as inputText:
    contents = inputText.readline().removesuffix("\n")
    # print(calculate(move(readString(contents))))

listToUse = [".", ".", ".", ".", "."]

move(listToUse, 3, 5)