"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for encountered_monster function in the monster module.
"""

from unittest import TestCase
from unittest.mock import patch
from monster import encountered_monster, run_away, combat


class TestEncounteredMonster(TestCase):
    def setUp(self):
        self.character = {'Name': 'Woody',
                          'HP': 10,
                          'Max_HP': 10,
                          'Pos_x': 0,
                          'Pos_y': 0}
        self.monster = {'Name': 'test monster', 'HP': 5}

    @patch('builtins.input', return_value="quit")
    @patch('monster.create_monster',
           return_value={'Name': 'test monster', 'HP': 5})
    def test_encountered_monster_quit(
            self, mock_create_monster, mock_input):
        """Test the user input quit."""
        expected = "quit"
        actual = encountered_monster(self.character, 6, 5, 10, 4)
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="run")
    @patch('monster.create_monster',
           return_value={'Name': 'test monster', 'HP': 5})
    def test_encountered_monster_run(
            self, mock_create_monster, mock_input):
        """Test the user input run."""
        stab_chance = 10
        stab_damage = 4
        expected = run_away(self.character, self.monster,
                            stab_chance, stab_damage)
        actual = encountered_monster(self.character, 6, 5,
                                     stab_chance, stab_damage)
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="combat")
    @patch('monster.create_monster',
           return_value={'Name': 'test monster', 'HP': 5})
    def test_encountered_monster_combat(
            self, mock_create_monster, mock_input):
        """Test the user input combat."""
        attack_damage = 5
        expected = combat(self.character, self.monster, attack_damage)
        actual = encountered_monster(self.character, 6, attack_damage, 10, 4)
        self.assertEqual(actual, expected)
