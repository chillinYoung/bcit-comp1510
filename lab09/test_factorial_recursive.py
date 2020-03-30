"""
COMP 1510 202010 Lab 09 - Unit Test
Young Kim (A01087377)

A unit test for the factorial_recursive function in the factorial module.
"""

from unittest import TestCase
from factorial import factorial_recursive


class TestFactorialRecursiveHelper(TestCase):

    def test_factorial_recursive_one(self):
        """Test one."""
        expected = 1
        actual = factorial_recursive(1)[1]
        self.assertEqual(actual, expected)

    def test_factorial_recursive_three(self):
        """Test three."""
        expected = 6
        actual = factorial_recursive(3)[1]
        self.assertEqual(actual, expected)

    def test_factorial_recursive_big_number(self):
        """Test thirty six."""
        expected = 371993326789901217467999448150835200000000
        actual = factorial_recursive(36)[1]
        self.assertEqual(actual, expected)
