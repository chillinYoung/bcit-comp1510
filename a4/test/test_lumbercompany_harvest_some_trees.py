from unittest import TestCase
from tree import Tree
from tree_farm import TreeFarm
from lumber_company import harvest_some_trees
from unittest.mock import patch
import io


class TestHarvestSomeTree(TestCase):

    def setUp(self) -> None:

        # empty tree object
        self.farm = TreeFarm()

        # initialize some tree objects
        self.palm_tree = Tree("palm tree", 5, 1)
        self.coconut_tree = Tree("coconut tree", 8, 5000.153)
        self.maple_tree = Tree("maple", 150, 50)
        self.willow_tree = Tree("willow", 10, 123.456)

        # tree list
        self.tree_list = [self.willow_tree, self.palm_tree,
                          self.coconut_tree, self.maple_tree]

        # non-empty tree object
        self.farm2 = TreeFarm()
        for tree in self.tree_list:
            self.farm2.add(tree)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_harvest_some_trees_on_empty_tree(self, mock_stdout):
        harvest_some_trees(self.farm)
        self.assertEqual(mock_stdout.getvalue(), "The farm is empty.\n")

    @patch("builtins.input", return_value="4000")
    def test_harvest_some_trees_success_1_match(self, mock_input):
        harvest_some_trees(self.farm2)
        farm_size = len(self.farm2.get_tree_list())
        expected = 3
        self.assertEqual(farm_size, expected)

    @patch("builtins.input", return_value="123")
    def test_harvest_some_trees_success_multiple_matches(self, mock_input):
        harvest_some_trees(self.farm2)
        farm_size = len(self.farm2.get_tree_list())
        expected = 2
        self.assertEqual(farm_size, expected)

    @patch("builtins.input", return_value="10000")
    def test_harvest_some_trees_success_zero_match(self, mock_input):
        harvest_some_trees(self.farm2)
        farm_size = len(self.farm2.get_tree_list())
        expected = 4
        self.assertEqual(farm_size, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value="-123")
    def test_harvest_some_trees_fails_negative_circumference(self,
                                                           mock_input,
                                                           mock_stdout):
        harvest_some_trees(self.farm2)
        expected = "# Error: circumference must be a positive number\n"
        self.assertEqual(mock_stdout.getvalue(), expected)