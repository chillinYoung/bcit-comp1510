"""
COMP 1510 Suprise Quiz 3

Young Kim
Li Ting Yang (Lily)
"""


import doctest


def average_grade(grade1, grade2, grade3, grade4):
    """ Calculate average grade.

    :param grade1: an integer number between 1 and 100
    :param grade2: an integer number between 1 and 100
    :param grade3: an integer number between 1 and 100
    :param grade4: an integer number between 1 and 100
    :precondition: arguments must be an integer
    :postcondition: the correct average of best 3 grades as a float
    :return: the average of the best 3 grades as a float

    >>> average_grade(85, 90, 75, 88)
    87.66666666666667
    >>> average_grade(66, 66, 77, 77)
    73.33333333333333
    """
    grades = [grade1, grade2, grade3, grade4]
    grades.remove(min(grades))
    return float(sum(grades) / 3)


def get_index(sentence, substring):
    """Give index of the substring.

    :param sentence: the string sentence
    :param substring: the substring to search in the sentence
    :precondition: the arguments must be strings
    :postcondition: give the position as an index of substring in the sentence
    :return: the index of the substring in the sentence

    >>> get_index("Hello world", "world")
    6
    >>> get_index("Hi I am Young Kim", "ung")
    10
    """
    return sentence.find(substring)


def main():
    """
    Drive the program.
    """
    doctest.testmod()

    given_list = [4353, 2314, 2956, 3382, 9362, 3900]
    given_list.remove(3382)
    given_list.index(9362)
    given_list.insert(given_list.index(9362) + 1, 4499)
    given_list.append(5566)
    given_list.append(1830)
    given_list.reverse()
    given_list.sort()


if __name__ == "__main__":
    main()
