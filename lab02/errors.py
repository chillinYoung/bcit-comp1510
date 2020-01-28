"""
Comp1510 202010 Lab 02
Young Kim (A01087377)

Intentionally generated errors
"""


def main():
    """Execute some error scripts.

    A function that occurs ZeroDivisionError, IndexError, and TypeError.
    """

    # ZeroDivisionError
    zero_div_error = 3 / 0

    # IndexError
    index_error_1 = "Hello"
    print(index_error_1[5])

    quiz = "quiz"
    score = "score"
    index_error_2 = "I got a good {0} in the last {2}" .format(quiz, score)

    # TypeError
    type_error_1 = '5' + 5

    text = "example"
    type_error_2 = "This is a(n) %d." % text


if __name__ == "__main__":
    main()
