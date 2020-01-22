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
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        result = ''.join(random.sample(alphabets, length))
        return result.title()

    else:
        return None


def main():
    print("2 rolls with 6 sides: " + str(roll_die(2, 6)))
    print("4 rolls with 4 sides: " + str(roll_die(4, 4)))
    print()
    print("create name with 3 length: " + create_name(3))
    print("create name with 7 length: " + create_name(7))


if __name__ == "__main__":
    main()
