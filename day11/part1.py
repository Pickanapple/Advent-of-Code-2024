class Stone:
    def __init__(self, value):
        self.value = value

    def update(self):
        self.value = str(self.value)

        if self.value == "0":
            self.value = 1
        
        elif len(self.value) % 2 == 0:
            global contents

            midPoint = len(self.value) // 2
            leftSide, rightSide = str(int(self.value[:midPoint])), str(int(self.value[midPoint:]))

            self.value = leftSide
            contents.insert(contents.index(self) + 1, Stone(rightSide))

        else:
            self.value = int(self.value) * 2024
        
    def __str__(self):
        return str(self.value)

contents = []
with open("day11/input.txt", "r") as inputText:
    contents = [Stone(int(i)) for i in inputText.readline().split()]

for i in range(25):
    oldList = contents.copy()
    
    for i in oldList:
        i.update()

print([str(i) for i in contents])
print(len(contents))