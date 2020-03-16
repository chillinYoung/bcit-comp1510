"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for run_away function in the monster module.
"""

from unittest import TestCase
from unittest.mock import patch
from monster import run_away, lose_hp


class TestRunAway(TestCase):
    def setUp(self):
        self.monster = {'Name': 'test monster', 'HP': 5}

    @patch('random.randint', side_effect=[2, 3])
    def test_run_away_run_away_successfully(self, mock_randint):
        """Test successful run away."""
        character = {'Name': 'Woody',
                     'HP': 10,
                     'Max_HP': 10,
                     'Pos_x': 0,
                     'Pos_y': 0}
        expected = 10
        stab_chance = 10
        stab_damage = 4
        run_away(character, self.monster, stab_chance, stab_damage)
        actual = character['HP']
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[3, 1])
    def test_run_away_stabbed_with_damage_two(self, mock_randint):
        """Test run away but stabbed."""
        character = {'Name': 'Woody',
                     'HP': 10,
                     'Max_HP': 10,
                     'Pos_x': 0,
                     'Pos_y': 0}
        expected = 7
        stab_chance = 10
        stab_damage = 4
        run_away(character, self.monster, stab_chance, stab_damage)
        actual = character['HP']
        self.assertEqual(actual, expected)
