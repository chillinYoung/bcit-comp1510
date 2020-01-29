"""
COMP 1510 Lab 03
Young Kim (Set 1E, A01087377)

A function to sort the list elements.
"""


import doctest


def dijkstra(list):
    """Sort the list elements.

    In order to red, white, and blue

    :param list: the list that has red, white or blue as the elements
    :precondition: the list that only containes red, white, or blue elements
                   must be given.
    :postcondition: sort the list in order 'red, white, and blue'

    >>> list = ['red']
    >>> dijkstra(list)
    >>> print(list)
    ['red']
    >>> list = ['blue', 'white', 'red']
    >>> dijkstra(list)
    >>> print(list)
    ['red', 'white', 'blue']
    >>> list = ['red', 'red', 'red']
    >>> dijkstra(list)
    >>> print(list)
    ['red', 'red', 'red']
    >>> list = ['red', 'white', 'blue']
    >>> dijkstra(list)
    >>> print(list)
    ['red', 'white', 'blue']
    >>> list = ['white', 'blue', 'red', 'red', 'white', 'blue', 'white', 'blue', 'white', 'blue', 'red', 'white']
    >>> dijkstra(list)
    >>> print(list)
    ['red', 'red', 'red', 'white', 'white', 'white', 'white', 'white', 'blue', 'blue', 'blue', 'blue']
    >>> list = ['red', 'blue', 'red']
    >>> dijkstra(list)
    >>> print(list)
    ['red', 'red', 'blue']
    """
    list.sort()
    if 'blue' in list:
        count = list.count('blue')
        for i in range(count + 1):
            list.remove('blue')
            list.append('blue')


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
