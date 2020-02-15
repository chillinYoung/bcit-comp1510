"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from dnd import roll_die


class TestRollDie(TestCase):

    def test_roll_die_once_one_sided(self):
        expected = 1
        actual = roll_die(1, 1)
        self.assertEqual(expected, actual)

    def test_roll_die_once_six_sided(self):
        actual = roll_die(1, 6)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 6)

    def test_roll_die_once_eight_sided(self):
        actual = roll_die(1, 8)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 8)

    def test_roll_die_once_ten_sided(self):
        actual = roll_die(1, 10)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 10)

    def test_roll_die_once_twelve_sided(self):
        actual = roll_die(1, 12)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 12)

    def test_roll_die_once_twenty_sided(self):
        actual = roll_die(1, 20)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 20)

    def test_roll_die_tripple_times_six_sided(self):
        actual = roll_die(3, 6)
        self.assertGreaterEqual(actual, 3)
        self.assertLessEqual(actual, 18)
