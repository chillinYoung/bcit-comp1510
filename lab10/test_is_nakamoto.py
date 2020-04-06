"""
COMP 1510 202010 Lab 10 - Unit Test
Young Kim (A01087377)

A unit test for the is_nakamoto function in the regular_expressions module.
"""

from unittest import TestCase
from regular_expressions import is_nakamoto


class TestIsNakamoto(TestCase):
    """Test is_nakamoto function."""

    def test_is_nakamoto_only_with_the_last_name_false(self):
        """Test only with the last name."""
        expected = False
        actual = is_nakamoto("Nakamoto")
        self.assertEqual(actual, expected)

    def test_is_nakamoto_full_name_without_white_space_false(self):
        """Test full name without white space."""
        expected = False
        actual = is_nakamoto("SatoshiNakamoto")
        self.assertEqual(actual, expected)

    def test_is_nakamoto_first_name_as_lowercase_false(self):
        """Test first name as lowercase."""
        expected = False
        actual = is_nakamoto("satoshi Nakamoto")
        self.assertEqual(actual, expected)

    def test_is_nakamoto_last_name_as_lowercase_false(self):
        """Test last name as lowercase."""
        expected = False
        actual = is_nakamoto("Satoshi nakamoto")
        self.assertEqual(actual, expected)

    def test_is_nakamoto_no_first_name_but_with_title_false(self):
        """Test no first name but with title."""
        expected = False
        actual = is_nakamoto("Mr. Nakamoto")
        self.assertEqual(actual, expected)

    def test_is_nakamoto_true_name(self):
        """Test true example name."""
        expected = True
        actual = is_nakamoto("Satoshi Nakamoto")
        self.assertEqual(actual, expected)
