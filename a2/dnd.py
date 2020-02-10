"""
COMP 1510 202010 Assignment 2
Young Kim (A01087377)

Dungeons and Dragoons
"""

import doctest
import random


def roll_die(number_of_rolls, number_of_sides):
    """Roll the die.

    Roll the die with a given number of rolls and the number of sides of a die.

    :param number_of_rolls: a non-zero positive integer
    :param number_of_sides: a non-zero positive integer
    :precondition: the numbers must be a non-zero positive integer
    :postcondition: give the sum of randomly rolled die/dice
    :return: result of rolling the die/dice
    """
    rolled = 0
    idx = number_of_rolls
    while idx > 0:
        rolled += random.randint(1, number_of_sides)
        idx -= 1
    return rolled


def generate_name(syllables):
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    return


def generate_vowel():
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    return


def generate_consonant():
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    return


def generate_syllable():
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    return


def create_character(syllables):
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    return


def print_character(character):
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    return


def choose_inventory(obj):
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    print()


def combat_round(opponent_one, opponent_two):
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    print()


def attack():
    """

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    return


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
