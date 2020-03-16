"""
COMP 1510 202010 Assignment 3
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Main Module of Single User Dungeon (SUD)
"""

import doctest
from character import *
from monster import *
from game_map import *
from constant import *


def play():
    """Play the game."""

    # map initialize and print game welcome
    map_info = map_init(MAP_WIDTH, MAP_HEIGHT)
    print_game_welcome()

    # create character and print character welcome
    character = create_character(CHAR_MAX_HP, CHAR_INIT_POS_X, CHAR_INIT_POS_Y)
    check_quit_to_exit(character)
    print_character_welcome(character)

    # loop until SystemExit raised inside of play_move or check_zero_hp
    while True:
        current_pos = get_user_position(character)
        allowed = allowed_direction(current_pos, map_info)

        # print the room description and directions able to move
        print("_ " * 35)
        print(map_info.get(get_user_position(character))['description'])
        print_map(map_info, character)
        print(f"\nYou are currently at {current_pos}, "
              f"and only allowed to move {allowed}")

        play_move(map_info, character)
        check_zero_hp(character)


def play_move(map_info: dict, character: dict):
    """Make valid movement of the character.

    :param map_info: a dictionary
    :param character: a dictionary
    :precondition: the map_info and character must be correctly formed
            with the functions in this package
    :postcondition: make a movement of the character or show an error
            message after validate and check the given move_choice
    """
    move_choice = get_user_choice()
    check_quit_to_exit(move_choice)

    if validate_move(map_info, character, move_choice):
        move(character, move_choice)

        # found Andy on (3, 2), then Game End
        if (character['Pos_x'], character['Pos_y']) == (3, 2):
            print(map_info.get(get_user_position(character))['description'])
            check_quit_to_exit("quit")
        else:
            play_monster(character)

    # for invalid movement
    else:
        boundary_description(move_choice)


def play_monster(character: dict):
    """Play the moster appear part of the game.

    :param character: a dictionary
    :precondition: the character must be correctly formed with the
            create_character function in the character module
    :postcondition: play monster_appear or gain_hp depending on the
            random chance
    """
    if monster_appear(MONSTER_APPEAR_CHANCE):
        decision = encountered_monster(
            character, MONSTER_INIT_HP, ATTACK_DAMAGE_MAX, STAB_CHANCE,
            STAB_DAMAGE_MAX)
        check_quit_to_exit(decision)

    # if moster didn't appear, gain hp
    else:
        gain_hp(character, ADD_HP_AMOUNT)


def check_zero_hp(character: dict):
    """Check zero hp.

    :param character: a dictionary
    :precondition: the character must be correctly formed with the
            create_character function in the character module
    :postcondition: check if the character's hp is zero and end the program

    >>> character = {'HP': 2}
    >>> check_zero_hp(character)    # nothing happens
    """
    if character['HP'] == 0:
        check_quit_to_exit("quit")


def check_quit_to_exit(if_quit: str):
    """Check user input quit.

    :param if_quit: a string
    :postcondition: exit the program if if_quit is 'quit'

    >>> check_quit_to_exit("not going to quit yet")    # nothing happens
    """
    if if_quit == "quit":
        raise SystemExit("\n+++++ Game End +++++")


def print_game_welcome():
    """Print the welcome message."""
    print("Welcome to Toy Story and Monster! You are definitely in for "
          "a surprise\n\n"
          "##_####################_####################\n"
          "#| |_#___##_###_###___| |_#___##_#__#_###_##\n"
          "#| __/ _ \| | | | / __| __/ _ \| '__| | | |#\n"
          "#| || (_) | |_| | \__ \ || (_) | |  | |_| |#\n"
          "##\__\___/ \__, | |___/\__\___/|_|   \__, |#\n"
          "###########|___/######################|___/#\n"
          "############################################\n")


def print_character_welcome(character):
    """Print the character information.

    :param character: a character dictionary
    :postcondition: correctly print the desctiptions with the
            character's name inside of it"""
    print("_ " * 35,
          f"\n\nWise choice of character! Hi {character['Name']}! "
          f"You start with max health of {character['Max_HP']}.\n"
          "If you go below this, YOU WILL DIE!\n"
          "Your goal for this journey is to get back to Andy!\n"
          "Once you find Andy, you are home and will win the game.\n"
          "Each move you take might be a magical door that transports\n"
          "you further away or closer to home, or you might even come \n"
          "across some interesting monsters, so good luck!\n")


def get_user_choice() -> str:
    """Get user choice to move.

    :postcondition: ask prompt input to user repeatedly until user input
                    the valid direction
    :return: a string of user choice
    """
    valid = False
    while not valid:
        move_choice = input("So tell me, where would you like to go? "
                            "or 'quit' to exit: ").strip().lower()
        if move_choice in ["e", "w", "s", "n", "quit"]:
            valid = True

    return move_choice


def main():
    """
    Drive the program and doctest in this module.
    """
    doctest.testmod()

    # play game
    play()


if __name__ == "__main__":
    main()
