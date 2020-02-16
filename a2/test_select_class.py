"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from unittest.mock import patch
from dnd import select_class


class TestSelectClass(TestCase):

    @patch('builtins.input', side_effect=["BARBARIAN"])
    def test_select_class_uppercase_input(self, mock_input):
        """Test an uppercase class input."""
        actual = select_class()
        self.assertEqual(actual, "barbarian")

    @patch('builtins.input', side_effect=["BaRbArIAn"])
    def test_select_class_mixcase_input(self, mock_input):
        """Test a class input wit mixed case."""
        actual = select_class()
        self.assertEqual(actual, "barbarian")

    @patch('builtins.input', side_effect=["   barbarian   "])
    def test_select_class_strip(self, mock_input):
        """Test a class input with whitespaces before and after of it."""
        actual = select_class()
        self.assertEqual(actual, "barbarian")

    @patch('builtins.input', side_effect=[" b  a r b  a r i a n  "])
    def test_select_class_all_whitespaces(self, mock_input):
        """Test a class input with several whitespaces in a string."""
        actual = select_class()
        self.assertEqual(actual, "barbarian")
