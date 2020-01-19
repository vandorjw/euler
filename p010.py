# -*- coding: utf-8 -*-

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


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


def is_prime(x):
    """
    a number is prime if it has no factors except 1 and itself.
    """
    if len(factors(x)) > 2:
        return False
    else:
        return True


def primes_lt_limit(limit):
    num = 1
    primes = []
    while num < limit:
        num += 2
        if is_prime(num):
            primes.append(num)
            print(num)
    return primes


if __name__ == "__main__":
    print('Euler Problem 10')
    primes = primes_lt_limit(2000000)
    result = sum(primes)
    print(result)
