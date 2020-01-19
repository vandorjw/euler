# -*- coding: utf-8 -*-

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?


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


def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num


if __name__ == "__main__":
    limit = 10001
    num = nth_prime(limit)
    print(f"{num} is the {limit}th prime")
