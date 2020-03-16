"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for play_move function in the sud module.
"""

from unittest import TestCase
from unittest.mock import patch
from sud import play_move
from game_map import map_init


class TestPlayMove(TestCase):
    def setUp(self):
        self.map = map_init(5, 5)
        self.character = {'Name': 'Woody',
                          'HP': 10,
                          'Max_HP': 10,
                          'Pos_x': 0,
                          'Pos_y': 0}

    @patch('builtins.input', return_value="quit")
    def test_play_move_quit(self, mock_input):
        """Test quit input from user."""
        with self.assertRaises(SystemExit):
            play_move(self.map, self.character)

    @patch('builtins.input', return_value="s")
    def test_play_move_found_andy(self, mock_input):
        """Test found andy on (3, 2)."""
        character = {'Name': 'Woody',
                     'HP': 10,
                     'Max_HP': 10,
                     'Pos_x': 3,
                     'Pos_y': 3}
        with self.assertRaises(SystemExit):
            play_move(self.map, character)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["e", "quit"])
    def test_play_move_to_valid_direction_and_quit(
            self, mock_input, mock_randint):
        """Test possible direction and quit."""
        with self.assertRaises(SystemExit):
            play_move(self.map, self.character)

    @patch('builtins.input', return_value="w")
    def test_play_move_to_invalid_direction(self, mock_input):
        """Test impossible direction."""
        character = {'Name': 'Woody',
                     'HP': 10,
                     'Max_HP': 10,
                     'Pos_x': 0,
                     'Pos_y': 0}
        expected = (0, 0)
        play_move(self.map, character)
        actual = (character['Pos_x'], character['Pos_y'])
        self.assertEqual(actual, expected)
