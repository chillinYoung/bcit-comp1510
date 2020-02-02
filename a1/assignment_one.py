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
    """
    result = ""

    # split given number to (x >= 1000) and (1000 > x)
    thousands_convert = 0
    single_convert = str(positive_int)
    if positive_int >= 1000:
        thousands_convert = int(str(positive_int)[0:-3])
        single_convert = str(positive_int)[-3:]

    # for the split (1000 > x) number, convert every place value from back
    for i in range(len(single_convert)):
        single_int = single_convert[::-1]    # reverse given number
        converted = convert_single_roman(int(single_int[i]), (10 ** i))
        result = converted + result

    # for the split (x >= 1000) number, multiply it to "M"
    result = ("M" * thousands_convert) + result

    return result

    """
    Computational Thinking
        -Decomposition: split each place value and calculate each single number
                        and add each place value again in string. In case of
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
        -Algorithm/automation: converting each place value of the number to the
                        equivalent Roman number, the function can be used for
                        any number of integer digits repeatedly if the proper
                        Roman number notation is given.
    """


def convert_single_roman(single_int, place_value):
    """Convert a single integer to Roman number.

    :param single_int: a single integer between 1 and 9
    :param place_value: the integer that shows place value (e.g. 1, 10, 100)
    :precondition: an single_int must be a positibe single integer between
                    1 and 9, and place value must be the integer which is one
                    of '1, 10, and 100'
    :postcondition: converts the single integer to the correct Roman number
    :return: converted Roman number
    """

    # Roman notation = [prefix, carry number, quotient, remainder]
    # → in order '(1*10^n), (10*10^n), (5*10^n), and (1*10^n)' where n >= 0
    # prefix is for exceptions of the pattern which are 4 and 9
    notation = [["I", "X", "V", "I"],   # ones (units)
                ["X", "C", "L", "X"],   # tens
                ["C", "M", "D", "C"]]   # hundreds

    # analyzed = [prefix, carry_number, quotient, remainder]
    # prefix is for exceptions such as 4 and 9
    analyzed = [0, 0, (single_int // 5), (single_int % 5)]

    # in case of 4 and 9 (exceptions)
    if single_int == 4:
        analyzed = [1, 0, 1, 0]
    elif single_int == 9:
        analyzed = [1, 1, 0, 0]

    result = ""
    for i in range(4):
        position = len(str(place_value)) - 1    # place_value to index
        result += notation[position][i] * analyzed[i]

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
        -Pattern matching/data representation: two of primary colour are mixed
                        to a secondary colour regardless the input order.
        -Algorithm/automation: using list and list operator to check primary
                        colours regardless the order of input.
    """


