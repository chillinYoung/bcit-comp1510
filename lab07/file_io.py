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
    """
    filtered = re.sub("[^ a-z\n]+", "", string_contents)
    return filtered.split()


def count_words_in_list(words_list: list) -> dict:
    """Create a dictionary with counted words in the given list.

    :param words_list: the list with words
    :precondition: the words_list must be cleaned with clean_text function
            in this module
    :postcondition: correctly create a new dictionary contains counted words
            information
    :return: the dictionary contains counted words
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
