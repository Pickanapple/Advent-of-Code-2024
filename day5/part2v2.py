from random import shuffle
from functools import cache

def sortList(listToSort: list, rules: tuple):
    listToSort = list(listToSort)
    shuffled = []

    while True: 
        shuffle(listToSort)

        if tuple(listToSort) in shuffled:
            continue

        shuffled.append(tuple(listToSort))

        if handleRules(tuple(listToSort), tuple(rules)):
            return listToSort
    

def removeWorkingValues(input, rules): 
    newList = input[::]
    
    for i in input:
        newList.remove(i) if handleRules(tuple(i), tuple(rules)) else None
    
    return newList

@cache
def handleRules(input: tuple, rules: list) -> bool:
    input = tuple(input)

    for i in tuple(rules):
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

    lines = [tuple(map(int, filter(None, i.replace("\n", "").split(",")))) for i in contents[gap + 1:]]

    lines = removeWorkingValues(lines, rules)

    workingLines = []

    for i in range(len(lines)):
        print(f"Sorting list {i + 1} / {len(lines)}: {lines[i]}")
        workingLines.append(sortList(lines[i], rules))

    print(values(workingLines))