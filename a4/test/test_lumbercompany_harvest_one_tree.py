from unittest import TestCase
from tree import Tree
from tree_farm import TreeFarm
from lumber_company import harvest_one_tree
from unittest.mock import patch
import io


class TestHarvestOneTree(TestCase):

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
    def test_harvest_one_tree_on_empty_tree(self, mock_stdout):
        harvest_one_tree(self.farm)
        self.assertEqual(mock_stdout.getvalue(), "The farm is empty.\n")

    @patch("builtins.input", return_value="123")
    def test_harvest_one_tree_success(self, mock_input):
        harvest_one_tree(self.farm2)
        size_after_harvest = len(self.farm2.get_tree_list())
        expected = 3
        self.assertEqual(size_after_harvest, expected)

    @patch("builtins.input", return_value="6000")
    def test_harvest_one_tree_fails_no_match(self, mock_input):
        harvest_one_tree(self.farm2)
        size_after_harvest = len(self.farm2.get_tree_list())
        expected = 4 # no change
        self.assertEqual(size_after_harvest, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", return_value="-123")
    def test_harvest_one_tree_fails_negative_circumference(self,
                                                           mock_input,
                                                           mock_stdout):
        harvest_one_tree(self.farm2)
        expected = "# Error: circumference must be a positive number\n"
        self.assertEqual(mock_stdout.getvalue(), expected)