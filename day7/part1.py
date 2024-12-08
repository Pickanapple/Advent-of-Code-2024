#This is probably really slow, but I am just going to try every combination
#I will use reccursion

def checkCalculation(numbers: list, target):
    if len(numbers) == 1:
        return numbers[0] == target
    
    elif checkCalculation([numbers[0] * numbers[1]] + numbers[2:], int(target)):
        return True
    
    elif checkCalculation([numbers[0] + numbers[1]] + numbers[2:], int(target)):
        return True
    
    else:
        return False
    
with open("day7/input.txt", "r") as inputText:
    contents = inputText.readlines()
    actualContents = []
    total = 0

    for i in contents:
        semiColonIndex = i.index(":")
        actualContents.append((int(i[:semiColonIndex]),
                              i[semiColonIndex + 1:].split()))

    for i in actualContents:
        if checkCalculation([int(x) for x in i[1]], i[0]):
            total += i[0]

    print(total)