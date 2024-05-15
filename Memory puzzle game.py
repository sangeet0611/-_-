import random

# Function to generate the game board
def generate_board(size):
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    num_pairs = size * size // 2
    pairs = random.sample(symbols, num_pairs)
    board = pairs * 2
    random.shuffle(board)
    return [board[i:i+size] for i in range(0, len(board), size)]

# Function to display the game board
def display_board(board, revealed):
    for i in range(len(board)):
        row = ''
        for j in range(len(board[i])):
            if revealed[i][j]:
                row += board[i][j]
            else:
                row += '-'
            row += ' '
        print(row)

# Function to check if all pairs have been found
def all_revealed(revealed):
    return all(all(row) for row in revealed)

# Main function to run the game
def main():
    size = 4  
    board = generate_board(size)
    revealed = [[False] * size for _ in range(size)]
    display_board(board, revealed)

    while not all_revealed(revealed):
        print("Enter the coordinates (row and column) of the card you want to flip (e.g., '0 1'): ")
        try:
            row, col = map(int, input().split())
            if row < 0 or row >= size or col < 0 or col >= size:
                print("Invalid coordinates. Please try again.")
                continue
            if revealed[row][col]:
                print("This card has already been revealed. Please choose another.")
                continue
            revealed[row][col] = True
            display_board(board, revealed)
            print("Enter the coordinates of another card to flip: ")
            row2, col2 = map(int, input().split())
            if row2 < 0 or row2 >= size or col2 < 0 or col2 >= size:
                print("Invalid coordinates. Please try again.")
                continue
            if revealed[row2][col2]:
                print("This card has already been revealed. Please choose another.")
                continue
            revealed[row2][col2] = True
            display_board(board, revealed)
            if board[row][col] != board[row2][col2]:
                print("Cards do not match. Try again.")
                revealed[row][col] = revealed[row2][col2] = False
            else:
                print("Match found!")
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")

    print("Congratulations! You've found all the pairs!")

if __name__ == "__main__":
    main()
