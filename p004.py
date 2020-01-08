"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""



def is_palindromic(x):
    '''
    '''
    str_x = str(x)
    rev_str_x = ''.join(reversed(str_x))
    if str_x == rev_str_x:
       return True
    else:
        return False


def do3():
    a = 999
    b = 999
    c = 999
    m = a * b * c
    while not is_palindromic(m) and a > 0 and b > 0 and c > 0:
        if c > 1:
            c -= 1
        elif b > 1:
            b -= 1
            c = b
        else:
            a -= 1
            b = a
            c = b
        m = a * b * c
    return (m, a, b, c)

def do2():
    a = 999
    b = 999
    results = []
    while a > 99 and b > 99:
        if b > 100:
            b -= 1
        else:
            a -= 1
            b = a
        m = a * b
        if is_palindromic(m):
            results.append(m)
    return results

if __name__ == "__main__":
    print(max(do2()))
