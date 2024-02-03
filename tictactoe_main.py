from helpers import print_board, clear_screen

# Welcome message
print("""
=======================
Welcome to tic-tac-toe!
=======================
""")

print("""
Welcome to Tic-Tac-Toe, a classic two-player game played on a 3x3 grid.
The objective is to be the first to complete a row, column, or diagonal with your symbol, either 'X' or 'O'.
Players take turns placing their symbol on an empty spot on the board.
The game ends when one player achieves a winning combination or when the board is full, resulting in a draw.
Keep your wits about you, strategize your moves, and aim to outsmart your opponent in this timeless game of Tic-Tac-Toe!
""")

# Display numbered board to show 9 positions
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Print demo game board
print_board(board)

print("The board has 9 positions. Choose your position according to the board above.\n")

# Clear board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

input("Press Enter to continue...")
clear_screen()

# Initialize game
game_on = True
current_player = "X"  # Start with player X
move_count = 0

# Player move placement
def player_move(position):
    # Convert user_choice to an integer and update the board
    position = int(position) - 1
    row = position // 3
    col = position % 3
    board[row][col] = current_player  # Use current player's symbol

# Check for winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

while game_on:
    # Display game board
    print_board(board)

    # Check for winner
    winner = check_winner(board, current_player)
    if winner:
        print(f"Congratulations! Player {current_player} has won!")
        break

    # Check for draw
    if all(cell != " " for row in board for cell in row):
        print("It's a draw!")
        break

    # Get input from current player
    while True:
        print(f"Player {current_player}'s turn.")
        user_choice = input("Choose position 1 - 9 or q to quit: ")

        if user_choice.lower() == "q":
            print("Thanks for playing!")
            game_on = False
            break

        elif user_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = int(user_choice) - 1
            row = position // 3
            col = position % 3

            if board[row][col] == " ":  # Check if the cell is empty
                player_move(user_choice)  # Valid move, proceed
                move_count += 1
                break
            else:
                print("Invalid move. Cell already occupied.")

        else:
            print("Invalid input")

    # Switch players for the next turn
    current_player = "O" if current_player == "X" else "X"