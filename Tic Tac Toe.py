board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winner = None
gameRunning = True
#game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
#take player input
def playerInput(board):
    inp = int(input("Enter a number between 1-9: "))
    if inp >= 1 and inp <= 9 and board [inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Oops player is already in that spot")
        playerInput(board)

#check for win, tie or lose

#switch the player

#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)