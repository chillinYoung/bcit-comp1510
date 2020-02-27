"""
COMP 1510 202010 Lab 05 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from sparse_vector import sparse_add


class TestSparseVector(TestCase):
    def test_sparse_add_all_zeros(self):
        """Test adding two vectors with all zeros."""
        expected = {'length': 2}
        test_vec1 = {'length': 2}
        test_vec2 = {'length': 2}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_add_zeros_after_addition(self):
        """Test the two vectors which will be all zeros after addition."""
        expected = {'length': 10}
        test_vec1 = {'length': 10, 5: 7}
        test_vec2 = {'length': 10, 5: -7}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_add_different_position_of_length(self):
        """Test the different position of the length item in the dictionary."""
        expected = {'length': 5, 1: 2, 3: 1, 4: 7}
        test_vec1 = {1: 2, 'length': 5}
        test_vec2 = {3: 1, 'length': 5, 4: 7}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_add_different_length(self):
        """Test the different length of two vectors."""
        expected = None
        test_vec1 = {'length': 7, 6: 3}
        test_vec2 = {'length': 5, 2: 7}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_add_mixed_negative_values(self):
        """Test the vectors with negative values."""
        expected = {'length': 5, 1: -2, 3: 3, 4: -6}
        test_vec1 = {'length': 5, 1: -2, 4: 1}
        test_vec2 = {'length': 5, 3: 3, 4: -7}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_add_not_sorted_key_orders(self):
        """Test the vectors with not sorted orders."""
        expected = {'length': 7, 1: 4, 2: 4, 3: 2, 4: 2, 5: 1, 6: -2}
        test_vec1 = {6: -2, 2: 3, 'length': 7, 3: 1, 1: 2}
        test_vec2 = {5: 1, 1: 2, 2: 1, 4: 2, 3: 1, 'length': 7}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)
