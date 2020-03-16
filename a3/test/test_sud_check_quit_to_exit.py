"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for check_quit_to_exit function in the sud module.
"""

from unittest import TestCase
from sud import check_quit_to_exit


class TestPlayMove(TestCase):

    def test_check_quit_to_exit_quit_successfully(self):
        """Test successful exit of program."""
        with self.assertRaises(SystemExit):
            check_quit_to_exit("quit")

    def test_check_quit_to_exit_not_quit(self):
        """Test other strings that is not 'quit'."""
        actual = check_quit_to_exit("other things")
        expected = None
        self.assertEqual(actual, expected)
