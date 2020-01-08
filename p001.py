from math import floor

def sum_of_unique_multiples(a:list, b:list):
   return sum(set(a+b))


def multiples_of_x_less_than_y(x,y):
    max = int(floor(y/x))
    return [x*i for i in range(1, max+1) if x*i < y]



if __name__ == "__main__":
    a = multiples_of_x_less_than_y(3, 1000)
    b = multiples_of_x_less_than_y(5, 1000)
    c = sum_of_unique_multiples(a, b)
    print(c)
