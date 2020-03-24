"""
COMP 1510 202010 Lab 07c
Young Kim (A01087377)

Unit test for the __init__ method of Country Class.
"""

from unittest import TestCase
from country import Country


class TestInit(TestCase):

    def setUp(self):
        """Set up variables to use through this unit test."""
        self.canada = Country("Canada", 37_590_000, 9_985_000)
        self.denmark = Country("Denmark", 5_603_000, 42_933)

    def test___init___name(self):
        """Test initialized name."""
        expected = "Canada"
        actual = self.canada.name
        self.assertEqual(actual, expected)

    def test___init___population(self):
        """Test initialized population."""
        expected = 37590000
        actual = self.canada.population
        self.assertEqual(actual, expected)

    def test___init___area(self):
        """Test initialized area."""
        expected = 9985000
        actual = self.canada.area
        self.assertEqual(actual, expected)
