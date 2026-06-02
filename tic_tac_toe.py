import random 

board = [
    [' ', ' | ', ' ', ' | ', ' '],
    ['--', '-', '---', '-', '--'],
    [' ', ' | ', ' ', ' | ', ' '],
    ['--', '-', '---', '-', '--'],
    [' ', ' | ', ' ', ' | ', ' '],
]
    
def Print_board(board):
    print()
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end="")
        print()
    print()

def Utility(board):
    # Check Rows
    for row in range(0, len(board), 2):
        # Added != ' ' check
        if board[row][0] != ' ' and board[row][0] == board[row][2] == board[row][4]:
            return 1 if board[row][0] == 'X' else -1
            
    # Check Columns
    for col in range(0, len(board[0]), 2):
        if board[0][col] != ' ' and board[0][col] == board[2][col] == board[4][col]:
            return 1 if board[0][col] == 'X' else -1
            
    # Check Diagonals
    if board[0][0] != ' ' and board[0][0] == board[2][2] == board[4][4]:
        return 1 if board[0][0] == 'X' else -1
        
    if board[0][4] != ' ' and board[0][4] == board[2][2] == board[4][0]:
        return 1 if board[0][4] == 'X' else -1

    return 0

def Actions(board):
    moves = []
    for row in range(0, len(board), 2):
        for col in range(0, len(board[0]), 2):
            if board[row][col] == ' ':
                moves.append([row,col])
    return moves

def Terminal(board):
    if len(Actions(board)) == 0 or Utility(board) != 0: 
        return True
    return False

def Result(board, action, player):
    row = action[0]
    col = action[1]
    board[row][col] = player
    return board

def Max_value(board, alpha=-1e9, beta=1e9):
    player = 'X'
    if Terminal(board):
        return Utility(board)
    val = -1e9
    for action in Actions(board):
        val = max(val, Min_value(Result([r[:] for r in board], action, player), alpha, beta))

        # pruning logic 
        alpha = max(alpha, val)
        if beta <= alpha:
            break
    return val

def Min_value(board, alpha=-1e9, beta=1e9):
    player = 'O'
    if Terminal(board):
        return Utility(board)
    val = 1e9
    for action in Actions(board):
        val = min(val, Max_value(Result([r[:] for r in board], action, player), alpha, beta))

        beta = min(beta, val)
        if beta <= alpha:
            break
    return val

# ================= function to play game with an AI =================
def play_game(board):
    human_player = input("Choose one (X or O) : ")

    while not Terminal(board):
        # player1 logic 
        player1 = human_player

        player1_row = int(input("Choose row (0, 2, 4) : "))
        player1_col = int(input("Choose col (0, 2, 4) : "))
        player1_action = [player1_row, player1_col]
        board = Result(board, player1_action, player1)

        Print_board(board)

        if Terminal(board):break

        # player2 logic 
        print("Ai is thinking ...\n")

        if player1 == 'X':
            player2 = 'O'
            best_val = 1e9
            best_mov = None

            for action in Actions(board):
                mov_val = Max_value(Result([r[:] for r in board], action, player2), -1e9, 1e9)
                if mov_val < best_val:
                    best_val = mov_val
                    best_mov = action

            board = Result(board, best_mov, player2)
            Print_board(board)
            
        else:
            player2 = 'X'
            best_val = -1e9
            best_mov = None

            for action in Actions(board):
                mov_val = Min_value(Result([r[:] for r in board], action, player2), -1e9, 1e9)
                if mov_val > best_val:
                    best_val = mov_val
                    best_mov = action

            board = Result(board, best_mov, player2)
            Print_board(board)

    print(f"Final Utility of the board : {Utility(board)}")
    print(f"Resultant board : ")
    Print_board(board)

# ================= funtion to let two AI's play the game =================
def ai_vs_ai(board):
    while not Terminal(board):
        # Ai 1 logic 
        player1 = 'X'

        print("Ai 1 is thinking ...\n")
        player1_best_val = 1e9
        player1_best_moves = []

        for action in Actions(board):
            player1_mov_val = Max_value(Result([r[:] for r in board], action, player1), -1e9, 1e9)
            if player1_mov_val == player1_best_val:
                player1_best_moves.append(action)
            elif player1_mov_val < player1_best_val:
                player1_best_val = player1_mov_val
                player1_best_moves = [action]
        
        player1_best_mov = random.choice(player1_best_moves)
        board = Result(board, player1_best_mov, player1)
        Print_board(board)

        if Terminal(board): break

        # Ai 2 logic 
        player2 = 'O'

        print("Ai 2 is thinking ...\n")
        player2_best_val = -1e9
        player2_best_moves = []

        for action in Actions(board):
            player2_mov_val = Min_value(Result([r[:] for r in board], action, player2), -1e9, 1e9)
            if player2_mov_val == player2_best_val:
                player2_best_moves.append(action)
            elif player2_mov_val > player2_best_val:
                player2_best_val = player2_mov_val
                player2_best_moves = [action]

        player2_best_mov = random.choice(player2_best_moves)
        board = Result(board, player2_best_mov, player2)
        Print_board(board)

    print(f"Utilitiy of the board : {Utility(board)}")
    print("Resultant board : ")
    Print_board(board)

# Call the functions here 
# play_game(board)
# ai_vs_ai(board)
