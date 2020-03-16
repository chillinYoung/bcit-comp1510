"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for monster_appear function in the monster module.
"""

from unittest import TestCase
from unittest.mock import patch
from monster import monster_appear


class TestMonsterAppear(TestCase):

    def test_monster_appear_one_hundred_percent(self):
        """Test one hundred percent of the chance, which is always True"""
        actual = monster_appear(1)
        self.assertTrue(actual)

    @patch('random.randint', return_value=1)
    def test_monster_appear_fifty_percent_True(self, mock_randint):
        """Test fifty percent of the chance with True."""
        actual = monster_appear(2)
        self.assertTrue(actual)

    @patch('random.randint', return_value=2)
    def test_monster_appear_fifty_percent_False(self, mock_randint):
        """Test fifty percent of the chance with False."""
        actual = monster_appear(2)
        self.assertFalse(actual)

    @patch('random.randint', return_value=1)
    def test_monster_appear_less_than_one_percent_True(self, mock_randint):
        """Test the chance with less than one percent that is True."""
        actual = monster_appear(10000)
        self.assertTrue(actual)

    @patch('random.randint', return_value=1096)
    def test_monster_appear_less_than_one_percent_False(self, mock_randint):
        """Test the chance with less than one percent that is False."""
        actual = monster_appear(10000)
        self.assertFalse(actual)
