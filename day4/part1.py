def nextCharacter(index, text):
    global total

    if index == []:
        return

    for i in index:
        newIndex = []

        if text[i[0]][i[1]] == "S":
            total += 1
            return

        characterToFind = "XMAS"["XMAS".index(text[i[0]][i[1]]) + 1]

        print(characterToFind)

        if text[i[0] + 1][i[0]] == characterToFind:
            newIndex.append((i[0] + 1, i[0]))
        
        elif text[i[0]][i[0] + 1] == characterToFind:
            newIndex.append((i[0], i[0] + 1))
        
        elif text[i[0] - 1][i[0]] == characterToFind:
            newIndex.append((i[0] - 1, i[0]))
        
        elif text[i[0]][i[0] - 1] == characterToFind:
            newIndex.append((i[0], i[0] - 1))

        elif text[i[0] + 1][i[0] + 1] == characterToFind:
            newIndex.append((i[0] + 1, i[0] + 1))
        
        elif text[i[0] + 1][i[0] - 1] == characterToFind:
            newIndex.append((i[0] + 1, i[0] - 1))
        
        elif text[i[0] - 1][i[0] + 1] == characterToFind:
            newIndex.append((i[0] - 1, i[0] + 1))

        elif text[i[0] - 1][i[0] - 1] == characterToFind:
            newIndex.append((i[0] - 1, i[0] - 1))

        nextCharacter(newIndex, text)

with open("day4/testInput.txt", "r") as inputText:
    global total
    total = 0

    contents = inputText.readlines()

    for i in range(len(contents)):
        for j in range(len(contents[i])):
            if contents[i][j] == "X":
                nextCharacter([(i, j)], contents)


    print(total)