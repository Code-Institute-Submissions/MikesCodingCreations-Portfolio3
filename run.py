import random


# Function to display the game board
def display_board(board):
    size = len(board)
    print("  " + "   ".join([chr(65 + i) for i in range(size)]))
    print("  " + "+---" * size + "+")
    for i in range(size):
        row = [" " if cell == "S" else cell for cell in board[i]]
        print(str(i) + " | " + " | ".join(row) + " |")
        print("  " + "+---" * size + "+")


# Function to place a ship on the board
def place_ship(board, ship, direction, row, col):
    if direction == "H":
        for i in range(col, col + ship):
            board[row][i] = "S"
    elif direction == "V":
        for i in range(row, row + ship):
            board[i][col] = "S"


# Function to randomly place ships on the board
def random_ship_placement(board):
    size = len(board)
    ships = [5, 4, 3, 3, 2]
    for ship in ships:
        while True:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            direction = random.choice(["H", "V"])
            if validate_ship_placement(board, ship, direction, row, col):
                place_ship(board, ship, direction, row, col)
                break


# Function to check if a ship placement is valid
def validate_ship_placement(board, ship, direction, row, col):
    size = len(board)
    if direction == "H":
        if col + ship > size:
            return False
        for i in range(col, col + ship):
            if board[row][i] == "S":
                return False
    elif direction == "V":
        if row + ship > size:
            return False
        for i in range(row, row + ship):
            if board[i][col] == "S":
                return False
    return True


# Function to check if a shot hit a ship
def check_hit(board, row, col):
    return board[row][col] == "S"


# Function to update the board after a shot
def update_board(board, row, col, hit):
    if hit:
        board[row][col] = "X"
    else:
        board[row][col] = "O"


# Function to check if all the ships are sunk
def check_game_over(board):
    for row in board:
        if "S" in row:
            return False
    return True


# Function to generate the computer's shot
def generate_computer_shot(board):
    size = len(board)
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if board[row][col] in [" ", "S"]:
            return row, col


# Function to handle the player's turn
def player_turn(computer_board):
    print("\nPlayer's Turn")
    while True:
        shot = input("Enter your shot (e.g., A5): ").upper()
        size = len(computer_board)
        if len(shot) != 2 or not shot[0].isalpha() or not shot[1].isdigit():
            print("Invalid input! Please try again.")
            continue
        col = ord(shot[0]) - 65
        row = int(shot[1])
        if not (0 <= row < size) or not (0 <= col < size):
            print("Invalid input! Please try again.")
            continue
        if computer_board[row][col] in ["X", "O"]:
            print("You've already shot there! Please try again.")
            continue
        break
    hit = check_hit(computer_board, row, col)
    update_board(computer_board, row, col, hit)
    if hit:
        print("Congratulations! You hit an enemy ship!")
    else:
        print("You missed!")


# Function to handle the computer's turn
def computer_turn(player_board):
    print("\nComputer's Turn")
    size = len(player_board)
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if player_board[row][col] in [" ", "S"]:
            break
    hit = check_hit(player_board, row, col)
    update_board(player_board, row, col, hit)
    if hit:
        print("Oh no! The computer hit one of your ships!")
    else:
        print("Phew! The computer missed!")


# Function to check if the game is over
def is_game_over(player_board, computer_board):
    return check_game_over(player_board) or check_game_over(computer_board)


# Function to play the game
def play_game(size):
    # Initialize the player and computer boards
    player_board = [[" " for _ in range(size)] for _ in range(size)]
    computer_board = [[" " for _ in range(size)] for _ in range(size)]

    # Random ship placement for the player and computer
    random_ship_placement(player_board)
    random_ship_placement(computer_board)

    # Game loop
    while True:
        display_board(player_board)
        player_turn(computer_board)
        if is_game_over(player_board, computer_board):
            print("Congratulations! You sank all the enemy ships. You win!")
            break
        computer_turn(player_board)
        if is_game_over(player_board, computer_board):
            print("Oh no! The computer sank all your ships. You lose!")
            break


# Function to display game rules and how to play
def display_rules():
    print("=== Battleships Game ===")
    print("\nRules:")
    print("1. The game is played on a grid of your chosen size.")
    print("2. Players has five ships of different lengths: 5, 4, 3, 3, and 2.")
    print("3. Players guess the location of the opponent's ships in turns.")
    print("4. The first player to sink all of the opponent's ships wins.")
    print("\nHow to Play:")
    print("1. For your turn, enter the location to target (e.g., A5).")
    print("2. A hit is indicated by 'X', and a miss is indicated by 'O'.")
    print("3. The computer will automatically take its turn after you.")


# Function to select game difficulty
def select_difficulty():
    print("\n=== Select Difficulty ===")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter the difficulty level (1-3): ")
        if choice not in ["1", "2", "3"]:
            print("Invalid input! Please try again.")
            continue
        return int(choice)


# Function to select game grid size
def select_grid_size():
    print("\n=== Select Grid Size ===")
    print("1. 5x5")
    print("2. 6x6")
    print("3. 7x7")
    print("4. 8x8")
    print("5. 9x9")
    print("6. 10x10")

    while True:
        choice = input("Enter the grid size (1-6): ")
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid input! Please try again.")
            continue
        return int(choice) + 4


# Function for the main menu
def main_menu():
    while True:
        print("\n=== Battleships Game ===")
        print("1. Play Game")
        print("2. Game Rules and How to Play")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            size = select_grid_size()
            play_game(size)
        elif choice == "2":
            display_rules()
        elif choice == "3":
            print("\nThank you for playing Battleships!")
            break
        else:
            print("Invalid input! Please try again.")


# Run the main menu
if __name__ == "__main__":
    main_menu()
