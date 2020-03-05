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


def main():
    """
    """
    pass


if __name__ == "__main__":
    main()
