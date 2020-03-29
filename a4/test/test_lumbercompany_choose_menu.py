from unittest import TestCase
from unittest.mock import patch
from lumber_company import choose_menu


class TestChooseMenu(TestCase):

    @patch("builtins.input", side_effect=['9', '8', '1'])
    def test_choose_menu_return_1(self, mock_input):
        actual = choose_menu()
        expected = '1'
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=['7', '2'])
    def test_choose_menu_return_2(self, mock_input):
        actual = choose_menu()
        expected = '2'
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=['3'])
    def test_choose_menu_return_3(self, mock_input):
        actual = choose_menu()
        expected = '3'
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=['0', '5', '4'])
    def test_choose_menu_return_4(self, mock_input):
        actual = choose_menu()
        expected = '4'
        self.assertEqual(actual, expected)