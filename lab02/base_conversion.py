# Comp1510 202010 Lab 02
# Young Kim (A01087377)


'''
Base conversion of a nubmer
'''


def remainder(devidend, divisor):
    '''
    The function to get remainder of division.

    :param devidend: the number that will be devided
    :param divisor: the number that does the deviding
    :return: remainder of division result
    '''
    return devidend % divisor


def get_qutients(devidend, divisor, result):
    '''
    The function to get a set of qutients by dividing given values

    :param devidend: the number that will be devided
    :param divisor: the number that does the deviding
    :param result: the variable that has empty string value
    :return: qutients in string
    '''
    if devidend == 0:
        return result

    result += str(remainder(devidend, divisor))
    return get_qutients(devidend // divisor, divisor, result)


def base_conversion():
    '''
    Function to convert a number into a different base number

    :return: converted number in 4 digits
    '''
    base_num = int(input("Enter base number between 2 and 9: "))
    max_num = ((base_num ** 4) - 1)
    print("The maximum number is " + str(max_num))
    decimal_num = int(input("Enter the number to convert: "))

    if decimal_num <= max_num:
        converted_num = ""
        print(get_qutients(decimal_num, base_num, converted_num)[::-1])

    else:
        # input number is more than 4 digits in base number
        print("# ERROR: the number is too big to convert!")


def main():
    '''
    The function to test codes, which is invoked by "if __name__ == '__main__'"
    '''
    base_conversion()


if __name__ == '__main__':
    main()
