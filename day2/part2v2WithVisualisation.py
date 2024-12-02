import pygame as pg

def descending(inputText, problemDampened = False):

    text = inputText[::]

    i = 0

    while i < len(text) - 1:
        difference = text[i] - text[i + 1]
        if not (1 <= difference <= 3):
            if not problemDampened:
                problemDampened = True

                try: 
                    if not(1 <= (text[i] - text[i + 2]) <= 3):
                        text.pop(i)
                        i -= 1
                    else:
                        text.pop(i + 1)

                except IndexError:
                    text.pop(i)
                    
                i -= 1

            else:
                return False
        
        i += 1

    return True

def ascending(inputText, problemDampened = False):
    
    text = inputText[::]

    i = 0

    while i < len(text) - 1:
        difference = text[i + 1] - text[i]
        if not (1 <= difference <= 3):
            if not problemDampened:
                problemDampened = True

                try: 
                    if not(1 <= (text[i + 2] - text[i]) <= 3):
                        text.pop(i)
                        i -= 1
                    else:
                        text.pop(i + 1)
                
                except IndexError:
                    text.pop(i)

                i -= 1

            else:
                return False
        
        i += 1 

    return True

def safe(text):

    if text[0] == text[1] == text[2]:
        return False
    elif text[0] == text[1]:
        text.pop(0)

        return descending(text, True) or ascending(text, True)
    
    else:
        return descending(text) or ascending(text)

def initPygame():
    pg.init()
    global screen

    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

with open("input.txt", "r") as inputText:
    data = inputText.readlines()

    amountSafe = 0

    for i in data:
        if safe([int(j) for j in i.split()]):
            amountSafe += 1
            

        else:
            pass

    print(amountSafe)