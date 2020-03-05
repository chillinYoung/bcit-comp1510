"""
COMP 1510 202010 Lab 06
Young Kim (A01087377)
"""

import doctest


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


def main():
    """
    """
    pass


if __name__ == "__main__":
    main()
