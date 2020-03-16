"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for choose_character function in the character module.
"""

from unittest import TestCase
from unittest.mock import patch
from character import choose_character


class TestChooseCharacter(TestCase):

    @patch("builtins.input", return_value="1")
    def test_choose_character_valid_entry(self, mock_input):
        actual = choose_character()
        expected = "Woody"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["woody", "1"])
    def test_choose_character_invalid_entry_first_then_valid(self, mock_input):
        actual = choose_character()
        expected = "Woody"
        self.assertEqual(actual, expected)

    @patch("builtins.input", return_value="quit")
    def test_choose_character_quit_and_exit(self, mock_input):
        actual = choose_character()
        expected = "quit"
        self.assertEqual(actual, expected)
