# -*- coding: utf-8 -*-
from eulerlibs.factors import multi_least_common_multiple, range1

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

"""
What this question is asking for, is the least common multiple of all numbers between 1 and 20
"""

list_1_to_20 = [x for x in range1(20)]

lcm = multi_least_common_multiple(list_1_to_20)

print(lcm)  # this is the answer
