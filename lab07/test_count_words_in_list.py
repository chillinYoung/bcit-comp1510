"""
COMP 1510 202010 Lab 07b
Young Kim (A01087377)

Unit test for count_words_in_list function of Lab 07b.
"""

from unittest import TestCase
from file_io import count_words_in_list


class TestCountWordsInList(TestCase):
    def test_count_words_in_list_empty(self):
        """Test an empty list."""
        test_list = []
        expected = dict()
        actual = count_words_in_list(test_list)
        self.assertEqual(actual, expected)

    def test_count_words_in_list_no_same_words(self):
        """Test the list with only unique words."""
        test_list = ['what', 'is', 'the', 'meaning', 'of', 'unique']
        expected = {'what': 1, 'is': 1, 'the': 1, 'meaning': 1,
                    'of': 1, 'unique': 1}
        actual = count_words_in_list(test_list)
        self.assertEqual(actual, expected)

    def test_count_words_in_list_all_same_words(self):
        """Test the list with all same words."""
        test_list = ['hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi']
        expected = {'hi': 7}
        actual = count_words_in_list(test_list)
        self.assertEqual(actual, expected)

    def test_count_words_in_list_mixed_words(self):
        """Test mixed words."""
        test_list = ['vary', 'very', 'hungry', 'hungry', 'hungry', 'pie']
        expected = {'vary': 1, 'very': 1, 'hungry': 3, 'pie': 1}
        actual = count_words_in_list(test_list)
        self.assertEqual(actual, expected)
