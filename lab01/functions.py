# Comp1510 202010 Lab 01
# Young Kim (A01087377)


def format_name(first_name, last_name):

    first_name = first_name.replace(' ', '').title()
    last_name = last_name.replace(' ', '').title()
    return 'The full name is: ' + first_name + ' ' + last_name


def tripler(user_input):
    return user_input * 3
    # print('Result: ' + (user_input * 3))


def this_year():
    year = int((8 * (8 * 8 * 8 - 8) + 8) * 8/(8 + 8))
    print('This year is : ' + str(year))


def base_conversion():

    base_num = int(input("Enter base number between 2 and 9: "))
    max_num = ((base_num ** 4) - 1)
    print("The maximum number is " + str(max_num))
    decimal_num = int(input("Enter the number to convert: "))

    first_num = ""
    second_num = ""
    third_num = ""
    fourth_num = ""

    if decimal_num <= max_num:
        # calculate remainder and store it to variable
        # keep qutient to calculate later one
        first_num = str(decimal_num % base_num)
        qutient = decimal_num // base_num

        if qutient != 0:
            second_num = str(qutient % base_num)
            qutient = qutient // base_num

        if qutient != 0:
            third_num = str(qutient % base_num)
            qutient = qutient // base_num

        if qutient != 0:
            fourth_num = str(qutient % base_num)

        # print final converted number by adding nums reversed
        print(fourth_num + third_num + second_num + first_num)

    else:
        # input number is more than 4 digits in base number
        print("# ERROR: the number is too big to convert!")


if __name__ == '__main__':

    # # to test format_name()
    # input_first = input("Enter your first name: ")
    # input_last = input("Enter your last name: ")
    # print(format_name(input_first, input_last))
    # print()

    # # to test tripler()
    # input_tripler = input("Enter any character or word to repeat: ")
    # print(tripler(input_tripler))
    # print()

    # # to test this_year()
    # this_year()
    # print()

    # to test base_conversion()
    base_conversion()
    print()

