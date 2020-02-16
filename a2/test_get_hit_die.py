"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from dnd import get_hit_die


class TestGetHitDie(TestCase):

    def test_get_hit_die_barbarian(self):
        actual = get_hit_die("barbarian")
        self.assertEqual(actual, 12)

    def test_get_hit_die_bard(self):
        actual = get_hit_die("bard")
        self.assertEqual(actual, 8)

    def test_get_hit_die_cleric(self):
        actual = get_hit_die("cleric")
        self.assertEqual(actual, 8)

    def test_get_hit_die_druid(self):
        actual = get_hit_die("druid")
        self.assertEqual(actual, 8)

    def test_get_hit_die_fighter(self):
        actual = get_hit_die("fighter")
        self.assertEqual(actual, 10)

    def test_get_hit_die_monk(self):
        actual = get_hit_die("monk")
        self.assertEqual(actual, 8)

    def test_get_hit_die_paladin(self):
        actual = get_hit_die("paladin")
        self.assertEqual(actual, 10)

    def test_get_hit_die_ranger(self):
        actual = get_hit_die("ranger")
        self.assertEqual(actual, 10)

    def test_get_hit_die_rogue(self):
        actual = get_hit_die("rogue")
        self.assertEqual(actual, 8)

    def test_get_hit_die_sorcerer(self):
        actual = get_hit_die("sorcerer")
        self.assertEqual(actual, 6)

    def test_get_hit_die_warlock(self):
        actual = get_hit_die("warlock")
        self.assertEqual(actual, 8)

    def test_get_hit_die_wizard(self):
        actual = get_hit_die("wizard")
        self.assertEqual(actual, 6)
