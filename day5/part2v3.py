#How did I struggle this much on this one!?!?!

from functools import cache

@cache
def handleRules(input: tuple, rules: tuple) -> bool:
    for i in rules:
        if i[0] not in input or i[1] not in input:
            continue
        
        if input.index(i[0]) > input.index(i[1]):
            return False
        
    return True

def changeListByRules(input: list, rules: tuple) -> bool:
    print("Sorting list")

    while True:
        for i in rules:
            if i[0] not in input or i[1] not in input:
                continue
            
            if input.index(i[0]) > input.index(i[1]):
                firstIndex, secondIndex = input.index(i[0]), input.index(i[1])
                first, second = i[0], i[1]

                input[firstIndex], input[secondIndex] = second, first
                
        if handleRules(tuple(input), tuple(rules)):
            print("Sorted list")
            return input

def values(input, rules): 
    sum = 0

    for i in input:
        sum += i[len(i)//2]

    print(sum)

def removeWorkingValues(input, rules): 
    newList = input[::]

    for i in input:
        newList.remove(i) if handleRules(tuple(i), tuple(rules)) else None
    
    return newList

with open("day5/input.txt", "r") as inputText: 
    contents: list = inputText.readlines()

    gap = contents.index("\n")
    
    rules = [tuple(map(int, i.replace("\n", "").split("|"))) for i in contents[:gap]]

    lines = [tuple(map(int, i.split(","))) for i in contents[gap + 1:]]

    lines = removeWorkingValues(lines, rules)

    sortedLines = [changeListByRules(list(i), rules) for i in lines]

    values(sortedLines, rules)