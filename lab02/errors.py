# Comp1510 202010 Lab 02
# Young Kim (A01087377)


'''
Intentionally generated errors
'''


def main():
    '''
    main function to excute some error scripts
    '''

    # ZeroDivisionError
    will_error = 3 / 0

    # IndexError
    say_hi = "Hello"
    print(say_hi[5])

    new_list = [0, 1, 2, 3, 4, 5]
    print(new_list[10])

    # TypeError
    type_error_1 = '5' + 5

    text = "example"
    type_error_2 = "This is a(n) %d." % text


if __name__ == "__main__":
    main()
