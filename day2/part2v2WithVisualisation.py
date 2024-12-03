import pygame as pg
import pygame.font as font
from time import sleep

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
                return (False, False)
        
        i += 1

    return (True, problemDampened)

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
                return False, problemDampened
        
        i += 1 

    return True, problemDampened

def safe(text):

    if text[0] == text[1] == text[2]:
        return False, True
    elif text[0] == text[1]:
        text.pop(0)

        result = descending(text, True) or ascending(text, True)
        return (result, True)
    
    else:
        resultAscending = ascending(text)
        resultDescending = descending(text)

        if resultAscending[0] == True:
            return resultAscending
        elif resultDescending[0] == True:
            return resultDescending
        else:
            return (False, False)

def initPygame():
    pg.init()
    font.init()

    global screen
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    global ycoord
    ycoord = 0

    global xcoord
    xcoord = 0

    global fontSize
    fontSize = 13
    
    global textFont
    textFont = font.Font(None, fontSize)

initPygame()

with open("day2/input.txt", "r") as inputText:
    data = inputText.readlines()

    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")

    amountSafe = 0

    for i in data:
        if ycoord >= screen.get_height():
            ycoord = 0
            xcoord += screen.get_width() * 1/15

        text_surface = textFont.render(i, True, (255, 255, 255))

        screen.blit(text_surface, (xcoord, ycoord))

        pg.display.flip()

        sleep(0.001)

        result = safe([int(j) for j in i.split()])

        if result[0]:
            amountSafe += 1
            if not result[1]:
                text_surface = textFont.render(i, True, (0, 255, 0))
            else:
                text_surface = textFont.render(i, True, (0, 0, 255))

            screen.blit(text_surface, (xcoord, ycoord))

            ycoord += fontSize

        else:
            text_surface = textFont.render(i, True, (255, 0, 0))

            screen.blit(text_surface, (xcoord, ycoord))

            ycoord += fontSize
            
        pg.display.flip()

    print(amountSafe)


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

            pg.display.flip()