"""
COMP 1510 202010 Lab 05 Unit Test
Young Kim (A01087377)
"""


from unittest import TestCase
from sparse_vector import sparse_add


class TestSparseVector(TestCase):
    def test_sparse_add_all_zeros(self):
        expected = {'length': 2}
        test_vec1 = {'length': 2}
        test_vec2 = {'length': 2}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_add_zeros_after_addition(self):
        expected = {'length': 10}
        test_vec1 = {'length': 10, 5: 7}
        test_vec2 = {'length': 10, 5: -7}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_add_different_position_of_length(self):
        expected = {'length': 5, 1: 2, 4: 7}
        test_vec1 = {1: 2, 'length': 5}
        test_vec2 = {'length': 5, 4: 7}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)

    def test_sparse_add_different_length_of_vectors(self):
        expected = None
        test_vec1 = {'length': 7, 6: 3}
        test_vec2 = {'length': 5, 2: 7}
        actual = sparse_add(test_vec1, test_vec2)
        self.assertEqual(actual, expected)
