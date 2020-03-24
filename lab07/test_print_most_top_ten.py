"""
COMP 1510 202010 Lab 07b
Young Kim (A01087377)

Unit test for print_most_top_ten function of Lab 07b.
"""

from unittest import TestCase
from unittest.mock import patch
from file_io import print_most_top_ten
import io


class TestPrintMostTopTen(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_most_top_ten_empty_dict(self, mock_stdout):
        """Test empty dictionary."""
        test_dict = dict()
        expected = ""
        print_most_top_ten(test_dict)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_most_top_ten_dict_with_one_element(self, mock_stdout):
        """Test the dictionary with one element."""
        test_dict = {'this': 3}
        expected = "this - 3\n"
        print_most_top_ten(test_dict)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_most_top_ten_unordered_dict(self, mock_stdout):
        """Test the unordered dictionary."""
        test_dict = {'a': 1, 'the': 7, 'this': 21, 'hi': 3}
        expected = "this - 21\nthe - 7\nhi - 3\na - 1\n"
        print_most_top_ten(test_dict)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_most_top_ten_same_values(self, mock_stdout):
        """Test the dictionary with same values."""
        test_dict = {'a': 3, 'the': 3, 'this': 3, 'hi': 3}
        # sorted with the order of reversed keys
        expected = "this - 3\nthe - 3\nhi - 3\na - 3\n"
        print_most_top_ten(test_dict)
        self.assertEqual(mock_stdout.getvalue(), expected)
