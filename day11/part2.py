from functools import cache

class Stone:
    def __init__(self, value):
        self.value = value
    
    @cache
    def update(self, value):
        global seenResults
        global contents

        self.value = str(self.value)

        # if self.value in list(seenResults.keys()):
        #     try:
        #         if type(seenResults[self.value]) == tuple:
        #             try:
        #                 self.value = seenResults[self.value][0]
        #                 contents.insert(contents.index(self) + 1, Stone(seenResults[self.value][1]))
                    
        #             except TypeError:
        #                 self.value = seenResults[self.value]

        #         else:
        #             self.value = seenResults[self.value]

        #         return

        #     except:
        #         pass

        if self.value == "0":
            newValue = 1

            seenResults[self.value] = newValue
            self.value = newValue
        
        elif len(self.value) % 2 == 0:
            midPoint = len(self.value) // 2
            leftSide, rightSide = str(int(self.value[:midPoint])), str(int(self.value[midPoint:]))

            seenResults[self.value] = (leftSide, rightSide)

            self.value = leftSide
            contents.insert(contents.index(self) + 1, Stone(rightSide))

        else:
            newValue = int(self.value) * 2024
        
            seenResults[self.value] = newValue
            self.value = newValue

    def __str__(self):
        return str(self.value)

contents = []
seenResults = {}

with open("day11/testInput.txt", "r") as inputText:
    contents = [Stone(int(i)) for i in inputText.readline().split()]

for i in range(25):
    print(f"Checking attempt {i + 1}")
    oldList = contents.copy()
    
    for j in oldList:
        j.update(j.value)
    
    print(f"Finished checking attempt {i + 1}")

print([str(i) for i in contents])
print(len(contents))