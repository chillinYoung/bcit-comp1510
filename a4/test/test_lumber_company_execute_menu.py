from unittest import TestCase
from tree_farm import TreeFarm
from lumber_company import execute_menu


class TestExecuteMenu(TestCase):

    def test_execute_menu_SystemExitError_raised(self):
        with self.assertRaises(SystemExit):
            execute_menu(TreeFarm(), "4")
