"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for check_zero_hp function in the sud module.
"""

from unittest import TestCase
from sud import check_zero_hp


class TestPlayMove(TestCase):

    def test_check_zero_hp_with_zero(self):
        """Test hp with zero."""
        character = {'HP': 0}
        with self.assertRaises(SystemExit):
            check_zero_hp(character)

    def test_check_zero_hp_with_not_zero(self):
        """Test hp with non-zero."""
        character = {'HP': 3}
        actual = check_zero_hp(character)
        expected = None
        self.assertEqual(actual, expected)
