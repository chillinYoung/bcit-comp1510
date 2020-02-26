"""
COMP 1510 202010 Lab 05 Unit Test
Young Kim (A01087377)
"""


from unittest import TestCase
from sparse_vector import convert_vector_list_to_dict


class TestSparseVector(TestCase):
    def test_convert_vector_list_to_dict_empty(self):
        """Test ."""
        expected = {'length': 0}
        test_list = []
        actual = convert_vector_list_to_dict(test_list)
        self.assertEqual(actual, expected)

    def test_convert_vector_list_to_dict_one_element_with_non_zero(self):
        """Test ."""
        expected = {'length': 1, 0: 3}
        test_list = [3]
        actual = convert_vector_list_to_dict(test_list)
        self.assertEqual(actual, expected)

    def test_convert_vector_list_to_dict_all_zeros(self):
        """Test ."""
        expected = {'length': 5}
        test_list = [0, 0, 0, 0, 0]
        actual = convert_vector_list_to_dict(test_list)
        self.assertEqual(actual, expected)

    def test_convert_vector_list_to_dict_one_non_zero_number(self):
        """Test ."""
        expected = {'length': 5, 2: 1}
        test_list = [0, 0, 1, 0, 0]
        actual = convert_vector_list_to_dict(test_list)
        self.assertEqual(actual, expected)

    def test_convert_vector_list_to_dict_several_non_zero_numbers(self):
        """Test ."""
        expected = {'length': 6, 1: 3, 2: 7, 4: 2, 5: 1}
        test_list = [0, 3, 7, 0, 2, 1]
        actual = convert_vector_list_to_dict(test_list)
        self.assertEqual(actual, expected)

    def test_convert_vector_list_to_dict_mixed_negative_numbers(self):
        """Test ."""
        expected = {'length': 6, 1: -3, 2: 7, 4: -2, 5: -1}
        test_list = [0, -3, 7, 0, -2, -1]
        actual = convert_vector_list_to_dict(test_list)
        self.assertEqual(actual, expected)
