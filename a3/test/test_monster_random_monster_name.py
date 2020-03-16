"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for random_monster_name function in the monster module.
"""

from unittest import TestCase
from unittest.mock import patch
from monster import random_monster_name


class TestRandomMonsterName(TestCase):

    @patch('random.choice', return_value="monster name")
    def test_random_monster_name_random_choice(self, mock_rand_choice):
        """Test the chosen name"""
        expected = "monster name"
        actual = random_monster_name()
        self.assertEqual(actual, expected)
