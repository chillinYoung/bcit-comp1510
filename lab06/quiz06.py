"""
COMP 1510 202010 Quiz 06
Young Kim (A01087377)
Partners: Lily, HyungJoon
"""

import math
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        executed_func = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.5f} seconds.")
        return [f"{run_time:.5f}", func.__name__]
    return wrapper


@timer
def eratosthenes_young(upperbound):
    nums = list(range(2, upperbound + 1))
    # to get range between 2 to root of upperbound, inclusive
    check_nums = range(2, math.floor(upperbound ** 0.5) + 1)

    for check_num in check_nums:
        copy_nums = nums    # shallow copy to refresh it
        for num in copy_nums:
            if (num % check_num == 0) and (num != check_num):
                nums.remove(num)

    return nums


@timer
def eratosthenes_hyungjoon(num):
    prime_list = []
    for i in range(2, num + 1):
        if i == 2:
            prime_list.append(i)
        else:
            maximum = int(math.sqrt(i)) + 2
            for j in range(2, maximum):
                if i % j != 0 and j == maximum - 1:
                    prime_list.append(i)
                    break
                if i % j == 0:
                    break
    return prime_list


@timer
def eratosthenes_lily(upperbound):
    prime_numbers = list(range(0, upperbound))
    for value in prime_numbers[:]:
        if value <= 1:
            prime_numbers.remove(value)
        else:
            if not is_prime_lily(value):
                prime_numbers.remove(value)
    return prime_numbers


def is_prime_lily(number):
    number_is_prime = True
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            number_is_prime = False
            break
    return number_is_prime


def main():
    print("Young Version: ", end="")
    young = eratosthenes_young(1000)
    print("Lily Version: ", end="")
    lily = eratosthenes_lily(1000)
    print("HyungJoon Version: ", end="")
    hyungjoon = eratosthenes_hyungjoon(1000)

    versions = [young, lily, hyungjoon]
    run_time_dict = {time: name for time, name in versions}
    fastest_name = run_time_dict[min(run_time_dict)]

    print(f"\nThe fastest one is {fastest_name!r}.")


if __name__ == "__main__":
    main()
