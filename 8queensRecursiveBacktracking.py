# Define a recursive function to place the queens
# row: the current row being considered
# board: the current state of the chess board
def placeQueens(row, board):
    # If we have placed all 8 queens, print the board and return 1
    if row == 8:
        printBoard(board)
        return 1

    # Initialize a variable to keep track of the count of solutions found
    count = 0

    # Try placing the queen in each column of the current row
    for col in range(8):
        # Check if it's safe to place the queen in this column
        if isSafe(row, col, board):
            # If it's safe, place the queen and move on to the next row
            board[row][col] = 1
            count += placeQueens(row+1, board)
            board[row][col] = 0

    # Return the count of solutions found for this row
    return count

# Check if it's safe to place a queen at the given row and column
def isSafe(row, col, board):
    # Check if there is already a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
        # Check if there is already a queen in the diagonal
        # going from top left to bottom right
        j = row - i
        if col-j >= 0 and board[i][col-j] == 1:
            return False
        # Check if there is already a queen in the diagonal
        # going from top right to bottom left
        if col+j < 8 and board[i][col+j] == 1:
            return False
    # If it's safe, return True
    return True

# Print the current state of the board
def printBoard(board):
    for row in board:
        print(row)
    print()

# Initialize the board and call the placeQueens function
board = [[0 for i in range(8)] for j in range(8)]
count = placeQueens(0, board)
print(f"Total solutions: {count}")
