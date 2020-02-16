"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)

The unit test for generate_vowel function in the dnd module.
"""

from unittest import TestCase
from dnd import generate_vowel


class TestGenerateVowel(TestCase):

    def test_generate_vowel_correctness(self):
        """Test the correctness of a generated vowel."""
        actual = generate_vowel()
        self.assertIn(actual, "aeiouy")

    def test_generate_vowel_length(self):
        """Test the lenghth of a generated vowel."""
        actual = len(generate_vowel())
        self.assertEqual(actual, 1)

    def test_generate_vowel_type(self):
        """Test the type of a generated vowel."""
        actual = type(generate_vowel())
        self.assertEqual(actual, str)
