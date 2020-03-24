"""
COMP 1510 202010 Lab 07c
Young Kim (A01087377)

Unit test for the __repr__ method of Country Class.
"""

from unittest import TestCase
from country import Country


class TestStr(TestCase):

    def setUp(self):
        self.canada = Country("Canada", 37_590_000, 9_985_000)

    def test___repr___invoke_method_with_dunder(self):
        expected = 'Country("Canada", 37590000, 9985000)'
        actual = self.canada.__repr__()
        self.assertEqual(actual, expected)

    def test___repr___invoke_builtin_repr_function(self):
        expected = 'Country("Canada", 37590000, 9985000)'
        actual = repr(self.canada)
        self.assertEqual(actual, expected)
