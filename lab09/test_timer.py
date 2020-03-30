"""
COMP 1510 202010 Lab 09 - Unit Test
Young Kim (A01087377)

A unit test for the timer function in the factorial module.
"""

from unittest import TestCase
from unittest.mock import patch
from factorial import timer
from factorial import factorial_iterative
import time


class TestTimer(TestCase):

    @patch('time.perf_counter', side_effect=[6.328844335, 11.039815492])
    def test_timer_time_calculation(self, mock_time_counter):
        """Test time calculation."""
        expected = 4.710971157
        actual = factorial_iterative(5)[0]
        self.assertEqual(actual, expected)

    def test_timer_return_calculation_result(self):
        """Test returning factorial calculation result."""
        expected = 720
        actual = factorial_iterative(6)[1]
        self.assertEqual(actual, expected)

    @patch('time.perf_counter', side_effect=[2.511, 5.141])
    def test_timer_return_value(self, mock_time_counter):
        """Test correct return value and form."""
        expected = (2.63, 120)
        actual = factorial_iterative(5)
        self.assertEqual(actual, expected)
