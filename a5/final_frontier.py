"""
COMP 1510 202010 Assignment 5
Young Kim (A01087377)
"""

import requests
import time
import datetime
import json
import random


def get_nasa_data(date):
    """Get the apod data from the source.

    :param date: yyyy-mm-dd format of a date as a string
    :precondition: date must be between 1996-06-20 and current date in a
            well-formed string
    :postcondition: get the data from the source and return it
    :return: apod_data of the specific date as a string
    """
    nasa_source = ("https://api.nasa.gov/planetary/apod?"
                   "api_key=P4qp7CB0hw20YtuFmzwqnDtCJGyBbbgYalRd1PZe"
                   f"&start_date={date}&end_date={date}")
    res = requests.get(nasa_source)

    try:
        apod_data = json.loads(res.text)
    except KeyError:
        print("# Error: couldn't load the source data")
        apod_data = None
    else:
        return apod_data


def random_date_generator():
    """Generate a valid random date for apod data.

    :postcondition: genrate a valid random date which is valid to get a apod
            data from the source
    :return: yyyy-mm-dd format of a date as a string
    """
    # FIRST_DATE is the date the first picture took (available start point).
    FIRST_DATE = datetime.date(1996, 6, 20)
    start_date = FIRST_DATE.toordinal()
    end_date = datetime.datetime.today().toordinal()
    random_date = datetime.date.fromordinal(
        random.randint(start_date, end_date))

    return random_date.strftime("%Y-%m-%d")


def main():
    """Drive the program."""
    print("Welcome to online exhibition of Astronomy Picture of the Day.\n"
          "(Press 'ctrl + c' to exit this program.)\n")


if __name__ == "__main__":
    main()
