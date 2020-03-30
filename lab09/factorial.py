"""
COMP 1510 202010 Lab 09
Young Kim (A01087377)
"""

import time
import doctest


def timer(func):
    """Calculate the executed time of a function.

    :param func: a function to time
    :precondition: func must be a function can be executable
    :postcondition: correctly calculate the executed time of a function
    :return: the executed time of a function
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        executed_func = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        return run_time, executed_func
    return wrapper


@timer
def factorial_iterative(number):
    """Calculate factorial with a plain loop.

    :param number: an positive integer to calculate factorial
    :precondition: number must be an positive integer
    :postcondition: correctly calculate the factorial of the given number
    :return: the calculated result
    """
    result = 1
    for num in range(number, 0, -1):
        result *= num
    return result


@timer
def factorial_recursive(number):
    """Wrap the recursive factorial helper function.

    A function that wraps the factorial_recursive_helper so that timer can
    calculate the whole time including all recursions.

    :param number: an positive integer to calculate factorial
    :precondition: number must be an positive integer
    :postcondition: correctly invoke the factorial_recursive_helper function
    :return: the return value of the factorial_recursive_helper function
    """
    return factorial_recursive_helper(number)


def factorial_recursive_helper(number):
    """Calculate factorial by recursion.

    :param number: an positive integer to calculate factorial
    :precondition: number must be an positive integer
    :postcondition: correctly calculate the factorial of the given number
    :return: the calculated result

    >>> factorial_recursive_helper(3)
    6
    >>> factorial_recursive_helper(10)
    3628800
    """
    if number == 0:
        return 1
    else:
        return number * factorial_recursive_helper(number - 1)


def main():
    """Drive the program and the doctest in this module."""
    doctest.testmod()

    filename = "results.txt"
    total_iterative_time = 0
    total_recursive_time = 0

    for num in range(1, 101):
        iter_time, iter_calc = factorial_iterative(num)
        recur_time, recur_calc = factorial_recursive(num)
        total_iterative_time += float(iter_time)
        total_recursive_time += float(recur_time)
        run_time_dict = {iter_time: 'factorial_iterative',
                         recur_time: 'factorial_recursive'}
        fastest_name = run_time_dict[min(run_time_dict)]

        output = (f"Factorials for {num}: {iter_calc}\n"
                  f"Finished factorial_iterative in {iter_time:.7f} seconds.\n"
                  f"Finished factorial_recursive in {recur_time:.7f} seconds."
                  f"\n\t->{fastest_name!r} function is faster!\n\n")

        with open(filename, 'a') as results:
            results.write(output)

    with open(filename, 'a') as results:
        results.write(f"\nTotal time of iterative: {total_iterative_time:.7f}"
                      f"\nTotal time of recursive: {total_recursive_time:.7f}"
                      "\n\n")


if __name__ == "__main__":
    main()
