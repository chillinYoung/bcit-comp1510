"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for validate_move function in the character module.
"""

from unittest import TestCase
from unittest.mock import patch
from character import validate_move
from game_map import map_init


class TestValidateMove(TestCase):

    def test_validate_move_return_false_move_north(self):
        map_info = map_init(5, 5)
        char = {'Name': 'Woody',
                'Pos_x': 4,
                'Pos_y': 4}
        move_direction = 'n'
        self.assertFalse(validate_move(map_info, char, move_direction))

    def test_validate_move_return_true_move_north(self):
        map_info = map_init(5, 5)
        char = {'Name': 'Woody',
                'Pos_x': 4,
                'Pos_y': 3}
        move_direction = 'n'
        self.assertTrue(validate_move(map_info, char, move_direction))

    def test_validate_move_return_true_move_east(self):
        map_info = map_init(5, 5)
        char = {'Name': 'Woody',
                'Pos_x': 3,
                'Pos_y': 4}
        move_direction = 'e'
        self.assertTrue(validate_move(map_info, char, move_direction))

    def test_validate_move_return_false_move_east(self):
        map_info = map_init(5, 5)
        char = {'Name': 'Woody',
                'Pos_x': 4,
                'Pos_y': 4}
        move_direction = 'e'
        self.assertFalse(validate_move(map_info, char, move_direction))

    def test_validate_move_return_false_move_south(self):
        map_info = map_init(5, 5)
        char = {'Name': 'Woody',
                'Pos_x': 4,
                'Pos_y': 0}
        move_direction = 's'
        self.assertFalse(validate_move(map_info, char, move_direction))

    def test_validate_move_return_true_move_south(self):
        map_info = map_init(5, 5)
        char = {'Name': 'Woody',
                'Pos_x': 4,
                'Pos_y': 1}
        move_direction = 's'
        self.assertTrue(validate_move(map_info, char, move_direction))

    def test_validate_move_return_false_move_west(self):
        map_info = map_init(5, 5)
        char = {'Name': 'Woody',
                'Pos_x': 0,
                'Pos_y': 0}
        move_direction = 'w'
        self.assertFalse(validate_move(map_info, char, move_direction))

    def test_validate_move_return_true_move_west(self):
        map_info = map_init(5, 5)
        char = {'Name': 'Woody',
                'Pos_x': 1,
                'Pos_y': 1}
        move_direction = 'w'
        self.assertTrue(validate_move(map_info, char, move_direction))
