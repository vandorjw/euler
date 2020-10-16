# -*- coding: utf-8 -*-
from eulerlibs.factors import factors


# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(x):
    """
    a number is prime if it has no factors except 1 and itself.
    """
    if len(factors(x)) > 2:
        return False
    else:
        return True


def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 2
        if is_prime(num):
            count += 1
    return num


if __name__ == "__main__":
    limit = 10001
    num = nth_prime(limit)
    print(f"{num} is the {limit}th prime")
