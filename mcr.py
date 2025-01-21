# Constants
BOARD_SIZE = 3
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY_CELL = ' '

def is_win(game):
    """Check if there is a winner in the game."""
    for i in range(BOARD_SIZE):
        # Check rows
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] in [PLAYER_X, PLAYER_O]:
            return True
        # Check columns
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] in [PLAYER_X, PLAYER_O]:
            return True

    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] in [PLAYER_X, PLAYER_O]:
        return True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] in [PLAYER_X, PLAYER_O]:
        return True

    return False

def main():
    """Main function to run the tic-tac-toe game."""
    # Initialize the game board
    game = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    print(f"{PLAYER_X} = Player 1")
    print(f"{PLAYER_O} = Player 2")

    turn = False  # False for Player 1's turn, True for Player 2's turn.

    for n in range(BOARD_SIZE * BOARD_SIZE):
        turn = not turn  # Switch turns
        current_player = PLAYER_X if not turn else PLAYER_O

        # Prompt the current player for input
        print(f"Player {1 if not turn else 2}: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1

        # Validate input
        if not (0 <= i < BOARD_SIZE and 0 <= j < BOARD_SIZE):
            print("Invalid input. Please try again.")
            continue
        if game[i][j] != EMPTY_CELL:
            print("Cell already occupied. Please choose another.")
            continue

        # Mark the cell
        game[i][j] = current_player

        # Check if the current player wins
        if is_win(game):
            print(f"Player {1 if not turn else 2} ({current_player}) wins!")
            break

        # Show the game board
        for row in game:
            print(" ".join(row))

        # Check for a tie
        if n == BOARD_SIZE * BOARD_SIZE - 1:
            print("Tie!")

if __name__ == "__main__":
    main()
