# Comp1510 202010 Lab 02
# Young Kim (A01087377)


'''

'''

import random


def roll_die(number_of_rolls, number_of_sides):

    if number_of_rolls > 0 and number_of_sides > 0:
        result = random.randint(number_of_rolls, (number_of_rolls * number_of_sides))
    else:
        result = 0
    return result


def create_name(length):

    if length > 0:
        


def main():
    # print(roll_die(2, 6))




if __name__ == "__main__":
    main()
