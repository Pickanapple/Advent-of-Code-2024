from random import shuffle

def sortList(listToSort: list, rules):
    listToSort = list(listToSort)

    checkedShuffles = []
    
    while True: 
        shuffle(listToSort)
        
        if listToSort in checkedShuffles:
            continue

        checkedShuffles.append(listToSort.copy())

        if handleRules(listToSort, rules):
            return listToSort
    

def removeWorkingValues(input, rules): 
    newList = input[::]
    
    for i in input:
        newList.remove(i) if handleRules(i, rules) else None
    
    return newList

def handleRules(input: tuple, rules: list) -> bool:
    for i in rules:
        if i[0] not in input or i[1] not in input:
            continue
        
        if input.index(i[0]) > input.index(i[1]):
            return False
        
    return True

def values(input): 
    sum = 0

    for i in input:
            sum += i[len(i)//2]

    print(sum)

with open("day5/input.txt", "r") as inputText: 
    contents: list = inputText.readlines()

    gap = contents.index("\n")
    
    rules = [tuple(map(int, i.replace("\n", "").split("|"))) for i in contents[:gap]]

    lines = [tuple(map(int, i.split(","))) for i in contents[gap + 1:]]

    lines = removeWorkingValues(lines, rules)

    workingLines = []

    for i in range(len(lines)):
        print(f"Sorting list {i + 1} / {len(lines)}: {lines[i]}")
        workingLines.append(sortList(lines[i], rules))

    print(values(workingLines))