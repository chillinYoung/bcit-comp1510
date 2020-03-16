"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for combat function in the monster module.
"""

from unittest import TestCase
from unittest.mock import patch
from monster import combat, attack
import io


class TestCombat(TestCase):
    def setUp(self):
        self.character = {'Name': 'Woody',
                          'HP': 10,
                          'Max_HP': 10,
                          'Pos_x': 0,
                          'Pos_y': 0}
        self.monster = {'Name': 'Test Monster', 'HP': 5}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[1, 10])
    def test_combat_the_first_attacker_monster(
            self, mock_randint, mock_stdout):
        """Test the first attacker is the monster."""
        expected = ("\n\tYou decided to combat.\n"
                    "\t* The first attacker is Test Monster.\n"
                    "\tWoody got 10 of damage.\n"
                    "\t=== Woody DIED... ===\n")
        attack_damage_max = 10
        combat(self.character, self.monster, attack_damage_max)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[0, 6])
    def test_combat_the_first_attacker_character(
            self, mock_randint, mock_stdout):
        """Test the first attacker is the character."""
        expected = ("\n\tYou decided to combat.\n"
                    "\t* The first attacker is Woody.\n"
                    "\tTest Monster got 6 of damage.\n"
                    "\t=== Test Monster DIED... ===\n")
        attack_damage_max = 6
        combat(self.character, self.monster, attack_damage_max)
        self.assertEqual(mock_stdout.getvalue(), expected)
