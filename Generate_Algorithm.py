solved_board = [
    [8,2,7,1,5,4,3,9,6],
    [9,6,5,3,2,7,1,4,8],
    [3,4,1,6,8,9,7,5,2],
    [5,9,3,4,6,8,2,7,1],
    [4,7,2,5,1,3,6,8,9],
    [6,1,8,9,7,2,4,3,5],
    [7,8,6,2,3,5,9,1,4],
    [1,5,4,7,9,6,8,2,3],
    [2,3,9,8,4,1,5,6,7]
]
mask = [
    [False,True,False,False,False,True,True,False,False,],
    [True,False,False,False,True,False,False,False,True,],
    [False,False,False,True,False,True,False,True,False,],
    [False,False,False,False,False,False,False,False,True,],
    [False,True,True,True,False,True,True,True,False,],
    [True,False,False,False,False,False,False,False,False,],
    [False,True,False,True,False,True,False,False,False,],
    [True,False,False,False,True,False,False,False,True,],
    [False,False,True,True,False,False,False,True,False,]
]
row = len(solved_board[0])
col = len(solved_board[0])

unsolved_board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

top_left = 0
top_middle = 0
top_right = 0
middle_left = 0
middle_middle = 0
middle_right = 0
bottom_left = 0
bottom_middle = 0
bottom_right = 0
one_counter = 0
two_counter = 0
three_counter = 0
four_counter = 0
five_counter = 0
six_counter = 0
seven_counter = 0
eight_counter = 0
nine_counter = 0

def PrintPuzzle(board):
    for i in range(row):
        for j in range(col):
            if(( i == 0 and j == 0) or ( i == 3 and j == 0) or ( i == 6 and j == 0)):
                print("-------------")
            if (j == 0):
                print("|", end='')
            if mask[i][j] == True:
                print(board[i][j], end='')
            else:
                print(" ", end='')
            if (j == 2 or j == 5 or j == 8):
                print("|", end='')
            
        print()
    print("-------------")

def CopyPuzzle():
    for i in range(row):
        for j in range(col):
            if mask[i][j] == True:
                unsolved_board[i][j] = solved_board[i][j]

def CountAllSquares(board):
    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    one_counter = 0
    two_counter = 0
    three_counter = 0
    four_counter = 0
    five_counter = 0
    six_counter = 0
    seven_counter = 0
    eight_counter = 0
    nine_counter = 0
    CheckTopLeftSquare(board)
    CheckTopMiddleSquare(board)
    CheckTopRightSquare(board)
    CheckMiddleLeftSquare(board)
    CheckMiddleMiddleSquare(board)
    CheckMiddleRightSquare(board)
    CheckBottomLeftSquare(board)
    CheckBottomMiddleSquare(board)
    CheckBottomRightSquare(board)
    
def CheckTopLeftSquare(board):
    global top_left
    top_left = 0
    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                top_left = top_left + 1
                # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                if board[i][j] == 1:
                    one_counter = one_counter + 1
                if board[i][j] == 2:
                    two_counter = two_counter + 1
                if board[i][j] == 3:
                    three_counter = three_counter + 1
                if board[i][j] == 4:
                    four_counter = four_counter + 1
                if board[i][j] == 5:
                    five_counter = five_counter + 1
                if board[i][j] == 6:
                    six_counter = six_counter + 1
                if board[i][j] == 7:
                    seven_counter = seven_counter + 1
                if board[i][j] == 8:
                    eight_counter = eight_counter + 1
                if board[i][j] == 9:
                    nine_counter = nine_counter + 1
    return
def CheckTopMiddleSquare(board):
    global top_middle
    top_middle = 0

    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(3):
            for j in range(3,6):
                if board[i][j] != 0:
                    top_middle = top_middle + 1
                    # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                    if board[i][j] == 1:
                        one_counter = one_counter + 1
                    if board[i][j] == 2:
                        two_counter = two_counter + 1
                    if board[i][j] == 3:
                        three_counter = three_counter + 1
                    if board[i][j] == 4:
                        four_counter = four_counter + 1
                    if board[i][j] == 5:
                        five_counter = five_counter + 1
                    if board[i][j] == 6:
                        six_counter = six_counter + 1
                    if board[i][j] == 7:
                        seven_counter = seven_counter + 1
                    if board[i][j] == 8:
                        eight_counter = eight_counter + 1
                    if board[i][j] == 9:
                        nine_counter = nine_counter + 1
def CheckTopRightSquare(board):
    global top_right
    top_right = 0

    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(3):
            for j in range(6,9):
                if board[i][j] != 0:
                    top_right = top_right + 1
                    # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                    if board[i][j] == 1:
                        one_counter = one_counter + 1
                    if board[i][j] == 2:
                        two_counter = two_counter + 1
                    if board[i][j] == 3:
                        three_counter = three_counter + 1
                    if board[i][j] == 4:
                        four_counter = four_counter + 1
                    if board[i][j] == 5:
                        five_counter = five_counter + 1
                    if board[i][j] == 6:
                        six_counter = six_counter + 1
                    if board[i][j] == 7:
                        seven_counter = seven_counter + 1
                    if board[i][j] == 8:
                        eight_counter = eight_counter + 1
                    if board[i][j] == 9:
                        nine_counter = nine_counter + 1
