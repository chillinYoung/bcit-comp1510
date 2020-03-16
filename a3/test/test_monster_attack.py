"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for attack function in the monster module.
"""

from unittest import TestCase
from unittest.mock import patch
from monster import attack
import io


class TestAttack(TestCase):
    def setUp(self):
        self.character = {'Name': 'Woody',
                          'HP': 10,
                          'Max_HP': 10,
                          'Pos_x': 0,
                          'Pos_y': 0}
        self.monster = {'Name': 'Test Monster', 'HP': 5}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=6)
    def test_attack_character_first_with_no_switch(
            self, mock_randint, mock_stdout):
        """Test attack of character first."""
        expected = ("\tTest Monster got 6 of damage.\n"
                    "\t=== Test Monster DIED... ===\n")
        attack_damage_max = 6
        attacker = self.character
        defender = self.monster
        attack(attacker, defender, attack_damage_max)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=10)
    def test_attack_monster_first_with_no_switch(
            self, mock_randint, mock_stdout):
        """Test attack of monster first."""
        expected = ("\tWoody got 10 of damage.\n"
                    "\t=== Woody DIED... ===\n")
        attack_damage_max = 10
        attacker = self.monster
        defender = self.character
        attack(attacker, defender, attack_damage_max)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[3, 3, 5, 1, 3])
    def test_attack_monster_first_with_several_switches(
            self, mock_randint, mock_stdout):
        """Test several switches with the monster's first attack."""
        expected = ("\tWoody got 3 of damage.\n"
                    "\tNow Woody's HP is 7.\n\n"
                    "\tTest Monster got 3 of damage.\n"
                    "\tNow Test Monster's HP is 2.\n\n"
                    "\tWoody got 5 of damage.\n"
                    "\tNow Woody's HP is 2.\n\n"
                    "\tTest Monster got 1 of damage.\n"
                    "\tNow Test Monster's HP is 1.\n\n"
                    "\tWoody got 3 of damage.\n"
                    "\t=== Woody DIED... ===\n")
        attack_damage_max = 5
        attacker = self.monster
        defender = self.character
        attack(attacker, defender, attack_damage_max)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[2, 1, 4])
    def test_attack_character_first_with_several_switches(
            self, mock_randint, mock_stdout):
        """Test several switches with the character's first attack."""
        expected = ("\tTest Monster got 2 of damage.\n"
                    "\tNow Test Monster's HP is 3.\n\n"
                    "\tWoody got 1 of damage.\n"
                    "\tNow Woody's HP is 9.\n\n"
                    "\tTest Monster got 4 of damage.\n"
                    "\t=== Test Monster DIED... ===\n")
        attack_damage_max = 10
        attacker = self.character
        defender = self.monster
        attack(attacker, defender, attack_damage_max)
        self.assertEqual(mock_stdout.getvalue(), expected)
