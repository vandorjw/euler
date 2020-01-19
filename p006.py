# -*- coding: utf-8 -*-

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.


def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        total += i*i
    return total


def square_of_sums(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total*total


if __name__ == "__main__":
    limit = 100
    a = sum_of_squares(limit)
    b = square_of_sums(limit)
    c = b - a
    print(c)
