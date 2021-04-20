import random
import copy

class Tile(object):
    def __init__(self,num):
        self.value = 0
        self.possible_values=["1","2","3","4","5","6","7","8","9"]
        self.tileNum = num
        self.possible_length = len(self.possible_values)

board = [ [],[],[],[],[],[],[],[],[] ]
butterflyBoard = [ [],[],[],[],[],[],[],[],[] ]
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
    if (board[i][j].value == 0) and (len(board[i][j].possible_values) > 0):
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
            x = board[i][j].possible_values
            print(x, end='')
            print(" ", end='')
            if (j == 2 or j == 5 or j == 8):
                print("| ", end='')
            
        print()
    print("-------------------------")

def GenerateButterflyBoard(board):
    smallestPossible = 9
    smallestiIndex = -1
    smallestjIndex = -1
    while(True):
        i = random.randint(0,8)
        j = random.randint(0,8)
        f = i % 3
        g = j % 3
        # Go through all tiles and find the smallest possible length of values it can be
        for c in range(9):
            for d in range(9):
                if (len(board[c][d].possible_values) <= smallestPossible) and (len(board[c][d].possible_values) != 0):
                    smallestPossible = len(board[c][d].possible_values)
                    smallestiIndex = c
                    smallestjIndex = d
        if smallestPossible == 1:
            break
        # Place a Number randomly
        if (board[i][j].value == 0) and (len(board[i][j].possible_values) > 0):
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
    print("Generate Butterfly: smallestPossible", smallestPossible, "smallestiIndex:", smallestiIndex, " smallestjIndex: ",smallestjIndex)

def ContinueButterflyBoard(board):
    for i in range(9):
        for j in range(9):
            if (board[i][j].value == 0) and (len(board[i][j].possible_values) == 1):
                f = i % 3
                g = j % 3
                # We are humans who aren't picking randomly!
                x = board[i][j].possible_values[0]
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
                # Recursively do this function till either a finish board or we have to guess
                print("Continue was called and able to place", x, "at", "board[", i, "]","[", j, "]")
                ContinueButterflyBoard(board)

def Update(butterflyboard, board):
    smallestPossible = 9
    smallestiIndex = -1
    smallestjIndex = -1
    for c in range(9):
            for d in range(9):
                if (len(butterflyboard[c][d].possible_values) <= smallestPossible) and (len(butterflyboard[c][d].possible_values) > 0):
                    smallestPossible = len(board[c][d].possible_values)
                    smallestiIndex = c
                    smallestjIndex = d
    if (butterflyboard[smallestiIndex][smallestjIndex].value == 0):
        f = smallestiIndex % 3
        g = smallestjIndex % 3
        # We need to pick a random number to update our original puzzle because it wasn't complete
        x = random.choice(butterflyboard[smallestiIndex][smallestjIndex].possible_values)
        board[smallestiIndex][smallestjIndex].value = x
        # clear possible values from column
        for a in range(9):
            if board[smallestiIndex][a].possible_values.count(str(x)) > 0:
                board[smallestiIndex][a].possible_values.remove(x)
        # clear possible values from row
        for b in range(9):
            if board[b][smallestjIndex].possible_values.count(str(x)) > 0:
                board[b][smallestjIndex].possible_values.remove(x)
        # clear possible values from all in square
        for numx in range(3):
            for numy in range(3):
                if board[smallestiIndex-f+numx][smallestjIndex-g+numy].possible_values.count(str(x)) > 0:
                    board[smallestiIndex-f+numx][smallestjIndex-g+numy].possible_values.remove(x)
        board[smallestiIndex][smallestjIndex].possible_values.clear()
    print("Update was called and able to place", x, "at", "board[", smallestiIndex, "]","[", smallestjIndex, "]")


GenerateButterflyBoard(board)
butterflyBoard = copy.deepcopy(board)
PrintPuzzle(butterflyBoard)
ContinueButterflyBoard(butterflyBoard)
PrintPuzzle(butterflyBoard)
Update(butterflyBoard, board) # Maybe do a check in this to see if all tiles are filled in butterfly?
print("v butterfly board after update v")
PrintPuzzle(butterflyBoard)
print("v board after update v")
PrintPuzzle(board)
butterflyBoard = copy.deepcopy(board)
print("v butterfly board after clone v")
PrintPuzzle(butterflyBoard)

ContinueButterflyBoard(butterflyBoard)
print("v butterfly board after continue #2 v")
PrintPuzzle(butterflyBoard)
# At this point it is possible to have a complete board but not likely
# We need to save off the GenerateButterflyBoard and pass continue a clone
# When we update the board we need to pass the update function the Continued Butterfly Board and whatever change it makes, we need to make the same change on the original.
# I need to pass the update board my butterfly board because it's been updated but changed to butterfly board need to be reflected into the orginal and 
# the butterfly board will then be 
# Generate -> make BUTTERFLY ->continue the BUTTERFLY-> Update ORIGNAL using passed BUTTERFLY-> recopy BUTTERFLY-> continue the butterfly till solved

# The above comments now work!
# Now just need to put them in a while loop and combine them all together