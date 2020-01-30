"""
COMP 1510 Assignment #1
Young Kim (Set 1E, A01087377)

The first assignment for COMP 1510.
"""


import random
import doctest


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


def colour_mixer():
    """Mix two primary colours.

    :precondition: user must input two different primary colours
    :postcondition: the correct secondary colour
    """
    print("Primary Colours: Red, Yellow, Blue")
    colour1 = input("Enter the first primary colour to mix: ").strip().lower()
    colour2 = input("Enter the second primary colour to mix: ").strip().lower()

    orange = ["red", "yellow"]
    green = ["yellow", "blue"]
    purple = ["red", "blue"]

    if colour1 == colour2:
        print("Error: you entered same colour.")
    elif (colour1 in orange) and (colour2 in orange):
        print("Orange")
    elif (colour1 in green) and (colour2 in green):
        print("Green")
    elif (colour1 in purple) and (colour2 in purple):
        print("Purple")
    else:
        print("Error: invalid input.")

    """
    Computational Thinking
        -Decomposition: get user input, compare/validate data, and print
                        correct secondary colour.
        -Pattern matching/data representation: two of primary colour are mixed
                        to a secondary colour regardless the input order.
        -Abstraction/generalization: print result color after two prompt input
                        colours are validated and checked.
        -Algorithm/automation: using list and list operator to check primary
                        colours regardless the order of input.
    """


def time_calculator(seconds):
    """Convert seconds to day, hour, minute, and seconds.

    :param seconds: seconds in positive integer
    :precondition: seconds must be given with only positive integer
    :postcondition: convert seconds to correct day, hour, minute, and seconds

    >>> time_calculator(92464)
    '1 1 41 4'
    >>> time_calculator(361)
    '0 0 6 1'
    >>> time_calculator(777777)
    '9 0 2 57'
    """
    # time = [day, hour, minute, second] in seconds
    time = [(60 * 60 * 24), (60 * 60), 60, 1]
    result = []
    for t in time:
        result.append(str(seconds // t))
        seconds = (seconds % t)
    print(' '.join(result))

    """
    Computational Thinking
        -Decomposition: divide seconds until it gets 0, store data, and print
                        result in given format.
        -Pattern matching/data representation: divide input repeatedly and get
                        quotients.
        -Abstraction/generalization: divide given number (seconds) until it
                        gets 0, and every quotient is part of a result
                        sequentially.
        -Algorithm/automation: divide given number by each converted time in
                        the time list, and append the result to result list.
                        Combine result list items with join method.
    """


def compound_interest():
    """

    """
    return

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation:
        -Abstraction/generalization:
        -Algorithm/automation:
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
        -Decomposition: 
        -Pattern matching/data representation:
        -Abstraction/generalization:
        -Algorithm/automation:
    """


def number_generator():
    """

    """
    return

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation:
        -Abstraction/generalization:
        -Algorithm/automation:
    """


def number_translator():
    """

    """
    return

    """
    Computational Thinking
        -Decomposition: 
        -Pattern matching/data representation:
        -Abstraction/generalization:
        -Algorithm/automation:
    """


def main():
    """Drive the program.

    The tests of the fuctions
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
