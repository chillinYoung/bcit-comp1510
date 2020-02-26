"""
COMP 1510 202010 Lab 05 Unit Test
Young Kim (A01087377)
"""


from unittest import TestCase
from sparse_vector import convert_vector_dict_to_list


class TestSparseVector(TestCase):
    def test_convert_vector_dict_to_list_zero_length(self):
        """Test ."""
        expected = []
        test_dict = {'length': 0}
        actual = convert_vector_dict_to_list(test_dict)
        self.assertEqual(actual, expected)

    def test_convert_vector_dict_to_list_all_zeros(self):
        """Test ."""
        expected = [0, 0, 0, 0, 0]
        test_dict = {'length': 5}
        actual = convert_vector_dict_to_list(test_dict)
        self.assertEqual(actual, expected)

    def test_convert_vector_dict_to_list_one_non_zero_number(self):
        """Test ."""
        expected = [0, 0, 0, 1, 0]
        test_dict = {'length': 5, 3: 1}
        actual = convert_vector_dict_to_list(test_dict)
        self.assertEqual(actual, expected)

    def test_convert_vector_dict_to_list_several_non_zero_numbers(self):
        """Test ."""
        expected = [0, 3, 7, 0, 2, 1]
        test_dict = {'length': 6, 1: 3, 2: 7, 4: 2, 5: 1}
        actual = convert_vector_dict_to_list(test_dict)
        self.assertEqual(actual, expected)

    def test_convert_vector_dict_to_list_mixed_negative_numbers(self):
        """Test ."""
        expected = [0, -3, 7, 0, -2, -1]
        test_dict = {'length': 6, 1: -3, 2: 7, 4: -2, 5: -1}
        actual = convert_vector_dict_to_list(test_dict)
        self.assertEqual(actual, expected)

    def test_convert_vector_dict_to_list_different_position_of_length(self):
        """Test ."""
        expected = [1, 0, 7, 1, 2, 3, 0]
        test_list = {0: 1, 2: 7, 3: 1, 4: 2, 'length': 7, 5: 3}
        actual = convert_vector_dict_to_list(test_list)
        self.assertEqual(actual, expected)

    def test_convert_vector_dict_to_list_mixed_orders(self):
        """Test ."""
        expected = [1, 0, 7, 1, 2, 3, 0]
        test_list = {5: 3, 2: 7, 4: 2, 'length': 7, 3: 1, 0: 1}
        actual = convert_vector_dict_to_list(test_list)
        self.assertEqual(actual, expected)
