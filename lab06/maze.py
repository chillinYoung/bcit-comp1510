"""
COMP 1510 202010 Lab 06
Young Kim (A01087377)
"""

import doctest


def game():
    """
    """
    board = make_board()
    character = make_character()

    reached_goal = False
    while not reached_goal:
        print(f"You are now on {character}.")
        move_choice = get_user_choice()

        if validate_move(board, character, move_choice):
            move_character(character, move_choice)
            reached_goal = check_reached_goal(board, character)
        else:
            print("# ERROR: invalid direction input.")

    print("\n=== Game End === You Win!! ===")


def make_board() -> list:
    """
    """
    BOARD_SIZE = 5

    board = []
    for x in range(0, BOARD_SIZE):
        board.append([])
        for y in range(0, BOARD_SIZE):
            board[x].append((x, y))
    return board


def make_character() -> list:
    """
    """
    CHAR_INIT_X_POS = 0
    CHAR_INIT_Y_POS = 0
    return [CHAR_INIT_X_POS, CHAR_INIT_Y_POS]


def get_user_choice() -> str:
    """
    """
    valid = False
    while not valid:
        move_choice = input("Where do you want to go? (up, down, left, "
                            "or right): ").replace(" ", "").lower()
        if move_choice in ["up", "down", "left", "right"]:
            valid = True
            break

    return move_choice


def move_character(character: dict, direction: str):
    """
    """
    directions = {'right': [0, 1], 'left': [0, -1],
                  'up': [1, -1], 'down': [1, 1]}

    character[directions[direction][0]] += directions[direction][1]


def validate_move(board: list, character: list, direction: str) -> bool:
    """
    """
    directions = {'left': [0, -1], 'right': [0, 1],
                  'up': [1, -1], 'down': [1, 1]}
    expected_position = (character[directions[direction][0]]
                         + directions[direction][1])
    if direction in directions:
        if 0 <= expected_position < len(board):
            return True
    return False


def check_reached_goal(board: list, character: list) -> bool:
    """
    """
    goal_pos = [len(board[0]) - 1, len(board) - 1]
    return True if character == goal_pos else False


def main():
    """
    """
    game()


if __name__ == "__main__":
    main()
