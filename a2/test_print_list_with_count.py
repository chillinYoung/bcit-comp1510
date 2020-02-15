"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from unittest.mock import patch
import io
from dnd import print_list_with_count


class TestPrintListWithCount(TestCase):

    def setUp(self):
        self.list_sample = ["one", "two", "three", "four", "five"]

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_list_with_count_strings(self, mock_stdout):
        expected = ("1. one\n2. two\n3. three\n4. four\n5. five\n")
        actual = print_list_with_count(self.list_sample)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_list_with_count_zero(self, mock_stdout):
        expected = ""
        actual = print_list_with_count([])
        self.assertEqual(mock_stdout.getvalue(), expected)
