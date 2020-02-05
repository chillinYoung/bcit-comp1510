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
    check_nums = range(2, math.floor(upperbound ** 0.5) + 1)

    for check_num in check_nums:
        copy_nums = nums
        for num in copy_nums:
            if (num % check_num == 0) and (num != check_num):
                nums.remove(num)

    return nums


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
