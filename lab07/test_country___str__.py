"""
COMP 1510 202010 Lab 07c
Young Kim (A01087377)

Unit test for the __str__ method of Country Class.
"""

from unittest import TestCase
from country import Country
from unittest.mock import patch
from io import StringIO


class TestStr(TestCase):

    def setUp(self):
        self.canada = Country("Canada", 37_590_000, 9_985_000)

    @patch('sys.stdout', new_callable=StringIO)
    def test___str__canada(self, mock_stdout):
        expected = ("Canada has a population of 37590000 and is 9985000 "
                    "square kilometres.\n")
        print(self.canada)
        self.assertEqual(mock_stdout.getvalue(), expected)
