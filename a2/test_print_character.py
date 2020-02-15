"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from unittest.mock import patch
import io
from dnd import print_character


class TestPrintCharacter(TestCase):

    def setUp(self):
        self.character_sample = {'Name': 'Qaba',
                                 'Inventory': [],
                                 'XP': 0,
                                 'Class': 'barbarian',
                                 'Race': 'dragonborn',
                                 'HP': [5, 0],
                                 'Strength': 11,
                                 'Intelligence': 12,
                                 'Wisdom': 7,
                                 'Dexterity': 14,
                                 'Constitution': 12,
                                 'Charisma': 12}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_formed_dictionary(self, mock_stdout):
        actual = print_character(self.character_sample)
        expected = ("{'Name': 'Qaba', 'Inventory': [], 'XP': 0, "
                    "'Class': 'barbarian', 'Race': 'dragonborn', "
                    "'HP': [5, 0], 'Strength': 11, 'Intelligence': 12, "
                    "'Wisdom': 7, 'Dexterity': 14, 'Constitution': 12, "
                    "'Charisma': 12}\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_empty_dictionary(self, mock_stdout):
        actual = print_character({})
        expected = "{}\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
