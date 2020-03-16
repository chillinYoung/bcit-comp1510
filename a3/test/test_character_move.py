"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for move function in the character module.
"""

from unittest import TestCase
from character import move


class TestMove(TestCase):
    def test_move_char_to_north(self):
        char = {'Name': 'Woody',
                'HP': 10,
                'Max_HP': 10,
                'Pos_x': 0,
                'Pos_y': 0}
        move(char, 'n')
        actual = (char['Pos_x'], char['Pos_y'])
        expected = (0, 1)
        self.assertEqual(actual, expected)

    def test_move_char_to_east(self):
        char = {'Name': 'Woody',
                'HP': 10,
                'Max_HP': 10,
                'Pos_x': 0,
                'Pos_y': 0}
        move(char, 'e')
        actual = (char['Pos_x'], char['Pos_y'])
        expected = (1, 0)
        self.assertEqual(actual, expected)

    def test_move_char_to_west(self):
        char = {'Name': 'Woody',
                'HP': 10,
                'Max_HP': 10,
                'Pos_x': 2,
                'Pos_y': 1}
        move(char, 'w')
        actual = (char['Pos_x'], char['Pos_y'])
        expected = (1, 1)
        self.assertEqual(actual, expected)

    def test_move_char_to_south(self):
        char = {'Name': 'Woody',
                'HP': 10,
                'Max_HP': 10,
                'Pos_x': 2,
                'Pos_y': 1}
        move(char, 's')
        actual = (char['Pos_x'], char['Pos_y'])
        expected = (2, 0)
        self.assertEqual(actual, expected)
