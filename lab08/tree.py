"""
COMP 1510 202010 Lab 08
Young Kim (A01087377)

A class that can be used to represent a tree.
"""

import doctest


class Tree:
    """A class that represents a tree."""

    def __init__(self, species: str, age: int, circumference: float) -> None:
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
        """
        if species.strip() == "":
            raise ValueError("# Value Error: species argument is empty")
        else:
            self.species = species

        if age < 0:
            raise ValueError("# Value Error: the age can not be negative")
        else:
            self.age = age

        if circumference < 0:
            raise ValueError("# Value Error: the circumference can not"
                             " be negative")
        else:
            self.circumference = circumference

    def set_species(self, species: str):
        """Set species of the tree.

        :param species: the species as a string
        :precondition: species must be a string
        :postcondition: correctly set tree's species
        """
        if species.strip() != "":
            self.species = species

    def set_age(self, age: int):
        """Set age of the tree.

        :param age: the age as an integer
        :precondition: age must be an positive integer
        :postcondition: correctly set tree's age
        """
        if age >= 0:
            self.age = age

    def set_circumference(self, circumference: float):
        """Set circumfernce of the tree.

        :param circumference: the circumference in centimetres
        :precondition: circumference must be a positive float
        :postcondition: correcly set tree's circumference
        """
        if circumference >= 0:
            self.circumference = circumference

    def get_species(self):
        """Return the species.

        :return: species as a string
        """
        return self.species

    def get_age(self):
        """Return the age.

        :return: age as an integer
        """
        return self.age

    def get_circumference(self):
        """Return the circumference.

        :return: circumference as a float
        """
        return self.circumference

    def __str__(self) -> str:
        """Return the object in informal representation.

        :return: an informal representation of a tree object
        """
        return (f"This {self.species} tree is {self.age} years old and"
                f" has {self.circumference} centimetres of circumference.")

    def __repr__(self) -> str:
        """Return the object in official representation.

        :return: an official representation of a tree object
        """
        return (f"Tree(\"{self.species}\", {self.age}, {self.circumference})")


def main():
    """Drive the doctest in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
