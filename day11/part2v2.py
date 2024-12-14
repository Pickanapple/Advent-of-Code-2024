def update(value):
    global contents

    value = str(value)

    try:
        if contents[value] > 0:
           contents[value] -= 1
        else: 
            contents[value] = 0

    except KeyError:
        if contents[int(value)] > 0:
            contents[int(value)] -= 1
        else:
            contents[int(value)] = 0

    if value == "0":
        try:
            contents[1] += 1
        except KeyError:
            contents[1] = 1
    
    elif len(value) % 2 == 0:
        midPoint = len(value) // 2
        leftSide, rightSide = str(int(value[:midPoint])), str(int(value[midPoint:]))
        
        try: 
            contents[leftSide] += 1
        except KeyError:
            contents[leftSide] = 1

        try: 
            contents[rightSide] = 1
        except KeyError:
            contents[rightSide] = 1 
            contents[rightSide] += 1
    else:
        try:
            contents[int(value) * 2024] += 1
        except KeyError:
            contents[int(value) * 2024] = 1
 
contents = {}

with open("day11/testInput.txt", "r") as inputText:
    contents.update({int(i): 1 for i in inputText.readline().split()})

for _ in range(25):
    contentKeys = list(contents.keys())
    for key in contentKeys:
        for _ in range(contents[key]):
            update(key)

total = 0

for i in contents.values():
    total += i

print(total - 1)