# Function to print the current board
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" *(len(board[i]*3)))

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

# Function to take player input and make a move
def player_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0, 1, or 2) separated by space: ").split())
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This position is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column between 0 and 2.")

# Main function to play the game
def play_game():
    board = [[" " for i in range(3)] for j in range(3)]  # Empty board
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        if current_player=="X":
            current_player="O"
        else:
            current_player="X"    

# Start the game
play_game()
