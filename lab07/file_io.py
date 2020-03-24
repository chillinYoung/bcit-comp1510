"""
COMP 1510 202010 Lab 07b
Young Kim (A01087377)
"""

import doctest
import re


def clean_text(string_contents: str) -> list:
    """Clean the text to have only alphabets.

    :param string_contents: the contents as string
    :precondition: string_contents must be given as string
    :postconsition: correctly clean the text to have only alphabets
    :return: the list with cleaned and splited words

    >>> clean_text("PLEASE CLEAN THIS")
    ['please', 'clean', 'this']
    >>> clean_text("hey@@ there## :) hi()*@&$^")
    ['hey', 'there', 'hi']
    >>> clean_text("may          be")
    ['may', 'be']
    >>> clean_text("Almost,,..!@#   THerE(@)($))%   wait....   !!")
    ['almost', 'there', 'wait']
    """
    filtered = re.sub("[^ a-z\n]+", "", string_contents.lower())
    return filtered.split()


def count_words_in_list(words_list: list) -> dict:
    """Create a dictionary with counted words in the given list.

    :param words_list: the list with words
    :precondition: the words_list must be cleaned with clean_text function
            in this module
    :postcondition: correctly create a new dictionary contains counted words
            information
    :return: the dictionary contains counted words

    >>> test_list = []
    >>> count_words_in_list(test_list)
    {}
    >>> test_list = ['almost', 'there', 'wait']
    >>> count_words_in_list(test_list)
    {'almost': 1, 'there': 1, 'wait': 1}
    >>> test_list = ['hello', 'hello', 'hello', 'hi']
    >>> count_words_in_list(test_list)
    {'hello': 3, 'hi': 1}
    """
    word_counts = dict()
    for word in words_list:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_most_top_ten(word_counts: dict):
    """Print the most top ten words.

    :param word_counts: the dictionary with counted words information
    :precondition: the wood_counts dict must be correctly formed with
            count_words_in_list function in this module
    :postcondition: correctly print the most top ten words

    >>> test_dict = {'hello': 3, 'hi': 1}
    >>> print_most_top_ten(test_dict)
    hello - 3
    hi - 1

    >>> test_dict = {'test': 1, 'a': 3, 'the': 7, 'this': 2, 'hi': 10,
    ...              'please': 7, 'no': 2, 'more': 15, 'moving': 1,
    ...              'apple': 9, 'orange': 17, 'and': 27, 'today': 3,
    ...              'one': 1, 'two': 2}
    >>> print_most_top_ten(test_dict)
    and - 27
    orange - 17
    more - 15
    hi - 10
    apple - 9
    the - 7
    please - 7
    today - 3
    a - 3
    two - 2
    """
    count_list = [(value, key) for key, value in word_counts.items()]
    count_list.sort(reverse=True)

    for item in count_list[0:10]:
        print(f"{item[1]} - {item[0]}")


def main():
    """Drive the program and the doctest in this module.

    :raise FileNotFoundError: if the file name input by the user is not founded
    """
    doctest.testmod()

    # run the program
    file_choose = input("Please enter the name of a file to open: ")
    try:
        with open(file_choose) as text_file:
            contents = text_file.read().lower()
    except FileNotFoundError as fnfe:
        print(f"# {fnfe}")
    else:
        words = clean_text(contents)
        word_counts = count_words_in_list(words)
        print_most_top_ten(word_counts)


if __name__ == "__main__":
    main()
