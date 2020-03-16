"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for play function in the sud module.
"""

from unittest import TestCase
from unittest.mock import patch
from sud import play


class TestPlay(TestCase):

    @patch('builtins.input', return_value="quit")
    def test_play_quit_when_choose_character(self, mock_input):
        """Test quit input from user during choosing character."""
        with self.assertRaises(SystemExit):
            play()

    @patch('builtins.input', side_effect=["1", "quit"])
    def test_play_quit_when_choose_direction(self, mock_input):
        """Test quit input from user during choosing direction to move."""
        with self.assertRaises(SystemExit):
            play()

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["1", "e", "quit"])
    def test_play_quit_when_encountered_monster(
            self, mock_input, mock_randint):
        """Test quit input from user during choosing direction to move."""
        with self.assertRaises(SystemExit):
            play()

    @patch('random.randint', side_effect=[3, 1, 2, 2, 2, 2])
    @patch('builtins.input', side_effect=["1", "e", "n", "run",
                                          "n", "e", "e", "e"])
    def test_play_found_andy_with_one_run(
            self, mock_input, mock_randint):
        """Test found andy after a little of journey."""
        with self.assertRaises(SystemExit):
            play()

    @patch('random.randint', side_effect=[1, 1, 5, 1, 5])
    @patch('builtins.input', side_effect=["1", "e", "combat"])
    def test_play_character_lose(self, mock_input, mock_randint):
        """Test losing of the character after a combat."""
        with self.assertRaises(SystemExit):
            play()
