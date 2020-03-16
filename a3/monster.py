"""
COMP 1510 202010 Assignment 3
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Monster Module for Single User Dungeon (SUD)
"""

import doctest
import random


def create_monster(init_hp: int) -> dict:
    """Create a monster.

    :param init_hp: an integer
    :precondition: the init_hp must be a positive non-zero integer
    :postcondition: correctly form a monster information with dictionary
    :return: a dictionary
    """
    return {'Name': random_monster_name(), 'HP': init_hp}


def random_monster_name() -> str:
    """Pick a random monster name.

    :return: a string
    """
    monsters_list = ("Sulley from Monster Inc.",
                     "Mike from Monster Inc.",
                     "Randall from Monster Inc.",
                     "Waternoose from Monster Inc.",
                     "Celia Mae from Monster Inc.")
    return random.choice(monsters_list)


def monster_appear(monster_appear_chance) -> bool:
    """Generate a random chance by 1d4.

    :param monster_appear_chance: an integer
    :precondition: the monster_appear_chance must be a positive integer
            equal or greater than one
    :postcondition: generate the random chance by 1d4 and indicatae as
            a boolean value
    :return: a boolean
    """
    # (1 / (monster_appear_chance) * 100) percent of the chance
    return True if random.randint(1, monster_appear_chance) == 1 else False


def encountered_monster(character: dict, monster_hp: int,
                        attack_damage_max: int,
                        stab_chance: int, stab_damage_max: int):
    """Get user choice for monster encounters.

    :param character: a character dictionary
    :param monster_hp: an integer
    :param attack_damage_max: an integer
    :param stab_chance: an integer
    :param stab_damage_max: an integer
    :precondition: the character must be correctly formed by
            create_character function in the character module, and
            integers must be a positive non-zero integer
    :postcondition: ask the user input until it is valid, and do the post
            action depending on the user choice
    :return: a string if choice is 'quit', if not, None
    """
    monster = create_monster(monster_hp)
    print(f"\nOh, No! {monster['Name']} appeared!\n"
          f"The current {character['Name']}'s' HP is {character['HP']}.")

    # loop until user input the valid choice
    valid = False
    while not valid:
        choice = input("Do you want to run away or combat? "
                       "(enter 'run', 'combat', or 'quit'): ").strip().lower()
        if choice in ["run", "combat", "quit"]:
            valid = True

    if choice == "quit":
        return "quit"
    elif choice == "combat":
        combat(character, monster, attack_damage_max)
    elif choice == "run":
        run_away(character, monster, stab_chance, stab_damage_max)


def run_away(character: dict, monster: dict,
             stab_chance: int, stab_damage_max: int):
    """Let the character run away from the monster.

    :param character: a character dictionary
    :param monster: a monster dictionary
    :param stab_chance: an integer
    :param stab_damage_max: an integer
    :precondition: the character must be correctly formed by
            create_character function in the character module, and
            integers must be a positive non-zero integer
    :postcondition: generate random chance and random damage correctly,
            and apply it to the character
    """
    print("\n\tYou decided to run away.")
    damage = random.randint(1, stab_damage_max)

    if random.randint(1, stab_chance) == 1:
        print(f"\tOh no... {character['Name']} were stabbed from back "
              f"by {monster['Name']} with {damage} of damage.")
        lose_hp(character, damage)
    else:
        print("\tSuccessfully runned away!")


def combat(character: dict, monster: dict, attack_damage_max: int):
    """Choose the first attacker and defender.

    :param character: a character dictionary
    :param monster: a monster dictionary
    :param attack_damage_max: an integer
    :precondition: the character and monster must be correctly formed by
            functions in this package, and attack_damage_max must be
            a positive non-zero integer
    :postcondition: generate random order to attack
    """
    print("\n\tYou decided to combat.")

    # choose first attcker by flipping the coin
    combatants = [character, monster]
    flip_coin = random.randint(0, 1)
    first_attacker = combatants[flip_coin]
    first_defender = combatants[abs(flip_coin - 1)]
    print(f"\t* The first attacker is {first_attacker['Name']}.")

    attack(first_attacker, first_defender, attack_damage_max)


def attack(attacker: dict, defender: dict, attack_damage_max: int):
    """Attack each other until one dies

    :param attacker: a monster or character dictionary
    :param defender: a monster or character dictionary
    :param attack_damage_max: an integer
    :precondition: the dictionaries must be correctly formed with
            create_monster and create_character functions, and
            attack_damage_max must be a positive non-zero integer
    :postcondition: attack and then lose random health points until one
            dies, and change attacker and defender for each attack
    """
    someone_die = False
    while not someone_die:
        damage = random.randint(1, attack_damage_max)
        print(f"\t{defender['Name']} got {damage} of damage.")
        lose_hp(defender, damage)

        if defender['HP'] == 0:
            someone_die = True

        # switch the role
        attacker, defender = defender, attacker


def lose_hp(target: dict, damage_amount: int):
    """Reduce the target's hp.

    :param target: a character or monster dictionary
    :param dagame_amount: an integer
    :precondition: the target dictionary must be corretly formed by
            create_monster or create_character, and damage_amount must
            be a positive non-zero integer
    :postcondition: reduce the target's health point with given
            damage_amount, and if target's health point is reached zero,
            notify that target is dead

    >>> character = {'Name': 'Woody', 'HP': 7}
    >>> lose_hp(character, 2)    #doctest: +NORMALIZE_WHITESPACE
        Now Woody's HP is 5.
    <BLANKLINE>

    >>> monster = {'Name': 'Test Monster', 'HP': 1}
    >>> lose_hp(monster, 2)    #doctest: +NORMALIZE_WHITESPACE
        === Test Monster DIED... ===
    """
    # hp reduced but greater than zero
    if target['HP'] - damage_amount > 0:
        target['HP'] -= damage_amount
        print(f"\tNow {target['Name']}'s HP is {target['HP']}.\n")

    # hp reached to the zero → die
    else:
        target['HP'] = 0
        print(f"\t=== {target['Name']} DIED... ===")


def main():
    """
    Drive the doctest in this module.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
