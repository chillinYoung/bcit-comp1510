"""
COMP 1510 202010 Lab 04 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from lab04 import cash_money


class Test(TestCase):

    def test_cash_money_zero(self):
        """Test an zero argument"""

        argument = 0
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "Input is zero.")

    def test_cash_money_decimals(self):
        """Test a number with more than three decimal places"""

        argument = 123.35903
        # it is same result with 'argument = 123.35'
        expected = [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input has more than 3 decimal places.")

    def test_cash_money_no_decimals(self):
        """Test a number without decimal places"""

        argument = 777
        # it is same result with 'argument = 777.00'
        expected = [7, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input doesn't have decimal places.")

    def test_cash_money_negative(self):
        """Test an negative value"""

        argument = -144.03
        expected = [-2, 1, 0, 0, 1, 0, 0, 3, 2, 0, 2]
        self.assertEqual(expected, cash_money(argument),
                         "The input is a negative number.")

    def test_cash_money_smallest(self):
        """Test the smallest input number"""

        argument = 0.01
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(expected, cash_money(argument),
                         "The smallest input that can be converted.")

    def test_cash_money_biggest(self):
        """Test a big input number"""

        argument = 4158667293863.59
        expected = [41586672938, 1, 0, 1, 0, 1, 1, 2, 0, 1, 4]
        self.assertEqual(expected, cash_money(argument),
                         "The input is a big number.")
