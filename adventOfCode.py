#I noticed that I was writing lots of the same code every day
#so here is a short package for lots of this code

from functools import cache, lru_cache

def getInput(day, input = "regular", replaceNewLines = True):
    if input == "test":
        with open(f"day{day}/testInput.txt", "r") as text:
            contents = text.readlines()
            
    elif input == "regular":
        with open(f"day{day}/input.txt", "r") as text:
            contents = text.readlines()

    else:
        raise KeyError(f"Input type {input} is not acceptable. Use \"regular\" or \"test\"")
            
    if replaceNewLines:
        contents = [i.replace("\n", "") for i in contents]
    
    return contents

if __name__ == "__main__":
    print(getInput(3))
    print(getInput(3, "test"))
