"""
COMP 1510 202010 Lab 07c
Young Kim (A01087377)

A class that can be used to represent a country.
"""


class Country:
    """A class that represents a country."""

    def __init__(self, name: str, population: int, area: int) -> None:
        """Initialize attributes to describe a country.

        :param name: country's name as string
        :param population: the country's population as integer
        :param area: the country's area as integer in square kilometres
        :precondition: the arguments must be given with proper types
        :postcondition: correctly form a country object
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
        """
        try:
            density = self.area / self.population
        except ZeroDivisionError as zde:
            print(f"{zde}")
        else:
            return density

    def __str__(self) -> str:
        """Return the object in informal representation.

        :return: an informal representation of a Country object
        """
        return (f"{self.name.title()} has a population of {self.population} "
                f"and is {self.area} square kilometres.")

    def __repr__(self) -> str:
        """Return the object in official representation.

        :return: an informal representation of a Country object
        """
        return f"Country({self.name.title()}, {self.population}, {self.area})"


def main():
    pass


if __name__ == "__main__":
    main()
