"""
COMP 1510 202010 Lab 07c
Young Kim (A01087377)

Unit test for the population_density method of Country Class.
"""

from unittest import TestCase
from country import Country
from unittest.mock import patch
import io


class TestPopulationDensity(TestCase):

    def setUp(self):
        self.canada = Country("Canada", 37_590_000, 9_985_000)
        self.denmark = Country("Denmark", 5_603_000, 42_933)
        self.zero_area = Country("Zero Area", 1_010_000, 0)
        self.zero_population = Country("Zero population", 0, 737_000)

    def test_population_density_canada(self):
        expected = 3.764646970
        actual = self.canada.population_density()
        self.assertAlmostEqual(actual, expected)

    def test_population_density_denmark(self):
        expected = 130.505671627
        actual = self.denmark.population_density()
        self.assertAlmostEqual(actual, expected)

    def test_population_density_zero_population(self):
        expected = 0
        actual = self.zero_population.population_density()
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_population_density_zero_area(self, mock_stdout):
        expected = "division by zero\n"
        self.zero_area.population_density()
        self.assertEqual(mock_stdout.getvalue(), expected)
