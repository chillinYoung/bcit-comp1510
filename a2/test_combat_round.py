"""
COMP 1510 202010 Assignment 2 Unit Test
Young Kim (A01087377)
"""

from unittest import TestCase
from unittest.mock import patch
import io
import dnd


class TestCombatRound(TestCase):

    def setUp(self):
        self.opponent_one = {'Name': 'Gaga',
                             'Inventory': ["axe"],
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

        self.opponent_two = {'Name': 'Jukiku',
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
    @patch('random.randint', side_effect=[10, 3, 11, 9])
    def test_combat_round_done_in_one_attack(self, mock_randint, mock_stdout):
        expected = ("\n---------- Combat starts! ----------\n\n"
                    "Gaga (HP: 11) vs. Jukiku (HP: 8)\n"
                    "Gaga is the first attacker.\n"
                    "\nGaga's attack was successful!!\n"
                    "\tJukiku is hit with 9 point(s) and Killed.\n"
                    "\n------ Gaga WIN!! GAME OVER. ------\n\n")
        dnd.combat_round(self.opponent_one, self.opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[7, 10, 19, 5, 11, 3, 3, 17, 8])
    def test_combat_round_several_attacks(self, mock_randint, mock_stdout):
        expected = ("\n---------- Combat starts! ----------\n\n"
                    "Gaga (HP: 11) vs. Jukiku (HP: 8)\n"
                    "Jukiku is the first attacker.\n"
                    "\nJukiku's attack was successful!!\n"
                    "\tGaga's HP is reduced 5 point(s)."
                    "\n\tCONTINUE the round.\n\t"
                    "Jukiku (HP: 8) vs. Gaga (HP: 6)\n"
                    "\nGaga's attack was successful!!\n"
                    "\tJukiku's HP is reduced 3 point(s)."
                    "\n\tCONTINUE the round.\n\t"
                    "Gaga (HP: 6) vs. Jukiku (HP: 5)\n"
                    "\nJukiku's attack was failed... "
                    "CONTINUE the round.\n"
                    "\nGaga's attack was successful!!\n"
                    "\tJukiku is hit with 8 point(s) and Killed.\n"
                    "\n------ Gaga WIN!! GAME OVER. ------\n\n")
        dnd.combat_round(self.opponent_one, self.opponent_two)
        self.assertEqual(mock_stdout.getvalue(), expected)
