"""
COMP 1510 202010 Assignment 3
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Character Module for Single User Dungeon (SUD)
"""

import doctest


def create_character(max_hp: int, init_pos_x: int, init_pos_y: int) -> dict:
    """Create a character to play.

    :param max_hp: an integer
    :param init_pos_x: an integer
    :param init_pos_y: an integer
    :precondition: max_hp must be an integer > 0 and <= 10, and init_pos_x
            and init_pos_y must be a positive integer and it must be within
            the coordinates of the gamp_map
    :postcondition: correctly form a character information with dictionary
    :return: a dictionary
    """
    name = choose_character()
    # when user input quit to exit the program
    if name == "quit":
        return name

    character_init = {'Name': name,
                      'HP': max_hp,
                      'Max_HP': max_hp,
                      'Pos_x': init_pos_x,
                      'Pos_y': init_pos_y}
    return character_init


def move(character: dict, move_choice: str):
    """Move the character.

    :param character: a character dictionary
    :param move_choice: a string indicates a direction
    :precondition: move_choice must be validated by validate_move function
            before given to this function, and the character must be
            correctly formed by create_character function in this module
    :postcondition: move the character's position to the given direction

    >>> char = {'Name': 'Woody', 'HP': 10, 'Max_HP': 10,
    ...         'Pos_x': 0, 'Pos_y': 0}
    >>> move(char, 'n')
    >>> print(char)
    {'Name': 'Woody', 'HP': 10, 'Max_HP': 10, 'Pos_x': 0, 'Pos_y': 1}

    >>> move(char, 'e')
    >>> print(char)
    {'Name': 'Woody', 'HP': 10, 'Max_HP': 10, 'Pos_x': 1, 'Pos_y': 1}

    """
    directions = {'e': ['Pos_x', 1], 'w': ['Pos_x', -1],
                  's': ['Pos_y', -1], 'n': ['Pos_y', 1]}

    character[directions[move_choice][0]] += directions[move_choice][1]


def validate_move(map_info: dict, character: dict, move_choice: str) -> bool:
    """Validate the direction to move.

    :param map_info: a map dictionary
    :param character: a character dictionary
    :param move_choice: a string indicates a direction
    :precondition: the map list amd the character dictionary must be
            correctly formed, and mvoe_choice must be validated by
            validate_move function before given
    :postcondition: check if the move_choice is valid to move by the data
            stored in the map information list
    :return: a boolean value

    >>> map_info = {(0, 0): {'e': True, 'w': False, 's': False, 'n': True}}
    >>> char = {'Name': 'Woody', 'Pos_x': 0, 'Pos_y': 0}
    >>> move_choice = "s"
    >>> validate_move(map_info, char, move_choice)
    False

    >>> move_choice = "e"
    >>> validate_move(map_info, char, move_choice)
    True
    """
    # return is a boolean value from the map_info dictionary
    return map_info.get(get_user_position(character)).get(move_choice)


def choose_character() -> str:
    """Choose a character.

    :postcondition: ask the user to choose character in the given list
            until the user input is valid and returns valid input
    :return: a string name of the character chosen
    """
    character_list = {1: "Woody",
                      2: "Buzz",
                      3: "Rex",
                      4: "Jessie"}

    # print the available character lists
    print("Here are a list of character to choose from: ")
    for num, char_name in character_list.items():
        print(f"{num}: {char_name}")

    # loop until the user input valid
    while True:
        user_choice = (input("Enter the number to pick your character, "
                             "or 'quit' to exit: ").strip().lower())
        if user_choice.isdigit() and int(user_choice) in character_list:
            return character_list[int(user_choice)]
        elif user_choice == "quit":
            return user_choice
        else:
            print("Not a valid entry, please try again.")


def gain_hp(character: dict, hp_amount: int):
    """Add the health points.

    :param character: a character dictionary
    :param hp_amount: an integer
    :precondition: the character must be the correctly formed by
            create_character function in this module.
    :postcondition: add the given character's health points, and HP
            doesn't over the max HP of the character
    """
    if character['HP'] + hp_amount >= character['Max_HP']:
        character['HP'] = character['Max_HP']
    else:
        character['HP'] += hp_amount

    print(f"\n\t{character['Name']} gained {hp_amount} points of HP\n"
          "\tdue to successfully entered into a safe room.\n"
          f"\tNow {character['Name']}'s' HP is {character['HP']}.")


def get_user_position(character: dict) -> tuple:
    """Give current position of the character.

    :param character: a dictionary
    :precondition: the character must be correctly formed by
            create_character function in this module
    :postcondition: correctly returns the user position as a tuple
            of coordinates
    :return: a tuple

    >>> char = {'Name': 'Lily', 'Pos_x': 2, 'Pos_y': 1}
    >>> get_user_position(char)
    (2, 1)

    >>> char = {'Name': 'Lily', 'Pos_x': 0, 'Pos_y': 4}
    >>> get_user_position(char)
    (0, 4)
    """
    return character['Pos_x'], character['Pos_y']


def main():
    """
    Drive the doctest in this module.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
