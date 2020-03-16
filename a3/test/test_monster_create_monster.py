"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for create_monster function in the monster module.
"""

from unittest import TestCase
from unittest.mock import patch
from monster import create_monster


class TestCreateMonster(TestCase):

    @patch('random.choice', return_value="monster1")
    def test_create_monster_name(self, mock_rand_choice):
        """Test correctly formed name."""
        argument = 5
        expected = "monster1"
        actual = create_monster(argument)['Name']
        self.assertEqual(actual, expected)

    def test_create_monster_hp(self):
        """Test correctly formed hp."""
        argument = 5
        expected = argument
        actual = create_monster(argument)['HP']
        self.assertEqual(actual, expected)

    def test_create_monster_name_key(self):
        """Test correctly formed Name key for dictionary."""
        actual = create_monster(5)
        self.assertIn('Name', actual)

    def test_create_monster_hp_key(self):
        """Test correctly formed HP key for dictionary."""
        actual = create_monster(5)
        self.assertIn('HP', actual)
