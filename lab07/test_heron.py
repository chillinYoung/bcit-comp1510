"""
COMP 1510 202010 Lab 07a
Young Kim (A01087377)

Unit test for heron function.
"""

from unittest import TestCase
from exceptions import heron


class TestHeron(TestCase):
    def test_heron_zero(self):
        """Test zero."""
        expected = 0
        actual = heron(0)
        self.assertEqual(actual, expected)

    def test_heron_one(self):
        """Test one."""
        expected = 1
        actual = heron(1)
        self.assertEqual(actual, expected)

    def test_heron_seventeen(self):
        """Test seventeen."""
        expected = 4.1231056
        actual = heron(17)
        self.assertAlmostEqual(actual, expected)

    def test_heron_negative_one(self):
        """Test negative_one."""
        expected = -1
        actual = heron(-1)
        self.assertEqual(actual, expected)
