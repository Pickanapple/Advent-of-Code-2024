import re

match = "mul\(\d+,\d+\)"

with open("day3/input.txt", "r") as file:
    contents = file.readlines()

    muls = []

    total = 0

    for i in contents:
        muls.append(re.findall(match, i))

    for i in muls:
        for j in i:
            j = j.replace("mul(", "")
            j = j.replace(")", "")

            commaIndex = j.index(",")

            total += int(j[:commaIndex]) * int(j[commaIndex + 1:])

    print(total)