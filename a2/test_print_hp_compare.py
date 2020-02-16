"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from unittest.mock import patch
import io
import dnd


class TestPrintHpCompare(TestCase):

    def setUp(self):
        """Set up the dictionaries to test this test module."""
        self.opponent_one = {'Name': 'Kiki',
                             'HP': [11, 5]}

        self.opponent_two = {'Name': 'Huhaya',
                             'HP': [8, 7]}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hp_compare(self, mock_stdout):
        """Test the print of hp comparing."""
        expected = "Kiki (HP: 5) vs. Huhaya (HP: 7)\n"
        dnd.print_hp_compare(self.opponent_one, self.opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected)
