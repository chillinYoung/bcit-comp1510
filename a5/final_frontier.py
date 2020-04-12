"""
COMP 1510 202010 Assignment 5
Young Kim (A01087377)
"""

import requests
import time
import datetime
import json
import random
import numpy
import cv2


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
    # url = art['url']
    # image_show(url)


def image_show(apod_data):
    """
    """
    url = apod_data[0]['url']
    photo = requests.get(url, stream=True).raw
    img = numpy.asarray(bytearray(photo.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    cv2.imshow('APOD', img)
    cv2.waitKey(3000)    # 1000 miliseconds → 1 sec
    cv2.destroyWindow("APOD")
    cv2.waitKey(1)
    # cv2.destroyAllWindows()


def main():
    """Drive the program."""
    print("Welcome to online exhibition of Astronomy Picture of the Day.\n"
          "(Press 'ctrl + c' to exit this program.)\n")
    try:
        while True:
            random_date = random_date_generator()
            apod = get_nasa_data(random_date)
            print_apod(apod)
            image_show(apod)
            time.sleep(20)    # should be 300 for the instruction
    except KeyboardInterrupt:
        print("\n=== Thank you. Bye. ===")

    # random_date = random_date_generator()
    # apod = get_nasa_data(random_date)
    # image_show(apod)
    # time.sleep(20)


if __name__ == "__main__":
    main()
