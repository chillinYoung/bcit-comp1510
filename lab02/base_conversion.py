# Comp1510 202010 Lab 02
# Young Kim (A01087377)

'''
Base conversion of a nubmer
'''


def base_conversion():
    '''
    Function to convert base number

    :return: converted number in 4 digits
    '''
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
        return (fourth_num + third_num + second_num + first_num)

    else:
        # input number is more than 4 digits in base number
        return "# ERROR: the number is too big to convert!"


def main():
    # to test base_conversion()
    print(base_conversion())
    print()


if __name__ == '__main__':
    main()
