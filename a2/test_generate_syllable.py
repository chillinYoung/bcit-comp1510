"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)

The unit test for generate_syllable function in the dnd module.
"""

from unittest import TestCase
from dnd import generate_syllable


class TestGenerateSyllable(TestCase):

    def test_generate_syllable_length(self):
        """Test the lenghth of generated syllable."""
        actual = len(generate_syllable())
        self.assertEqual(actual, 2)

    def test_generate_syllable_type(self):
        """Test the type of generated syllable."""
        actual = type(generate_syllable())
        self.assertEqual(actual, str)

    def test_generate_syllable_consonant_first_position(self):
        """Test if the first position of the syllable is consonant."""
        actual = generate_syllable()[0]
        self.assertIn(actual, "bcdfghjklmnpqrstvwxyz")

    def test_generate_syllable_vowel_second_position(self):
        """Test if the second position of the syllable is vowel."""
        actual = generate_syllable()[1]
        self.assertIn(actual, "aiueoy")
