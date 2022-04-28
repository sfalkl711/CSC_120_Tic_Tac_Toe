"""
CSC 120 - Example Tic Tac Toe
board.py
Description:  first version, limited function
just creates an empty board and displays it
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

def main():
    board = init_board()    # initialize board
    display_board(board)    # display board

# invoke main
main()
