# -*- coding: utf-8 -*-

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

def is_x_divisible_by_n(x, n):
    if x % n == 0:
        return True
    else:
        return False


# 1,,3,4,

# multiple of 20
# multiple of 17

# 1. get the primes between 1 and 20
# 2. starting at 20, check
# if false: multiply by next greatest? prime and check..


if __name__ == "__main__":
    print('todo')
