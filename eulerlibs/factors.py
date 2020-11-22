# -*- coding: utf-8 -*-
import math
from collections import Counter


def factors(x):
    # We will store all factors in `result`
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i * i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if x // i != i:  # In Python, // operator performs integer/floored division
                result.append(x // i)
        i += 1
    # Return the list of factors of x
    return result


def prime_factors(x):
    """
    return the prime factors of x

    eg: the prime factors of 18 are: 2, 3, 3
    """
    # base case
    if x < 4:
        return [1, x]

    # store the prime factors in results
    results = []

    # get all the factors that are not 1 or itself.
    the_factors_of_x = [f for f in sorted(factors(x)) if f not in [1, x]]
    count_of_factors = len(the_factors_of_x)

    if count_of_factors == 0:
        results = [1, x]

    index = 0

    remainder = x
    while count_of_factors > 0 and remainder > 1 and index <= count_of_factors:
        factor = the_factors_of_x[index]
        if remainder % factor == 0:
            results.append(factor)
            remainder = remainder / factor
        else:
            index += 1
    return results


def is_prime(x):
    """
    a number is prime if it has no factors except 1 and itself.
    """
    if len(factors(x)) > 2:
        return False
    else:
        return True


def list_union(a, b):
    """
    Takes 2 list, a and b, and creates a new list.
    The new list: (A intersect B) + (A minus (A intersect B))  + (B minus (A intersect B))

    example:
    >> a = [2,2,3]
    >> b = [2,3,3]

    >> result = [2,2,3,3]
    """

    # Following the example:
    a = dict(Counter(a))  # a = {2:2, 3:1}
    b = dict(Counter(b))  # b = {2:1, 3:2}

    # For each key in dict a and b, we want the largest value
    # merged becomes {2:2, 3:2}
    merged = {k: max(a.get(k, 0), b.get(k, 0)) for k in set(a) | set(b)}

    result = []
    for key, value in merged.items():
        # looping over merged, we want a list with 2 twos, and 2 threes
        for _ in range(value):
            result.append(key)

    return result


def least_common_multiple(a, b):
    """
    finds the lowest common multiple between 2 numbers.
    example:
    lcm(18, 12)
    """
    prime_factors_of_a = prime_factors(a)
    prime_factors_of_b = prime_factors(b)

    union = list_union(prime_factors_of_a, prime_factors_of_b)

    lcm = math.prod(union)
    return lcm


def multi_least_common_multiple(list_of_numbers):

    union = []
    for natural_number in set(list_of_numbers):
        union = list_union(union, prime_factors(natural_number))

    lcm = math.prod(union)
    return lcm


def range1(end):
    """
    returns a range, starting at 1, ending at the number given.
    example:
    >> range1(10)
    >> [1,2,3,4,5,6,7,8,9,10]
    """
    return range(1, end+1)
