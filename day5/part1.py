def handleRules(input: tuple, rules: list) -> bool:
    for i in rules:
        if i[0] not in input or i[1] not in input:
            continue
        
        if input.index(i[0]) > input.index(i[1]):
            return False
        
    return True

def values(input, rules): 
    sum = 0

    for i in input:
        if handleRules(i, rules):
            sum += i[len(i)//2]

    print(sum)

with open("day5/input.txt", "r") as inputText: 
    contents: list = inputText.readlines()

    gap = contents.index("\n")
    
    rules = [tuple(map(int, i.replace("\n", "").split("|"))) for i in contents[:gap]]

    lines = [tuple(map(int, i.split(","))) for i in contents[gap + 1:]]

    values(lines, rules)