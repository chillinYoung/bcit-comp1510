"""
COMP 1510 202010 Lab 10 - Unit Test
Young Kim (A01087377)

A unit test for the is_poker function in the regular_expressions module.
"""

from unittest import TestCase
from regular_expressions import is_poker


class TestIsPoker(TestCase):
    """Test is_poker function."""

    def test_is_poker_full_house_not_in_order_false(self):
        """Test full house not in order."""
        expected = False
        actual = is_poker("2q2q2")
        self.assertEqual(actual, expected)

    def test_is_poker_full_house_true(self):
        """Test full house in order."""
        expected = True
        actual = is_poker("222qq")
        self.assertEqual(actual, expected)

    def test_is_poker_full_house_pair_and_pair_of_three_false(self):
        """Test full house not in order which has pair and pair of three."""
        expected = False
        actual = is_poker("qq222")
        self.assertEqual(actual, expected)

    def test_is_poker_straight_reversed_order_false(self):
        """Test straight in reversed order."""
        expected = False
        actual = is_poker("6789t")
        self.assertEqual(actual, expected)

    def test_is_poker_straight_in_order_true(self):
        """Test straight in order."""
        expected = True
        actual = is_poker("t9876")
        self.assertEqual(actual, expected)

    def test_is_poker_with_six_characters_false(self):
        """Test six characters."""
        expected = False
        actual = is_poker("555533")
        self.assertEqual(actual, expected)

    def test_is_poker_all_same_characters(self):
        """Test all same characters."""
        expected = False
        actual = is_poker("99999")
        self.assertEqual(actual, expected)
