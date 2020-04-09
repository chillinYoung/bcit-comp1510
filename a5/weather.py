"""
COMP 1510 202010 Assignment 5
Young Kim (A01087377)
"""

import json
import requests
import time
import datetime
import doctest


def get_weather_info() -> dict:
    """Load the weather data from openweathermap.org.

    A function that loads Vancouver's weather data from
    https://openweathermap.org.

    :return: the raw weather data as a dict if the data were correctly loaded
    """
    weather_source = ("https://api.openweathermap.org/data/2.5/onecall?"
                      "lat=49.2497&lon=-123.1193&units=metric"
                      "&appid=b9c2a82ac031adfa45f6cb2800cbb30c")
    res = requests.get(weather_source)

    try:
        weather_data = json.loads(res.text)['daily']
    except KeyError:
        print("# Error: couldn't load the data")
        weather_data = None
    else:
        return weather_data


def convert_utc_time(utc_time: int) -> str:
    """Convert UTC time to 24-hour form of the clock time.

    :param utc_time: the integer as a UTC time format
    :precondition: utc_time must be an positive integer
    :return: 24-hour format of the time as a string

    >>> convert_utc_time(1586462760)
    '13:06'
    >>> convert_utc_time(1600762760)
    '01:19'
    """
    return time.strftime('%H:%M', time.localtime(utc_time))


def convert_utc_date(utc_time: int) -> str:
    """Convert UTC time to yyyy-mm-dd date form.

    :param utc_time: the integer as a UTC time format
    :precondition: utc_time must be an positive integer
    :return: yyyy-mm-dd format of the date as a string

    >>> convert_utc_date(1586462760)
    '2020-04-09'
    >>> convert_utc_date(1600468736)
    '2020-09-18'
    """
    return time.strftime('%Y-%m-%d', time.localtime(utc_time))


def parse_weather_data(data: dict) -> list:
    """Parse the weather list data to formed data.

    :param data: a dict contains raw weather data gotten by get_weather_info
            function in this module
    :precondition: data must be gotten by the get_weather_info function
    :postcondition: correctly form the essential data to be shown to the user
    :return: parsed data as a list
    """
    reformed = []
    for day in data:
        reformed.append({
            'date': convert_utc_date(day['dt']),
            'weather': day['weather'][0]['main'],
            'sunrise': convert_utc_time(day['sunrise']),
            'sunset': convert_utc_time(day['sunset']),
            'temp': f"{day['temp']['day']}{chr(176)}C",
            'feels_like': f"{day['feels_like']['day']}{chr(176)}C",
            'humidity': f"{day['humidity']}%"
        })
    return reformed


def print_weather_data(data: list, days: int):
    """Print the weather data for given days.

    :param data: a dictionary contains formed weather data
    :param days: a positive integer less than or equal to five
    :precondition: data must be formed by parse_weather_data in this module,
            and days must be an integer between 1 and 7
    :postcondition: print the correctly formed data
    """
    counter = 0
    while counter < days:
        print()
        for title, detail in data[counter].items():
            print(f"{title}: {detail}")
        counter += 1


def get_user_input_days() -> int:
    """Ask user to input the number of days to see the weather.

    :postcondition: repeat asking until user input is valid
    :return: the days as an integer
    """
    while True:
        try:
            days = int(input("How many days of weather you'd like to see?: "))
        except ValueError:
            print("# Error: please enter an integer.\n")
        else:
            if 1 <= days <= 7:
                return days
            else:
                print("# Error: please enter an integer between 1 and 7.\n")


def main():
    """Drive the program and the doctest in this module."""
    doctest.testmod()

    # drives the weather program from here
    weather_info = get_weather_info()
    # if weather info was loaded correctly, drive the rest of the program.
    if weather_info is not None:
        days = get_user_input_days()
        data = parse_weather_data(weather_info)
        print_weather_data(data, days)

    print("\n=== Thank you for using our service. See you again! ===")


if __name__ == "__main__":
    main()
