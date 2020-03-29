"""
COMP 1510 202010 Assignment 4 - Lumber Company
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

A module that drives a program 'Lumber Company'.
"""
import doctest
from tree import Tree
from tree_farm import TreeFarm


def choose_menu():
    """Return user choice from menu.

    :postcondition: correctly returns user choice as a string
    :return: user choice as a string from 1 - 4
    """
    while True:
        menu = {'1': 'Add a Tree',
                '2': 'Harvest one Tree',
                '3': 'Harvest some Trees',
                '4': 'Quit'}
        for key, value in menu.items():
            print(f"{key}: {value}")

        choice = input(">>> ")
        if choice in menu:
            return choice


def add_a_tree(farm: TreeFarm):
    """Add a tree to farm.

    :param farm: a well-formed TreeFarm object
    :precondition: the farm must be a TreeFarm object
    :postcondition: adds a new tree to farm
    """
    try:
        species = input("Enter the species: ")
        age = int(input("Enter the age: "))
        circumference = float(input("Enter the circumference: "))
        new_tree = Tree(species, age, circumference)
    except ValueError as ve:
        print(f"#Error: {ve}")
    else:
        farm.add(new_tree)
        print(f"Successfully added!")
        print(farm)


def harvest_one_tree(farm: TreeFarm):
    """Harvest one tree.

    :param farm: a well-formed TreeFarm object
    :precondition: farm must be a TreeFarm object
    :postcondition: successfully removes 1 tree >= circumference or print
    message informing user of farm state
    :return: None if tree farm is empty
    """
    if not farm.get_tree_list():
        print("The farm is empty.")
        return None

    try:
        circumference = float(input("Enter the circumference: "))
    except TypeError as te:
        print(te)
    else:
        removed = farm.remove_tree(circumference)
        if circumference >= 0 and removed is not None:
            print(f"Harvested: {removed.get_species()},"
                  f" {removed.get_age()}yr, {removed.get_circumference()}cm")
        elif circumference < 0:
            print("# Error: circumference must be a positive number")


def harvest_some_trees(farm: TreeFarm):
    """Harvest some tree.

    :param farm: a well-formed TreeFarm object
    :precondition: farm must be a TreeFarm object
    :postcondition: successfully removes tree(s) >= circumference or print
    message informing user of farm state
    :return: None if tree farm is empty
    """
    if not farm.get_tree_list():
        print("The farm is empty.")
        return None

    try:
        circumference = float(input("Enter the circumference: "))
    except TypeError as te:
        print(te)
    else:
        removed = farm.remove_trees(circumference)
        if circumference >= 0 and removed is not None:
            print("Harvested:")
            for tree in removed:
                print(f"\t{tree.get_species()}, {tree.get_age()}yr,"
                      f" {tree.get_circumference()}cm")
        elif circumference < 0:
            print("# Error: circumference must be a positive number")


def execute_menu(farm: TreeFarm, choice: str):
    """Execute the correct function based on user choice.

    :param farm: well-formed TreeFarm object
    :param choice: an integer
    :precondition: choice must be an int and farm must be a TreeFarm object
    :postcondition: correctly executes the corresponding function based on
    user choice
    """

    if choice == "1":
        add_a_tree(farm)
    elif choice == "2":
        harvest_one_tree(farm)
    elif choice == "3":
        harvest_some_trees(farm)
    elif choice == "4":
        raise SystemExit("\n=== Bye, see you again. ===")


def main():
    """Drive the program and doctest in this module."""
    doctest.testmod()

    farm = TreeFarm()
    while True:
        execute_menu(farm, choose_menu())
        print()


if __name__ == "__main__":
    main()
