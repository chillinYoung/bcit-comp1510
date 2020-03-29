"""
COMP 1510 202010 Lab 08 - Unit Test
Young Kim (A01087377)

A unit test for the Tree class.
"""

from unittest import TestCase
from tree import Tree


class TestTree(TestCase):

    def test___init___create_tree(self):
        """Test created tree by __init__."""
        new_tree = Tree("Oak", 3, 42.1)
        self.assertIsInstance(new_tree, Tree)

    def test___init___empty_species(self):
        """Test creating tree with empty species."""
        with self.assertRaises(ValueError):
            new_tree = Tree("   ", 3, 42.1)

    def test___init___negative_age(self):
        """Test creating tree with negative age."""
        with self.assertRaises(ValueError):
            new_tree = Tree("Oak", -3, 42.1)

    def test___init___negative_circumference(self):
        """Test creating tree with negative circumference."""
        with self.assertRaises(ValueError):
            new_tree = Tree("Oak", 3, -42.1)

    def test_set_age_positive_number(self):
        """Test setting age with positive number."""
        expected = 3
        new_tree = Tree("Oak", 1, 42.1)
        new_tree.set_age(3)
        actual = new_tree.get_age()
        self.assertEqual(actual, expected)

    def test_set_age_negative_number(self):
        """Test setting age with negative number."""
        expected = 1
        new_tree = Tree("Oak", 1, 42.1)
        new_tree.set_age(-3)
        actual = new_tree.get_age()
        self.assertEqual(actual, expected)

    def test_set_circumference_positive_number(self):
        """Test setting circumference with positive number."""
        expected = 21.4
        new_tree = Tree("Oak", 1, 13.2)
        new_tree.set_circumference(21.4)
        actual = new_tree.get_circumference()
        self.assertEqual(actual, expected)

    def test_set_circumference_negative_number(self):
        """Test setting circumference with negative number."""
        expected = 13.2
        new_tree = Tree("Oak", 1, 13.2)
        new_tree.set_circumference(-21.4)
        actual = new_tree.get_circumference()
        self.assertEqual(actual, expected)

    def test_get_species(self):
        expected = "Maple"
        new_tree = Tree("Maple", 1, 13.2)
        actual = new_tree.get_species()
        self.assertEqual(actual, expected)

    def test_get_age(self):
        expected = 4
        new_tree = Tree("Maple", 4, 13.2)
        actual = new_tree.get_age()
        self.assertEqual(actual, expected)

    def test_get_circumference(self):
        expected = 13.2
        new_tree = Tree("Oak", 1, 13.2)
        actual = new_tree.get_circumference()
        self.assertEqual(actual, expected)

    def test___str__(self):
        expected = ("This Oak tree is 1 years old and has 13.2 centimetres"
                    " of circumference.")
        new_tree = Tree("Oak", 1, 13.2)
        actual = new_tree.__str__()
        self.assertEqual(actual, expected)

    def test___repr__(self):
        expected = 'Tree("Maple", 4, 13.2)'
        new_tree = Tree("Maple", 4, 13.2)
        actual = new_tree.__repr__()
        self.assertEqual(actual, expected)
