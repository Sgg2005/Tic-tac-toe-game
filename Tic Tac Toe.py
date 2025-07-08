# Tic Tac Toe Game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
winner = None
gameRunning = True

# Get custom symbols from players
player1_symbol = input("Player 1, choose your symbol: ")
while len(player1_symbol) != 1 or player1_symbol == "-":
    player1_symbol = input("Invalid symbol. Choose a single character (not '-'): ")

player2_symbol = input("Player 2, choose your symbol: ")
while len(player2_symbol) != 1 or player2_symbol == "-" or player2_symbol == player1_symbol:
    player2_symbol = input("Invalid symbol. Choose a different single character (not '-'): ")

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input
def playerInput(board, mark, player_num):
    inp = int(input(f"Enter a number between 1-9 player {player_num}: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = mark
    else:
        print("Oops player is already in that spot")
        playerInput(board, mark, player_num)

# check for win, tie or lose
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board and winner is None:
        printBoard(board)
        print("It's a tie! no one wins")
        gameRunning = False
        return True
    return False

def checkWin():
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board):
        printBoard(board)
        if winner == player1_symbol:
            print("The winner is Player 1!")
        elif winner == player2_symbol:
            print("The winner is Player 2!")
        return True

while gameRunning:
    printBoard(board)
    # Player 1
    playerInput(board, player1_symbol, 1)
    if checkTie(board) or checkWin():
        break
    printBoard(board)
    # Player 2
    playerInput(board, player2_symbol, 2)
    if checkTie(board) or checkWin():
        break