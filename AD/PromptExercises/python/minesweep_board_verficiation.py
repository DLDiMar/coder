def verify_board(input_board):
    # Allow 0-8 as integers
    for row in input_board:
        for cell in row:
            if cell != '@' and not 0 <= cell <= 8:
                return False

    # Memoize '@' indices
    memo = {}
    for i in range(len(input_board)):
        for j in range(len(input_board[0])):
            if input_board[i][j] == '@':
                memo[(i, j)] = True

    # Verify values near mines
    for i in range(len(input_board)):
        for j in range(len(input_board[0])):
            if input_board[i][j] != '@':
                # Count number of '@' indices adjacent to current index
                count = 0
                for k in (-1, 0, 1):
                    for l in (-1, 0, 1):
                        if (i + k >= 0) and (i + k < len(input_board)) and \
                           (j + l >= 0) and (j + l < len(input_board[0])):
                            # Check if the key exists in memo before accessing it
                            if (i + k, j + l) in memo and memo[(i + k, j + l)]:
                                count += 1

                # Check if value at current index equals number of '@' indices adjacent to it
                if input_board[i][j] != count:
                    return False

    return True

# Example usage (unchanged):
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

if verify_board(input_board):
    print("Board is valid!")
else:
    print("Board is not valid!")
