# Single-player battleship, 2 ships
# Setting up the board
from random import randint

board = []

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):
    for row in board:
        print " ".join(row)

# Starting the game
print "Let's play Battleship! Guess coordinates between 0 and 5. If you find one of the two ships, you win!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship1_row = random_row(board)
ship1_col = random_col(board)

ship2_row = random_row(board)
ship2_col = random_col(board)

if ship1_row == ship2_row and ship1_col == ship2_col:
    ship2_row = ship2_row + 1
    if ship2_row > 5:
        ship2_row = ship2_row - 2
 
# Player input guesses
for turn in range(4):
    
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship1_row and guess_col == ship1_col:
        print "Congratulations! You sunk my battleship!"
        break
    elif guess_row == ship2_row and guess_col == ship2_col:
        print "Congratulations! You sunk my battleship!"
        break
    elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    if turn == 3:
        print "Game Over."
        break
    print "Turn", turn+1
    print_board(board)