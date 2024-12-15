import re
from functools import cache, lru_cache

class Soldier:
    def __init__(self, pos: list, velocity: tuple, listToUse):
        self.pos = pos
        self.velocity = velocity

        listToUse[self.pos[1]][self.pos[0]] = 1 if listToUse[self.pos[1]][self.pos[0]] == "." else listToUse[self.pos[1]][self.pos[0]] + 1
        self.tempList = listToUse

    def update(self, listToUse):
        if listToUse[self.pos[1]][self.pos[0]] == 1:
            listToUse[self.pos[1]][self.pos[0]] = "."
        else:
            listToUse[self.pos[1]][self.pos[0]] -= 1

        target = []

        if self.pos[1] + self.velocity[1] < 0:
            difference = abs(self.velocity[1]) - self.pos[1]
            target.append(len(listToUse) - difference)
            pass
        
        elif self.pos[1] + self.velocity[1] >= len(listToUse):
            difference = len(listToUse) - self.pos[1] - self.velocity[1]
            target.append(abs(difference))
            pass

        else: 
            target.append(self.pos[1] + self.velocity[1])

        if self.pos[0] + self.velocity[0] < 0:
            difference = abs(self.velocity[0]) - self.pos[0]
            target.append(len(listToUse[0]) - difference)
            pass
        
        elif self.pos[0] + self.velocity[0] >= len(listToUse[0]):
            difference = len(listToUse[0]) - self.pos[0] - self.velocity[0]
            target.append(abs(difference))
            pass

        else: 
            target.append(self.pos[0] + self.velocity[0])

        self.pos = [target[1], target[0]]
        listToUse[target[0]][target[1]] = 1 if listToUse[target[0]][target[1]] == "." else listToUse[target[0]][target[1]] + 1
        return listToUse

    def __str__(self):
        return f"{self.pos} - {self.velocity}"

def safetyScore(quadrant):
    amount = 0

    for i in quadrant:
        tempAmount = 0
        digits = re.findall("\d", str(i))

        for i in digits:
            tempAmount += int(i)

        amount += tempAmount
    
    return amount

def countQuadrants(listToCount):
    upperY = listToCount[:len(listToCount) // 2]
    lowerY = listToCount[len(listToCount) // 2 + 1:]

    topLeft = [row[:len(row) // 2] for row in upperY]
    topRight = [row[len(row) // 2 + 1:] for row in upperY]
    bottomLeft = [row[:len(row) // 2] for row in lowerY]
    bottomRight = [row[len(row) // 2 + 1:] for row in lowerY]

    total = safetyScore(topLeft) * safetyScore(topRight) * safetyScore(bottomLeft) * safetyScore(bottomRight)
    
    return total

# with open("day14/testInput.txt", "r") as inputText:
with open("day14/input.txt", "r") as inputText:
    contents = [i.replace("\n", "") for i in inputText.readlines()]

actualContents = []

bathroom = [["." for i in range(101)] for j in range(103)] #Real
# bathroom = [["." for i in range(11)] for j in range(7)] #Test

for i in contents:
    iSplit = i.replace("p=", "").replace("v=", "").split()

    actualContents.append(
        Soldier(
            list(map(int, iSplit[0].split(","))),
            tuple(map(int, iSplit[1].split(","))),
            bathroom
        )
    )

    bathroom = actualContents[-1].tempList

for _ in range(100):
    for i in actualContents: 
        bathroom = i.update(bathroom)

print(countQuadrants(bathroom))