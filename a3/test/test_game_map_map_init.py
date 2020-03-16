"""
COMP 1510 202010 Assignment 3 Unit Test
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Unit test for map_init function in the game_map module.
"""

from unittest import TestCase
from game_map import map_init


class TestMapInit(TestCase):
    def test_map_init_with_1_width_1_height(self):
        actual = map_init(1, 1)
        expected = {
            (0, 0):
            {'description':
             "\nYou just woke up, and you feel the ground moving\n"
             "beneath you. 'Where am I', you think to yourself; you try to\n"
             "trace your memory back to where you saw Andy last, but no\n"
             "luck. You look around, and it's unfamiliar to you, you can't\n"
             "recognize a thing! You look outside and you realized you are\n"
             "inside a train filled with cargo heading to the United States\n"
             "! 'Oh No! I am a lost toy', you cried; There are 2 doors in \n"
             "front of you, one labeled 'North', the other labeled East, \n"
             "pick one, and see if that will take you home.\n",
             'e': False, 'w': False, 'n': False, 's': False},
            'Width': 1, 'Height': 1}
        self.assertEqual(actual, expected)

    def test_map_init_with_2_width_2_height(self):
        actual = map_init(2, 2)
        expected = {
            (0, 0):
            {'description':
             "\nYou just woke up, and you feel the ground moving\n"
             "beneath you. 'Where am I', you think to yourself; you try to\n"
             "trace your memory back to where you saw Andy last, but no\n"
             "luck. You look around, and it's unfamiliar to you, you can't\n"
             "recognize a thing! You look outside and you realized you are\n"
             "inside a train filled with cargo heading to the United States\n"
             "! 'Oh No! I am a lost toy', you cried; There are 2 doors in \n"
             "front of you, one labeled 'North', the other labeled East, \n"
             "pick one, and see if that will take you home.\n",
             'e': True, 'w': False, 'n': True, 's': False},

            (0, 1):
            {'description':
             "\nThe wind almost blew you away, you realized you are now \n"
             "on top of the train! 'AAAAAAAAhhhhh', you hear a loud cry \n"
             "just a few meters ahead of you; you crouch down so you can \n"
             "grab hold of something and you realized that it's Mr.\n"
             "Potatoe Head!!! He again has parts detached away from his \n"
             "body and you are stepping on his eye ball! 'OWWWWWWWW, quit \n"
             "it! You are stepping on me!', Mr. Potatoe head said \n"
             "grouchingly. You apologized and explained that you are lost \n"
             "and is trying to get back to Andy. At least now you have a \n"
             "friend.\n",
             'e': True, 'w': False, 'n': False, 's': True},

            (1, 0):
            {'description':
             "\nIt's dark and wet in here. You can't see or \n"
             "hear anything. You reach out your hands to feel and try to\n"
             "walk cautiously; and there's just no sound, it's eerily \n"
             "quite. 'Did I just enter a black hole?', you think to \n"
             "yourself; 'OUCH!', finally you bump into something hard, \n"
             "it feels like a door...\n",
             'e': False, 'w': True, 'n': True, 's': False},

            (1, 1):
            {'description':
             "\nLights buzzing, music pounding, you hear game noises, \n"
             "where could you be? Woooooo, you are in the arcade!\n"
             "Maybe someone in here will have the clues back to Andy's"
             "\nplace?\n",
             'e': False, 'w': True, 'n': False, 's': True},
            'Width': 2, 'Height': 2}
        self.assertEqual(actual, expected)
