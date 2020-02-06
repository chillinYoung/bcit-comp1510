"""
COMP 1510 202010 Quiz 04
Young Kim(A01087377)
Li Ting Yang (Lily)
"""


import doctest


def statistics(number_list):
    """Give statistics of number list.

    :param number_list: the list with numbers
    :precondition: the list must have only numbers in it
    :postcondition: show the statistics of the given number list in order to
                    [num_of_items, min_num, max_num, average, spread]
    :return: a list that has 5 different statistics

    >>> statistics([])
    [None, None, None, None, None]
    >>> statistics([0])
    [1, 0, 0, 0.0, 0]
    >>> statistics([15])
    [1, 15, 15, 15.0, 0]
    >>> statistics([1, 1, 1])
    [3, 1, 1, 1.0, 0]
    >>> statistics([1, 2, 3, 4, 5])
    [5, 1, 5, 3.0, 4]
    >>> statistics([5.0, 3, 15, 21.7, 5, 2, 1, 5.77])
    [8, 1, 21.7, 7.30875, 20.7]
    """
    if not number_list:
        result = [None, None, None, None, None]
    else:
        num_of_items = len(number_list)
        min_num = min(number_list)
        max_num = max(number_list)
        average = sum(number_list) / num_of_items
        spread = max_num - min_num
        result = [num_of_items, min_num, max_num, average, spread]

    return result


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
