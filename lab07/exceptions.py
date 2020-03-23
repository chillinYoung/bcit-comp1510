"""
COMP 1510 202010 Lab 07a
Young Kim (A01087377)
"""

import doctest


def heron(num: int) -> float:
    """Return the square root.

    :param num: a positive integer
    :precondition: the num must be a positive integer
    :postcondition: return a square root as a float
    :raise ZeroDivisionError: if num is negative one
    :return: a square root as a float

    >>> heron(0)
    0
    >>> heron(4)
    2.000000000000002
    >>> heron(17)
    4.123105625617805
    """
    TOL = 0.0000001
    approx = num
    try:
        while abs(approx ** 2 - num) > TOL:
            approx = (approx + num / approx) / 2
        return approx
    except ZeroDivisionError as zde:
        print(f"# Calculation Error: negative number input")
        return -1


def find_an_even(input_list: list) -> int:
    """Return the first even number in input_list.

    :param input_list: a list of integers
    :precondition: input_list must be a list of integer
    :postcondition: return the first even number in input_list
    :raise ValueError: if input_list does not contain an even number
    :return: first even number in input_list

    >>> test_list = [3, 1, 4, 6, 2]
    >>> find_an_even(test_list)
    2
    >>> test_list = [3, 1, 5, 9, 10, 7, 11]
    >>> find_an_even(test_list)
    10
    """
    even_list = [num for num in input_list if num % 2 == 0]
    try:
        return min(even_list)
    except ValueError as ve:
        print(f"# Not Found Error: no even numbers in the list")


def main():
    """Drive the doctest in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
