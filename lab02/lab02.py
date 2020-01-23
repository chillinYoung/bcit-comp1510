# Comp1510 202010 Lab 02
# Young Kim (A01087377)


'''
Simple genarating program that can roll die and create a name
'''


import random


def roll_die(number_of_rolls, number_of_sides):
    '''
    The function to get the total score of rolling die

    :param number_of_rolls: the number of how much roll the die
    :param number_of_sides: the number of sides of the die
    :return: the total score of rolling die
    '''
    if number_of_rolls > 0 and number_of_sides > 0:
        result = random.randint(number_of_rolls,
                                (number_of_rolls * number_of_sides))
    else:
        result = 0
    return result


def create_name(length):
    '''
    The function to create a name with the given length

    :param length: the length to create name
    :return: randomly chosen titled letters with the given length
    '''
    if length > 0:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        result = ''.join(random.sample(alphabets, length))
        return result.title()

    else:
        return None


def main():
    '''
    Drives the program
    '''
    print("--- Let's roll the die! ---")
    rolls = int(input("Enter the numbers of rolls: "))
    sides = int(input("Enter the numbers of sides of the die: "))
    print("The total score you've got is " + str(roll_die(rolls, sides)))
    print()

    print("--- Let's generate some letters! ---")
    length = int(input("Enter the number of length: "))
    print("The genarated name is: " + create_name(length))


if __name__ == "__main__":
    main()
