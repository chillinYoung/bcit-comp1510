"""
COMP 1510 202010 Lab 09 Part Two
Young Kim (A01087377)
"""

import doctest


def init_foods():
    """Initialize foods dictionary.

    :return: a initialized foods dictionary

    >>> test_foods = init_foods()
    >>> test_foods    #doctest: +NORMALIZE_WHITESPACE
    {'lettuce': 5, 'carrot': 52, 'apple': 72, 'bread': 66, 'pasta': 221,
    'rice': 225, 'milk': 122, 'cheese': 115, 'yogurt': 145, 'beef': 240,
    'chicken': 140, 'butter': 102}
    """
    foods = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
             "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
             "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}
    return foods


def total_calories(food_dict: dict) -> int:
    """Calculate total calories in food dictionary.

    :param food_dict: a foods dictionary with food items as keys and calories
            as values
    :precondition: the values in the dictionary must be integers
    :postcondition: correctly calculate the sum of calories in the dictionary
    :return: the sum of calories

    >>> test_foods = init_foods()
    >>> total_calories(test_foods)
    1505
    """
    return sum([calories for calories in food_dict.values()])


def food_item_names(food_dict: dict) -> list:
    """Return the list of the food item names.

    :param food_dict: a foods dictionary with food items as keys
    :precondition: the food_dict must have keys as string
    :postcondition: correctly return the list of the food names
    :return: the list of the food item names

    >>> test_foods = init_foods()
    >>> food_item_names(test_foods)    #doctest: +NORMALIZE_WHITESPACE
    ['lettuce', 'carrot', 'apple', 'bread', 'pasta', 'rice', 'milk',
    'cheese', 'yogurt', 'beef', 'chicken', 'butter']
    """
    return [item for item in food_dict.keys()]


def print_foods_info(food_dict: dict):
    """Print the foods' information.

    :param food_dict: a foods dictionary with food items as keys and calories
            as values
    :precondition: the food_dict must be well formed with food names as
            the keys of strings and the calories as the values of integers
    :postcondition: correctly print the information of the foods

    >>> test_foods = init_foods()
    >>> print_foods_info(test_foods)    #doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    Food Items: ['apple', 'beef', 'bread', 'butter', 'carrot', 'cheese',
    'chicken', 'lettuce', 'milk', 'pasta', 'rice', 'yogurt']
    Total Calories: 1505 Average Calories:  125.4
    <BLANKLINE>
    """
    print(f"\nFood Items: {sorted(food_item_names(food_dict))}\n"
          f"Total Calories: {total_calories(food_dict)} "
          "Average Calories: "
          f"{total_calories(food_dict) / len(food_dict): .1f}\n")


def check_quit(user_input):
    """Check if user wants quit.

    :param user_input: a string that user input
    :postcondition: if user_input is 'q' exit the program
    :raise SystemExit: if user_input is 'q'
    """
    if user_input == 'q':
        raise SystemExit()


def main():
    """Drive the program and doctest in this module."""
    doctest.testmod()

    foods = init_foods()
    while True:
        new_item = input("Enter food item to add, or 'q' to exit: ")
        check_quit(new_item)

        foods[new_item] = int(input("Enter calories for " + new_item + ": "))
        print_foods_info(foods)


if __name__ == "__main__":
    main()
