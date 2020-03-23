"""
COMP 1510 202010 Lab 07a
Young Kim (A01087377)

Unit test for find_an_even function.
"""

from unittest import TestCase
from exceptions import find_an_even
from unittest.mock import patch
import io


class TestFindAnEven(TestCase):
    def test_test_an_even_zero(self):
        """Test the list with mixed numbers."""
        expected = 0
        test_list = [0]
        actual = find_an_even(test_list)
        self.assertEqual(actual, expected)

    def test_test_an_even_positive_numbers(self):
        """Test the list with mixed numbers."""
        expected = 2
        test_list = [5, 2, 3, 1, 4, 8]
        actual = find_an_even(test_list)
        self.assertEqual(actual, expected)

    def test_test_an_even_negative_numbers(self):
        """Test the list with mixed numbers."""
        expected = -10
        test_list = [-5, -2, -3, -8, -10]
        actual = find_an_even(test_list)
        self.assertEqual(actual, expected)

    def test_test_an_even_mixed_list(self):
        """Test the list with mixed numbers."""
        expected = -4
        test_list = [-1, 0, 3, 7, -4, 10]
        actual = find_an_even(test_list)
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_test_an_even_no_even_numbers(self, mock_stdout):
        """Test the list with no even numbers."""
        expected = "# Not Found Error: no even numbers in the list\n"
        test_list = [5, 9, 3, 1, 7]
        find_an_even(test_list)
        self.assertEqual(mock_stdout.getvalue(), expected)
