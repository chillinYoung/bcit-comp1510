"""
COMP 1510 202010 Lab 07c
Young Kim (A01087377)

Unit test for the is_larger method of Country Class.
"""

from unittest import TestCase
from country import Country


class TestIsLarger(TestCase):

    def setUp(self):
        self.canada = Country("Canada", 37_590_000, 9_985_000)
        self.denmark = Country("Denmark", 5_603_000, 42_933)
        self.south_korea = Country("South Korea", 51_709_098, 100_363)

    def test_canada_is_larger_than_denmark_true(self):
        expected = True
        actual = self.canada.is_larger(self.denmark)
        self.assertEqual(actual, expected)

    def test_denmark_is_larger_than_korea_false(self):
        expected = False
        actual = self.denmark.is_larger(self.south_korea)
        self.assertEqual(actual, expected)

    def test_canada_is_larger_than_canada_false(self):
        expected = False
        actual = self.canada.is_larger(self.canada)
        self.assertEqual(actual, expected)
