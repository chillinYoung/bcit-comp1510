"""
COMP 1510 Assignment #1
Young Kim (Set 1E, A01087377)

The first assignment for COMP 1510.
"""


import random
import doctest


def convert_single_roman(single_int, notation):
    """Convert single integer to Roman number.

    :param single_int: a single number to convert to Roman numeral
    :param notation: the list that has 4 Roman alphabets
    :precondition: the list must has 4 strings which are in order
                   '(1*10^n), (10*10^n), (5*10^n), and (1*10^n)' where n <= 0
                   e.g. ["I", "X", "V", "I"] or ["C", "M", "D", "C"]
    :postcondition: converts the single integer (place value)
                    to the correct Roman number
    :return: converted Roman number
    """

    # analized = [prefix, carry_number, quotient, remainder]
    # prefix is for exceptions such as 4 and 9
    analized = [0, 0, (single_int // 5), (single_int % 5)]

    if single_int == 4:
        analized = [1, 0, 1, 0]
    elif single_int == 9:
        analized = [1, 1, 0, 0]

    result = ""
    for i in range(4):
        result += notation[i] * analized[i]

    return result


def convert_to_roman_numeral(positive_int):
    """Convert positive integer to Roman numeral.

    :param positive_int: positive integer
    :precondition: input number must be a positive integer in range 1 to 10_000
    :postcondition: convert the correct Roman numeral
    :return: converted Roman numeral in string

    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    >>> convert_to_roman_numeral(49)
    'XLIX'
    >>> convert_to_roman_numeral(135)
    'CXXXV'
    """

    # Roman notation order → prefix, carry number, quotient, remainder
    # → in order '(1*10^n), (10*10^n), (5*10^n), and (1*10^n)' where n <= 0
    # prefix is for exceptions of the pattern which are 4 and 9
    notation = [["I", "X", "V", "I"],   # ones (units)
                ["X", "C", "L", "X"],   # tens
                ["C", "M", "D", "C"]]   # hundreds
    result = ""

    # split given number to (x >= 1000) and (1000 > x)
    single_convert = str(positive_int)
    thousands_convert = 0
    if positive_int >= 1000:
        single_convert = str(positive_int)[-3:]
        thousands_convert = int(str(positive_int)[0:-3])

    # for the splited (1000 > x) number, convert every place value from back
    for i in range(len(single_convert)):
        single_int = int(single_convert[-(i+1)])
        result = (convert_single_roman(single_int, notation[i]) + result)

    # for the splited (x >= 1000) number, multiply it to "M"
    result = ("M" * thousands_convert) + result
    return result

    """
    Computational Thinking
        -Decomposition: split each place value and calculate each single number
                        and add each palce value again in string. In case of
                        the number over thousand in this assignment, it is
                        simply multiplied to the Roman alphabet.
        -Pattern matching/data representation: The roman numbers have a pattern
                        that is only using three different characters for each
                        place value, and the numbers are the combination of
                        those three characters. Also, the combination has a
                        similar pattern in the number every five and ten times.
        -Abstraction/generalization: make the patterns to a generalized set of
                        numbers so that it can be converted to the numbers of
                        the any place value.
        -Algorithm/automation: converting each place value of the nubmer to the
                        equivalent Roman number, the function can be used for
                        any nubmer of integer digits repeatedly if the proper
                        Roman number notation is given.
    """


def colour_mixer():
    """

    """
    return

    """
    Computational Thinking
        - Decomposition: 
        - Pattern matching/data representation:
        - Abstraction/generalization:
        - Algorithm/automation:
    """


def time_caculator():
    """

    """
    return

    """
    Computational Thinking
        - Decomposition: 
        - Pattern matching/data representation:
        - Abstraction/generalization:
        - Algorithm/automation:
    """


def compound_interest():
    """

    """
    return

    """
    Computational Thinking
        - Decomposition: 
        - Pattern matching/data representation:
        - Abstraction/generalization:
        - Algorithm/automation:
    """


def rock_paper_scissors():
    """Rock, paper, scissors game.

    A function that play one round of rock, paper, scissors with computer.
    """
    # user_choice = (input("Enter the one of the 'Rock, Paper, Scissors': ")
    #                .replace(" ", "").lower())
    # computer_choice = random.randint(0, 2)
    # choice_list = ["rock", "paper", "scissors"]

    # if user_choice not in choice_list:
    #     print("ERROR: Invalid Input:",
    #           "Please enter 'rock' or 'paper' or 'scissors'")
    # else:
    #     user_choice = choice_list.index(user_choice)

    #     if is_odd_num(add(user_choice, computer_choice)):
            


    # elif user_choice == computer_choice:
    #     print("Computer's choice is: %s" % computer_choice,
    #           "Result: DRAW!")

    """
    Computational Thinking
        - Decomposition: 
        - Pattern matching/data representation:
        - Abstraction/generalization:
        - Algorithm/automation:
    """


def number_generator():
    """

    """
    return

    """
    Computational Thinking
        - Decomposition: 
        - Pattern matching/data representation:
        - Abstraction/generalization:
        - Algorithm/automation:
    """


def number_translator():
    """

    """
    return

    """
    Computational Thinking
        - Decomposition: 
        - Pattern matching/data representation:
        - Abstraction/generalization:
        - Algorithm/automation:
    """


def main():
    """Drive the program.

    The tests of the fuctions
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
