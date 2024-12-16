import os
from random import choice, randint
from time import sleep

directionDecoder = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def printBoard(board):
    for j in board:
        for k in j: 
            print(k, end = "")
        
        print()

def GPS(position):
    return position[0] * 100 + position[1]

def move(moveChosen, coordinates, listToUse):
    direction = directionDecoder[moveChosen]

    try:
        nextItem = listToUse[coordinates[0] + direction[0]][coordinates[1] + direction[1]]
    except: 
        nextItem = None

    if nextItem == None or nextItem == "\033[31m#\033[0m":
        return coordinates, listToUse
    
    elif nextItem == "\033[32mO\033[0m":
        i = 1
        
        if direction[0] == 0:
            while listToUse[coordinates[0]][coordinates[1] + (direction[1] * i)] == "\033[32mO\033[0m":
                i += 1

                try: 
                    if listToUse[coordinates[0]][coordinates[1] + (direction[1] * i)] == "\033[31m#\033[0m":
                        return coordinates, listToUse
                except: 
                    return coordinates, listToUse

            listToUse[coordinates[0]][coordinates[1] + (direction[1] * i)] = "\033[32mO\033[0m"
            listToUse[coordinates[0]][coordinates[1] + direction[1]] = "\033[33m@\033[0m"

        else:
            while listToUse[coordinates[0] + (direction[0] * i)][coordinates[1]] == "\033[32mO\033[0m":
                i += 1

                try: 
                    if listToUse[coordinates[0] + (direction[0] * i)][coordinates[1]] == "\033[31m#\033[0m":
                        return coordinates, listToUse
                except: 
                    return coordinates, listToUse
                
            listToUse[coordinates[0] + (direction[0] * i)][coordinates[1]] = "\033[32mO\033[0m"
            listToUse[coordinates[0] + direction[0]][coordinates[1]] = "\033[33m@\033[0m"

        listToUse[coordinates[0]][coordinates[1]] = "."

        coordinates = [coordinates[0] + direction[0], coordinates[1] + direction[1]]
        return coordinates, listToUse

    else:
        listToUse[coordinates[0]][coordinates[1]] = "."
        listToUse[coordinates[0] + direction[0]][coordinates[1] + direction[1]] = "\033[33m@\033[0m"

        coordinates = [coordinates[0] + direction[0], coordinates[1] + direction[1]]
        return coordinates, listToUse

#Setup
cls()
boardLength = int(input("Board length: "))
boardWidth = int(input("Board width: "))
delay = float(input("Delay (seconds): "))
boxCount = int(input("Box count: "))
obstacleCount = int(input("Obstacle count: "))
amountOfRobots = int(input("Amount of robots: "))

board = [ ["." for i in range(boardWidth)] for j in range(boardLength)]

for i in range(boardWidth):
    board[0][i] = "\033[31m#\033[0m"
    board[boardLength - 1][i] = "\033[31m#\033[0m"

for i in range(boardLength):
    board[i][0] = "\033[31m#\033[0m"
    board[i][boardWidth - 1] = "\033[31m#\033[0m"

takenSpots = []

for i in range(obstacleCount):
    while True:
        obstacleCoord = (randint(1, boardLength - 2), randint(1, boardWidth - 2))

        if obstacleCoord in takenSpots:
            continue

        board[obstacleCoord[0]][obstacleCoord[1]] = "\033[31m#\033[0m"
        takenSpots.append(obstacleCoord)
        break

for i in range(boxCount):
    while True:
        obstacleCoord = (randint(1, boardLength - 2), randint(1, boardWidth - 2))

        if obstacleCoord in takenSpots:
            continue

        board[obstacleCoord[0]][obstacleCoord[1]] = "\033[32mO\033[0m"
        takenSpots.append(obstacleCoord)
        break

robots = []

for i in range(amountOfRobots):
    while True: 
        coordinates = [randint(1, boardLength - 2), randint(1, boardWidth - 2)]

        if coordinates in takenSpots:
            continue

        board[coordinates[0]][coordinates[1]] = "\033[33m@\033[0m"
        takenSpots.append(coordinates)
        robots.append(coordinates)
        break

printBoard(board)
input("Start? ")

while True:
    cls()

    for i in range(len(robots)):
        moveChosen = choice([">", "<", "^", "v"])
        robots[i], board = move(moveChosen, robots[i], board)

    printBoard(board)

    total = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "\033[32mO\033[0m":
                total += GPS((i, j))

    print(f"\nGPS sum: {total}")

    sleep(delay)