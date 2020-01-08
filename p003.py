"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""



def factors_naive(x):
    '''
    A factor of x is any natural number for which the division of x is 0
    '''
    factors = [n for n in range(1, x) if x%n == 0]
    return factors


def factors(x):
    # We will store all factors in `result`
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                result.append(x//i)
        i += 1
    # Return the list of factors of x
    return result


def isPrime(x):
    '''
    a number is prime if it has no factors except 1 and itself.
    '''
    if len(factors(x)) > 2:
        return False
    else:
        return True



if __name__ == "__main__":
    factor_list = factors(600851475143)
    print(factor_list)
    prime_factors = [x for x in factor_list if isPrime(x)]
    print(prime_factors)
    print(max(prime_factors))
