"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from unittest.mock import patch
from dnd import create_character


class TestCreateCharacter(TestCase):

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_name_zero(self, mock_input):
        actual = create_character(0)
        self.assertIsNone(actual)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_not_integer(self, mock_input):
        actual = create_character("test")
        self.assertIsNone(actual)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_name_length(self, mock_input):
        actual = len(create_character(3)['Name'])
        self.assertEqual(actual, 6)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_inventory(self, mock_input):
        actual = create_character(3)['Inventory']
        self.assertEqual(actual, [])

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_xp(self, mock_input):
        actual = create_character(3)['XP']
        self.assertEqual(actual, 0)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_class(self, mock_input):
        actual = create_character(3)['Class']
        self.assertEqual(actual, "druid")

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_race(self, mock_input):
        actual = create_character(3)['Race']
        self.assertEqual(actual, "elf")

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_hp_max(self, mock_input):
        actual = create_character(3)['HP'][0]
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 8)    # druid's hit-die

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_hp_current(self, mock_input):
        actual = create_character(3)['HP'][1]
        self.assertEqual(actual, 0)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_strength(self, mock_input):
        actual = create_character(3)['Strength']
        self.assertGreaterEqual(actual, 3)
        self.assertLessEqual(actual, 18)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_intelligence(self, mock_input):
        actual = create_character(3)['Intelligence']
        self.assertGreaterEqual(actual, 3)
        self.assertLessEqual(actual, 18)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_wisdom(self, mock_input):
        actual = create_character(3)['Wisdom']
        self.assertGreaterEqual(actual, 3)
        self.assertLessEqual(actual, 18)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_dexterity(self, mock_input):
        actual = create_character(3)['Dexterity']
        self.assertGreaterEqual(actual, 3)
        self.assertLessEqual(actual, 18)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_constitution(self, mock_input):
        actual = create_character(3)['Constitution']
        self.assertGreaterEqual(actual, 3)
        self.assertLessEqual(actual, 18)

    @patch('builtins.input', side_effect=["druid", "elf"])
    def test_create_character_charisma(self, mock_input):
        actual = create_character(3)['Charisma']
        self.assertGreaterEqual(actual, 3)
        self.assertLessEqual(actual, 18)
