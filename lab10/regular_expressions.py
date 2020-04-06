"""
COMP 1510 202010 Lab 10
Young Kim (A01087377)
"""

import doctest
import re


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
    >>> is_email("ykim222_13kj@bcit.comcomcom")
    False
    """
    email_regex = re.compile(r"\w+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$")
    return True if email_regex.match(address) else False


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
    nakamoto_regex = re.compile(r"[A-Z][a-z]+ Nakamoto$")
    return True if nakamoto_regex.match(name) else False


def is_poker(hand: str) -> bool:
    """Determine if hand is valid poker cards.

    :param hand: 5-character string with each character representing a card
    :precondition: hand must have the charancters among 'akqjt98765432'
    :postcondition: determine if given hand is valid cards for the poker
    :return: a boolean value

    >>> is_poker("55552")
    True
    >>> is_poker("222qq")
    True
    >>> is_poker("2q2q2")
    False
    >>> is_poker("98765")
    True
    >>> is_poker("jjj32")
    True
    >>> is_poker("5544t")
    True
    >>> is_poker("tt874")
    True
    >>> is_poker("t7632")
    True
    >>> is_poker("22333")
    False
    >>> is_poker("77777")
    False
    """
    poker_regex = re.compile(r'''
        # Four of a kind
        ([akqjt2-9a])\1\1\1(?!\1)[akqjt2-9a]$
        # Full house
        |([akqjt2-9a])\2\2(?!\2)([akqjt2-9a])\3$
        # Straight OR High card
        |(?=[akqjt2-9a]{5}$)a?k?q?j?t?9?8?7?6?5?4?3?2?a?$
        # Three of a kind
        |([akqjt2-9a])\4\4(?!\4)([akqjt2-9a])(?!\5)[akqjt2-9a]$
        # Two pair
        |(?:([akqjt2-9a])\6(?!\6)){2}[akqjt2-9a]$
        # One pair
        |([akqjt2-9a])\7(?!\7)([akqjt2-9a])(?!\8)([akqjt2-9a])(?!\9)
        [akqjt2-9a]$
        ''', re.VERBOSE)
    return True if poker_regex.match(hand) else False


def main():
    """Drive the program and the doctest in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
