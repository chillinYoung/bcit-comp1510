"""
COMP1510 TEAM 4 Hackathon - Final Exam

Team Members:
- Young
- Joshua
- Hyung Joon
- Lily

Main application module.
"""

import json
import re
import webbrowser
import time
from datetime import datetime, timedelta
import itertools
import app_gmaps

# THE APPLICATION IS COMPOSED OF TWO OR MORE FUNCTIONS (MAIN PLUS OTHERS)
# PEP8 STYLE COMPLAINTS ARE ELIMINATED
# IDENTIFIERS ARE MEANINGFUL AND APPROPRIATE
# CODE DUPLICATION IS MINIMIZED OR, BETTER YET, ELIMINATED ENTIRELY
# ALL MODULES, CLASSES, FUNCTIONS HAVE CORRECT BRIEF DOCSTRINGS
# CODE IS IDIOMATIC PYTHON, I.E., EAFP, NOT LBYL
# THERE ARE NO GLOBAL VARIABLES
# FORMATTED OUTPUT IS CONSISTENT AND EASY TO READY FOR THE USER
# FUNCTIONS ARE SHORTER THAN 20 LINES OF CODES


def timer(func):
    """Invoke decorator function.

    A function that tells how long did the user have used this app

    :param func: A function from @timer
    :precondition: function need to be called that must has a "@timer"
    :postconditon: call correct decorator function
    :return: wrapper function
    """
    # CORRECT USE OF AT LEAST ONE FUNCTION DECORATOR
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"\n\nGood bye! You spent a total of {run_time:.5f} seconds\n"
              f"in our Museum Explorer app. Come again next time.\n")

    return wrapper


def get_user_name() -> str:
    """Return valid name of user.

    :postcondition: ask user to create name with only valid characters and
    return the name as string.
    :return: user's name as a string
    """
    # CORRECT USE OF REGULAR EXPRESSION
    pattern = re.compile(r'^[a-zA-Z]+$')
    user_name = input("What is your name?\n"
                      "Your name must only have valid alphabets [a-zA-z]: ")

    while not pattern.search(user_name):
        user_name = input("Please try again, only valid letters are allowed: ")

    return user_name.lower().title()


def greet_user(user_name: str):
    """A simple function saying invitation.

    :param user_name: a string
    :precondition: user_name must be a valid string
    :postcondition: greet user correctly
    """
    print(f"\nHello {user_name},\n"
          "nice to meet you! Welcome to the Museum Explorer.\n"
          "Here, you will see a list of recommended museums around the "
          "world,\nand give you a chance to escape from your boring room,\n"
          "and go to a world-renown museum!\n\n"
          "If you want to exit from the program,\n"
          "please press 'ctrl + c'.")
    time.sleep(3)


def parse_json() -> dict:
    """A simple function that load Json file data.

    :postcondition: correctly call json file
    :return: a dictionary with data parsed from file
    """
    with open('data.json') as json_obj:
        museum_data = json.load(json_obj)
        return museum_data


def choose_country(data: dict) -> list:
    """Allows the user to select a country to travel to from ten random
    countries.

    :param data: a dictionary of database pulled from the data.json file
    :precondition: the data must be a dictionary, containing the country
            name as a key and a list of dictionary/ies as the value
    :postcondition: correctly returns list of museums in user-selected country
    :return: a list of museums in the selected country
    """
    print("\nHere is the list of countries you can travel to!\n"
          "We randomly picked ten countries for YOU!\n")
    time.sleep(2)

    # put the countries in a set so that we can randomize country list
    # USE OF AT LEAST ONE SET
    countries = set(data.keys())

    # USE OF RANGE FUNCTION AND LIST SLICING
    rand_countries = sorted(list(countries)[0:10])
    # THIS SATISFIES REQUIREMENT "CORRECT USE OF ENUMERATE()"
    for num, country in enumerate(rand_countries, start=1):
        print(f"{num}: {country}")
    time.sleep(1)

    # EXCEPTION HANDLING IS EMPLOYED TO PREVENT THE APPLICATION FROM CRASHING
    while True:
        try:
            user_choice = int(input("\nEnter the number of a country: "))
            if user_choice not in range(1, len(rand_countries) + 1):
                raise ValueError
        except ValueError:
            print("# ERROR: invalid number: please try again")
        else:
            print(f"\nYou are now in: {rand_countries[user_choice - 1]}")
            return data[rand_countries[user_choice - 1]]


