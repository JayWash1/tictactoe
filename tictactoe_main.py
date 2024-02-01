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
    #Display game board
    print_board(board)
    #Get input from player
    choice = input("Choose position: ")
    if choice == "1":
        board[0][0] = "X"
    if choice == "2":
        board[0][1] = "X"
    if choice == "3":
        board[0][2] = "X"
    if choice == "4":
        board[1][0] = "X"
    if choice == "5":
        board[1][1] = "X"
    if choice == "6":
        board[1][2] = "X"
    if choice == "7":
        board[2][0] = "X"
    if choice == "8":
        board[2][1] = "X"
    if choice == "9":
        board[2][2] = "X"
    else:
        game_on = False

#board[0][0] = "X"

print_board(board)

#player_1 is x and player_2 is o

#check for win or tie

#switch the player

#check for win or tie