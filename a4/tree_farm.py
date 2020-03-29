"""
COMP 1510 202010 Assignment 4 - Tree Farm
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

A class that can be used to represent a tree farm.
"""

import doctest
from tree import Tree


class TreeFarm:
    """A class that represents a tree farm."""
    def __init__(self):
        """Instantiate a tree farm.

        :postcondition: correctly creates an instance of a tree farm

        >>> new_farm = TreeFarm()
        >>> new_farm.get_tree_list()
        []
        """
        self.__tree_list = []

    def add(self, tree: Tree):
        """Add tree to the tree farm.

        :param tree: an object of the Tree class
        :precondition: tree must be the tree object
        :postcondition: add the given tree to the tree list of the farm
        :raise TypeError: if the argument is not an instance of the Tree class

        >>> new_tree = Tree("Oak", 2, 15.2)
        >>> new_farm = TreeFarm()
        >>> new_farm.add(new_tree)
        """
        if isinstance(tree, Tree):
            self.__tree_list.append(tree)
        else:
            raise TypeError("# TypeError: it is not a Tree")

    def print_trees(self):
        """Print trees in the farm.

        :postcondition: correctly print all trees in the farm

        >>> new_tree = Tree("Oak", 2, 15.2)
        >>> new_farm = TreeFarm()
        >>> new_farm.add(new_tree)
        >>> new_farm.print_trees()
        Oak, 2
        """
        for tree in self.__tree_list:
            print(f"{tree.get_species()}, {tree.get_age()}")

    def remove_tree(self, circumference: float):
        """Remove a tree.

        :param circumference: a float number
        :precondition: circumference must be a positive float number
        :postcondition: correctly remove the tree from the farm and show
                which one is removed
        :return: the removed tree object if it exists

        >>> new_tree = Tree("Maple", 3, 23.1)
        >>> new_farm = TreeFarm()
        >>> new_farm.add(new_tree)
        >>> new_farm.remove_tree(30)
        Nothing to harvest.

        >>> new_farm.remove_tree(20)
        Tree('Maple', 3, 23.1)
        """
        tree_list = self.__tree_list[:]
        for tree in tree_list:
            if tree.get_circumference() >= circumference:
                self.__tree_list.remove(tree)
                return tree
        print("Nothing to harvest.")

    def remove_trees(self, circumference: float):
        """Remove trees.

        :param circumference: a float number
        :precondition: circumference must be a positive float number
        :postcondition: correctly remove the trees from the farm and show
                which trees are removed
        :return: the list of the removed tree objects if they exist

        >>> maple = Tree("Maple", 3, 23.1)
        >>> oak = Tree("Oak", 2, 15.2)
        >>> new_farm = TreeFarm()
        >>> new_farm.add(maple)
        >>> new_farm.add(oak)
        >>> new_farm.remove_trees(40)
        Nothing to harvest.

        >>> new_farm.remove_trees(10)
        [Tree('Maple', 3, 23.1), Tree('Oak', 2, 15.2)]
        """
        harvested = []
        tree_list = self.__tree_list[:]
        for tree in tree_list:
            if tree.get_circumference() >= circumference:
                self.__tree_list.remove(tree)
                harvested.append(tree)

        if len(harvested) > 0:
            return harvested
        else:
            print("Nothing to harvest.")

    def get_tree_list(self):
        """Return the tree list.

        :return: the tree list in the farm

        >>> new_farm = TreeFarm()
        >>> new_farm.get_tree_list()
        []

        >>> new_tree = Tree("Oak", 2, 15.2)
        >>> new_farm.add(new_tree)
        >>> new_farm.get_tree_list()
        [Tree('Oak', 2, 15.2)]
        """
        return self.__tree_list

    def __repr__(self):
        """Return the object in official representation.

        :return: an official representation of a tree_farm object

        >>> new_farm = TreeFarm()
        >>> repr(new_farm)
        'TreeFarm()'
        >>> new_farm
        TreeFarm()
        """
        return f"TreeFarm()"

    def __str__(self):
        """Return the object in informal representation.

        :return: an informal representation of a tree_farm object with the
                number of trees in the list

        >>> new_tree = Tree("Oak", 2, 15.2)
        >>> new_farm = TreeFarm()
        >>> new_farm.add(new_tree)
        >>> str(new_farm)
        'TreeFarm has 1 tree(s).'

        >>> farm = TreeFarm()
        >>> print(farm)
        TreeFarm has 0 tree(s).
        """
        return f"TreeFarm has {len(self.__tree_list)} tree(s)."


def main():
    """Drive the doctest in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
