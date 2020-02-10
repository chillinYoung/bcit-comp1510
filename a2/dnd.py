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
    """Generate a name.

    :param syllables: a positive non-zero integer
    :precondition: the number must be a positive non-zero integer
    :postcondition: generate a name with given syllables of which each syllable
                    is a consonant followed by a vowel
    :return: a generated name
    """
    generated = ""
    idx = syllables
    while idx > 0:
        generated += generate_syllable()
        idx -= 1
    return generated.capitalize()


def generate_vowel():
    """Generate a single vowel.

    :postcondition: generate a single vowel including 'y'
    :return: a single vowel
    """
    return random.choice("aeiouy")


def generate_consonant():
    """Generate a single consonant.

    :postcondition: generate a single consonant including 'y'
    :return: a single consonant
    """
    return random.choice("bcdfghjklmnpqrstvwxyz")


def generate_syllable():
    """Generate the two-letter syllable.

    :postcondition: generate the two-letter syllable which is the combination
                    of a single consonant and a single vowel
    :return: the two-letter syllable
    """
    return generate_consonant() + generate_vowel()


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
