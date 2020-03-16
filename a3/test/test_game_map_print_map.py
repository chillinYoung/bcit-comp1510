"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for print_map function in the game_map module.
"""

from unittest import TestCase
from unittest.mock import patch
import io
from game_map import print_map


class TestPrintMap(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_map_with_char_at_0_0(self, mock_stdout):
        test_map = {'Width': 5,
                    'Height': 5}
        char = {'Pos_x': 0,
                'Pos_y': 0}
        print_map(test_map, char)
        expected = ("[_][_][_][_][_]\n"
                    "[_][_][_][_][_]\n"
                    "[_][_][_][_][_]\n"
                    "[_][_][_][_][_]\n"
                    "[x][_][_][_][_]\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_map_with_char_at_2_3(self, mock_stdout):
        test_map = {'Width': 5,
                    'Height': 5}
        char = {'Pos_x': 2,
                'Pos_y': 3}
        print_map(test_map, char)
        expected = ("[_][_][_][_][_]\n"
                    "[_][_][x][_][_]\n"
                    "[_][_][_][_][_]\n"
                    "[_][_][_][_][_]\n"
                    "[_][_][_][_][_]\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_map_with_char_at_4_4(self, mock_stdout):
        test_map = {'Width': 5,
                    'Height': 5}
        char = {'Pos_x': 4,
                'Pos_y': 4}
        print_map(test_map, char)
        expected = ("[_][_][_][_][x]\n"
                    "[_][_][_][_][_]\n"
                    "[_][_][_][_][_]\n"
                    "[_][_][_][_][_]\n"
                    "[_][_][_][_][_]\n")
        self.assertEqual(mock_stdout.getvalue(), expected)
