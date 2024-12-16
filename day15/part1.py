directionDecoder = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

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

    if nextItem == None or nextItem == "#":
        return coordinates, listToUse
    
    elif nextItem == "O":
        i = 1
        
        if direction[0] == 0:
            while listToUse[coordinates[0]][coordinates[1] + (direction[1] * i)] == "O":
                i += 1

                try: 
                    if listToUse[coordinates[0]][coordinates[1] + (direction[1] * i)] == "#":
                        return coordinates, listToUse
                except: 
                    return coordinates, listToUse

            listToUse[coordinates[0]][coordinates[1] + (direction[1] * i)] = "O"
            listToUse[coordinates[0]][coordinates[1] + direction[1]] = "@"

        else:
            while listToUse[coordinates[0] + (direction[0] * i)][coordinates[1]] == "O":
                i += 1

                try: 
                    if listToUse[coordinates[0] + (direction[0] * i)][coordinates[1]] == "#":
                        return coordinates, listToUse
                except: 
                    return coordinates, listToUse
                
            listToUse[coordinates[0] + (direction[0] * i)][coordinates[1]] = "O"
            listToUse[coordinates[0] + direction[0]][coordinates[1]] = "@"

        listToUse[coordinates[0]][coordinates[1]] = "."

        coordinates = [coordinates[0] + direction[0], coordinates[1] + direction[1]]
        return coordinates, listToUse

    else:
        listToUse[coordinates[0]][coordinates[1]] = "."
        listToUse[coordinates[0] + direction[0]][coordinates[1] + direction[1]] = "@"

        coordinates = [coordinates[0] + direction[0], coordinates[1] + direction[1]]
        return coordinates, listToUse


with open ("day15/input.txt", "r") as f:
    contents = f.readlines()

    moves = ""
    board = []

    for i in range(contents.index("\n"), len(contents)):
        moves += contents[i].replace("\n", "")

    for i in range(contents.index("\n")):
        board.append([i for i in contents[i].replace("\n", "")])

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "@":
            coordinates = [i, j]
            break

for i in moves:
    coordinates, board = move(i, coordinates, board)

printBoard(board)

total = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "O":
            total += GPS((i, j))

    printBoard(board)

print(f"\nGPS sum: {total}")