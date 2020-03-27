"""
COMP 1510 202010 Assignment 4
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

A module that drives a program 'Lumber Company'.
"""

from tree import Tree
from tree_farm import TreeFarm


def chooseMenu():
    """
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
    """
    """
    species = input("Enter the species: ")
    age = int(input("Enter the age: "))
    circumference = float(input("Enter the circumference: "))

    try:
        new_tree = Tree(species, age, circumference)
    except ValueError as ve:
        print(ve)
    else:
        farm.add(new_tree)
        print(f"Successfully added!")


def harvest_one_tree(farm: TreeFarm):
    circumference = float(input("Enter the circumference: "))

    if circumference > 0:
        harvested = farm.remove_tree(circumference)
        print(f"Harvested: {harvested.species}, {harvested.age}yr,"
              f" {harvested.circumference}cm")
    else:
        print("# Error: circumference must be a positive number")


def harvest_some_trees(farm: TreeFarm):
    circumference = float(input("Enter the circumference: "))

    if circumference > 0:
        harvested = farm.remove_trees(circumference)
        print("Harvested Trees:")
        for tree in harvested:
            print(f"{tree.species}, {tree.age}yr, {tree.circumference}cm")
    else:
        print("# Error: circumference must be a positive number")


def quit():
    raise SystemExit("\n=== Bye, see you again. ===")


def executeMenu(farm, choice):
    if choice == "1":
        add_a_tree(farm)
    elif choice == "2":
        harvest_one_tree(farm)
    elif choice == "3":
        harvest_some_trees(farm)
    elif choice == "4":
        quit()


def main():
    """Drive the program."""
    farm = TreeFarm()
    while True:
        executeMenu(farm, chooseMenu())
        print()


if __name__ == "__main__":
    main()
