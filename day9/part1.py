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

def move(listToUse: list):
    while "." in listToUse:
        for i in range(len(listToUse) - 1, -1, -1):
            if listToUse[i] != ".":
                listToUse[listToUse.index(".")] = listToUse.pop(i)
                break
    
    return listToUse

def calculate(listToUse: list):
    total = 0
    for i in range(len(listToUse)):
        total += listToUse[i] * i
    return total

with open("day9/input.txt", "r") as inputText:
    contents = inputText.readline().removesuffix("\n")
    print(calculate(move(readString(contents))))