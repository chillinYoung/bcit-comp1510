from unittest import TestCase
from tree import Tree
from tree_farm import TreeFarm
from lumber_company import add_a_tree
from unittest.mock import patch
import io


class TestAddATree(TestCase):

    def setUp(self) -> None:

        # instantiate an empty tree object
        self.farm = TreeFarm()

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=['willow', '-1', '123.45'])
    def test_add_a_tree_fail_age_error(self, mock_input, mock_stdout):
        # tree size should not change because of error
        add_a_tree(self.farm)
        actual_tree_size_after = len(self.farm.get_tree_list())
        expected_tree_size = 0
        expected_error_msg = "#Error: The age cannot be negative or zero\n"
        self.assertEqual([actual_tree_size_after, mock_stdout.getvalue()],
                         [expected_tree_size, expected_error_msg])

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["", '10', "1234.45"])
    def test_add_a_tree_fail_species_error(self, mock_input, mock_stdout):
        # tree size should not change because of error
        add_a_tree(self.farm)
        actual_tree_size_after = len(self.farm.get_tree_list())
        expected_tree_size = 0
        expected_error_msg = "#Error: Tree species cannot be empty or only " \
                             "have white spaces\n"
        self.assertEqual([actual_tree_size_after, mock_stdout.getvalue()],
                         [expected_tree_size, expected_error_msg])

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=['willow', '4', '-123.45'])
    def test_add_a_tree_fail_circumference_error(self, mock_input, mock_stdout):
        # tree size should not change because of error
        add_a_tree(self.farm)
        actual_tree_size_after = len(self.farm.get_tree_list())
        expected_tree_size = 0
        expected_error_msg = "#Error: The circumference cannot be negative " \
                             "or zero\n"
        self.assertEqual([actual_tree_size_after, mock_stdout.getvalue()],
                         [expected_tree_size, expected_error_msg])

    @patch("builtins.input", side_effect=['willow', '5', '123.45'])
    def test_add_a_tree_success(self, mock_input):
        add_a_tree(self.farm)
        actual_tree_size = len(self.farm.get_tree_list())
        expected_tree_size = 1
        self.assertEqual(actual_tree_size, expected_tree_size)