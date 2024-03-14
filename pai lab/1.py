import random

def print_board(board):
    print("  1 2 3")
    for i in range(3):
        print(f"{i+1} {' '.join(board[i])}")

def check_winner(board, player):
    # Check for row wins
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check for column wins
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check for diagonal wins
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
                return row - 1, col - 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def computer_move(board, computer, player):
    available_moves = get_available_moves(board)
    
    # Try to win
    for move in available_moves:
        board[move[0]][move[1]] = computer
        if check_winner(board, computer):
            return move
        board[move[0]][move[1]] = ' '  # Undo move

    # Block player from winning
    for move in available_moves:
        board[move[0]][move[1]] = player
        if check_winner(board, player):
            board[move[0]][move[1]] = computer
            return move
        board[move[0]][move[1]] = ' '  # Undo move

    # Otherwise, make a random move
    return random.choice(available_moves)

def play_game():
    board = [[' ' for i in range(3)] for j in range(3)] 
    player = 'X'
    computer = 'O'

    while True:
        print_board(board)

        if check_winner(board, player):
            print("Congratulations! You win!")
            break
        elif check_winner(board, computer):
            print("Computer wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        if player == 'X':
            row, col = player_move(board)
            board[row][col] = 'X'
            if check_winner(board, 'X'):
                print_board(board)
                print("Congratulations! You win!")
                return
            player = 'O'
            computer = 'X'
        else:
            row, col = computer_move(board, computer, player)
            board[row][col] = 'O'
            if check_winner(board, 'O'):
                print_board(board)
                print("Computer wins!")
                return
            player = 'X'
            computer = 'O'


if __name__ == "__main__":
    play_game()



