"""
We can think of this as a set of simultaneous equations: 
xbutton1 and yButton2 = endGoal

All of these have exactly 2 values, and we know button1, button2 and endgoal

n*b1x + m*b2x = endGoalx
n*b1y + m*b2y = endGoaly

Solvable as a simultaneous equation
"""

import sympy as sym

n, m = sym.symbols("n, m")

with open("day13/input.txt", "r") as inputText:
    contents = inputText.readlines()

actualContents = []

i = 0
while i < len(contents):
    actualContents.append([
        contents[i].replace(" ", "").replace("\n", "").replace("X+", "").replace("Y+", "").split(":")[1].split(","),
        contents[i + 1].replace(" ", "").replace("\n", "").replace("X+", "").replace("Y+", "").split(":")[1].split(","),
        contents[i + 2].replace(" ", "").replace("\n", "").replace("X=", "").replace("Y=", "").split(":")[1].split(","),
    ])

    actualContents[-1][2][0] = 10000000000000 + int(actualContents[-1][2][0])
    actualContents[-1][2][1] = 10000000000000 + int(actualContents[-1][2][1])

    i += 4

# print(actualContents)

totalPresses = 0

for i in actualContents:
    buttonAX, buttonAY = map(int, i[0])
    buttonBX, buttonBY = map(int, i[1])
    endX, endY = map(int, i[2])

    eqX, eqY = sym.Eq(buttonAX * n + buttonBX * m, endX), sym.Eq(buttonAY * n + buttonBY * m, endY)

    solution = sym.solve([eqX, eqY], (n, m))

    buttonA, buttonB = float(solution[n]), float(solution[m])

    if buttonA.is_integer() and buttonB.is_integer() and abs(buttonA) == buttonA and abs(buttonB) == buttonB: 
        totalPresses += buttonA * 3 + buttonB

print(totalPresses)