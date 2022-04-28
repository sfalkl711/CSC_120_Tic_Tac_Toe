"""
CSC 120 - Example Tic Tac Toe
board.py
Description:  third version, complete game
"""

# Define Constants
NUM_ROWS = 3     # number of rows
NUM_COLS = 3     # number of constant

def init_board():
    """
    initialize board as a list of lists
        where - means empty
    """

    board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]

    return board

def display_board(board):
    """
    display tic tac toe board
    """

    print("\n")
    for row in range(0,NUM_ROWS):
        for col in range(0,NUM_COLS):
            if col != NUM_COLS  - 1:
                # not the last column
                print(board[row][col]+" | ",end="")
            else:
                print(board[row][col])
    print("\n")

def is_valid_move(board,row,col):
    """
    returns True or False indicating of a move or row
    and column is valid for tic tac toe
    """

    if row > NUM_ROWS or row < 1:
       return False
    elif col > NUM_COLS or col < 1:
        return False
    elif board[row - 1][col - 1] != "-":
        return False
    else:
        return True

def player_move(board,symbol):
    """
    get move from a player with symbol and return updated board
    after the move
    """

    row_choice = int(input(f"Choose a row position from 1 to {NUM_ROWS}: "))
    col_choice = int(input(f"Choose a column position from 1 to {NUM_COLS}: "))

    # invalidation loop
    # continue to ask user their move until they enter a valid move
    while not is_valid_move(board,row_choice,col_choice):
        print("That is not a valid move choice.  Try again")
        row_choice = int(input(f"Choose a row position from 1 to {NUM_ROWS}: "))
        col_choice = int(input(f"Choose a column position from 1 to {NUM_COLS}: "))

    # update board with player move
    board[row_choice - 1][col_choice - 1] = symbol

    return(board)

def is_board_full(board):
    """
    returns True or False indicating if board is full
    """
    count_nonempty = 0    # initialize count of nonempty positions
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if board[row][col] != "-":
                # not empty
                count_nonempty += 1

    if count_nonempty == NUM_ROWS * NUM_COLS:
        # all positions are full
        return True
    else:
        return False

def is_row_won(board,row,symbol):
    """
    are all positions in the row the indicated symbol ?
    if yes, the player with that symbol WON
    """

    for col in range(NUM_COLS):
        if board[row - 1][col] != symbol:
            return False

    # all positions in the row have symbol, indicating WON
    return True

def is_col_won(board,col,symbol):
    """
    do all positions in the col the indicate symbol ?
    if yes, the player with that symbol WON
    """
    for row in range(NUM_ROWS):
        if board[row][col - 1] != symbol:
            return False

    # all positions in the rcol have symbol, indicating WON
    return True

def is_any_row_won(board,symbol):
    """
    did any row win for symbol
    """
    for row in range(NUM_ROWS):
        if is_row_won(board,row,symbol):
            return True

    # no row won
    return False

def is_any_col_won(board,symbol):
    """
    did any col win for symbol
    """
    for col in range(NUM_ROWS):
        if is_col_won(board,col,symbol):
            return True

    # no col won
    return False

def is_diag1_won(board,symbol):
    """
    do all positions in diagonal from high left to low right indicate symbol ?
    if yes, the player with that symbol WON
    """
    for row in range(NUM_ROWS):
        col = row
        if board[row][col] != symbol:
            return False

    # all positions in the diagonal from high left to low right have symbol, indicating WON
    return True

def is_diag2_won(board,symbol):
    """
    do all positions in diagonal from low left to high right indicate symbol ?
    if yes, the player with that symbol WON
    """
    for col in range(NUM_COLS):
        row = NUM_ROWS - 1 - col
        if board[row][col] != symbol:
            return False

    # all positions in the diagonal from low left to high right have symbol, indicating WON
    return True

def is_won(board,symbol):
    """
    has player with symbol WON the game
    """
    return is_any_row_won(board,symbol) or is_any_col_won(board,symbol) or is_diag1_won(board,symbol) or is_diag2_won(board,symbol)

def play_tictactoe():
    """
    play tic tac toe
    """
    is_game_over = False    # is the game finished
    board = init_board()    # initialize board
    current_player_symbol = "X"  # "X" goes first

    display_board(board)    # display board
    # continue to play until game is over
    while not is_game_over:
        print(f"\nPlayer {current_player_symbol}'s Turn:")
        board = player_move(board,current_player_symbol)   # player moves
        display_board(board)   # display the board

        if is_won(board,current_player_symbol):
            print(f"Player {current_player_symbol} won !")
            is_game_over = True
        elif is_board_full(board):
            print(f"Game Over as a DRAW")
            is_game_over = True
        else:
            # game is not over yet

            # switch players
            if current_player_symbol == "X":
                current_player_symbol = "O"
            else:
                current_player_symbol = "X"

    # game is over
    print("Thank you for Playing Tic Tac Toe ")

def main():
    play_tictactoe()

# invoke main
main()
