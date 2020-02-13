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

    selected_class = select_class()
    character_info = {'Name': generate_name(syllables),
                      'Inventory': [],
                      'XP': 0,
                      'Class': selected_class,
                      'Race': select_race(),
                      # HP → [maxHP, currentHP]
                      'HP': [roll_die(1, get_hit_points(selected_class)), 0]}

    attributes = ['Strength', 'Intelligence', 'Wisdom',
                  'Dexterity', 'Constitution', 'Charisma']
    for attr in attributes:
        character_info[attr] = roll_die(3, 6)

    return character_info


def get_hit_points(class_of_character):
    hit_points = {'barbarian': 12, 'bard': 8, 'cleric': 8, 'druid': 8,
                  'fighter': 10, 'monk': 8, 'paladin': 10, 'ranger': 10,
                  'rogue': 8, 'sorcerer': 6, 'warlock': 8, 'wizard': 6}
    if class_of_character in hit_points:
        return hit_points[class_of_character]


def select_class():
    """Select a class.

    A function to select a class of a character to play.

    :postcondition: make the chosen class input to lower string
    :return: chosen class
    """
    classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter',
               'monk', 'paladin', 'ranger', 'rogue', 'sorcerer',
               'warlock', 'wizard']
    print("Classes:", ", ".join(classes))
    class_choice = (input("Choose the class for your character: ")
                    .strip().lower())
    return class_choice


def select_race():
    """Select a race.

    A function to select a race of a character to play.

    :postcondition: make the chosen race input to lower string
    :return: chosen race
    """
    races = ['dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf',
             'halfling', 'half-orc', 'human', 'tiefling']
    print("Races:", ", ".join(races))
    race_choice = input("Choose the race for your character: ").strip().lower()
    return race_choice


def print_character(character):
    """Print character information.

    :param character: a dictionary
    :precondition: character information must be a dictionary format created by
                    create_character function in this domule
    :postcondition: print given character's information
    """
    print(character)


def choose_inventory(character_obj):
    """Choose inventory.

    Choose the goods to be added to a given character's inventory.

    :param character_obj: a character object
    :precondition: a character object must be well-formed by create_character
                    function in this module
    :postcondition: add all the chosen goods to the character object
    """
    goods_list = ["sword", "dagger", "heavy blunt", "spear", "staff",
                  "blade", "bow", "beam", "poison", "axe"]

    print("Welcome to the Olde Tyme Merchant!\n")
    print("Here is what we have for sale:\n")
    print_list_with_count(goods_list)

    choice_list = []
    user_choice = 0
    while user_choice != -1:
        user_choice = int(input("What would you like to buy (-1 to finish): "))

        if 0 < user_choice <= len(goods_list):
            choice_list.append(goods_list[user_choice - 1])
        elif user_choice != -1:
            print("ERROR: invalid input. "
                  "Please enter the number of an item.\n")
            print_list_with_count(goods_list)

    for item in choice_list:
        character_obj['Inventory'].append(item)


def print_list_with_count(list_to_print):
    """Print a list with counter.

    :param list_to_print: a list to print
    :precondition: a list must be given as an argument
    :postcondition: print the given list with counter from 1
                    such as '1. element'
    """
    for counter, elem in zip(itertools.count(1), list_to_print):
        print(f"{counter}. {elem}")


def combat_round(opponent_one, opponent_two):
    """Represent combat.

    A function that represents a single round of combat.

    :param opponent_one: a character object (dictionary)
    :param opponent_two: a character object (dictionary)
    :precondition: both parameters must be well-formed dictionaries each
                    containing a correct character
    :postcondition:
    """
    set_full_hp(opponent_one)
    set_full_hp(opponent_two)
    print("\n----------- Combat starts! -----------")
    print_hp_compare(opponent_one, opponent_two)

    attacker, defender = choose_first_attacker(opponent_one, opponent_two)
    print(f"\t{attacker['Name']} is the first attacker.")

    game_over = False
    while not game_over:
        attack_success = attack(attacker, defender)
        att_name = attacker['Name']
        dfn_name = defender['Name']

        if attack_success is True:
            print(f"\n\t{att_name}'s attack was successful!!")
            hit = roll_die(1, get_hit_points(attacker['Class']))

            if defender['HP'][1] - hit <= 0:
                defender['HP'][1] = 0
                print(f"\t\t{dfn_name} is hit with {hit} point(s) and Killed.")
                print(f"-------- {att_name} WIN!! GAME OVER. --------\n")
                game_over = True

            else:
                defender['HP'][1] -= hit
                print(f"\t\t{dfn_name}'s HP is reduced {hit} point(s).")
                print("\t\tCONTINUE the round.\n\t\t", end="")
                print_hp_compare(opponent_one, opponent_two)
        else:
            print(f"\n\t{att_name}'s attack was failed... CONTINUE the round.")

        attacker, defender = defender, attacker


def set_full_hp(character):
    character['HP'][1] = character['HP'][0]


def print_hp_compare(opponent_one, opponent_two):
    print(f"{opponent_one['Name']} (HP {opponent_one['HP'][1]})"
          f" vs. {opponent_two['Name']} (HP {opponent_two['HP'][1]})")


def choose_first_attacker(opponent_one, opponent_two):
    same_num = True
    while same_num:
        opp_one = roll_die(1, 20)
        opp_two = roll_die(1, 20)
        if opp_one != opp_two:
            same_num = False

    attack_order = {opp_one: opponent_one, opp_two: opponent_two}
    attacker = attack_order[max(attack_order)]
    defender = attack_order[min(attack_order)]

    return attacker, defender


def attack(attacker, defender):
    """Attack the defender.

    A function that attacker attacks the defender and find the winner.

    :param attacker: a character object
    :param defender: a character object
    :precondition: both parameters must be well-formed dictionaries each
                    containing a correct character
    :postcondition: find a winner
    :return:
    """
    attacker_num = roll_die(1, 20)
    defender_num = defender['Dexterity']
    if attacker_num > defender_num:
        return True
    elif attacker_num < defender_num:
        return False
    else:
        return None


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
