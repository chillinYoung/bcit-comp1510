"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for get_user_choice function in the sud module.
"""

from unittest import TestCase
from unittest.mock import patch
from sud import get_user_choice


class TestEncounteredMonster(TestCase):

    @patch('builtins.input', return_value="quit")
    def test_get_user_choice_quit(self, mock_input):
        """Test the user input quit."""
        expected = "quit"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="e")
    def test_get_user_choice_e_lowercase(self, mock_input):
        """Test the user input e for east."""
        expected = "e"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="E")
    def test_get_user_choice_e_uppercase(self, mock_input):
        """Test the user input E for east as an uppercase."""
        expected = "e"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="w")
    def test_get_user_choice_w_lowercase(self, mock_input):
        """Test the user input w for west."""
        expected = "w"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="W")
    def test_get_user_choice_w_uppercase(self, mock_input):
        """Test the user input W for west as an uppercase."""
        expected = "w"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="s")
    def test_get_user_choice_s_lowercase(self, mock_input):
        """Test the user input s for south."""
        expected = "s"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="S")
    def test_get_user_choice_s_uppercase(self, mock_input):
        """Test the user input S for south as an uppercase."""
        expected = "s"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="n")
    def test_get_user_choice_n_lowercase(self, mock_input):
        """Test the user input n for north."""
        expected = "n"
        actual = get_user_choice()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="N")
    def test_get_user_choice_n_uppercase(self, mock_input):
        """Test the user input N for north as an uppercase."""
        expected = "n"
        actual = get_user_choice()
        self.assertEqual(actual, expected)
