from os import system

def mul(contents):
    total = 0
    
    while "mul" in contents: 
        location = contents.find("mul")

        num1, num2 = "0", "0"

        finding1 = True

        found = True
        rangeEnd = location + 3

        if contents[location + 3] == "(":
            i = location + 4

            while contents[i] != ")":
                try:
                    int(contents[i])

                    if finding1: 
                        num1 += str(contents[i])

                    else:
                        num2 += str(contents[i])

                except ValueError:
                    if contents[i] == ",":
                        finding1 = False
                    else:
                        found = False
                        break

                i += 1

            rangeEnd = i

        else: 
            found = False

        contents = contents[rangeEnd:]

        if found:
            total += int(num1) * int(num2)
    
    return total

with open("day3/input.txt", "r") as inputText:
    system("cls")

    contentsInLines = inputText.readlines()

    total = 0

    result = (0, True)

    for i in contentsInLines:
        total += mul(i)

    with open("day3/outputs.txt", "r") as earlier:
        numbers = [int(line.strip()) for line in earlier.readlines()]

    with open("day3/outputs.txt", "a") as earlier:

        if total in numbers:
            print(f"{total}, already seen")
        else:
            print(total)
            earlier.write(str(total))