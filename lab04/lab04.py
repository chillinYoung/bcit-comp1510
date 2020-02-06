"""
COMP 1510 202010 Lab 04
Young Kim (A01087377)
"""

import math
import doctest


def eratosthenes(upperbound):
    """Give prime numbers in a range.

    :param upperbound: a positive integer
    :precondition: the number must be a positive integer
    :postcondition: gives prime numbers in the range of given positive integer
    :return: a list with prime numbers in the given range, inclusive

    >>> eratosthenes(47)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> eratosthenes(1)
    []
    >>> eratosthenes(2)
    [2]
    """
    nums = list(range(2, upperbound + 1))
    # to get range between 2 to root of upperbound, inclusive
    check_nums = range(2, math.floor(upperbound ** 0.5) + 1)

    for check_num in check_nums:
        copy_nums = nums    # shallow copy to refresh it
        for num in copy_nums:
            if (num % check_num == 0) and (num != check_num):
                nums.remove(num)

    return nums


def cash_money(canadian_money):
    """Calculate the fewest bill and coins.

    A function that gives a list with the numbers of how many of each bill and
    coins are required to be the fewest.

    :param canadian_money: a positive floating point number
    :precondition: the number must be a positive floating point number that has
                    at most 2 decimal places
    :postcondition: a list that shows how many of each denomanation are
                    required for given amount of money
    :return: a list with the numbers broken down by denominations

    >>> cash_money(66.53)
    [0, 1, 0, 1, 1, 0, 1, 2, 0, 0, 3]
    >>> cash_money(188.41)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> cash_money(0.01)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    """
    denominations = (100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01)
    FLOAT_HANDLE = 100    # convert to int to avoid floating-point error
    dividend = int(canadian_money * FLOAT_HANDLE)
    result = []

    for denomination in denominations:
        denomination = int(denomination * FLOAT_HANDLE)    # convert to int
        result.append(dividend // denomination)
        dividend = dividend % denomination
    return result


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
