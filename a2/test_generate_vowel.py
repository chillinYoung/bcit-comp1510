"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from dnd import generate_vowel


class TestGenerateVowel(TestCase):

    def test_generate_vowel(self):
        actual = generate_vowel()
        self.assertIn(actual, "aeiouy")

    def test_generate_vowel_length(self):
        actual = len(generate_vowel())
        self.assertEqual(actual, 1)

    def test_generate_vowel_type(self):
        actual = type(generate_vowel())
        self.assertEqual(actual, str)
