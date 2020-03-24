"""
COMP 1510 202010 Lab 07b
Young Kim (A01087377)
"""

import doctest
import re


def clean_text(string_contents: str) -> list:
    """

    :return: the list with cleaned and splited words
    """
    filtered = re.sub("[^ a-z\n]+", "", string_contents)
    return filtered.split()


def count_words_in_list(words_list: list) -> dict:
    """
    """
    word_counts = dict()
    for word in words_list:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_most_top_ten(word_counts: dict):
    """
    """
    count_list = [(value, key) for key, value in word_counts.items()]
    count_list.sort(reverse=True)

    for item in count_list[0:10]:
        print(f"{item[1]} - {item[0]}")


def main():
    """Drive the program and the doctest in this module."""
    doctest.testmod()

    # file_choose = input("Please enter the name of a file to open: ")
    file_choose = "moby_dick.txt"

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
