import pandas as pd

def timesInList(num, data):
    times = 0

    for i in data:
        if i == num:
            times += 1

    return times

data = pd.read_csv("Advent-of-Code-2024\day1\input.csv")

left  = list(data["right"])
right = list(data["left"])

similarityScore = 0

for i in left:
    similarityScore += i * timesInList(i, right)

print(similarityScore)