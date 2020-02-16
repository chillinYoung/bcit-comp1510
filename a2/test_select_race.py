"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from unittest.mock import patch
from dnd import select_race


class TestSelectRace(TestCase):

    @patch('builtins.input', side_effect=["DRAGONBORN"])
    def test_select_race_uppercase_input(self, mock_input):
        """Test an uppercase class input."""
        actual = select_race()
        self.assertEqual(actual, "dragonborn")

    @patch('builtins.input', side_effect=["DrAgoNBorN"])
    def test_select_race_mixcase_input(self, mock_input):
        """Test a class input wit mixed case."""
        actual = select_race()
        self.assertEqual(actual, "dragonborn")

    @patch('builtins.input', side_effect=["   dragonborn   "])
    def test_select_race_strip(self, mock_input):
        """Test a class input with whitespaces before and after of it."""
        actual = select_race()
        self.assertEqual(actual, "dragonborn")

    @patch('builtins.input', side_effect=[" d  r a g o n   b o rn "])
    def test_select_race_all_whitespaces(self, mock_input):
        """Test a class input with several whitespaces in a string."""
        actual = select_race()
        self.assertEqual(actual, "dragonborn")
