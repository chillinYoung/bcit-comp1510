from unittest import TestCase
from unittest.mock import patch
from tree import Tree
from tree_farm import TreeFarm
import io


class TestTreeFarm(TestCase):

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

    def test__init__success(self):
        tree_farm = TreeFarm()
        actual = str(tree_farm)
        expected = "TreeFarm has 0 tree(s)."
        self.assertEqual(actual, expected)

    def test_add_fail_non_tree_type(self):
        type_list = ["tree1", 5]
        with self.assertRaises(TypeError):
            for tree_type in type_list:
                self.farm.add(tree_type)

    def test_add_success_tree_type(self):
        for tree_type in self.tree_list:
            self.farm.add(tree_type)
        actual = len(self.farm.get_tree_list())
        expected = 4
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_trees_empty_farm(self, mock_stdout):
        self.farm.print_trees()
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_trees_non_empty_farm(self, mock_stdout):
        self.farm2.print_trees()
        expected = "willow, 10\n" \
                   "palm tree, 5\n" \
                   "coconut tree, 8\n" \
                   "maple, 150\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_remove_tree_success_has_matching_tree(self):
        actual = repr(self.farm2.remove_tree(123))
        expected = "Tree('willow', 10, 123.456)"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_tree_success_but_no_matching_tree(self, mock_stdout):
        self.farm2.remove_tree(10000)
        self.assertEqual(mock_stdout.getvalue(), "Nothing to harvest.\n")

    def test_remove_trees_success_has_1_matching_tree(self):
        actual = repr(self.farm2.remove_trees(4000))
        expected = "[Tree('coconut tree', 8, 5000.153)]"
        self.assertEqual(actual, expected)

    def test_remove_trees_success_has_multiple_matching_trees(self):
        actual = repr(self.farm2.remove_trees((123)))
        expected = "[Tree('willow', 10, 123.456), " \
                   "Tree('coconut tree', 8, 5000.153)]"
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_trees_success_zero_match(self, mock_stdout):
        self.farm2.remove_trees(10000)
        self.assertEqual(mock_stdout.getvalue(), "Nothing to harvest.\n")

    def test_get_tree_list_empty_farm(self):
        actual = len(self.farm.get_tree_list())
        expected = 0
        self.assertEqual(actual, expected)

    def test_get_tree_list_non_empty_farm(self):
        actual = len(self.farm2.get_tree_list())
        expected = 4
        self.assertEqual(actual, expected)

    def test__repr__(self):
        actual = repr(self.farm2)
        expected = "TreeFarm()"
        self.assertEqual(actual, expected)

    def test__str__empty_treefarm(self):
        actual = str(self.farm)
        expected = "TreeFarm has 0 tree(s)."
        self.assertEqual(actual, expected)

    def test__str__non_empty_treefarm(self):
        actual = str(self.farm2)
        expected = "TreeFarm has 4 tree(s)."
        self.assertEqual(actual, expected)
