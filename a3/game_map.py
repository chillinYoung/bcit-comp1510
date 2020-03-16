"""
COMP 1510 202010 Assignment 3
Li Ting Yang (Lily, A00794517)
Young Kim (A01087377)

Game Map Module for Single User Dungeon (SUD)
"""

import doctest


def map_init(width: int, height: int) -> dict:
    """Initialize the game map.

    :param width: an integer
    :param height: an integer
    :precondition: the width must be 5 and height must be 5 in order for
            the scenario and goal to make sense for this game
    :postcondition: correctly creates a map for the game with whimsical
            and descriptive scenarios in each coordinate
    :return: a dictionary

    >>> map_init(0, 0)
    {'Width': 0, 'Height': 0}
    """

    STORY = [["\nYou just woke up, and you feel the ground moving\n"
              "beneath you. 'Where am I', you think to yourself; you try to\n"
              "trace your memory back to where you saw Andy last, but no\n"
              "luck. You look around, and it's unfamiliar to you, you can't\n"
              "recognize a thing! You look outside and you realized you are\n"
              "inside a train filled with cargo heading to the United States\n"
              "! 'Oh No! I am a lost toy', you cried; There are 2 doors in \n"
              "front of you, one labeled 'North', the other labeled East, \n"
              "pick one, and see if that will take you home.\n",

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

              "\nIt's dark in here, and it's a smell of paint, puke, and \n"
              "children all over here, you wonder where you are, and then \n"
              "you hear a voice! 'Hey!, you there! Where did you come from?'\n"
              ", says the mystery female voice; 'I belong to Andy, I need \n"
              "to go home, where am I'? The toy whispered 'We are in Sunny \n"
              "Side Daycare, this is a box of toys that they store away \n"
              "when they are damaged, you don't look damaged though.'; you \n"
              "started feeling around you hoping to find the exit.\n",

              "\nYou finally found a way out of the toy box!\n"
              "But it still smells the same, then you realized you are still\n"
              "in Sunny Side Daycare. 'Hello there! I am Lots-o'-Hugging\n"
              "bear, all the toys here are cast aways and abandoned, but you\n"
              "are never going to get hurt here! Let's take a tour shall we?\n"
              "You can choose to go with Lotso to go north, or you can \n"
              "choose other direction to continue your journey home\n",

              "\nI see, you decided to go with Lotso; Lotso is taking you \n"
              "to the spa room to convince you how wonderful this place is. \n"
              "You can get pampered and polished, and all the equipment you \n"
              "need for taking care of your body. He's evil plan is to get \n"
              "you to stay and not go back to an owner since he doesn't \n"
              "have one himself.\n"],

             ["\nIt's dark and wet in here. You can't see or \n"
              "hear anything. You reach out your hands to feel and try to\n"
              "walk cautiously; and there's just no sound, it's eerily \n"
              "quite. 'Did I just enter a black hole?', you think to \n"
              "yourself; 'OUCH!', finally you bump into something hard, \n"
              "it feels like a door...\n",

              "\nLights buzzing, music pounding, you hear game noises, \n"
              "where could you be? Woooooo, you are in the arcade!\n"
              "Maybe someone in here will have the clues back to Andy's\n"
              "place?\n",

              "\nThat person looks familiar, he's hammering the hamster \n"
              "machine like a crazy maniac. He....oh no! He's Sid!\n"
              "He sees you and is walking towards you, quick, run from him\n"
              "but he also can't see that you can move, so you have to\n"
              "pretend you are lying down on the floor. Sid picks you up and\n"
              "puts you in his backpack.\n",

              "\nYou are at the movie theatre inside the arcade just hiding \n"
              "behind one of the chairs, there's lots of people you must \n"
              "not be seen and quickly choose a direction to go so but be \n"
              "careful, the direction you choose, you might end up meeting \n"
              "Sid! The toy torturer.\n",

              "\nThe next room Lotso took you to was a room filled\n"
              "with other toys, there's baby, stretch the octopus, ken doll,\n"
              "and many many others, and they all said hi and introduced \n"
              "each other. You may continue this tour which is to your east \n"
              "or choose to go back\n"],

             ["\nNice safe! You could have been stuck with Sid and be \n"
              "tortured to death! You are now in the grocery store! There's \n"
              "lots of people trying to buy food for the new years!\n"
              "Quick, let us head to the toy section and get some hints from\n"
              "the other toys if they saw Andy in here or not!\n",

              "\nIt's bright in here, and there's a metal looking thing \n"
              "hanging in the ceiling; what is it? 'claw is the master', \n"
              "Aliens whisper as they gather around you and point to the \n"
              "claw being the master. They desire to be taken by the claw \n"
              "to a better place, but you know it will only lead to doom! \n"
              "Oh no! Sid is at the claw machine, and he sees me, and wants \n"
              "to take me home! Quick I need to find a way out! But going \n"
              "with Sid might also be a step closer to home back to Andy; \n"
              "Ggh! Life is so hard! Why do I have to make these decisions \n"
              "just so that I can be back in Andy's arms?\n",

              "\nOh no! I am at Sid's home, he just stole Hanna's\n"
              "toy and he cut the toy's head off!!!! There's a lot of\n"
              "amputated toys lying around and I am scared! What's going to\n"
              "happen to me? The dog is fierce and wants to chew me into\n"
              "pieces; Ewwww, I don't want to drown in his saliva! I am \n"
              "going to find the exit and escape! wants to chew me apart \n"
              "and\n",

              "\nYou are now inside the arcade's bathroom, stinky! It's \n"
              "so smelly in here that you can't breathe, you must get out\n",

              "\nNext is the Caterpiller room. Lotso is saying that this \n"
              "is the room where you will get all the play time a toy ever \n"
              "asks for so you will never be lonely or be cast away or get \n"
              "heart broken, but later you find out out that this room is \n"
              "where the toddlers chew, and break toys..ah!!\n"],

             ["\nIt's Andy's mom! She's at the grocery store doing\n"
              "errands for dinner, you must maneuver stealthily so she \n"
              "doesn't see you walking or moving. You must find her car \n"
              "and hop into it! There, I see it! It's just right outside \n"
              "in the parking lot! Here goes nothing! You need to move \n"
              "north in order to get into the car. If you move east, you \n"
              "might end up somewhere unexpected.\n",

              "\nWoohooooo! Success! You have successfully entered Andy's \n"
              "mom's car, and she's driving homeeeeeeeee. You are soooooo\n"
              "closeeee! You need to move north in order to get home. But \n"
              "if you are not careful and make the wrong move, you could \n"
              "leap out of the window.\n",

              "\nCONGRATULATIONS! YOU FOUND ANDY! HOME AT LAST!\n"
              "Andy sees you with delight as you've been gone for 2 weeks!\n"
              "'I thought I lost you forever', cries Andy; then he tuck you\n"
              "in bed.\n",

              "\nPhew! That was a close one! 'I didn't think I'd make it!', \n"
              "you think to yourself and took a moment to get collected \n"
              "Looking around; you smell something familiar, it's like \n"
              "you've been here before! Ewwww, it's the garbage truck! \n"
              "You are inside the garbage truck! Luckily, the truck is \n"
              "actually stopping at Andy's place to collect garbage, you \n"
              "must choose the right door out of the garbage truck! You are \n"
              "so close!!!! You really are almost home, you just have to \n"
              "make the right move!\n",

              "\nLotso is now taking you to the storage room\n"
              "where he tells you all the toys that try to run away are\n"
              "stored here, and if you also try to run away, you will\n"
              "end up with the same fate. Run! You gotta run before he\n"
              "finds out!\n"],

             ["\nYou are at the toy aisle and the barbies are having a pool \n"
              "party! You cried out in a loud voice, 'hey! you guys! Do you\n"
              "know which way is the way back to Andy?', the tour guide \n"
              "barbie jumps to your rescue and starts taking control of the \n"
              "toy car you were in and started to give you a tour. You \n"
              "exclaimed, 'I don't have time for a tour, I need to get \n"
              "home', which was ignored by the tour guide barbie.\n",

              "\nUgh! What happened? You are fallingggggg~~. 'ow, ow, ow', \n"
              "You grumbled as you landed on the ground and had to pick \n"
              "yourself back up so you can understand what just happened?. \n"
              "You are now in a grass field, but you don't recall how you \n"
              "got here. The journey home is getting harder and harder. But \n"
              "you see 2 doors. The door on the north or will you pick the \n"
              "door on the west, or south? Your choice\n",

              "\nNice! But maybe not...you are inside the garbage that is \n"
              "just across the street from Andy's home, you will have to \n"
              "cross the street! Watch out for the cars! \n"
              "Don't get run over!\n",

              "\nOh no! You are stolen by Al the toy collector! He is \n"
              "going to sell you for big bucks, but unfortunately, your arm\n"
              "was accidentally ripped off during the stealing process, so \n"
              "Al had to get help to fix you before he can auction you off! \n"
              "Lets escape after the polish! Pick a direction to escape!\n",

              "\nLast but for least, we are at ken's dream house It's \n"
              "beautiful, it's got everything you ever wished for in a \n"
              "dream world. There's tea sets, and he's preparing for barbie\n"
              "to join him\n"]]

    # initialize the game board
    board = {(x, y): {} for x in range(0, width) for y in range(0, height)}

    for x, y in board.keys():
        board.get((x, y))['description'] = STORY[x][y]
        board.get((x, y))['e'] = True if x + 1 in range(0, width) else False
        board.get((x, y))['w'] = True if x - 1 in range(0, width) else False
        board.get((x, y))['n'] = True if y + 1 in range(0, height) else False
        board.get((x, y))['s'] = True if y - 1 in range(0, height) else False

    # add the width and height information into the game board dict
    board['Width'] = width
    board['Height'] = height

    return board


