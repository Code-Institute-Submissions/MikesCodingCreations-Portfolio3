import random


# Function to display the game board
def display_board(board):
    size = len(board)
    print("   " + " ".join(chr(65 + i) for i in range(size)))
    print("  +" + "- " * size + "+")

    for i in range(size):
        print(f"{i + 1} |" + " ".join(board[i]) + "|")
    
    print("  +" + "- " * size + "+")


# Function to check if all ships are sunk
def check_game_over(board):
    for row in board:
        if "S" in row:
            return False
    return True


# Function to place player's ships
def place_player_ships(board, num_ships):
    size = len(board)
    
    for i in range(num_ships):
        print(f"\nPlacing Ship {i + 1}")
        while True:
            display_board(board)
            ship_pos = input(f"Enter the position for Ship {i + 1} (e.g., A1): ").upper()

            if len(ship_pos) != 2 or ship_pos[0] < "A" or ship_pos[0] >= chr(65 + size) or not ship_pos[1:].isdigit():
                print("Invalid input! Please enter a valid position.")
                continue

            col = ord(ship_pos[0]) - ord("A")
            row = int(ship_pos[1:]) - 1

            if not (0 <= row < size) or not (0 <= col < size):
                print("Invalid input! Please enter a valid position.")
                continue

            if board[row][col] == "S":
                print("There is already a ship here! Please choose another.")
                continue

            board[row][col] = "S"
            break


# Function to place computer's ships randomly
def random_ship_placement(board, num_ships):
    size = len(board)
    ships_placed = 0

    while ships_placed < num_ships:
        col = random.randint(0, size - 1)
        row = random.randint(0, size - 1)

        if board[row][col] != "S":
            board[row][col] = "S"
            ships_placed += 1


# Function to play the game
def play_game():
    size = int(input("Enter the size of the game board (4-10): "))
    num_ships = int(input("Enter the number of battleships to play with: "))
    
    player_board = [[" " for _ in range(size)] for _ in range(size)]
    computer_board = [[" " for _ in range(size)] for _ in range(size)]
    
    print("\nPlacing player's battleships...")
    place_player_ships(player_board, num_ships)
    
    print("\nPlacing computer's battleships...")
    random_ship_placement(computer_board, num_ships)
    
    player_turn = True

    while True:
        print("\nPlayer's Turn" if player_turn else "\nComputer's Turn")
        if player_turn:
            print("Player Board:")
            display_board(player_board)
        else:
            print("Computer Board:")
            display_board([[cell if cell != "S" else " " for cell in row] for row in computer_board])

        if player_turn:
            target_pos = input("Enter the position to attack (e.g., A1), or 'Q' to quit: ").upper()

            if target_pos == "Q":
                print("\nGame ended by the player. Goodbye!")
                break

            if len(target_pos) != 2 or target_pos[0] < "A" or target_pos[0] >= chr(65 + size) or not target_pos[1:].isdigit():
                print("Invalid input! Please enter a valid position.")
                continue

            col = ord(target_pos[0]) - ord("A")
            row = int(target_pos[1:]) - 1

            if not (0 <= row < size) or not (0 <= col < size):
                print("Invalid input! Please enter a valid position.")
                continue

            if computer_board[row][col] == "X" or computer_board[row][col] == "O":
                print("You've already attacked here! Please choose another.")
                continue

            if computer_board[row][col] == "S":
                print("You hit a battleship!")
                computer_board[row][col] = "X"
                if check_game_over(computer_board):
                    print("\nCongratulations! You won the game!")
                    break
            else:
                print("You missed.")
                computer_board[row][col] = "O"

        else:
            target_pos = (random.randint(0, size - 1), random.randint(0, size - 1))

            if player_board[target_pos[0]][target_pos[1]] == "X" or player_board[target_pos[0]][target_pos[1]] == "O":
                continue

            if player_board[target_pos[0]][target_pos[1]] == "S":
                print("The computer hit your battleship!")
                player_board[target_pos[0]][target_pos[1]] = "X"
                if check_game_over(player_board):
                    print("\nGame over! The computer won the game.")
                    break
            else:
                print("The computer missed.")
                player_board[target_pos[0]][target_pos[1]] = "O"

        player_turn = not player_turn


# Function to display the starting screen
def display_starting_screen():
    print("Welcome to Mike's Battleship Game!")
    while True:
        print("\nMenu:")
        print("1. Game Rules")
        print("2. Play Game")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            display_game_rules()
        elif choice == "2":
            play_game()
        elif choice == "3":
            print("\nGame ended. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


# Function to display the game rules
def display_game_rules():
    print("Game Rules:")
    print("1. The game board is a grid where you place battleships.")
    print("2. The goal is to sink all opponent's battleships.")
    print("3. Each battleship occupies multiple cells either H or V.")
    print("4. You target a position on the opponent's board.")
    print("5. If your target hits a battleship, it's a hit.")
    print("6. Otherwise, it's a miss.")
    print("7. The game continues till all battleships of one player are sunk.")
    print("8. Good luck and have fun!")


# Start the game
display_starting_screen()
