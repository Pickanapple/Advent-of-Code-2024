import pandas as pd

data = pd.read_csv("Advent-of-Code-2024\day1\input.csv")

left  = list(data["right"])
right = list(data["left"])

difference = 0

while len(left) > 0:
    difference += abs(left.pop(left.index(min(left))) - right.pop(right.index(min(right))))

print(difference)