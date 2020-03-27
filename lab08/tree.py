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
        :raise ValueError:
        :raise ValueError:
        :raise ValueError:
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
        if species.strip() != "":
            self.species = species

    def set_age(self, age: int):
        if age >= 0:
            self.age = age

    def set_circumference(self, circumference: float):
        if circumference >= 0:
            self.circumference = circumference

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

    test = Tree("Oak", 1, 1.0)
    test.set_age(-2)


if __name__ == "__main__":
    main()