def CheckMiddleLeftSquare(board):
    global middle_left
    middle_left = 0

    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(3,6):
        for j in range(3):
            if board[i][j] != 0:
                middle_left = middle_left + 1
                # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                if board[i][j] == 1:
                    one_counter = one_counter + 1
                if board[i][j] == 2:
                    two_counter = two_counter + 1
                if board[i][j] == 3:
                    three_counter = three_counter + 1
                if board[i][j] == 4:
                    four_counter = four_counter + 1
                if board[i][j] == 5:
                    five_counter = five_counter + 1
                if board[i][j] == 6:
                    six_counter = six_counter + 1
                if board[i][j] == 7:
                    seven_counter = seven_counter + 1
                if board[i][j] == 8:
                    eight_counter = eight_counter + 1
                if board[i][j] == 9:
                    nine_counter = nine_counter + 1
def CheckMiddleMiddleSquare(board):
    global middle_middle
    middle_middle = 0

    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(3,6):
        for j in range(3,6):
            if board[i][j] != 0:
                middle_middle = middle_middle + 1
                # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                if board[i][j] == 1:
                    one_counter = one_counter + 1
                if board[i][j] == 2:
                    two_counter = two_counter + 1
                if board[i][j] == 3:
                    three_counter = three_counter + 1
                if board[i][j] == 4:
                    four_counter = four_counter + 1
                if board[i][j] == 5:
                    five_counter = five_counter + 1
                if board[i][j] == 6:
                    six_counter = six_counter + 1
                if board[i][j] == 7:
                    seven_counter = seven_counter + 1
                if board[i][j] == 8:
                    eight_counter = eight_counter + 1
                if board[i][j] == 9:
                    nine_counter = nine_counter + 1
def CheckMiddleRightSquare(board):
    global middle_right
    middle_right = 0

    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(3,6):
        for j in range(6,9):
            if board[i][j] != 0:
                middle_right = middle_right + 1
                # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                if board[i][j] == 1:
                    one_counter = one_counter + 1
                if board[i][j] == 2:
                    two_counter = two_counter + 1
                if board[i][j] == 3:
                    three_counter = three_counter + 1
                if board[i][j] == 4:
                    four_counter = four_counter + 1
                if board[i][j] == 5:
                    five_counter = five_counter + 1
                if board[i][j] == 6:
                    six_counter = six_counter + 1
                if board[i][j] == 7:
                    seven_counter = seven_counter + 1
                if board[i][j] == 8:
                    eight_counter = eight_counter + 1
                if board[i][j] == 9:
                    nine_counter = nine_counter + 1
def CheckBottomLeftSquare(board):
    global bottom_left
    bottom_left = 0

    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(6,9):
        for j in range(3):
            if board[i][j] != 0:
                bottom_left = bottom_left + 1
                # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                if board[i][j] == 1:
                    one_counter = one_counter + 1
                if board[i][j] == 2:
                    two_counter = two_counter + 1
                if board[i][j] == 3:
                    three_counter = three_counter + 1
                if board[i][j] == 4:
                    four_counter = four_counter + 1
                if board[i][j] == 5:
                    five_counter = five_counter + 1
                if board[i][j] == 6:
                    six_counter = six_counter + 1
                if board[i][j] == 7:
                    seven_counter = seven_counter + 1
                if board[i][j] == 8:
                    eight_counter = eight_counter + 1
                if board[i][j] == 9:
                    nine_counter = nine_counter + 1
def CheckBottomMiddleSquare(board):
    global bottom_middle
    bottom_middle = 0

    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(6,9):
        for j in range(3,6):
            if board[i][j] != 0:
                bottom_middle = bottom_middle + 1
                # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                if board[i][j] == 1:
                    one_counter = one_counter + 1
                if board[i][j] == 2:
                    two_counter = two_counter + 1
                if board[i][j] == 3:
                    three_counter = three_counter + 1
                if board[i][j] == 4:
                    four_counter = four_counter + 1
                if board[i][j] == 5:
                    five_counter = five_counter + 1
                if board[i][j] == 6:
                    six_counter = six_counter + 1
                if board[i][j] == 7:
                    seven_counter = seven_counter + 1
                if board[i][j] == 8:
                    eight_counter = eight_counter + 1
                if board[i][j] == 9:
                    nine_counter = nine_counter + 1
def CheckBottomRightSquare(board):
    global bottom_right
    bottom_right = 0

    global one_counter
    global two_counter
    global three_counter
    global four_counter
    global five_counter
    global six_counter
    global seven_counter
    global eight_counter
    global nine_counter
    for i in range(6,9):
            for j in range(6,9):
                if board[i][j] != 0:
                    bottom_right = bottom_right + 1
                    # This code is implemented inside of the if statement to limit comparisons and have fail fast behavior
                    if board[i][j] == 1:
                        one_counter = one_counter + 1
                    if board[i][j] == 2:
                        two_counter = two_counter + 1
                    if board[i][j] == 3:
                        three_counter = three_counter + 1
                    if board[i][j] == 4:
                        four_counter = four_counter + 1
                    if board[i][j] == 5:
                        five_counter = five_counter + 1
                    if board[i][j] == 6:
                        six_counter = six_counter + 1
                    if board[i][j] == 7:
                        seven_counter = seven_counter + 1
                    if board[i][j] == 8:
                        eight_counter = eight_counter + 1
                    if board[i][j] == 9:
                        nine_counter = nine_counter + 1

CopyPuzzle()
PrintPuzzle(unsolved_board)
CountAllSquares(unsolved_board)
