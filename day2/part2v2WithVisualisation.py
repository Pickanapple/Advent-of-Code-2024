import pygame as pg
import pygame.font as font

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
    font.init()

    global screen
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    global ycoord
    ycoord = 0

    global xcoord
    xcoord = 0

    global fontSize
    fontSize = 12

    global textFont
    textFont = font.Font(None, fontSize)

initPygame()

with open("input.txt", "r") as inputText:
    data = inputText.readlines()

    amountSafe = 0

    for i in data:
        if ycoord >= screen.get_height():
            ycoord = 0
            xcoord += screen.get_width() * 1/15

        if safe([int(j) for j in i.split()]):
            amountSafe += 1
            text_surface = textFont.render(i, True, (0, 255, 0))

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