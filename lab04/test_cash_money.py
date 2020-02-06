"""
COMP 1510 202010 Lab 04 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from lab04 import cash_money


class TestCashMoney(TestCase):

    def test_cash_money_zero(self):
        """Test an zero argument"""

        argument = 0.00
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "Input is zero.")

    def test_cash_money_penny(self):
        """Test the input penny"""

        argument = 0.01
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(expected, cash_money(argument),
                         "The input is penny.")

    def test_cash_money_two_pennies(self):
        """Test the input two pennies"""

        argument = 0.02
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
        self.assertEqual(expected, cash_money(argument),
                         "The input is 0.02.")

    def test_cash_money_nickel(self):
        """Test the input nickel"""

        argument = 0.05
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is nickel.")

    def test_cash_money_dime(self):
        """Test the input dime"""

        argument = 0.10
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is dime.")

    def test_cash_money_quarter(self):
        """Test the input quarter"""

        argument = 0.25
        expected = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is quarter.")

    def test_cash_money_loonie(self):
        """Test the input loonie"""

        argument = 1.00
        expected = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is loonie.")

    def test_cash_money_loonie_nickel(self):
        """Test the input loonie and nickel"""

        argument = 1.05
        expected = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is 1.05.")

    def test_cash_money_toonie(self):
        """Test the input toonie"""

        argument = 2.00
        expected = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is toonie.")

    def test_cash_money_fin(self):
        """Test the input fin"""

        argument = 5.00
        expected = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is fin.")

    def test_cash_money_ten(self):
        """Test the input ten dollars"""

        argument = 10.00
        expected = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is ten dollars.")

    def test_cash_money_ten_with_twenty_seven(self):
        """Test the input ten with twenty seven"""

        argument = 10.27
        expected = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2]
        self.assertEqual(expected, cash_money(argument),
                         "The input is 10.27.")

    def test_cash_money_twenty(self):
        """Test the input twenty"""

        argument = 20.00
        expected = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is 20.00.")

    def test_cash_money_fifty(self):
        """Test the input fifty"""

        argument = 50.00
        expected = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is 50.00.")

    def test_cash_money_hundred(self):
        """Test the input hundred"""

        argument = 100.00
        expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, cash_money(argument),
                         "The input is 100.00.")

    def test_cash_money_hundred_with_fifty_seven(self):
        """Test the input hundred with fifty seven"""

        argument = 100.57
        expected = [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 2]
        self.assertEqual(expected, cash_money(argument),
                         "The input is 100.57.")

    def test_cash_money_sum_of_nominations(self):
        """Test the input the sum of nominations"""

        argument = 188.41
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(expected, cash_money(argument),
                         "The input is the sum of nominations.")

    def test_cash_money_big(self):
        """Test a big input number"""

        argument = 4158667293863.59
        expected = [41586672938, 1, 0, 1, 0, 1, 1, 2, 0, 1, 4]
        self.assertEqual(expected, cash_money(argument),
                         "The input is a big number.")
