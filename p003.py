# -*- coding: utf-8 -*-
from eulerlibs.factors import factors, is_prime


# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def factors_naive(x):
    """
    A factor of x is any natural number for which the division of x is 0
    """
    results = [n for n in range(1, x) if x % n == 0]
    return results


if __name__ == "__main__":
    factor_list = factors(600851475143)
    print(factor_list)
    prime_factors = [x for x in factor_list if is_prime(x)]
    print(prime_factors)
    print(max(prime_factors))
