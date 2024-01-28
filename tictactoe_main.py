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

#print game board
#game board has 9 positions
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

print_board(board)

#take player input

#player_1 is x and player_2 is o

#check for win or tie

#switch the player

#check for win or tie