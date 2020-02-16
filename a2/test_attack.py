"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)

The unit test for attack function in the dnd module.
"""

from unittest import TestCase
from unittest.mock import patch
import io
import dnd


class TestAttack(TestCase):

    def setUp(self):
        """Set up characters to test this test module."""
        self.attacker = {'Name': 'Gaga',
                         'Inventory': ['axe'],
                         'XP': 0,
                         'Class': 'barbarian',
                         'Race': 'dragonborn',
                         'HP': [11, 0],
                         'Strength': 11,
                         'Intelligence': 12,
                         'Wisdom': 7,
                         'Dexterity': 14,
                         'Constitution': 12,
                         'Charisma': 12}

        self.defender = {'Name': 'Jukiku',
                         'Inventory': [],
                         'XP': 0,
                         'Class': 'druid',
                         'Race': 'elf',
                         'HP': [8, 0],
                         'Strength': 8,
                         'Intelligence': 13,
                         'Wisdom': 5,
                         'Dexterity': 10,
                         'Constitution': 6,
                         'Charisma': 11}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[11, 10])
    def test_attack_one_time(self, mock_randint, mock_stdout):
        """Test the one time attack and finished."""
        expected = ("\nGaga's attack was successful!!\n"
                    "\tJukiku is hit with 10 point(s) and Killed.\n"
                    "\n------ Gaga WIN!! GAME OVER. ------\n\n")
        dnd.attack(self.attacker, self.defender)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[16, 7, 15, 7, 2, 15, 5])
    def test_attack_several_attacks(self, mock_randint, mock_stdout):
        """Test the several times of attack and finished."""
        self.attacker['HP'][1] = 11
        self.defender['HP'][1] = 8
        expected = ("\nGaga's attack was successful!!\n"
                    "\tJukiku's HP is reduced 7 point(s)."
                    "\n\tCONTINUE the round."
                    "\n\tGaga (HP: 11) vs. Jukiku (HP: 1)\n"
                    "\nJukiku's attack was successful!!\n"
                    "\tGaga's HP is reduced 7 point(s)."
                    "\n\tCONTINUE the round."
                    "\n\tJukiku (HP: 1) vs. Gaga (HP: 4)\n"
                    "\nGaga's attack was failed... "
                    "CONTINUE the round.\n"
                    "\nJukiku's attack was successful!!\n"
                    "\tGaga is hit with 5 point(s) and Killed.\n"
                    "\n------ Jukiku WIN!! GAME OVER. ------\n\n")
        dnd.attack(self.attacker, self.defender)
        self.assertEqual(mock_stdout.getvalue(), expected)