def choose_museum(list_of_museums: list) -> dict:
    """Allows the user to find a museum by selecting a country from listed
    countries.

    :param list_of_museums: a list of museums in the country, based on the
            database
    :precondition: list_of_museums must be a list of dictionaries
    :postcondition: correctly returns the user-selected museum information
            as a dictionary
    :return: a dictionary containing the information of museum which the
            user selected
    """
    print("-" * 78)
    # USE OF AT LEAST ONE FUNCTION FROM ITERTOOLS
    for index, museum in zip(itertools.count(1), list_of_museums):
        print(f"#{index}\n"
              f"Name: {museum['name']}\n"
              f"Address: {museum['address']}\n"
              f"Website: {museum['website']}")
        print("-" * 78)

    # get user input for museum choice
    while True:
        try:
            user_choice = int(input("From the above options, please enter the "
                                    "number of museum you wish to visit: "))
            if user_choice not in range(1, len(list_of_museums) + 1):
                raise ValueError
        except ValueError:
            print("# ERROR: invalid number: please try again")
        else:
            return list_of_museums[user_choice - 1]


def visit_museum(museum_info: dict):
    """Open the street view of the museum on the webbrowser.

    :param museum_info: a dictionary that contains the information of one
            specific museum
    :precondition: museum_info must be one of the museums parsed from
            'data.json' by parse_json function in this module
    :postcondition: open the web brower with the correct URL to the
            given specific museum
    """
    latitude = museum_info['coordinates'][0]
    longitude = museum_info['coordinates'][1]

    # formulate a url to be opened using webbrower open function
    url = ("https://www.google.com/maps/@?api=1&map_action=pano&viewpoint="
           f"{latitude},{longitude}")
    webbrowser.open(url)


def continue_visit() -> bool:
    """Ask the user to continue the tour.

    :postcondition: ask the user to continue the tour until input is valid
    :return: a boolean
    """
    while True:
        user_choice = input("\nDo you wish to visit another museum? "
                            "Enter Y for yes, and N for no: ")
        if user_choice.lower() == 'y':
            return True
        elif user_choice.lower() == 'n':
            return False


def update_check():
    """Check last update date and update the database.

    :postcondition: if the last update of database is exceeded more than
            two days, update the database correctly
    """
    print("The program is finding updates of our Museum data......")
    time.sleep(2)

    today = datetime.today()
    with open('last_update_log.txt', 'r+') as update_log:
        last_update = datetime.fromisoformat(update_log.readline()[:19])
        print(f"The last update was {last_update}\n")
        if today - last_update >= timedelta(days=2):
            print("Updating the database........\n")
            app_gmaps.main()    # execute app_gmaps program to update database

            # update the date of the update_log
            update_log.seek(0)
            update_log.truncate()
            update_log.write(today.strftime("%Y-%m-%d %H:%M:%S"))

    print("Great! The information are up to date!\n")
    time.sleep(1)


@timer
def main():
    """Drive this program."""
    try:
        update_check()
        database = parse_json()
        greet_user(get_user_name())

        # use while loop to repeatedly visit other museums after the first one
        user_want_continue = True
        while user_want_continue:
            museums_list = choose_country(database)
            museum_choice = choose_museum(museums_list)
            visit_museum(museum_choice)
            user_want_continue = continue_visit()

    except KeyboardInterrupt:
        pass    # goodbye message will be printed by timer

    # RUBRIC COMMENTS ARE CLEARLY LABELED IN THE CODE USING COMMENTS
    # IN ALL CAPS


if __name__ == "__main__":
    main()
