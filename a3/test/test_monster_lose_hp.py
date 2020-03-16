"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for lose_hp function in the monster module.
"""

from unittest import TestCase
from unittest.mock import patch
from monster import lose_hp
import io


class TestLoseHp(TestCase):

    def test_lose_hp_of_character(self):
        """Test lose hp with character."""
        character = {'Name': 'Woody',
                     'HP': 10,
                     'Max_HP': 10,
                     'Pos_x': 0,
                     'Pos_y': 0}
        expected = 7
        damage_amount = 3
        lose_hp(character, damage_amount)
        actual = character['HP']
        self.assertEqual(actual, expected)

    def test_lose_hp_of_monster(self):
        """Test lose hp with monster."""
        monster = {'Name': 'Test Monster', 'HP': 5}
        expected = 2
        damage_amount = 3
        lose_hp(monster, damage_amount)
        actual = monster['HP']
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lose_hp_of_character_print_died(self, mock_stdout):
        """Test print after character lost hp and died."""
        character = {'Name': 'Rex',
                     'HP': 10,
                     'Max_HP': 10,
                     'Pos_x': 0,
                     'Pos_y': 0}
        expected = "\t=== Rex DIED... ===\n"
        damage_amount = 10
        lose_hp(character, damage_amount)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lose_hp_of_monster_print_died(self, mock_stdout):
        """Test print after monster lost hp and died."""
        monster = {'Name': 'Test Monster', 'HP': 5}
        expected = "\t=== Test Monster DIED... ===\n"
        damage_amount = 5
        lose_hp(monster, damage_amount)
        self.assertEqual(mock_stdout.getvalue(), expected)
