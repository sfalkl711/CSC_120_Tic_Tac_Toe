"""
CSC 120 - Example Tic Tac Toe
board.py
Description:  second version, somewhat more function
includes player move to update board
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

def main():
    board = init_board()    # initialize board
    display_board(board)    # display board

    board = player_move(board, symbol = "X")
    display_board(board)

# invoke main
main()

