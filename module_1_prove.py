"""
CSE210
Week 2: Module 1: Tictactoe Assignment
Author: Gary Sibanda
"""

# board
# print board
# play game
# check win
# check tie
# swap turn

# Global variable declaration
game_still_on = True
current_player ="x"
winner = None

# Main function (play game)
def main():
    board = make_board()
    show_board(board)

    while game_still_on:
        handle_turn(board)
        check_win(board)

        swap_player()
    print("Great game. Thanks for playing.")
    print(f"{winner} wins the game.")


# Make the board
def make_board():
    board = []
    for position in range(9):
        board.append(position + 1)
    return board

# Display the board.
def show_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("- + - + -")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("- + - + -")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Prompt user for a board position.
def handle_turn(board):
    position = int(input(f"{current_player}'s turn to choose a square(1-9): "))
    position -= 1

    board[position] = current_player

    show_board(board)

# Alternate players with each turn.
def swap_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"

# Check if game has a winner.
def check_win(board):
    global current_player
    global winner
    global game_still_on
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8]):
        winner = current_player
        game_still_on = False
    else:
        game_still_on = True


main()