"""
COMP 1510 202010 Lab 10
Young Kim (A01087377)
"""

import doctest


def is_email(address: str) -> bool:
    """Determine email address.

    :param address: an email address as a string
    :precondition: address must be a string type
    :postcondition: determine if given email address has the right format
    :return: a boolean value

    >>> is_email("ykim_12345@bcit.ca")
    True
    >>> is_email("ykim001.bcit.ca")
    False
    >>> is_email("ykim111@bcitca")
    False
    >>> is_email("ykim12345!@bcit.ca")
    False
    >>> is_email("ykim333@bc00it.com")
    True
    """
    pass


def is_nakamoto(name: str) -> bool:
    """Determine the last name is Nakamoto.

    :param name: a full name as a string
    :precondition: name must be a string type
    :postcondition: determine if given full name's last name is 'Nakamoto'
    :return: a boolean value

    >>> is_nakamoto("Satoshi Nakamoto")
    True
    >>> is_nakamoto("Mr. Nakamoto")
    False
    >>> is_nakamoto("satoshi Nakamoto")
    False
    >>> is_nakamoto("Nakamoto")
    False
    >>> is_nakamoto("Satoshi nakamoto")
    False
    """
    pass


def is_poker(hand: str) -> bool:
    """

    :param hand: 5-character string with each character representing a card
    :precondition: hand must have the charancters among 'akqjt23456789'
    :postcondition: determine if given hand is valid cards for the poker
    :return: a boolean value
    """
    pass


def main():
    """Drive the program and the doctest in this module."""
    pass


if __name__ == "__main__":
    main()
