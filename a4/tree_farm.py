"""
COMP 1510 202010 Assignment 4
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

A class that can be used to represent a tree farm.
"""

import doctest
from tree import Tree


class TreeFarm:
    """A class that represents a tree farm."""

    trees = []

    def add(self, tree: Tree):
        """
        """
        if isinstance(tree, Tree):
            TreeFarm.trees.append(tree)
        else:
            raise TypeError("# TypeError: it is not a Tree")

    def print_trees(self):
        """
        """
        for tree in TreeFarm.trees:
            print(f"{tree.species}, {tree.age}")

    def remove_tree(self, circumference: float):
        """
        """
        tree_list = TreeFarm.trees[:]
        for tree in tree_list:
            if tree.circumference >= circumference:
                TreeFarm.trees.remove(tree)
                return tree

    def remove_trees(self, circumference: float):
        """
        """
        harvested = []
        tree_list = TreeFarm.trees[:]
        for tree in tree_list:
            if tree.circumference >= circumference:
                TreeFarm.trees.remove(tree)
                harvested.append(tree)

        if len(harvested) > 0:
            return harvested


def main():
    """Drive the doctest in this module."""
    doctest.testmod()

    one = Tree("Oak", 1, 20.0)
    two = Tree("Oak", 5, 42.1)
    three = Tree("Maple", 8, 52.9)
    farm = TreeFarm()
    farm.add(one)
    farm.add(three)
    farm.add(two)
    farm.print_trees()
    print()

    print(farm.remove_tree(40))
    # print(farm.remove_trees(40))
    farm.print_trees()


if __name__ == "__main__":
    main()
