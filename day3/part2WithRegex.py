#Does not work

import re

match = r"mul\(\d{1,3},\d{1,3}\)"

def trimList(list, enabled):
    while "do" in list:
        if not enabled and "do()" in list:
            enabled = True 
            list = list[list.find("do()" + 4):]

        if enabled and "don't()" in list:
            if "do()" in list:
                list = list[:list.find("don't()") + 1] + list[list.find("do()") + 1:]
            else:
                list = list[:list.find("don't()") + 1]
                enabled = False

    return list, enabled

with open("day3/input.txt", "r") as file:
    contents = file.readlines()

    muls = []

    total = 0

    enabled = True

    for i in contents: 
        i, enabled = trimList(i, enabled)
        muls.append(re.findall(match, i))

    for i in muls:
        for j in i:
            j = j.replace("mul(", "")
            j = j.replace(")", "")

            commaIndex = j.index(",")

            total += int(j[:commaIndex]) * int(j[commaIndex + 1:])

    print(total)