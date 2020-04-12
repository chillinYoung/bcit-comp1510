"""
COMP 1510 202010 Assignment 5
Young Kim (A01087377)
"""

import requests
import time
import datetime
import json
import random
import subprocess


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


def print_apod(apod_data):
    """Print apod data.

    :param apod_data: one apod data returned by get_nasa_data function in
            this module
    :precondition: apod_data must be gotten by get_nasa_data function
    """
    art = apod_data[0]
    print(f"Title: {art['title']}\nDate: {art['date']}")
    try:
        print(f"Author: {art['copyright']}")
    except KeyError:
        pass
    print(f"Explanation: \n\t{art['explanation']}\n")


def image_show(apod_data):
    """Show image for the apod data.

    :param apod_data: one apod data returned by get_nasa_data function in
            this module
    :precondition: apod_data must be gotten by get_nasa_data function
    :postcondition: show the linked image in apod data in the Chrome window
    """
    # 'ERROR:browser_switcher_service' will occur for every time window
    # is terminated and opened new one because it is considered as a abnomal
    # exit of the program by Google Chrome itself.
    url = apod_data[0]['url']
    exe_app = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    option = '--window-size=700,700'
    status = subprocess.Popen([exe_app, option, url])
    time.sleep(5)    # show image for 5 seconds
    subprocess.check_call(['kill', str(status.pid)])


def main():
    """Drive the program."""
    # to terminate existing chrome windows to prevent error occurred
    # → cannot get PID of specific window
    # because of Chrome itself's PID management system
    subprocess.Popen(['killall', 'Google Chrome'])
    time.sleep(1)

    # main program starts here
    print("Welcome to online exhibition of Astronomy Picture of the Day.\n"
          "This program is written for MacOS.\n\n"
          "(Press 'ctrl + c' to exit this program.)\n")
    try:
        while True:
            random_date = random_date_generator()
            apod = get_nasa_data(random_date)
            print_apod(apod)
            try:
                image_show(apod)
            except FileNotFoundError:
                print("# Sorry, cannot show the image due to "
                      "Google Chrome couldn't be found on your Mac.\n")
            time.sleep(10)    # wait 10 seconds for the next image and data
    except KeyboardInterrupt:
        print("\n=== Thank you. Bye. ===")


if __name__ == "__main__":
    main()
