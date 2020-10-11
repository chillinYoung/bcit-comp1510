"""
COMP1510 TEAM 4 Hackathon - Final Exam

Team Members:
- Young
- Joshua
- Hyung Joon
- Lily

Sub module that is to manage museum data for main app module.
"""

import googlemaps
import json
import doctest
import time
import apikey


def get_place_ids(maps: googlemaps) -> list:
    """Create a list of place ids required for googlemaps.place function.

    :param maps: a googlemaps Client class object, with api key
    :precondition: the googlemaps client object must be valid, with a valid
                    api key
    :postcondition: correctly returns a list of place_ids, which are
                    retrieved from the google maps api
    :return: a list of place ids in string format
    """
    place_ids = []

    # read museums list and store it in a list
    with open('museums.txt', 'r') as txt_obj:
        museums = [item for item in txt_obj.read().splitlines() if item != ""]

    # find the place_id using the museum names
    for museum in museums:
        result = maps.find_place(museum, 'textquery', fields=['place_id'])

        try:
            place_id = result['candidates'][0]['place_id']
        except IndexError:
            pass
        else:
            place_ids.append(place_id)

    return place_ids


def get_place_detail(maps: googlemaps, id_list: list) -> dict:
    """Return details of each place in a dictionary.

    :param maps: a googlemaps client object
    :param id_list: a list valid place_id's returned from google place api
    :precondition: the googlemaps client object must be valid and the id_list
                    must be a well-formed list with valid place_id's from
                    google's api
    :postcondition: correctly returns a dictionary with data for each place
                    id
    :return: a dictionary
    """
    detail_data = {}
    for place_id in id_list:
        # the 'fields' arg is to request only specific information
        place = maps.place(
            place_id, fields=['name', 'formatted_address', 'plus_code',
                              'website', 'formatted_phone_number', 'geometry'])

        try:
            # SYNTACTIC SUGAR (DICTIONARY COMPREHENSION)
            details = {key: value for (key, value) in place['result'].items()}

            # form the data
            country = details['plus_code']['compound_code'].split(', ')[-1]
            db_format = place_detail_format(details)

        except KeyError:    # missing key in the data -> ignore it
            pass

        else:
            if country not in detail_data.keys():
                detail_data[country] = [db_format]
            else:
                detail_data[country].append(db_format)

    return detail_data


def place_detail_format(place_details: dict) -> dict:
    """Return formed data of place details.

    A helper function that reorginizes the given data for batabase.

    :param place_details: a dictionary that contains detail data of the place
    :precondition: place_details must be the data of one place that is result
                    of the request from Google Maps API
    :postcondition: organize the data in a good format and return it
    :return: a dictionary
    """
    db_format = {'name': place_details['name'],
                 'address': place_details['formatted_address'],
                 'phone_number': place_details['formatted_phone_number'],
                 'website': place_details['website'],
                 'coordinates': (place_details['geometry']['location']['lat'],
                                 place_details['geometry']['location']['lng'])}

    return db_format


def database(data: dict):
    """Write database.json file with given data.

    :param data: a dictationary that contains place information
    :precondition: data must be correctly formed by get_place_detail in
                    this module
    :postcondition: correctly form the database with given data
    """
    with open('data.json', 'w') as txt_obj:
        # indent=3 is for the indentation of each key:value pairs to be 3 chars
        json.dump(data, txt_obj, indent=3)


def main():
    """Drive this program."""
    # doctest.testmod()
    g_maps = googlemaps.Client(apikey.APIKEY)
    list_place_ids = get_place_ids(g_maps)
    print("Please wait a little bit longer.....")
    places_data = get_place_detail(g_maps, list_place_ids)
    database(places_data)


if __name__ == "__main__":
    main()
