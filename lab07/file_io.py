"""
COMP 1510 202010 Lab 07b
Young Kim (A01087377)
"""

import doctest
import re


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
        filtered = re.sub("[^ a-z\n]+", "", contents)
        words = filtered.split()

        word_counts = dict()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        count_list = [(value, key) for key, value in word_counts.items()]
        count_list.sort(reverse=True)
        for item in count_list[0:10]:
            print(f"{item[1]} - {item[0]}")


if __name__ == "__main__":
    main()
