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


def main():
    """Drive the doctest in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
