"""
COMP 1510 202010 Lab 06
Young Kim (A01087377)

Maze Game
"""

import doctest


def game():
    """Play the game.

    :postcondition: play the game until user reached to the goal
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
    """Make 5x5 game board.

    :postcondition: make correct size of the game board with tuple items
                    which contain position information
    :return: a game board list
    """
    BOARD_SIZE = 5

    board = []
    for x in range(0, BOARD_SIZE):
        board.append([])
        for y in range(0, BOARD_SIZE):
            board[x].append((x, y))
    return board


def make_character() -> list:
    """Create character.

    :postcondition: create the character that contains correct initial
                    position of the character
    :return: a list

    >>> print(make_character())
    [0, 0]
    """
    CHAR_INIT_X_POS = 0
    CHAR_INIT_Y_POS = 0
    return [CHAR_INIT_X_POS, CHAR_INIT_Y_POS]


def get_user_choice() -> str:
    """Get user choice to move.

    :postcondition: ask prompt input to user repeatedly until user input
                    the valid direction
    :return: a string of user choice
    """
    valid = False
    while not valid:
        move_choice = input("Where do you want to go? (up, down, left, "
                            "or right): ").replace(" ", "").lower()
        if move_choice in ["up", "down", "left", "right"]:
            valid = True
            break

    return move_choice


def move_character(character: list, direction: str):
    """Move character.

    :param character: a character list
    :param direction: a string
    :precondition: the character list must have x-position and y-position
                    of the character, and the direction must be the one
                    of left, right, up and down
    :postcondition: change the character's position with given direction

    >>> character = [0, 0]
    >>> move_character(character, "right")
    >>> character
    [1, 0]
    >>> character = [2, 2]
    >>> move_character(character, "up")
    >>> character
    [2, 1]
    """
    directions = {'right': [0, 1], 'left': [0, -1],
                  'up': [1, -1], 'down': [1, 1]}

    character[directions[direction][0]] += directions[direction][1]


def validate_move(board: list, character: list, direction: str) -> bool:
    """Validate expected move.

    A function that validates the expected move of given direction.

    :param board: a game board list
    :param character: a character list
    :param direction: a string
    :precondition: the board must be correctly formed by make_board, the
                    character list must have x-position and y-position of
                    the character, and the direction must be the one of
                    left, right, up and down
    :postcondition: check if the given direction is valid to move or not
                    in the given game board
    :return: a boolean

    >>> board = [[(0, 0), (0, 1)], [(1, 0), (1, 1)]]
    >>> character = [0, 0]
    >>> validate_move(board, character, "left")
    False
    >>> validate_move(board, character, "down")
    True
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
    """Check if character reached the goal.

    :param board: a game board list
    :param character: a character list
    :precondition: the board must be correctly formed by make_board, the
                    character list must have x-position and y-position of
                    the character.
    :postcondition: check the character position is on the goal position
                    which it lower right side of the board
    :return: a boolean

    >>> board = [[(0, 0), (0, 1)], [(1, 0), (1, 1)]]
    >>> character = [0, 1]
    >>> check_reached_goal(board, character)
    False
    >>> character = [1, 1]
    >>> check_reached_goal(board, character)
    True
    """
    goal_pos = [len(board[0]) - 1, len(board) - 1]
    return True if character == goal_pos else False


def main():
    """
    Drive the program and the doctest in this module.
    """
    doctest.testmod()

    # Play Game
    game()


if __name__ == "__main__":
    main()
