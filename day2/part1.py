def safe(text):
    if text[0] > text[1]: #Decreasing
        for i in range(len(text) - 1):
            if text[i] - text[i + 1] > 3 or text[i] - text[i + 1] < 1:
                return False

    elif text[0] < text[1]: #Increasing
        for i in range(len(text) - 1):
            if text[i + 1] - text[i] > 3 or text[i + 1] - text[i] < 1:
                return False

    else: #Neither increasing nor decreasing
        return False
    
    return True

with open("inputText.txt", "r") as inputText:
    data = inputText.readlines()

    amountSafe = 0

    for i in data:
        if safe([int(j) for j in i.split()]):
            amountSafe += 1

print(amountSafe)