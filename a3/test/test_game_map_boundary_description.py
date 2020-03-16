"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for boundary_description function in the game_map module.
"""

from unittest import TestCase
from unittest.mock import patch
import io
from game_map import boundary_description


class TestBoundaryDescription(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boundary_description_for_north(self, mock_stdout):
        boundary_description('n')
        expected = ("\n\t# Can't go this way, "
                    "it will lead you to the valley of death.\n\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boundary_description_for_south(self, mock_stdout):
        boundary_description('s')
        expected = ("\n\t# You will fall out of the train in this direction "
                    "and be crushed into a million pieces! Don't go here!\n\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boundary_description_for_west(self, mock_stdout):
        boundary_description('w')
        expected = ("\n\t# If you force your way this way, "
                    "it's a black hole and you will never see Andy again!\n\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boundary_description_for_east(self, mock_stdout):
        boundary_description('e')
        expected = "\n\t# It's not this way! This will take you to hell.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_boundary_description_for_invalid_direction(self, mock_stdout):
        boundary_description('up')
        expected = "\n\t# Invalid entry.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
