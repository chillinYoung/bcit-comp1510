"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from dnd import generate_name


class TestGenerateName(TestCase):

    def test_generate_name_length(self):
        actual = len(generate_name(5))
        self.assertEqual(actual, 10)

    def test_generate_name_type(self):
        actual = type(generate_name(5))
        self.assertEqual(actual, str)

    def test_generate_name_consonant_first_position(self):
        actual = generate_name(5)[0]
        self.assertIn(actual, "BCDFGHJKLMNPQRSTVWXYZ")

    def test_generate_name_vowel_second_position(self):
        actual = generate_name(5)[1]
        self.assertIn(actual, "aiueoy")

    def test_generate_name_consonant_third_position(self):
        actual = generate_name(5)[2]
        self.assertIn(actual, "bcdfghjklmnpqrstvwxyz")
