def clawMachine(button1, button2, xVal, yVal):
    if (xVal - xVal // button1[0]) % button2[0] == 0 and (yVal - yVal / button1[1]) % button2[1] == 0:
        return 


with open("day13/testInput.txt", "r") as inputText:
    contents = inputText.readlines()

actualContents = []

i = 0
while i < len(contents) - 4:
    actualContents.append([
        contents[i].replace(" ", "").replace("\n", "").replace("X+", "").replace("Y+", "").split(":")[1].split(","),
        contents[i + 1].replace(" ", "").replace("\n", "").replace("X+", "").replace("Y+", "").split(":")[1].split(","),
        contents[i + 2].replace(" ", "").replace("\n", "").replace("X=", "").replace("Y=", "").split(":")[1].split(","),
    ])

    i += 4

print(actualContents)