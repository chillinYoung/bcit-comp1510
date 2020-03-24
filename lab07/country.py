"""
COMP 1510 202010 Lab 07c
Young Kim (A01087377)

A class that can be used to represent a country.
"""

import doctest


class Country:
    """A class that represents a country."""

    def __init__(self, name: str, population: int, area: int) -> None:
        """Initialize attributes to describe a country.

        :param name: country's name as string
        :param population: the country's population as integer
        :param area: the country's area as integer in square kilometres
        :precondition: the arguments must be given with proper types
        :postcondition: correctly form a country object

        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> canada.name
        'Canada'
        >>> canada.area
        9985000
        """
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, Country) -> bool:
        """Compare if area is larger.

        :param Country: a Country object
        :precondition: the Country object must be well initialized
        :postcondition: compare two countries' area and return boolean value
        :return: a boolean value

        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> denmark = Country("Denmark", 5_603_000, 42_933)
        >>> canada.is_larger(denmark)
        True
        """
        if self.area > Country.area:
            return True
        else:
            return False

    def population_density(self) -> float:
        """Calculate the population density.

        :postcondition: correctly calculate the population density
        :raise ZeroDivisionError: if population is zero
        :return: the density as float

        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> density = canada.population_density( )
        >>> print('%.7f' % density)
        3.7646470
        """
        try:
            density = self.population / self.area
        except ZeroDivisionError as zde:
            print(f"{zde}")
        else:
            return density

    def __str__(self) -> str:
        """Return the object in informal representation.

        :return: an informal representation of a Country object

        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> print(canada)
        Canada has a population of 37590000 and is 9985000 square kilometres.
        """
        return (f"{self.name.title()} has a population of {self.population} "
                f"and is {self.area} square kilometres.")

    def __repr__(self) -> str:
        """Return the object in official representation.

        :return: an informal representation of a Country object

        >>> canada = Country("Canada", 37_590_000, 9_985_000)
        >>> [canada]
        [Country("Canada", 37590000, 9985000)]
        """
        return (f"Country(\"{self.name.title()}\", "
                f"{self.population}, {self.area})")


def main():
    """Drive the doctest in this module."""
    doctest.testmod()


if __name__ == "__main__":
    main()
