"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from dnd import generate_consonant


class TestGenerateConsonant(TestCase):

    def test_generate_consonant(self):
        actual = generate_consonant()
        self.assertIn(actual, "bcdfghjklmnpqrstvwxyz")

    def test_generate_consonant_length(self):
        actual = len(generate_consonant())
        self.assertEqual(actual, 1)

    def test_generate_consonant_type(self):
        actual = type(generate_consonant())
        self.assertEqual(actual, str)
