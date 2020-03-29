"""
COMP 1510 202010 Assignment 4 - Tree
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

A class that can be used to represent a tree.
"""

import doctest


class Tree:
    """ a class to model a tree"""

    def __init__(self, species: str, age: int, circumference):
        """
        Instantiate an instance of Tree.

        :param species: a string
        :param age: an int or a float
        :param circumference: an int or a float
        :precondition: The parameters must be the indicated type and species must be a meaningful
        tree specie name
        :postcondition: Correctly creates an instance of a Tree
        :raise ValueError: if the species has less than 1 character
        :raise ValueError: if the age is zero or negative value
        :raise ValueError: if the circumference is zero or negative value

        >>> print(Tree("willow", 5, 123.24))
        Tree specie: 'willow', age: 5, circumference: 123.24

        >>> Tree("happy tree", 10.12, 125)
        Tree('happy tree', 10, 125.0)
        """
        if len(species.strip()) > 0:
            self.__species = species.strip()
        else:
            raise ValueError("Tree species cannot be empty or only have white spaces")

        if int(age) > 0:
            self.__age = int(age)
        else:
            raise ValueError("The age cannot be negative or zero")

        if float(circumference) > 0:
            self.__circumference = float(circumference)
        else:
            raise ValueError("The circumference cannot be negative or zero")

    def get_species(self) -> str:
        """Return Tree instance species.

        :postcondition: correctly returns the tree instance species value as a string.
        :return: tree instance species value as a string

        >>> tree = Tree("willow", 5, 123.24)
        >>> tree.get_species()
        'willow'

        >>> tree = Tree("happy tree", 10, 6000.2356)
        >>> tree.get_species()
        'happy tree'
        """
        return self.__species

    def get_age(self) -> float:
        """Return Tree instance age.

        :postcondition: correctly returns the age of the tree instance as a float
        :return: tree instance age as a float

        >>> tree = Tree("happy tree", 10, 6000.2356)
        >>> tree.get_age()
        10

        >>> tree = Tree("willow", 1.2, 123.24)
        >>> tree.get_age()
        1
        """
        return self.__age

    def get_circumference(self) -> float:
        """Return Tree instance circumference.

        :postcondition: correctly returns the circumference of the tree instance as a float
        :return: tree instance circumference as a float

        >>> tree = Tree("happy tree", 10, 6000.2356)
        >>> tree.get_circumference()
        6000.2356

        >>> tree = Tree("happy tree", 10, 125)
        >>> tree.get_circumference()
        125.0
        """
        return self.__circumference

    def set_age(self, age):
        """Update age of tree instance.

        :param age: an int or a float
        :precondition: age must be > 0
        :postcondition: correctly updates the age of the tree instance
        :raise ValueError: if the age is <= 0

        >>> tree = Tree("happy tree", 10, 125)
        >>> tree.set_age(6)
        >>> print(tree)
        Tree specie: 'happy tree', age: 6, circumference: 125.0

        >>> tree = Tree("happy tree", 10, 125)
        >>> tree.set_age(12.9)
        >>> print(tree)
        Tree specie: 'happy tree', age: 12, circumference: 125.0
        """
        if int(age) > 0:
            self.__age = int(age)
        else:
            raise ValueError("The age cannot be negative or zero")

    def set_circumference(self, circumference):
        """Update age of tree instance.

        :param circumference: an int or a float
        :precondition: circumference must be > 0
        :postcondition: correctly updates the circumference of the tree instance
        :raise ValueError: if the circumference is <= 0

        >>> tree = Tree("happy tree", 10, 125)
        >>> tree.set_circumference(123.34)
        >>> print(tree)
        Tree specie: 'happy tree', age: 10, circumference: 123.34
        """

        if float(circumference) > 0:
            self.__circumference = float(circumference)
        else:
            raise ValueError("The circumference cannot be negative or zero")

    def __str__(self) -> str:
        """
        Return string representation of object for user.

        :return: a string representation of the object
        """
        return f"Tree specie: '{self.get_species()}', " \
               f"age: {self.get_age()}, circumference: " \
               f"{self.get_circumference()}"

    def __repr__(self) -> str:
        """
        Return string representation of object for developers.

        :return: a string representation of the object
        """
        return f"Tree('{self.get_species()}', " \
               f"{self.get_age()}, " \
               f"{self.get_circumference()})"


def main():
    """Drive the doctest in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