def time_calculator(seconds):
    """Convert seconds to day, hour, minute, and seconds.

    :param seconds: seconds in positive integer
    :precondition: seconds must be given with only positive integer
    :postcondition: convert seconds to correct day, hour, minute, and seconds

    >>> time_calculator(361)
    0 0 6 1
    >>> time_calculator(777777)
    9 0 2 57
    """
    # time = [day, hour, minute, second] in seconds
    time = [(60 * 60 * 24), (60 * 60), 60, 1]
    result = []
    for t in time:
        result.append(str(seconds // t))    # quotient
        seconds = (seconds % t)             # remainder → re-divide
    print(' '.join(result))

    """
    Computational Thinking
        -Pattern matching/data representation: divide input repeatedly and get
                        quotients.
        -Abstraction/generalization: divide given number (seconds) until it
                        gets 0, and append the quotiont to result list. Combine
                        result list items with join method.
    """


def compound_interest(principal, annual_interest, compounded_nums, years):
    """Calculate compound interest.

    :param principal: principal amount in a float
    :param annual_interest: the annual interest rate in a float
    :param compound_interest: the number of times per year the interest is
                              compounded in an integer
    :param years: the number of years the account will be left alone to grow
    :precondition: principal and annual interest must be given as an float, and
                   compound interest and the number of years must be given as
                   an integer
    :postcondition: calculate correct compound interest added to principal
    :return: the amount of money after the given time

    >>> compound_interest(30000, 0.05, 2, 3)
    34790.8025463867
    >>> compound_interest(135000, 0.3, 5, 30)
    843749557.7619915
    """
    final_balance = (principal * (1 + (annual_interest / compounded_nums))
                     ** (compounded_nums * years))
    return final_balance

    """
    Computational Thinking
        -Abstraction/generalization: express a mathematical formula in the
                        function using python operators.
    """


def rock_paper_scissors():
    """Rock, paper, scissors game.

    A function that play one round of rock, paper, scissors with computer.

    :precondition: the prompt input must be one of 'rock, paper, and scissors'.
    :postcondition: print computer's choice and the play result.
    """
    user_input = (input("Enter the one of the 'Rock, Paper, Scissors': ")
                  .replace(" ", "").capitalize())
    choice_list = ["Rock", "Paper", "Scissors"]
    computer = random.randint(0, 2)

    if user_input not in choice_list:
        print("ERROR: Invalid Input")

    else:
        # change user input to a number (using in)
        user = choice_list.index(user_input)

        # the case for user wins
        if (user - computer == 1) or (user - computer == -2):
            print(f"Computer's choice: {choice_list[computer]}")
            print("You Win!!")

        # the case for user loses
        elif (computer - user == 1) or (computer - user == -2):
            print(f"Computer's choice: {choice_list[computer]}")
            print("You Lose...")

        else:
            print(f"Computer's choice: {choice_list[computer]}")
            print("DRAW")

    """
    Computational Thinking
        -Pattern matching/data representation: smaller number wins for 0 and 2,
                        but bigger number wins for other cases.
        -Algorithm/automation: clear the user input and convert it to a number
                        using list, then compare it to generated random number
                        between 0 and 2. If it is same, draw.
                        If user subtract computer is 1 or -2, user wins.
    """


def number_generator():
    """Generate 6 unique numbers.

    :postcondition: generate unique 6 numbers randomly between 1 and 48
    :return: a list that contains 6 unique numbers
    """
    numbers = random.sample(range(1, 49), 6)
    return sorted(numbers)
    """
    Computational Thinking
        -Abstraction/generalization: use sample method in the random module.
        -Algorithm/automation: get 6 unique number from the range, and return
                        the sorted list.
    """


def number_translator():
    """Translate alphabet to corresponding numbers

    :precondition: user input must be given in the format AAA-AAA-AAAA
    :postcondition: the correctly converted 10-character telephone numbers
                    as integers
    :return: converted integer phone numbers
    """
    orig_tel = input("Enter the 10-character phone numbers in alphabet"
                     " (e.g. ABC-DEF-GHIJ): ").replace(" ", "").upper()
    result = ""
    for tel in orig_tel:
        # 'A' to 'O'
        if ord(tel) in range(65, 80):
            result += str(((ord(tel) - 65) // 3) + 2)
        # 'P, Q, R, S'
        elif ord(tel) in range(80, 84):
            result += "7"
        # 'T, U, V'
        elif ord(tel) in range(84, 87):
            result += "8"
        # 'W, X, Y, Z'
        elif ord(tel) in range(87, 91):
            result += "9"
        # keep dashes
        else:
            result += tel

    return result

    """
    Computational Thinking
        -Pattern matching/data representation: the alphabet has range, and each
                        range of characters corresponds to a specific number.
        -Abstraction/generalization: use ord() to range it, range(65, 80) is
                        converted with mathematical formula, and last of it are
                        converted directly, and store it to result string.
        -Algorithm/automation: for alphabet between A and O,
                        converted number = ((ord(alphabet) - 65) // 3) + 2
                        , and for alphabet after P is directly converted.
    """


def main():
    """
    Test the functions in this module.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
