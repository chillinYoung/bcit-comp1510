'''
COMP 1510 Assignment #1
Young Kim (Set 1E, A01087377)

The first assignment for COMP 1510.
'''


import random


def quotient(dividend, divisor):
    return dividend // divisor


def remainder(dividend, divisor):
    return dividend % divisor


def convert_single_roman(single_int, notation):

    # analized = [prefix, carry_number, quotient, remainder]
    # quotient and remainder is the result dividing single number by 5
    analized = [0, 0, quotient(single_int, 5), remainder(single_int, 5)]

    if analized[3] == 4 and analized[2] == 0:
        analized = [1, 0, 1, 0]
    elif analized[3] == 4 and analized[2] == 1:
        analized = [1, 1, 0, 0]

    result = ""
    for i in range(4):
        result += notation[i] * analized[i]

    return result


def convert_to_roman_numeral(positive_int):
    '''Convert positive integer to roman numeral.

    :param positive_int: positive integer
    :precondition: input number must be a positive integer in range 1 to 10_000
    :postcondition: convert the correct roman numeral
    :return: converted roman numeral in string
    '''

    # notation order → prefix, carry number, quotient, remainder
    # quotient and remainder is the result dividing single number by 5
    notation = [["I", "X", "V", "I"],   # ones (units)
                ["X", "C", "L", "X"],   # tens
                ["C", "M", "D", "C"]]   # hundreds
    result = ""

    single_convert = str(positive_int)
    thousands_convert = 0
    if positive_int >= 1000:
        single_convert = str(positive_int)[-3:]
        thousands_convert = int(str(positive_int)[0:-3])

    for i in range(len(single_convert)):
        single_int = int(single_convert[-(i+1)])
        result = (convert_single_roman(single_int, notation[i]) + result)

    result = ("M" * thousands_convert) + result
    return result

    '''
    Decomposition:
    Pattern matching/data representation:
    Abstraction/generalization:
    Algorithm/automation:
    '''


def colour_mixer():
    '''

    '''
    return


def time_caculator():
    '''

    '''
    return


def compound_interest():
    '''

    '''
    return


def add(a, b):
    return a + b


def is_odd_num(num):
    return (num % 2 == 1)


def rock_paper_scissors():
    '''Rock, paper, scissors game.

    A function that play one round of rock, paper, scissors with computer.
    '''
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


def number_generator():
    '''

    '''
    return


def number_translator():
    '''

    '''
    return


def main():
    '''

    '''

    print(convert_to_roman_numeral(5234))

    # units = ["I", "X", "V", "I"]
    # tens = ["X", "C", "L", "X"]
    # hundreds = ["C", "M", "D", "C"]

    # print(convert_single_roman(9, units))


if __name__ == "__main__":
    main()
