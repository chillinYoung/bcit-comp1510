"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for create_character function in the character module.
"""

from unittest import TestCase
from unittest.mock import patch
from character import create_character


class TestCreateCharacter(TestCase):

    @patch("character.choose_character", return_value="Woody")
    def test_create_character_woody_at_0_0_coordinate(self,
                                                      mock_choose_character):
        """Test with 10 max_hp at (0, 0) position"""
        MAX_HP = 10
        INIT_POS_X = 0
        INIT_POS_Y = 0
        actual = create_character(MAX_HP, INIT_POS_X, INIT_POS_Y)
        expected = {'Name': 'Woody',
                    'HP': MAX_HP,
                    'Max_HP': MAX_HP,
                    'Pos_x': INIT_POS_X,
                    'Pos_y': INIT_POS_Y}
        self.assertEqual(actual, expected)

    @patch("character.choose_character", return_value="Buzz")
    def test_create_character_buzz_at_2_1_coordinate(self,
                                                     mock_choose_character):
        """Test with 1 max_hp at (2, 1) position"""
        MAX_HP = 1
        INIT_POS_X = 2
        INIT_POS_Y = 1
        actual = create_character(MAX_HP, INIT_POS_X, INIT_POS_Y)
        expected = {'Name': 'Buzz',
                    'HP': MAX_HP,
                    'Max_HP': MAX_HP,
                    'Pos_x': INIT_POS_X,
                    'Pos_y': INIT_POS_Y}
        self.assertEqual(actual, expected)
