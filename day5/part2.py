from statistics import mode

def handleRules(input: list, rules: list) -> bool:
    for i in rules:
        if i[0] not in input or i[1] not in input:
            continue
        
        if input.index(i[0]) > input.index(i[1]):
            return False
        
    return True

def order(rules):
    lowerRules = []

    for i in rules:
        lowerRules.append(i[0])

    order = []

    while len(lowerRules) > 0:
        order.append(mode(lowerRules))

        while order[-1] in lowerRules:
            lowerRules.remove(order[-1])

    print("Finished ordering")
    return order

def removeWorkingValues(input, rules): 
    newList = input[::]

    for i in input:
        newList.remove(i) if handleRules(i, rules) else None
    
    return newList
    
def correctLines(input, rules): 
    orderToUse = order(rules)

    usedRules = {}
    wronglyPlacedValues = []

    for i in orderToUse:
        if i in input:
            usedRules[i] = input.index(i)
    
    for i in orderToUse:
        pass

    print(usedRules)
    return input[len(input) // 2]

with open("day5/testInput.txt", "r") as inputText: 
    contents: list = inputText.readlines()

gap = contents.index("\n")

rules = [list(map(int, i.replace("\n", "").split("|"))) for i in contents[:gap]]

lines = [list(map(int, i.split(","))) for i in contents[gap + 1:]]

lines = removeWorkingValues(lines, rules)

for i in lines:
    print(correctLines(i, rules))