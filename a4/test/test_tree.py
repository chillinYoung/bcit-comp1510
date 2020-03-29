from unittest import TestCase
from tree import Tree


class TestTree(TestCase):

    def setUp(self):
        self.willow_tree = Tree("willow", 10, 123.456)

    def test__init__fail_age_valueError(self):
        age_list = range(-10, 1, 2)
        with self.assertRaises(ValueError):
            for age in age_list:
                Tree("tree", age, 1234.34)

    def test__init__fail_circumference_valueError(self):
        circumference_list = [-1234.345, -10, 0]
        with self.assertRaises(ValueError):
            for circumference in circumference_list:
                Tree("tree", 5, circumference)

    def test__init__fail_specie_valueError_bad_string(self):
        species_list = ["", "     "]
        with self.assertRaises(ValueError):
            for species in species_list:
                Tree(species, 10, 125.23)

    def test_get_species(self):
        actual = self.willow_tree.get_species()
        expected = 'willow'
        self.assertEqual(actual, expected)

    def test_get_age(self):
        actual = self.willow_tree.get_age()
        expected = 10
        self.assertEqual(actual, expected)

    def test_get_circumference(self):
        actual = self.willow_tree.get_circumference()
        expected = 123.456
        self.assertEqual(actual, expected)

    def test_set_age_success_int(self):
        self.willow_tree.set_age(15)
        actual = repr(self.willow_tree)
        expected = "Tree('willow', 15, 123.456)"
        self.assertEqual(actual, expected)

    def test_set_age_success_float(self):
        self.willow_tree.set_age(12.9)
        actual = repr(self.willow_tree)
        expected = "Tree('willow', 12, 123.456)"
        self.assertEqual(actual, expected)

    def test_set_age_fail_valueError(self):
        with self.assertRaises(ValueError):
            self.willow_tree.set_age(-10)

    def test_set_circumference_success(self):
        self.willow_tree.set_circumference(500.1534)
        actual = repr(self.willow_tree)
        expected = "Tree('willow', 10, 500.1534)"
        self.assertEqual(actual, expected)

    def test_set_circumference_fail_valueError(self):
        with self.assertRaises(ValueError):
            self.willow_tree.set_circumference(-102)

    def test__str__(self):
        actual = str(self.willow_tree)
        expected = "Tree specie: 'willow', age: 10, circumference: 123.456"
        self.assertEqual(actual, expected)

    def test__repr__(self):
        actual = repr(self.willow_tree)
        expected = "Tree('willow', 10, 123.456)"
        self.assertEqual(actual, expected)
