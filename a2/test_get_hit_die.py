"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from dnd import get_hit_die


class TestGetHitDie(TestCase):

    def test_get_hit_die_barbarian(self):
        """Test a hit die number of barbarian."""
        actual = get_hit_die("barbarian")
        self.assertEqual(actual, 12)

    def test_get_hit_die_bard(self):
        """Test a hit die number of bard."""
        actual = get_hit_die("bard")
        self.assertEqual(actual, 8)

    def test_get_hit_die_cleric(self):
        """Test a hit die number of cleric."""
        actual = get_hit_die("cleric")
        self.assertEqual(actual, 8)

    def test_get_hit_die_druid(self):
        """Test a hit die number of druid."""
        actual = get_hit_die("druid")
        self.assertEqual(actual, 8)

    def test_get_hit_die_fighter(self):
        """Test a hit die number of fighter."""
        actual = get_hit_die("fighter")
        self.assertEqual(actual, 10)

    def test_get_hit_die_monk(self):
        """Test a hit die number of monk."""
        actual = get_hit_die("monk")
        self.assertEqual(actual, 8)

    def test_get_hit_die_paladin(self):
        """Test a hit die number of paladin."""
        actual = get_hit_die("paladin")
        self.assertEqual(actual, 10)

    def test_get_hit_die_ranger(self):
        """Test a hit die number of ranger."""
        actual = get_hit_die("ranger")
        self.assertEqual(actual, 10)

    def test_get_hit_die_rogue(self):
        """Test a hit die number of rogue."""
        actual = get_hit_die("rogue")
        self.assertEqual(actual, 8)

    def test_get_hit_die_sorcerer(self):
        """Test a hit die number of sorcerer."""
        actual = get_hit_die("sorcerer")
        self.assertEqual(actual, 6)

    def test_get_hit_die_warlock(self):
        """Test a hit die number of warlock."""
        actual = get_hit_die("warlock")
        self.assertEqual(actual, 8)

    def test_get_hit_die_wizard(self):
        """Test a hit die number of wizard."""
        actual = get_hit_die("wizard")
        self.assertEqual(actual, 6)
