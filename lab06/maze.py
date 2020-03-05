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
        user_move = move_choice()
        if validate_move(board, character, user_move):
            move_character(character, user_move)
        else:
            print("# ERROR: invalid input.")

        if check_reached_goal(board, character):
            print("\n=== Game End === You Win!! ===")
            reached_goal = True


def make_board() -> list:
    """
    """
    BOARD_X = 5
    BOARD_Y = 5

    board = []
    for x in range(0, BOARD_X):
        board.append([])
        for y in range(0, BOARD_Y):
            board[x].append((x, y))
    return board


def make_character() -> list:
    """
    """
    return [0, 0]


def move_choice() -> str:
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


def move_character(character: dict, move_choice: str):
    """
    """
    directions = {'right': [0, 1], 'left': [0, -1],
                  'up': [1, -1], 'down': [1, 1]}

    character[directions[move_choice][0]] += directions[move_choice][1]


def validate_move(board: list, character: list, move_choice: str) -> bool:
    """
    """
    board_size = [len(board[0]), len(board)]
    directions = {'left': [0, -1], 'right': [0, 1],
                  'up': [1, -1], 'down': [1, 1]}
    xy = directions[move_choice][0]
    move = directions[move_choice][1]
    if move_choice in directions:
        if 0 <= character[xy] + move < board_size[xy]:
            return True
    return False


def check_reached_goal(board: list, character: list) -> bool:
    """
    """
    goal_pos = [len(board[0]) - 1, len(board) - 1]
    return True if character == goal_pos


def main():
    """
    """
    game()


if __name__ == "__main__":
    main()
