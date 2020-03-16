"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for play_monster function in the sud module.
"""

from unittest import TestCase
from unittest.mock import patch
from sud import play_monster
import monster


class TestPlayMonster(TestCase):

    @patch('random.randint', return_value=3)
    def test_play_monster_monster_not_appeared(self, mock_randint):
        """Test monster not appeared."""
        character = {'Name': 'Woody',
                     'HP': 5,
                     'Max_HP': 10,
                     'Pos_x': 0,
                     'Pos_y': 0}
        play_monster(character)
        actual = character['HP']
        expected = 7
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="run")
    @patch('random.randint', side_effect=[1, 1, 2])
    def test_play_monster_monster_appeared_and_run(self,
                                                   mock_randint, mock_input):
        """Test monster appear, and run away."""
        character = {'Name': 'Woody',
                     'HP': 5,
                     'Max_HP': 10,
                     'Pos_x': 0,
                     'Pos_y': 0}
        play_monster(character)
        actual = character['HP']
        expected = 5
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="quit")
    @patch('random.randint', return_value=1)
    def test_play_monster_monster_appeared_and_quit(self,
                                                    mock_randint, mock_input):
        """Test monster appear, and quit."""
        character = {'Name': 'Woody',
                     'HP': 5,
                     'Max_HP': 10,
                     'Pos_x': 0,
                     'Pos_y': 0}
        with self.assertRaises(SystemExit):
            play_monster(character)
