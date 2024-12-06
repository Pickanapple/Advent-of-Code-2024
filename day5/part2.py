def perfectOrder(rules):
    order = []
    
    for i in rules:
        if i[0] in order and i[1] in order:
            if order.index(i[0]) < order.index(i[1]):
                continue
            else:
                raise Exception("Rule problem")

        elif i[0] in order:
            order.append()
        elif i[1] in order:
            pass
        else:
            pass

    print("Finished ordering rules!")
    return order

def handleRules(input: tuple, rules: list) -> bool:
    for i in rules:
        if i[0] not in input or i[1] not in input:
            continue
        
        if input.index(i[0]) > input.index(i[1]):
            return False
        
    return True

def removeWorkingValues(input, rules): 
    newList = input[::]

    for i in input:
        newList.remove(i) if handleRules(i, rules) else None
    
    return newList
    
def correctLines(input, rules): 
    for i in rules:
        if i[0] not in input or i[1] not in input:
            continue
        
        index1 = input.index(i[0])
        index2 = input.index(i[1])

        input[index1] = i[1]
        input[index2] = i[0]

    if handleRules(input, rules):
        return input[len(input) // 2]
    else:
        correctLines(input, rules)

with open("day5/testInput.txt", "r") as inputText: 
    contents: list = inputText.readlines()

gap = contents.index("\n")

rules = [tuple(map(int, i.replace("\n", "").split("|"))) for i in contents[:gap]]

lines = [list(map(int, i.split(","))) for i in contents[gap + 1:]]

linesToCorrect = removeWorkingValues(lines, rules)

sum = 0

for i in linesToCorrect:
    sum += correctLines(i, rules)

print(sum)