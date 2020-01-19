# -*- coding: utf-8 -*-

"""


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""


def is_pythagorean(a, b, c):
    a_sqrd = a * a
    b_sqrd = b * b
    c_sqrd = c * c
    if a_sqrd + b_sqrd == c_sqrd:
        return True
    else:
        return False


def find():
    c = 998
    a_and_b = 2

    while c > 0:
        a = 1
        while a <= a_and_b / 2:
            b = a_and_b - a
            if is_pythagorean(a, b, c):
                return a, b, c
            else:
                a += 1
        c -= 1
        a_and_b += 1


if __name__ == "__main__":
    print('Euler Problem 9')
    a, b, c = find()
    print(f"{a}^2 + {b}^2 == {c}^2")
    print(f"{a} * {b} * {c} === {a * b * c}")
