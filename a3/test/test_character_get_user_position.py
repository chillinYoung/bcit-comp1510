"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for get_user_position function in the character module.
"""

from unittest import TestCase
from character import get_user_position


class TestGetUserPosition(TestCase):
    def test_get_user_position_at_0_0(self):
        char = {'Name': 'Woody',
                'HP': 6,
                'Max_HP': 10,
                'Pos_x': 0,
                'Pos_y': 0}

        actual = get_user_position(char)
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_get_user_position_at_2_1(self):
        char = {'Name': 'Woody',
                'HP': 6,
                'Max_HP': 10,
                'Pos_x': 2,
                'Pos_y': 1}

        actual = get_user_position(char)
        expected = (2, 1)
        self.assertEqual(actual, expected)
