# Representations:
# # - non-selected square so far
# @ - mine, game over if user selects it
# 0 - Empty space, no mines present on adjacent squares
# 1-8 - a mine is present on 1-8 of the adjacent squares

# Important note: Adjacent squares include diagonally located mines

# Define the board size
BOARD_SIZE = 10

# Define the representations as a dictionary
REPS = {
    '#': 0,  # non-selected square
    '@': -1,  # mine
    0: 0,  # empty space
    1: 1,  # 1 adjacent mine
    2: 2,  # 2 adjacent mines
    3: 3,  # 3 adjacent mines
    4: 4,  # 4 adjacent mines
    5: 5,  # 5 adjacent mines
    6: 6,  # 6 adjacent mines
    7: 7,  # 7 adjacent mines
    8: 8  # 8 adjacent mines
}

# Define the user-facing board as a 2D list
user_board = [
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Define the solution board as a 2D list
solution_board = []

# Function to set up the boards from a 2D array input
def setup_boards(input_board):
    global solution_board
    solution_board = [[REPS[square] for square in row] for row in input_board]

# Example usage:
input_board = [
    [ '@', 1, 0, 0, 1, 1, 1, 0, 2, '@' ],
    [ 2, 1, 0, 0, 1, '@', 1, 0, 2, '@' ],
    [ '@', 1, 0, 0, 1, 1, 1, 0, 1, 1 ],
    [ 1, 1, 0, 1, 1, 1, 0, 0, 0, 0 ],
    [ 0, 0, 1, 3, '@', 2, 0, 0, 1, 1 ],
    [ 1, 1, 1, '@', '@', 1, 1, 0, 2, '@' ],
    [ '@', 1, 1, 2, 2, 1, 0, 0, 2, '@' ],
    [ 1, 1, 0, 0, 0, 0, 0, 0, 1, 1 ],
    [ 0, 0, 0, 1, 1, 1, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, '@', 1, 0, 0, 0, 0 ]
]

setup_boards(input_board)

print('User Board: ')
print(user_board)
print(' ')
print('Solution Board: ')
print(solution_board)