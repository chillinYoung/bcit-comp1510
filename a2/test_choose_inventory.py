"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from unittest.mock import patch
import io
import dnd


class TestChooseInventory(TestCase):

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

    @patch('builtins.input', side_effect=["-1"])
    def test_choose_inventory_chose_finish(self, mock_input):
        expected = []
        dnd.choose_inventory(self.character_sample)
        actual = self.character_sample['Inventory']
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["3", "-1"])
    def test_choose_inventory_chose_one_item(self, mock_input):
        expected = 1
        dnd.choose_inventory(self.character_sample)
        actual = len(self.character_sample['Inventory'])
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["3", "2", "10", "7", "-1"])
    def test_choose_inventory_chose_one_item(self, mock_input):
        expected = 4
        dnd.choose_inventory(self.character_sample)
        actual = len(self.character_sample['Inventory'])
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["23", "-1"])
    def test_choose_inventory_chose_invalid_number(self, mock_input):
        expected = []
        dnd.choose_inventory(self.character_sample)
        actual = self.character_sample['Inventory']
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["spear", "-1"])
    def test_choose_inventory_chose_not_number(self, mock_input):
        expected = []
        dnd.choose_inventory(self.character_sample)
        actual = self.character_sample['Inventory']
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["32", "-1"])
    def test_choose_inventory_invalid_number_print(self, mock_input,
                                                   mock_stdout):
        expected = ("Welcome to the Olde Tyme Merchant!\n\n"
                    "Here is what we have for sale:\n\n"
                    "1. sword\n2. dagger\n3. heavy blunt\n4. spear\n5. staff\n"
                    "6. blade\n7. bow\n8. beam\n9. poison\n10. axe\n"
                    "ERROR: please enter the number of an item.\n\n"
                    "1. sword\n2. dagger\n3. heavy blunt\n4. spear\n5. staff\n"
                    "6. blade\n7. bow\n8. beam\n9. poison\n10. axe\n")
        actual = dnd.choose_inventory(self.character_sample)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["something", "-1"])
    def test_choose_inventory_not_number_print(self, mock_input, mock_stdout):
        expected = ("Welcome to the Olde Tyme Merchant!\n\n"
                    "Here is what we have for sale:\n\n"
                    "1. sword\n2. dagger\n3. heavy blunt\n4. spear\n5. staff\n"
                    "6. blade\n7. bow\n8. beam\n9. poison\n10. axe\n"
                    "ERROR: please enter the number of an item.\n\n"
                    "1. sword\n2. dagger\n3. heavy blunt\n4. spear\n5. staff\n"
                    "6. blade\n7. bow\n8. beam\n9. poison\n10. axe\n")
        actual = dnd.choose_inventory(self.character_sample)
        self.assertEqual(mock_stdout.getvalue(), expected)
