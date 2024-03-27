""" Problem 3: Largest prime factor """
import math


def prime_factor(n):
    """
    Returns the largest prime factor of a number.
    """
    all_numbers = populate_array(n)
    x = n

    while x >= 0:
        for i in all_numbers:
            if all_numbers[i] % x == 0:
                all_numbers.pop(i)
            print('all_numbers', all_numbers)

        x -= 1
    last = all_numbers[all_numbers.count(any) - 1]
    print('last', last)
    return last


def populate_array(n):
    array = []
    for i in range(2, n+1):
        array.append(i)
    return array
