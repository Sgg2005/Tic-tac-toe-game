import random

def get_player_symbol(name, taken_symbol=None):
    symbol = input(f"{name}, choose your symbol: ")
    while (
        len(symbol) != 1 or symbol == "-" or
        (taken_symbol is not None and symbol == taken_symbol)
    ):
        if taken_symbol is not None and symbol == taken_symbol:
            symbol = input("Invalid symbol. Choose a different single character (not '-'): ")
        else:
            symbol = input("Invalid symbol. Choose a single character (not '-'): ")
    return symbol

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board, mark, player_name):
    try:
        inp = int(input(f"{player_name}, enter a number between 1-9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = mark
        else:
            print("Oops, that spot is already taken or invalid.")
            playerInput(board, mark, player_name)
    except ValueError:
        print("Please enter a valid number.")
        playerInput(board, mark, player_name)

def aiInput_easy(board, mark):
    available = [i for i, spot in enumerate(board) if spot == "-"]
    # 70% chance to pick random, 30% to pick a really bad move (if possible)
    if random.random() < 0.3 and len(available) > 1:
        move = available[0]  # always pick the first available (stupid move)
    else:
        move = random.choice(available)
    print(f"AI (Easy) chooses position {move+1}")
    board[move] = mark

def aiInput_medium(board, ai_mark, player_mark):
    # Try to win
    for i in range(9):
        if board[i] == "-":
            board[i] = ai_mark
            if is_winner(board, ai_mark):
                print(f"AI (Medium) chooses position {i+1}")
                return
            board[i] = "-"
    # Try to block player win
    for i in range(9):
        if board[i] == "-":
            board[i] = player_mark
            if is_winner(board, player_mark):
                board[i] = ai_mark
                print(f"AI (Medium) chooses position {i+1}")
                return
            board[i] = "-"
    # Otherwise, pick random
    available = [i for i, spot in enumerate(board) if spot == "-"]
    move = random.choice(available)
    print(f"AI (Medium) chooses position {move+1}")
    board[move] = ai_mark

def aiInput_hard(board, ai_mark, player_mark):
    # 10% chance to make a random move (to keep it winnable)
    if random.random() < 0.1:
        available = [i for i, spot in enumerate(board) if spot == "-"]
        move = random.choice(available)
        print(f"AI (Hard, random) chooses position {move+1}")
        board[move] = ai_mark
        return
    # Otherwise, use minimax
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == "-":
            board[i] = ai_mark
            score = minimax(board, 0, False, ai_mark, player_mark)
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i
    print(f"AI (Hard) chooses position {best_move+1}")
    board[best_move] = ai_mark

def is_winner(board, mark):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diags
    ]
    for cond in win_conditions:
        if all(board[i] == mark for i in cond):
            return True
    return False

def minimax(board, depth, is_maximizing, ai_mark, player_mark):
    if is_winner(board, ai_mark):
        return 10 - depth
    if is_winner(board, player_mark):
        return depth - 10
    if "-" not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = ai_mark
                score = minimax(board, depth+1, False, ai_mark, player_mark)
                board[i] = "-"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = player_mark
                score = minimax(board, depth+1, True, ai_mark, player_mark)
                board[i] = "-"
                best_score = min(score, best_score)
        return best_score

def checkHorizontle(board):
    global winner
    for i in [0, 3, 6]:
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            winner = board[i]
            return True

def checkRow(board):
    global winner
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            winner = board[i]
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
        print("It's a tie! No one wins.")
        gameRunning = False
        return True
    return False

def checkWin(board, player1_symbol, player2_symbol, player1_name, player2_name):
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board):
        printBoard(board)
        if winner == player1_symbol:
            print(f"The winner is {player1_name}!")
        elif winner == player2_symbol:
            print(f"The winner is {player2_name}!")
        return True

def play_game(mode):
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    global winner, gameRunning
    winner = None
    gameRunning = True

    if mode == "1":
        player1_name = input("Player 1, enter your name: ")
        player1_symbol = get_player_symbol(player1_name)
        player2_name = input("Player 2, enter your name: ")
        player2_symbol = get_player_symbol(player2_name, player1_symbol)
        is_ai = False
        ai_level = None
    else:
        player1_name = input("Enter your name: ")
        player1_symbol = get_player_symbol(player1_name)
        player2_name = "AI"
        player2_symbol = "O" if player1_symbol != "O" else "X"
        is_ai = True
        print("Choose AI level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        ai_level = input("Enter 1, 2, or 3: ")
        while ai_level not in ("1", "2", "3"):
            ai_level = input("Invalid choice. Enter 1, 2, or 3: ")

    while gameRunning:
        printBoard(board)
        # Player 1
        playerInput(board, player1_symbol, player1_name)
        if checkTie(board) or checkWin(board, player1_symbol, player2_symbol, player1_name, player2_name):
            break
        printBoard(board)
        # Player 2 or AI
        if is_ai:
            if ai_level == "1":
                aiInput_easy(board, player2_symbol)
            elif ai_level == "2":
                aiInput_medium(board, player2_symbol, player1_symbol)
            else:
                aiInput_hard(board, player2_symbol, player1_symbol)
        else:
            playerInput(board, player2_symbol, player2_name)
        if checkTie(board) or checkWin(board, player1_symbol, player2_symbol, player1_name, player2_name):
            break
while True:
    print("Choose game mode:")
    print("1. Player vs Player")
    print("2. Player vs AI")
    mode = input("Enter 1 or 2: ")
    if mode not in ("1", "2"):
        print("Invalid choice.")
        continue
    play_game(mode)
    while True:
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay in ("y", "n"):
            break
        print("Invalid input. Please enter 'y' or 'n'.")
    if replay != "y":
        print("Thanks for playing!")
        break