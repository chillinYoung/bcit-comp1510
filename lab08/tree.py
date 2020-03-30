"""
COMP 1510 202010 Lab 08
Young Kim (A01087377)

A class that can be used to represent a tree.
"""

import doctest


class Tree:
    """A class that represents a tree."""

    def __init__(self, species: str, age: int, circumference: float):
        """Initialize attributes to describe a tree.

        :param species: species of a tree as string
        :param age: the age of the tree as an integer
        :param circumference: a trunk circumference of the tree measured
                in centimetres as a float
        :precondition: the arguments must be given with proper types
        :raise ValueError: if species string is empty or only-whitespace
        :raise ValueError: if age is negative number
        :raise ValueError: if circumference is negative number
        :postcondition: correctly form a tree object

        >>> new_tree = Tree("Oak", 2, 40.3)
        >>> new_tree.get_species()
        'Oak'
        >>> new_tree.get_age()
        2
        >>> new_tree.get_circumference()
        40.3
        """
        if species.strip() == "":
            raise ValueError("# Value Error: species argument is empty")
        else:
            self.__species = species.strip()

        if age < 0:
            raise ValueError("# Value Error: the age must be positive integer")
        else:
            self.__age = age

        if circumference < 0:
            raise ValueError("# Value Error: the circumference must be"
                             " positive number")
        else:
            self.__circumference = circumference

    def set_age(self, age: int):
        """Set age of the tree.

        :param age: the age as an integer
        :precondition: age must be an positive integer
        :postcondition: correctly set tree's age

        >>> new_tree = Tree("Maple", 2, 43.7)
        >>> new_tree.set_age(3)
        >>> new_tree.get_age()
        3
        """
        if age >= 0:
            self.__age = age

    def set_circumference(self, circumference: float):
        """Set circumfernce of the tree.

        :param circumference: the circumference in centimetres
        :precondition: circumference must be a positive float
        :postcondition: correcly set tree's circumference

        >>> new_tree = Tree("Cacao", 8, 60.1)
        >>> new_tree.set_circumference(64.9)
        >>> new_tree.get_circumference()
        64.9
        """
        if circumference > 0:
            self.__circumference = circumference

    def get_species(self) -> str:
        """Return the species.

        :return: species as a string

        >>> new_tree = Tree("Maple", 3, 23.2)
        >>> new_tree.get_species()
        'Maple'
        >>> new_tree = Tree("Cacao", 8, 60.1)
        >>> new_tree.get_species()
        'Cacao'
        """
        return self.__species

    def get_age(self) -> int:
        """Return the age.

        :return: age as an integer

        >>> new_tree = Tree("Maple", 3, 23.2)
        >>> new_tree.get_age()
        3
        >>> new_tree = Tree("Cacao", 8, 60.1)
        >>> new_tree.get_age()
        8
        """
        return self.__age

    def get_circumference(self) -> float:
        """Return the circumference.

        :return: circumference as a float

        >>> new_tree = Tree("Maple", 3, 23.2)
        >>> new_tree.get_circumference()
        23.2
        >>> new_tree = Tree("Cacao", 8, 60.1)
        >>> new_tree.get_circumference()
        60.1
        """
        return self.__circumference

    def __str__(self) -> str:
        """Return the object in informal representation.

        :return: an informal representation of a tree object

        >>> new_tree = Tree("Maple", 3, 23.2)
        >>> print(new_tree)    #doctest: +ELLIPSIS
        This Maple tree is 3 years old and has 23.2 ... circumference.

        >>> new_tree = Tree("Cacao", 8, 60.1)
        >>> print(new_tree)    #doctest: +NORMALIZE_WHITESPACE
        This Cacao tree is 8 years old and has 60.1 centimetres of
        circumference.
        """
        return (f"This {self.__species} tree is {self.__age} years old and"
                f" has {self.__circumference} centimetres of circumference.")

    def __repr__(self) -> str:
        """Return the object in official representation.

        :return: an official representation of a tree object

        >>> new_tree = Tree("Maple", 3, 23.2)
        >>> new_tree
        Tree("Maple", 3, 23.2)

        >>> new_tree = Tree("Cacao", 8, 60.1)
        >>> new_tree
        Tree("Cacao", 8, 60.1)
        """
        return (f"Tree(\"{self.__species}\", {self.__age},"
                f" {self.__circumference})")


def main():
    """Drive the doctest in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
