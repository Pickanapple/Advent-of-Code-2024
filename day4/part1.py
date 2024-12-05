def countWords(index, text):
    words = 0

    if text[index[0] + 1][index[1]] + text[index[0] + 2][index[1]] + text[index[0] + 3][index[1]] == "MAS":
        words += 1
    
    if text[index[0]][index[1] + 1] + text[index[0]][index[1] + 2] + text[index[0]][index[1] + 3] == "MAS":
        words += 1
    
    if text[index[0] - 1][index[1]] + text[index[0] - 2][index[1]] + text[index[0] - 3][index[1]] == "MAS":
        words += 1
    
    if text[index[0]][index[1] - 1] + text[index[0]][index[1] - 2] + text[index[0]][index[1] - 3] == "MAS":
        words += 1

    if text[index[0] + 1][index[1] + 1] + text[index[0] + 2][index[1] + 2] + text[index[0] + 3][index[1] + 3] == "MAS":
        words += 1

    if text[index[0] + 1][index[1] - 1] + text[index[0] + 2][index[1] - 2] + text[index[0] + 3][index[1] - 3] == "MAS":
        words += 1
    
    if text[index[0] - 1][index[1] + 1] + text[index[0] - 2][index[1] + 2] + text[index[0] - 3][index[1] + 3] == "MAS":
        words += 1

    if text[index[0] - 1][index[1] - 1] + text[index[0] - 2][index[1] - 2] + text[index[0] - 3][index[1] - 3] == "MAS":
        words += 1

    return words

with open("day4/input.txt", "r") as inputText:
    total = 0

    contents = inputText.readlines()

    for i in range(3, len(contents) - 3):
        for j in range(3, len(contents[i]) - 3):
            if contents[i][j] == "X":
                total += countWords((i, j), contents)

    print(total)