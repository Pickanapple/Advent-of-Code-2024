import re
from functools import cache, lru_cache
from os import system

#I am going to check for long lists of "#"
#I also spent ages trying to look for the tree in the 100 seconds...

TOLERANCE = 10

class Soldier:
    def __init__(self, pos: list, velocity: tuple, listToUse):
        self.pos = pos
        self.velocity = velocity

        listToUse[self.pos[1]][self.pos[0]] = "#"
        self.tempList = listToUse

    def update(self, listToUse):
        listToUse[self.pos[1]][self.pos[0]] = "."

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
        listToUse[target[0]][target[1]] = "#"
        return listToUse

    def __str__(self):
        return f"{self.pos} - {self.velocity}"

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

for i in range(1000000):

    for j in actualContents: 
        bathroom = j.update(bathroom)

    # print(f"Seconds elapsed: {i + 1}")

    for j in bathroom:
        for k in range(len(j) - TOLERANCE):
            hasFound = True

            for l in range(TOLERANCE):
                if j[k + l] == ".":
                    hasFound = False
                    break
            
            if hasFound:
                print(i + 1)

                for j in bathroom:
                    for k in j:
                        print(k, end="")
                    print()
                
                quit()