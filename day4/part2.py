def isX(index, text):
    if text[index[0] - 1][index[1] - 1] == "M": 
        if text[index[0] + 1][index[1] + 1] != "S":
            return False
    
    elif text[index[0] - 1][index[1] - 1] == "S":
        if text[index[0] + 1][index[1] + 1] != "M":
            return False
        
    else:
        return False

    if text[index[0] - 1][index[1] + 1] == "M": 
        if text[index[0] + 1][index[1] - 1] != "S":
            return False
    
    elif text[index[0] - 1][index[1] + 1] == "S":
        if text[index[0] + 1][index[1] - 1] != "M":
            return False
        
    else:
        return False
    
    return True

with open("day4/input.txt", "r") as inputText:
    total = 0

    contents = inputText.readlines()

    for i in range(3, len(contents) - 3):
        for j in range(3, len(contents[i]) - 3):
            if contents[i][j] == "A":
                total += isX((i, j), contents)

    print(total)