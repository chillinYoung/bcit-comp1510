"""
COMP 1510 202010 Lab 09 - Unit Test
Young Kim (A01087377)

A unit test for the factorial_recursive_helper function in the factorial
module.
"""

from unittest import TestCase
from factorial import factorial_recursive_helper
from factorial import factorial_recursive


class TestFactorialRecursiveHelper(TestCase):

    def test_factorial_recursive_helper_pass_one(self):
        """Test pass one."""
        expected = factorial_recursive(1)[1]
        actual = factorial_recursive_helper(1)
        self.assertEqual(actual, expected)

    def test_factorial_recursive_helper_pass_three(self):
        """Test pass three."""
        expected = factorial_recursive(3)[1]
        actual = factorial_recursive_helper(3)
        self.assertEqual(actual, expected)

    def test_factorial_recursive_helper_pass_big_number(self):
        """Test pass thirty six."""
        expected = factorial_recursive(36)[1]
        actual = factorial_recursive_helper(36)
        self.assertEqual(actual, expected)

    def test_factorial_recursive_direct_compare_six(self):
        """Test three."""
        expected = 720
        actual = factorial_recursive_helper(6)
        self.assertEqual(actual, expected)