def allowed_direction(char_coordinates: tuple, map_info: dict) -> list:
    """Check allowed directions.

    :param char_coordinates: a tuple
    :param map_info: a game map dictionary
    :precondition: the char_coordinates must have two integers which
            indicates one of the spot in the game map, and map_info must
            be correctly formed by map_init in this module
    :postcondition: correctly form the list with the possible directions
    :return: a list

    >>> map_info = {(0, 0): {'e': True, 'w': False, 's': False, 'n': True}}
    >>> allowed_direction((0, 0), map_info)
    ['e', 'n']

    >>> map_info = {(2, 2): {'e': True, 'w': True, 's': True, 'n': True}}
    >>> allowed_direction((2, 2), map_info)
    ['e', 'w', 's', 'n']
    """
    # 'datails' is the position's info
    details = map_info.get(char_coordinates)
    # return the list of the allowed directions
    return [key for key, value in details.items() if value is True]


def boundary_description(direction: str):
    """Print the description of the not allowed direction.

    :param direction: a string
    :precondition: the direction must be a value returned by
            get_user_choice function
    :postcondition: print the correct boundary message for the given
            direction
    """
    if direction == "n":
        print("\n\t# Can't go this way, "
              "it will lead you to the valley of death.\n")
    elif direction == "s":
        print("\n\t# You will fall out of the train in this direction "
              "and be crushed into a million pieces! Don't go here!\n")
    elif direction == "w":
        print("\n\t# If you force your way this way, "
              "it's a black hole and you will never see Andy again!\n")
    elif direction == "e":
        print("\n\t# It's not this way! This will take you to hell.\n")
    else:
        print("\n\t# Invalid entry.\n")


def print_map(map_info: dict, character: dict):
    """Print the game map.

    A function that prints the game map with the current position of
    the character.

    :param map_info: a game map dictionary
    :param character: a character dictionary
    :precondition: the character must be correctly formed with
            create_character function in the character module
    :postcondition: print the visual game map
    """
    # get the width and height info from the map_info dict
    width = map_info['Width']
    height = map_info['Height']

    # print the visual map
    for x in range(width - 1, -1, -1):
        for y in range(0, height):
            if x == character['Pos_y'] and y == character['Pos_x']:
                print(f"[x]", end="")
            else:
                print(f"[_]", end="")
        print()


def main():
    """
    Drive the doctest in this module.
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
