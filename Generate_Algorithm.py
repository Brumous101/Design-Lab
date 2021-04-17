import random

class Tile(object):
    def __init__(self,num):
        self.value = 0
        self.possible_values=["1","2","3","4","5","6","7","8","9"]
        self.tileNum = num
        self.possible_length = len(self.possible_values)

board = [ [],[],[],[],[],[],[],[],[] ]
tilelst = [Tile(i) for i in range(81)]
indexnum = 0
for tile in tilelst:
    if indexnum < 9:
        board[0].append(tile)
        indexnum += 1
    elif indexnum < 18:
        board[1].append(tile)
        indexnum += 1
    elif indexnum < 27:
        board[2].append(tile)
        indexnum += 1
    elif indexnum < 36:
        board[3].append(tile)
        indexnum += 1
    elif indexnum < 45:
        board[4].append(tile)
        indexnum += 1
    elif indexnum < 54:
        board[5].append(tile)
        indexnum += 1
    elif indexnum < 63:
        board[6].append(tile)
        indexnum += 1
    elif indexnum < 72:
        board[7].append(tile)
        indexnum += 1
    else:
        board[8].append(tile)
        indexnum += 1

row = 9
col = 9

def PrintPuzzle(board):
    for i in range(row):
        for j in range(col):
            if(( i == 0 and j == 0) or ( i == 3 and j == 0) or ( i == 6 and j == 0)):
                print("-------------------------")
            if (j == 0):
                print("| ", end='')
            #if mask[i][j] == True:
            #if board[i][j].value == 0:
            #    print(" ", end='')
            #else:
                # x = board[i][j].value
            x = board[i][j].value
            print(x, end='')
            #else:
            print(" ", end='')
            if (j == 2 or j == 5 or j == 8):
                print("| ", end='')
            
        print()
    print("-------------------------")

def Place(board):
    i = random.randint(0,8)
    j = random.randint(0,8)
    f = i % 3
    g = j % 3
    if board[i][j].value == 0:
        x = random.choice(board[i][j].possible_values)
        board[i][j].value = x
        # clear possible values from column
        for a in range(9):
            if board[i][a].possible_values.count(str(x)) > 0:
                board[i][a].possible_values.remove(x)
        # clear possible values from row
        for b in range(9):
            if board[b][j].possible_values.count(str(x)) > 0:
                board[b][j].possible_values.remove(x)
        # clear possible values from all in square
        for numx in range(3):
            for numy in range(3):
                if board[i-f+numx][j-g+numy].possible_values.count(str(x)) > 0:
                    board[i-f+numx][j-g+numy].possible_values.remove(x)

        board[i][j].possible_values.clear()
def PrintPuzzleVals(board):
    for i in range(row):
        for j in range(col):
            if(( i == 0 and j == 0) or ( i == 3 and j == 0) or ( i == 6 and j == 0)):
                print("-------------------------")
            if (j == 0):
                print("| ", end='')
            #if mask[i][j] == True:
            #if board[i][j].value == 0:
            #    print(" ", end='')
            #else:
                # x = board[i][j].value
            x = board[i][j].possible_values
            print(x, end='')
            #else:
            print(" ", end='')
            if (j == 2 or j == 5 or j == 8):
                print("| ", end='')
            
        print()
    print("-------------------------")

for number in range(78):
    Place(board)
PrintPuzzle(board)
PrintPuzzleVals(board)