"""
COMP 1510 202010 Lab 07b
Young Kim (A01087377)

Unit test for clean_text function of Lab 07b.
"""

from unittest import TestCase
from file_io import clean_text


class TestCleanText(TestCase):
    def test_clean_text_empty(self):
        """Test empty contents given."""
        contents = ""
        expected = []
        actual = clean_text(contents)
        self.assertEqual(actual, expected)

    def test_clean_text_multiple_spaces(self):
        """Test cleaned multiple spaces."""
        contents = "here   is    multiple    spaces"
        expected = ['here', 'is', 'multiple', 'spaces']
        actual = clean_text(contents)
        self.assertEqual(actual, expected)

    def test_clean_text_special_characters(self):
        """Test elimination of the special characters."""
        contents = "$ % ^^^ here&& is@!# special!!** characters() :)"
        expected = ['here', 'is', 'special', 'characters']
        actual = clean_text(contents)
        self.assertEqual(actual, expected)

    def test_clean_text_upper_cases(self):
        """Test cleaned upper cases."""
        contents = "HErE iS THE UppeR CaSE CharaCTERS"
        expected = ['here', 'is', 'the', 'upper', 'case', 'characters']
        actual = clean_text(contents)
        self.assertEqual(actual, expected)

    def test_clean_text_all_upper_special_whitespce_mixed(self):
        """Test totally tainted contents.

        A test that cleans contents tainted with all upper cases, special
        characters, and multiple whitespaces.
        """
        contents = "#$Oh, my, GOD!!    ++TOtally~#@ Tainted@! :(  :(    :("
        expected = ['oh', 'my', 'god', 'totally', 'tainted']
        actual = clean_text(contents)
        self.assertEqual(actual, expected)
