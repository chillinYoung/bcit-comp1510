"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for allowed_direction function in the game_map module.
"""

from unittest import TestCase
from game_map import allowed_direction


class TestAllowedDirection(TestCase):
    def test_allowed_direction_at_coordinate_0_0(self):
        """At starting position"""
        test_map = {(0, 0): {'e': True, 'w': False, 's': False, 'n': True}}
        char_coordinates = (0, 0)
        actual = allowed_direction(char_coordinates, test_map)
        expected = ['e', 'n']
        self.assertEqual(actual, expected)

    def test_allowed_direction_at_coordinate_4_4(self):
        """for a map of 5x5, at 4,4 char can only move 's', and 'w'"""
        test_map = {(4, 4): {'e': False, 'w': True, 's': True, 'n': False}}
        char_coordinates = (4, 4)
        actual = allowed_direction(char_coordinates, test_map)
        expected = ['w', 's']
        self.assertEqual(actual, expected)

    def test_allowed_direction_at_coordinate_2_2(self):
        """all direction is allowed"""
        test_map = {(2, 2): {'e': True, 'w': True, 's': True, 'n': True}}
        char_coordinates = (2, 2)
        actual = allowed_direction(char_coordinates, test_map)
        expected = ['e', 'w', 's', 'n']
        self.assertEqual(actual, expected)
