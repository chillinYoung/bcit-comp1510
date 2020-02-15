"""
COMP 1510 202010 Assignment 2
Young Kim (A01087377)

Dungeons and Dragoons
"""

import doctest
import random
import itertools


def roll_die(number_of_rolls, number_of_sides):
    """Roll the die.

    A function to roll the die with a given number of rolls and the number of
    sides of a die.

    :param number_of_rolls: a non-zero positive integer
    :param number_of_sides: a non-zero positive integer
    :precondition: the numbers must be a non-zero positive integer
    :postcondition: give the sum of randomly rolled die/dice
    :return: result of rolling the die/dice as an integer
    """
    rolled = 0
    idx = number_of_rolls
    while idx > 0:
        rolled += random.randint(1, number_of_sides)
        idx -= 1
    return rolled

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def generate_name(syllables):
    """Generate a name.

    :param syllables: a positive non-zero integer
    :precondition: the number must be a positive non-zero integer
    :postcondition: generate a name with given syllables of which each syllable
                    is a consonant followed by a vowel
    :return: a generated name as capitalized string
    """
    generated = ""
    idx = syllables
    while idx > 0:
        generated += generate_syllable()
        idx -= 1
    return generated.capitalize()

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def generate_vowel():
    """Generate a single vowel.

    :postcondition: generate a single vowel including 'y'
    :return: a single vowel as string
    """
    return random.choice("aeiouy")

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def generate_consonant():
    """Generate a single consonant.

    :postcondition: generate a single consonant including 'y'
    :return: a single consonant as string
    """
    return random.choice("bcdfghjklmnpqrstvwxyz")

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def generate_syllable():
    """Generate the two-letter syllable.

    :postcondition: generate the two-letter syllable which is the combination
                    of a single consonant and a single vowel
    :return: the two-letter syllable as string
    """
    return generate_consonant() + generate_vowel()

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def create_character(syllables):
    """Create a character.

    A function to create a character that contains information such as HP, XP,
    Class, Race, and name.

    :param syllables: a non-zero positive integer
    :precondition: the number must be a positive integer which is non-zero
    :postcondition: provide initialized and assembled character information
                    in a dictionary
    :return: a dictionary that contains character information
    """
    if syllables <= 0:
        print("ERROR: given number is not a positive integer.")
        return None

    selected_class = select_class()    # get user input
    character_info = {"Name": generate_name(syllables),
                      "Inventory": [],
                      "XP": 0,
                      "Class": selected_class,
                      "Race": select_race(),    # get user input
                      # HP → [maxHP, currentHP]
                      "HP": [roll_die(1, get_hit_die(selected_class)), 0]}

    attributes = ["Strength", "Intelligence", "Wisdom",
                  "Dexterity", "Constitution", "Charisma"]
    for attr in attributes:
        character_info[attr] = roll_die(3, 6)

    return character_info

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def get_hit_die(class_of_character):
    """Give the hit-die.

    A function that gives the hit-die of the given character.

    :param class_of_character: the class of character as string
    :precondition: the class of character must be given as string and a correct
                    name of one of the character classes
    :postcondition: give an integer that indicates hit die of the character
    :return: hit die as integer
    """
    hit_die = {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8,
               "fighter": 10, "monk": 8, "paladin": 10, "ranger": 10,
               "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6}

    return hit_die[class_of_character]

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def select_class():
    """Select a class.

    A function to select a class of a character to play.

    :postcondition: make the chosen class input to lower string
    :return: chosen class as string
    """
    classes = ["barbarian", "bard", "cleric", "druid", "fighter",
               "monk", "paladin", "ranger", "rogue", "sorcerer",
               "warlock", "wizard"]
    print("\nClasses:\n" + ", ".join(classes), "\n")
    class_choice = (input("Choose the class for your character: ")
                    .replace(" ", "").lower())
    return class_choice

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def select_race():
    """Select a race.

    A function to select a race of a character to play.

    :postcondition: make the chosen race input to lower string
    :return: chosen race as string
    """
    races = ["dragonborn", "dwarf", "elf", "gnome", "half-elf",
             "halfling", "half-orc", "human", "tiefling"]
    print("\nRaces:\n" + ", ".join(races), "\n")
    race_choice = (input("Choose the race for your character: ")
                   .replace(" ", "").lower())
    return race_choice

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def print_character(character):
    """Print character information.

    :param character: a dictionary
    :precondition: character information must be a dictionary format created by
                    create_character function in this domule
    :postcondition: print given character's information
    """
    print(character)

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def choose_inventory(character_obj):
    """Choose inventory.

    Choose the goods to be added to a given character's inventory.

    :param character_obj: a character object
    :precondition: a character object must be well-formed by create_character
                    function in this module
    :postcondition: add all the chosen goods to the character object dictionary
    """
    goods_list = ["sword", "dagger", "heavy blunt", "spear", "staff",
                  "blade", "bow", "beam", "poison", "axe"]

    print("Welcome to the Olde Tyme Merchant!\n")
    print("Here is what we have for sale:\n")
    print_list_with_count(goods_list)

    choice_list = []
    user_choice = 0
    while user_choice != "-1":
        user_choice = input("What would you like to buy (-1 to finish): ")

        if user_choice.isdigit() and (0 < int(user_choice) <= len(goods_list)):
            choice_list.append(goods_list[int(user_choice) - 1])

        elif user_choice != "-1":
            print("ERROR: please enter the number of an item.\n")
            print_list_with_count(goods_list)

    for item in choice_list:
        character_obj["Inventory"].append(item)

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def print_list_with_count(list_to_print):
    """Print a list with counter.

    :param list_to_print: a list to print
    :precondition: a list must be given as an argument
    :postcondition: print the given list with counter from 1
                    such as '1. element'
    """
    for counter, elem in zip(itertools.count(1), list_to_print):
        print(f"{counter}. {elem}")

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def combat_round(opponent_one, opponent_two):
    """Represent combat.

    A function that represents a single round of combat.

    :param opponent_one: a character object (dictionary)
    :param opponent_two: a character object (dictionary)
    :precondition: both parameters must be well-formed dictionaries each
                    containing a correct character
    :postcondition: represent combat and print result of combat
    """
    # set to full HP
    opponent_one["HP"][1] = opponent_one["HP"][0]
    opponent_two["HP"][1] = opponent_two["HP"][0]

    print("\n---------- Combat starts! ----------\n")

    # choose the first attacker
    same_num = True
    while same_num:
        opp_one = roll_die(1, 20)
        opp_two = roll_die(1, 20)
        if opp_one != opp_two:
            same_num = False

    opponents = {opp_one: opponent_one, opp_two: opponent_two}
    attacker, defender = opponents[max(opponents)], opponents[min(opponents)]

    print_hp_compare(opponent_one, opponent_two)
    print(f"{attacker['Name']} is the first attacker.")

    attack(attacker, defender)

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def attack(attacker, defender):
    """Attack each other.

    A function that two oppoenents attacks each other and find the winner.

    :param attacker: a character object, the first attacker
    :param defender: a character object, the first defender
    :precondition: both parameters must be well-formed dictionaries each
                    containing a correct character
    :postcondition: print every attack status and the result of attack
    """
    # attack start
    game_over = False
    while not game_over:
        attacker_num = roll_die(1, 20)
        defender_num = defender["Dexterity"]

        # if attack is succeed
        if attacker_num > defender_num:
            print(f"\n{attacker['Name']}'s attack was successful!!")
            hit = roll_die(1, get_hit_die(attacker["Class"]))

            # if defender died by attack
            if defender["HP"][1] - hit <= 0:
                defender["HP"][1] = 0
                print(f"\t{defender['Name']} is hit with {hit} point(s) "
                      "and Killed.")
                print(f"\n------ {attacker['Name']} WIN!! GAME OVER. ------\n")
                game_over = True

            # if defender is still alive after attack
            else:
                defender["HP"][1] -= hit
                print(f"\t{defender['Name']}'s HP is reduced {hit} point(s).")
                print("\tCONTINUE the round.\n\t", end="")
                print_hp_compare(attacker, defender)

        # if attack is failed
        else:
            print(f"\n{attacker['Name']}'s attack was failed... "
                  "CONTINUE the round.")

        # change turns
        attacker, defender = defender, attacker

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def print_hp_compare(opponent_one, opponent_two):
    """Print comparing current HP.

    Print the comparing current HP between two given characters.

    :param opponent_one: a character object
    :param opponent_two: a character object
    :precondition: the chracter objects must be well-formed dictionaries each
                    containing a correct character
    :postcondition: print the current HP of the both characters with their name
    """
    print(f"{opponent_one['Name']} (HP: {opponent_one['HP'][1]})"
          f" vs. {opponent_two['Name']} (HP: {opponent_two['HP'][1]})")

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation: 
        -Abstraction/generalization: 
        -Algorithm/automation: 
    """


def main():
    """Drive the program.

    A function that drives the program to test this module, which will play
    short D&D game to demonstrate it.
    """
    doctest.testmod()

    # create and set up the character
    print("Create a character.")
    syllables1 = int(input("Enter the number of syllables for the name: "))
    test_character_one = create_character(syllables1)
    print()

    # print character
    print("This is the formed your character!")
    print_character(test_character_one)
    print()

    # choose inventory
    print(f"Let's buy some goods for {test_character_one['Name']}")
    choose_inventory(test_character_one)
    print()

    # print character again
    print("Final check for your character!")
    print_character(test_character_one)
    print()

    # create and set up the hard-coded character
    test_character_two = {"Name": "Quluho",
                          "Inventory": ["sword", "heavy blunt"],
                          "XP": 0,
                          "Class": "bard",
                          "Race": "gnome",
                          "HP": [7, 0],
                          "Strength": 9,
                          "Intelligence": 11,
                          "Wisdom": 12,
                          "Dexterity": 13,
                          "Constitution": 8,
                          "Charisma": 16}

    # combat
    combat_round(test_character_one, test_character_two)
    print("Bye, see you again!")


if __name__ == "__main__":
    main()
