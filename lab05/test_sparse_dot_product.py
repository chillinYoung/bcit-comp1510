"""
COMP 1510 202010 Lab 05 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from sparse_vector import sparse_dot_product


class TestSparseVector(TestCase):
    def test_sparse_dot_product_empty_vectors(self):
        """Test the empty vectors."""
        expected = None
        test_vec1 = {'length': 0}
        test_vec2 = {'length': 0}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_all_zeros(self):
        """Test the vectors with all zeros."""
        expected = 0
        test_vec1 = {'length': 5}
        test_vec2 = {'length': 5}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_no_same_keys(self):
        """Test no same keys between the two vectors."""
        expected = 0
        test_vec1 = {'length': 7, 1: 1, 3: 2, 5: 1}
        test_vec2 = {'length': 7, 2: 2, 4: 1, 6: 4}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_one_same_key(self):
        """Test one same key element between the two vectors."""
        expected = 2
        test_vec1 = {'length': 7, 1: 2}
        test_vec2 = {'length': 7, 1: 1}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_many_same_keys(self):
        """Test many same key elements between the two vectors."""
        expected = 29    # (1 * 3) + (5 * 2) + (2 * 4) + (2 * 4)
        test_vec1 = {'length': 7, 1: 1, 2: 5, 3: 2, 5: 1, 6: 2}
        test_vec2 = {'length': 7, 1: 3, 2: 2, 3: 4, 4: 1, 6: 4}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_different_length(self):
        """Test different length of the two vectors."""
        expected = None
        test_vec1 = {'length': 4, 1: 1, 3: 2}
        test_vec2 = {'length': 7, 4: 1, 6: 4}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_defferent_position_of_length(self):
        """Test weird position of the length element."""
        expected = 10
        test_vec1 = {1: 2, 3: 3, 4: 1, 'length': 5}
        test_vec2 = {3: 1, 'length': 5, 4: 7}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_mixed_nagative_values(self):
        """Test the vectors with mixed positive and negative elements."""
        expected = -8
        test_vec1 = {'length': 8, 1: -1, 3: 2, 6: 1}
        test_vec2 = {'length': 8, 3: -2, 4: 1, 6: -4}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_dot_product_not_sorted_key_orders(self):
        """Test the vectors with the not sorted key orders."""
        expected = 8
        test_vec1 = {6: -2, 2: 3, 'length': 7, 3: 1, 1: 2}
        test_vec2 = {5: 1, 1: 2, 2: 1, 4: 2, 3: 1, 'length': 7}
        actual = sparse_dot_product(test_vec1, test_vec2)
        self.assertEqual(actual, expected)
