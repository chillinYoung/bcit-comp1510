"""
COMP 1510 202010 Lab 10 - Unit Test
Young Kim (A01087377)

A unit test for the is_email function in the regular_expressions module.
"""

from unittest import TestCase
from regular_expressions import is_email


class TestIsEmail(TestCase):
    """Test is_email function."""

    def test_is_email_with_only_alphabets(self):
        """Test email with only alphabets."""
        expected = True
        actual = is_email("ykimhithere@bcit.ca")
        self.assertEqual(actual, expected)

    def test_is_email_username_with_numbers(self):
        """Test email username with numbers."""
        expected = True
        actual = is_email("18563749@bcit.ca")
        self.assertEqual(actual, expected)

    def test_is_email_username_with_special_characters_false(self):
        """Test email username with numbers."""
        expected = False
        actual = is_email("ykim!#$^@bcit.ca")
        self.assertEqual(actual, expected)

    def test_is_email_username_with_alpha_and_underscores(self):
        """Test email username with alphabets and underscores."""
        expected = True
        actual = is_email("_y_kim_hi_there@bcit.ca")
        self.assertEqual(actual, expected)

    def test_is_email_username_mixed(self):
        """Test email mixed username with alphabets, numbers, and underscores.
        """
        expected = True
        actual = is_email("y_kim_13579@bcit.ca")
        self.assertEqual(actual, expected)

    def test_is_email_domain_with_underscores_false(self):
        """Test email domain with underscores."""
        expected = False
        actual = is_email("ykimhithere@bc_it.ca")
        self.assertEqual(actual, expected)

    def test_is_email_domain_with_only_numbers(self):
        """Test email domain with only numbers."""
        expected = True
        actual = is_email("ykimhithere@5353.ca")
        self.assertEqual(actual, expected)

    def test_is_email_domain_with_both_alphabets_and_numbers(self):
        """Test email domain with both alphabets and numbers."""
        expected = True
        actual = is_email("ykimhithere@bc00it11.ca")
        self.assertEqual(actual, expected)

    def test_is_email_without_at_symbol_false(self):
        """Test without @ symbol."""
        expected = False
        actual = is_email("ykim123bcit.ca")
        self.assertEqual(actual, expected)

    def test_is_email_witout_dot_after_domain_false(self):
        """Test without dot after domain name."""
        expected = False
        actual = is_email("ykim333@bcitca")
        self.assertEqual(actual, expected)

    def test_is_email_top_level_domain_with_one_character_false(self):
        """Test email top-level domain with one character."""
        expected = False
        actual = is_email("ykimhithere@bcit.c")
        self.assertEqual(actual, expected)

    def test_is_email_top_level_domain_with_four_character(self):
        """Test email top-level domain with four character."""
        expected = True
        actual = is_email("ykimhithere@bcit.info")
        self.assertEqual(actual, expected)
