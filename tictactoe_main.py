from helpers import print_board, clear_screen


#welcome message
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

#Display numbered board to show 9 positions
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

#print demo game board
print_board(board)

print("The board has 9 positions. Choose your positiona according to the board above.\n")

#clear board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

input("Press Enter to continue...")
clear_screen()

#Initialize game
game_on = True

while game_on:
    # Display game board
    print_board(board)
    
    # Get input from player
    user_choice = input("Choose position 1 - 9 or q to quit: ")
    
    if user_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        # Convert user_choice to an integer and update the board
        position = int(user_choice) - 1
        row = position // 3
        col = position % 3
        board[row][col] = "X"
    elif user_choice.lower() == "q":
        print("Thanks for playing!")
        game_on = False
    else:
        print("Invalid input")