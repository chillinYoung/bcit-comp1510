"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)

The unit test for generate_name function in the dnd module.
"""

from unittest import TestCase
from dnd import generate_name


class TestGenerateName(TestCase):

    def test_generate_name_length(self):
        """Test the lenghth of generated name."""
        actual = len(generate_name(5))
        self.assertEqual(actual, 10)

    def test_generate_name_type(self):
        """Test the type of generated name."""
        actual = type(generate_name(5))
        self.assertEqual(actual, str)

    def test_generate_name_consonant_first_position(self):
        """Test if the first position of name is uppercase consonant."""
        actual = generate_name(5)[0]
        self.assertIn(actual, "BCDFGHJKLMNPQRSTVWXYZ")

    def test_generate_name_vowel_second_position(self):
        """Test if the second position of name is lowercase vowel."""
        actual = generate_name(5)[1]
        self.assertIn(actual, "aiueoy")

    def test_generate_name_consonant_third_position(self):
        """Test if the third position of name is lowercase consonant."""
        actual = generate_name(5)[2]
        self.assertIn(actual, "bcdfghjklmnpqrstvwxyz")
