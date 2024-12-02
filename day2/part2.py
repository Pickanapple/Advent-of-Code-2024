def safe(text):
    foundIncreasingOrDecreasing = False
    problemDampened = False

    while not foundIncreasingOrDecreasing:
        
        if text[0] > text[1]: #Decreasing
            foundIncreasingOrDecreasing = True
            i = 0

            while i < len(text) - 1:

                if (text[i] - text[i + 1] > 3 or text[i] - text[i + 1] < 1):
                    if problemDampened:
                        return False
                    else:
                        problemDampened = True
                        text.pop(i + 1)
                        i -= 1

                i += 1

        elif text[0] < text[1]: #Increasing
            foundIncreasingOrDecreasing = True
            i = 0

            while i < len(text) - 1:
                if (text[i + 1] - text[i] > 3 or text[i + 1] - text[i] < 1):
                    if problemDampened:
                        return False
                    else:
                        problemDampened = True
                        text.pop(i + 1)
                        i -= 1

                i += 1

        else: #Neither increasing nor decreasing
            problemDampened = True
            text.pop(0)
    
    return True

with open("input.txt", "r") as inputText:
    data = inputText.readlines()

    amountSafe = 0

    for i in data:
        if safe([int(j) for j in i.split()]):
            amountSafe += 1

print(amountSafe)