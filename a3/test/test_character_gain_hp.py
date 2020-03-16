"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for gain_hp function in the character module.
"""

from unittest import TestCase
from character import gain_hp


class TestGainHp(TestCase):

    def test_gain_hp_when_user_has_9_hp(self):
        """the hp for the user should never exceed 10"""
        char_max_hp = 10
        char = {'Name': 'Woody',
                'HP': 9,
                'Max_HP': char_max_hp,
                'Pos_x': 1,
                'Pos_y': 1}
        gain_hp(char, 2)
        actual_char_hp = char['HP']
        expected_char_hp = 10
        self.assertEqual(actual_char_hp, expected_char_hp)

    def test_gain_hp_when_user_has_10_hp(self):
        """there shouldn't be changes to the char hp"""
        char_max_hp = 10
        char = {'Name': 'Woody',
                'HP': 10,
                'Max_HP': char_max_hp,
                'Pos_x': 1,
                'Pos_y': 1}
        gain_hp(char, 2)
        actual_char_hp = char['HP']
        expected_char_hp = 10
        self.assertEqual(actual_char_hp, expected_char_hp)

    def test_gain_hp_when_user_has_2_hp(self):
        """there shouldn't be changes to the char hp"""
        char_max_hp = 10
        char = {'Name': 'Woody',
                'HP': 2,
                'Max_HP': char_max_hp,
                'Pos_x': 1,
                'Pos_y': 1}
        gain_hp(char, 2)
        actual_char_hp = char['HP']
        expected_char_hp = 4
        self.assertEqual(actual_char_hp, expected_char_hp)
